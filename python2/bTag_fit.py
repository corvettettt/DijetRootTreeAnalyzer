#!/usr/bin/env python
import sys, os, copy, re
from array import array
from optparse import OptionParser
from framework import Config
import math
from ROOT import *

from rootTools import CMS_lumi as CMS_lumi
from rootTools import tdrstyle as setTDRStyle

gROOT.SetBatch(kTRUE)

################# configuration ######################
sqrtS = 13000.
#lumiValue = 4411 #[pb]
lumiValue = 20057 #[pb]
showCrossSection = 1 #1=cross section [pb] , 0=number of events/GeV
#drawSignalShapeAlsoAlone = 1
fixedRange = 1 #1=YES , 0=NO  (the option works only if showCrossSection=1; otherwise=0)
minY = 0.000003
maxY = 20000
if showCrossSection==1:
    lumi = lumiValue
else:
    lumi = 1
#massMin = 453
#massMax = 2037
massMin = 1181
massMax = 7866 
blindRegionMassMin = 0
#blindRegionMassMin = 649
blindRegionMassMax = 0
#blindRegionMassMax = 838
doBlind = False
if blindRegionMassMin != blindRegionMassMax:
    doBlind = True
xaxisTitle = "Dijet Mass [GeV]"
if showCrossSection==1:
    yaxisTitle_main = "d#sigma / dm_{jj}   [pb / GeV]"
else:
    yaxisTitle_main = "Number of events / GeV"
yaxisTitle_secondary = "#frac{(Data-Fit)}{#sigma_{Data}}   "
range_residual = 3.5
MinNumEvents = 10.
nParFit = 4
massBins_list = [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430, 10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000]
################### DO NOT MODIFY ######################
massBins_list_actual = []
firstBin = -1
lastBin = -1
index_bin_boundary=-1
for bin_boundary in massBins_list:
    index_bin_boundary = index_bin_boundary+1
    #print bin_boundary, massMin, massMax
    if (bin_boundary>=massMin and firstBin==-1 ):
        massMin = bin_boundary
        firstBin=1
        print "FIRST BIN is "+str(massMin)
    if (bin_boundary>(massMax+0.0000000001) and lastBin==-1 ):
        massMax = massBins_list[index_bin_boundary-1]
        lastBin=1
        print "LAST BIN is "+str(massMax)
    if (bin_boundary>=massMin and bin_boundary<=massMax):
        massBins_list_actual.append(bin_boundary)
print massBins_list_actual
massBins = array("d",massBins_list_actual)
N_massBins = len(massBins)-1
#########################################################

sel = "((mjj>"+str(massMin)+" && mjj<"+str(blindRegionMassMin)+") || (mjj>"+str(blindRegionMassMax)+" && mjj<"+str(massMax)+")) && fabs(deltaETAjj)<1.3 && PassJSON==1 && passHLT_CaloScoutingHT250==1"

#==================
# CMS style and lumi
#==================

#set tdr style
setTDRStyle.setTDRStyle()
#tdrStyle.SetNdivisions(505, "XYZ")

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.lumi_7TeV = "%1.f fb^{-1}" % lumiValue
CMS_lumi.lumi_8TeV = "%1.f fb^{-1}" % lumiValue
CMS_lumi.lumi_13TeV = "%1.f pb^{-1}" % lumiValue
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
CMS_lumi.cmsTextSize = 1.0

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 4

W = 600
H = 700
H_ref = 700
W_ref = 600
T = 0.08*H_ref
B = 0.12*H_ref
L = 0.12*W_ref
R = 0.04*W_ref

#######################################################################


usage = """usage: python python/fitMjj_btag.py -c config/bTag_analysis.cfg -b BTag2016"""

def main():

    ###################################################################                                                                                                                    
    parser = OptionParser(usage=usage)
    parser.add_option('-c','--config',dest="config",type="string",default="config/bTag_analysis.cfg",
                  help="Name of the config file to use")
    parser.add_option('-b','--box',dest="box", default="BTag2016",type="string",
                  help="box name")

    (options,args) = parser.parse_args()

    cfg = Config.Config(options.config)
    box = options.box

    inputHistoFileName       = cfg.getVariables(box,"inputDataHistos")
    outputLabel     = cfg.getVariables(box,"outputLabel")
    
    ###################################################################                          



    # input data
    inputDataFile = TFile(inputHistoFileName['data'][0])

    # mass variable
    mjj = RooRealVar('mjj', 'mjj', float(massMin), float(massMax))
    if doBlind:
        mjj.setRange("RangeLow", massMin, blindRegionMassMin)
        mjj.setRange("RangeHigh", blindRegionMassMax, massMax)

    # data
    dataInt = 1
    h_data = (inputDataFile.Get(inputHistoFileName['data'][1])).Clone("h_data")
    if doBlind:
        dataInt = h_data.Integral(massMin + 1, blindRegionMassMin) + h_data.Integral(blindRegionMassMax + 1, massMax)
    else:
        dataInt = h_data.Integral(massMin + 1, massMax)
        
    print "number of events in the fit range:", int(dataInt)

    h_data_roo = RooDataHist('h_data_roo', 'h_data_roo', RooArgList(mjj), h_data)
    h_data_roo.Print()

#    # trigger efficiency model
    m_eff = RooRealVar('m_eff','m_eff',495.7,450.,550.)
    sigma_eff = RooRealVar('sigma_eff','sigma_eff',96.0,80.,120.)
    m_eff.setConstant(kTRUE)
    sigma_eff.setConstant(kTRUE)
#    efficiency = RooGenericPdf('efficiency','(1/2)* ( 1 + TMath::Erf((@0-@1)/@2))',RooArgList(mjj,m_eff,sigma_eff))    
#    efficiency.Print()

    #old
    # background model
    norm = RooRealVar('norm', 'norm', dataInt, 0.0, 1.0e9)
    p1 = RooRealVar('p1', 'p1', 10 , -10., 100.0)
    p2 = RooRealVar('p2', 'p2', 5  , 0., 60.0)
    p3 = RooRealVar('p3', 'p3', 0   -10.0, 10.0)
    #p3.setConstant
    background = RooGenericPdf('background','(pow(1-@0/%.1f,@1)/pow(@0/%.1f,@2+@3*log(@0/%.1f)))'%(sqrtS,sqrtS,sqrtS),RooArgList(mjj,p1,p2,p3))
    background.Print()
    background_ext = RooAddPdf("model","b-only",RooArgList(background),RooArgList(norm))

    #new
    # background model
    #norm = RooRealVar('norm','norm',dataInt,0.,1e+09)
    #p1 = RooRealVar('p1','p1',10,0.,100.)
    #p2 = RooRealVar('p2','p2',5,0.,60.)
    #p3 = RooRealVar('p3','p3',0,-10.,10.)
    #background = RooGenericPdf('background','(1/2)*( 1 + TMath::Erf((@0-507.1)/94.2))*(pow(1-@0/%.1f,@1)/pow(@0/%.1f,@2+@3*log(@0/%.1f)))'%(sqrtS,sqrtS,sqrtS),RooArgList(mjj,p1,p2,p3))
    #background.Print()

    # fit
    num_regions = 1.0
    if doBlind:
        num_regions = 2.0
    # res_b = background_ext.fitTo(h_data_roo, RooFit.Range("RangeLow , RangeHigh"),
    #                              RooFit.Extended(kTRUE), RooFit.Save(kTRUE),
    #                              RooFit.Strategy(1))
    if doBlind:
        res_b = background_ext.fitTo(h_data_roo, RooFit.Range("RangeLow,RangeHigh"),
                                     RooFit.Extended(kTRUE), RooFit.Save(kTRUE),
                                     RooFit.Strategy(1))
    else:
        res_b = background_ext.fitTo(h_data_roo, RooFit.Extended(kTRUE),
                                     RooFit.Save(kTRUE), RooFit.Strategy(1))
    res_b.Print()

    # Try roosimultaneous fit

    # fit by hand
    #nll = background_ext.createNLL(h_data_roo,RooFit.Range(" RangeLow , RangeHigh "))
    #m = RooMinuit(nll)
    #m.setVerbose(kTRUE)
    #m.migrad()
    #m.hesse()
    #res_b = m.save()
    #res_b.Print()

    # fit results
    norm_b = res_b.floatParsFinal().find("norm") #normalization in extended LL
    #norm_b = RooRealVar('norm_b','norm_b',dataInt,0.,1e+09) #normalization without extended LL
    # p1_b = res_b.floatParsFinal().find("p1")
    # p2_b = res_b.floatParsFinal().find("p2")
    # p3_b = res_b.floatParsFinal().find("p3")
    p1_b = p1
    p2_b = p2
    p3_b = p3

    background_noNorm = TF1("background_noNorm","( TMath::Power(1-x/%.1f,[0]) ) / ( TMath::Power(x/%.1f,[1]+[2]*log(x/%.1f)) )"%(sqrtS,sqrtS,sqrtS),float(massMin),float(massMax))
    background_noNorm.SetParameter(0,p1_b.getVal())
    background_noNorm.SetParameter(1,p2_b.getVal())
    background_noNorm.SetParameter(2,p3_b.getVal())
    #background_noNorm.SetParameter(3,m_eff.getVal())
    #background_noNorm.SetParameter(4,sigma_eff.getVal())
    #int_b = background_noNorm.Integral(float(massMin),float(massMax))
    int_b = 1.0
    if doBlind:
        int_b = background_noNorm.Integral(float(massMin), float(blindRegionMassMin)) \
              + background_noNorm.Integral(float(blindRegionMassMax), float(massMax))
    else:
        int_b = background_noNorm.Integral(float(massMin), float(massMax))
    print "rescale for background function:", float(int_b)
    p0_b = norm_b.getVal() / (int_b*lumi) * num_regions
    #print "p0_b = " , norm_b.getVal()/int_b , " +" , norm_b.getErrorHi()/int_b , " -" , norm_b.getErrorLo()/int_b
    print "p0_b = " , p0_b , " +" , norm_b.getErrorHi()/int_b*math.sqrt(num_regions) , " -" , norm_b.getErrorLo()/int_b*math.sqrt(num_regions)
    print "p1_b = " , p1_b.getVal() , " +" , p1_b.getErrorHi() , " " , p1_b.getErrorLo()
    print "p2_b = " , p2_b.getVal() , " +" , p2_b.getErrorHi() , " " , p2_b.getErrorLo()
    print "p3_b = " , p3_b.getVal() , " +" , p3_b.getErrorHi() , " " , p3_b.getErrorLo()
    print "m_eff =", m_eff.getVal()
    print "sigma_eff =", sigma_eff.getVal()

    background = TF1("background","( [0]*TMath::Power(1-x/%.1f,[1]) ) / ( TMath::Power(x/%.1f,[2]+[3]*log(x/%.1f)) )"%(sqrtS,sqrtS,sqrtS),float(massMin),float(massMax))
    background.SetParameter(0,p0_b)
    background.SetParameter(1,p1_b.getVal())
    background.SetParameter(2,p2_b.getVal())
    background.SetParameter(3,p3_b.getVal())
    #background.SetParameter(4,m_eff.getVal())
    #background.SetParameter(5,sigma_eff.getVal())

    # plot test
    #canvas_test = TCanvas("canvas")
    #h_data.Draw("p e")
    #background.Draw("same l")

    # data graph
    h_data.Rebin(N_massBins, "h_data_varBin", massBins)
    g_data = TGraphAsymmErrors(h_data_varBin)
    #g_data_events = TGraphAsymmErrors(h_data_varBin)

    alpha = 1-0.6827
    for i in range(0,g_data.GetN()):
        N = g_data.GetY()[i]
        binWidth = g_data.GetEXlow()[i] + g_data.GetEXhigh()[i]
        #print str(g_data.GetX()[i])+" "+
        print str(g_data.GetX()[i]-g_data.GetEXlow()[i])+" "+str(g_data.GetX()[i]+g_data.GetEXhigh()[i])+" "+str(N) 

        L = 0
        if N!=0:
            L = ROOT.Math.gamma_quantile(alpha/2,N,1.)
        U = ROOT.Math.gamma_quantile_c(alpha/2,N+1,1)

        #g_data_events.SetPointEYlow(i, (N-L));
        #g_data_events.SetPointEYhigh(i, (U-N));
        #g_data_events.SetPoint(i, data_obs_TGraph.GetX()[i], N)

        g_data.SetPointEYlow(i, (N-L)/(binWidth * lumi));
        g_data.SetPointEYhigh(i, (U-N)/(binWidth * lumi));
        g_data.SetPoint(i, g_data.GetX()[i], N/(binWidth * lumi))

        if (g_data.GetX()[i]>blindRegionMassMin and g_data.GetX()[i]<blindRegionMassMax):
            g_data.SetPointEYlow(i, 0);
            g_data.SetPointEYhigh(i, 0);
            g_data.SetPoint(i, g_data.GetX()[i], 0)

    # output
    output = TFile(outputLabel+".root","RECREATE");
    h_data.Write()

    list_parameter = [p0_b, p1_b.getVal(), p2_b.getVal(), p3_b.getVal(),
                      m_eff.getVal(), sigma_eff.getVal(),
                      (norm_b.getErrorHi() - norm_b.getErrorLo())/(2.0*int_b)*math.sqrt(num_regions),
                      (p1_b.getErrorHi() - p1_b.getErrorLo())/2.0,
                      (p2_b.getErrorHi() - p2_b.getErrorLo())/2.0,
                      (p3_b.getErrorHi() - p3_b.getErrorLo())/2.0]

    # plot
    h_background = convertFunctionToHisto(background,"h_background",N_massBins,massBins)
    h_fit_residual_vs_mass = TH1D("h_fit_residual_vs_mass","h_fit_residual_vs_mass",N_massBins,massBins)
    list_chi2AndNdf_background = calculateChi2AndFillResiduals(g_data,h_background,h_fit_residual_vs_mass,1)
    drawAndSavePlot_background(g_data,h_background,h_fit_residual_vs_mass,outputLabel, list_chi2AndNdf_background, list_parameter, box)

    # h_fit_residual_vs_mass_unbinned = TH1D("h_fit_residual_vs_mass_unbinned",
    #                                        "h_fit_residual_vs_mass_unbinned",
    #                                        massMax - massMin, massMin, massMax)
    # calculateChi2AndFillResiduals(g_data, h_background,
    #                               h_fit_residual_vs_mass_unbinned, 0)

    # close output

    #raw_input("Press Enter to exit...")
    output.Close()


#==============================================================================


def convertFunctionToHisto(background_,name_,N_massBins_,massBins_):

    background_hist_ = TH1D(name_,name_,N_massBins_,massBins_)

    for bin in range (0,N_massBins_):
        xbinLow = massBins_[bin]
        xbinHigh = massBins_[bin+1]
        binWidth_current = xbinHigh - xbinLow
        value = background_.Integral(xbinLow , xbinHigh) / binWidth_current
        print "{0}: {1} {2} {3} {4}".format(massBins_[bin], xbinLow, xbinHigh,
                                            background_.Integral(xbinLow, xbinHigh),
                                            value)
        background_hist_.SetBinContent(bin+1,value)

    return background_hist_


def calculateChi2AndFillResiduals(data_obs_TGraph_,background_hist_,hist_fit_residual_vsMass_,prinToScreen_=0):
    
    print "-- "+str(background_hist_.GetName())

    N_massBins_ = data_obs_TGraph_.GetN()

    chi2_FullRangeAll = 0
    chi2_PlotRangeAll = 0
    chi2_PlotRangeNonZero = 0
    chi2_PlotRangeMinNumEvents = 0 

    N_FullRangeAll = 0
    N_PlotRangeAll = 0
    N_PlotRangeNonZero = 0
    N_PlotRangeMinNumEvents = 0 

    if(prinToScreen_):
        print ""
        print ""
        print "======== Number of events / GeV (data, errors, fit, residuals) ========"            
        print ""

    for bin in range (0,N_massBins_):

        ## Values and errors

        value_data = data_obs_TGraph_.GetY()[bin]
        err_low_data = data_obs_TGraph_.GetEYlow()[bin]
        err_high_data = data_obs_TGraph_.GetEYhigh()[bin]
        xbinCenter = data_obs_TGraph_.GetX()[bin] 
        xbinLow = data_obs_TGraph_.GetX()[bin]-data_obs_TGraph_.GetEXlow()[bin] 
        xbinHigh = data_obs_TGraph_.GetX()[bin]+data_obs_TGraph_.GetEXhigh()[bin]
        binWidth_current = xbinHigh - xbinLow
        #value_fit = background_.Integral(xbinLow , xbinHigh) / binWidth_current
        value_fit = background_hist_.GetBinContent(bin+1)
        
        ## Fit residuals

        err_tot_data = 0
        if (value_fit >= value_data):
            err_tot_data = err_high_data  
        else:
            err_tot_data = err_low_data  
        if (xbinCenter<blindRegionMassMin or xbinCenter>blindRegionMassMax):   
            fit_residual = (value_data - value_fit) / err_tot_data
            err_fit_residual = 1
        else:
            fit_residual = 0
            err_fit_residual = 0

        ## Fill histo with residuals

        hist_fit_residual_vsMass_.SetBinContent(bin+1,fit_residual)
        hist_fit_residual_vsMass_.SetBinError(bin+1,err_fit_residual)

        ## Chi2

        chi2_FullRangeAll += pow(fit_residual,2)
        N_FullRangeAll += 1
        if (xbinLow >= massMin and xbinHigh<=massMax):
            chi2_PlotRangeAll += pow(fit_residual,2)
            N_PlotRangeAll += 1
            if (value_data > 0):
                chi2_PlotRangeNonZero += pow(fit_residual,2)
                N_PlotRangeNonZero += 1
                if(value_data * binWidth_current * lumi > MinNumEvents):
                    chi2_PlotRangeMinNumEvents += pow(fit_residual,2)
                    N_PlotRangeMinNumEvents += 1
    
        if(prinToScreen_):
            print str(xbinLow)+" "+str(xbinHigh)+" "+str(binWidth_current)+" : "+str(value_data)+" "+str(value_data * binWidth_current * lumi)+" - "+str(err_low_data)+" + "+str(err_high_data)+" fit: "+str(value_fit)+" fit residual: "+str(fit_residual) 

    #==================
    # Calculate chi2/ndf
    #==================

    # ndf
    ndf_FullRangeAll = N_FullRangeAll - nParFit    
    ndf_PlotRangeAll = N_PlotRangeAll - nParFit    
    ndf_PlotRangeNonZero = N_PlotRangeNonZero - nParFit    
    ndf_PlotRangeMinNumEvents = N_PlotRangeMinNumEvents - nParFit    

    chi2_ndf_FullRangeAll = chi2_FullRangeAll / ndf_FullRangeAll
    chi2_ndf_PlotRangeAll = chi2_PlotRangeAll / ndf_PlotRangeAll
    chi2_ndf_PlotRangeNonZero = chi2_PlotRangeNonZero / ndf_PlotRangeNonZero
    chi2_ndf_PlotRangeMinNumEvents = chi2_PlotRangeMinNumEvents / ndf_PlotRangeMinNumEvents

    print "chi2/ndf FullRangeAll : %.8f / %d = %.2f" % ( chi2_FullRangeAll , ndf_FullRangeAll , chi2_ndf_FullRangeAll ) 
    print "chi2/ndf PlotRangeAll : %.1f / %d = %.2f" % ( chi2_PlotRangeAll , ndf_PlotRangeAll , chi2_ndf_PlotRangeAll ) 
    print "chi2/ndf PlotRangeNonZero : %.1f / %d = %.2f" % ( chi2_PlotRangeNonZero , ndf_PlotRangeNonZero , chi2_ndf_PlotRangeNonZero ) 
    print "chi2/ndf PlotRangeMinNumEvents : %.1f / %d = %.2f" % ( chi2_PlotRangeMinNumEvents , ndf_PlotRangeMinNumEvents , chi2_ndf_PlotRangeMinNumEvents ) 

    return [chi2_FullRangeAll, ndf_FullRangeAll, chi2_PlotRangeAll, ndf_PlotRangeAll, chi2_PlotRangeNonZero, ndf_PlotRangeNonZero, chi2_PlotRangeMinNumEvents, ndf_PlotRangeMinNumEvents]


def drawAndSavePlot_background(data_obs_TGraph_,background_TH1_,hist_fit_residual_vsMass_,outputLabel_, list_chi2AndNdf_, list_parameter_, box):

    global minY, maxY

    canvas = TCanvas("canvas","canvas",W,H)
    canvas.GetWindowHeight()
    canvas.GetWindowWidth()
    #canvas.SetLogy()
    canvas.SetTitle("")
    canvas.Divide(1,2,0,0,0)

    #pad1 - data spectrum
    canvas.cd(1)
    pad_1 = canvas.GetPad(1)
    #pad_1.SetPad(0.01,0.26,0.99,0.98) #FIXME
    pad_1.SetPad(0.01,0.36,0.99,0.98)
    pad_1.SetLogy()


    if 'PF' in box :
        pad_1.SetLogx()

    pad_1.SetRightMargin(0.05)
    pad_1.SetTopMargin(0.05)
    pad_1.SetFillColor(0)
    pad_1.SetBorderMode(0)
    pad_1.SetFrameFillStyle(0)
    pad_1.SetFrameBorderMode(0)



    if fixedRange==1 and showCrossSection==1:
        minY = 0.0000001/lumi
        #minY = 10.0/lumi
        maxY = data_obs_TGraph_.GetY()[0]*100
        
    #vFrame = pad_1.DrawFrame(minX_mass_plot,0.0001/lumi,maxX_mass_plot,data_obs_TGraph_.GetY()[0]*10)
    vFrame = pad_1.DrawFrame(massMin,minY,massMax,maxY)
    vFrame.SetTitle("")
    #vFrame.SetXTitle(xaxisTitle)
    #vFrame.SetYTitle(yaxisTitle_main)
    vFrame.GetXaxis().SetTitleSize(0.06)
    vFrame.GetXaxis().SetTitleOffset(0.95)
    #vFrame.GetXaxis().SetLabelSize(0.05)
    vFrame.GetYaxis().SetTitleSize(0.06)
    #vFrame.GetYaxis().SetTitleOffset(1.0)
    #vFrame.GetYaxis().SetLabelSize(0.05)

    #style data spectrum    
    gStyle.SetErrorX(1)

    data_obs_TGraph_.SetMarkerStyle(20)
    data_obs_TGraph_.SetMarkerColor(1)
    data_obs_TGraph_.SetLineColor(1)
    data_obs_TGraph_.SetTitle("")
    data_obs_TGraph_.GetXaxis().SetTitle(xaxisTitle)
    data_obs_TGraph_.GetYaxis().SetTitle(yaxisTitle_main)
    data_obs_TGraph_.GetXaxis().SetLimits(massMin,massMax)
    #data_obs_TGraph_.GetYaxis().SetRangeUser(0.0001/lumi,data_obs_TGraph_.GetY()[0]*10)
    data_obs_TGraph_.GetYaxis().SetRangeUser(minY,maxY)

    #style background function
    background_TH1_.SetLineColor(2)
    background_TH1_.SetLineWidth(2)
    background_TH1_.SetTitle("")
    background_TH1_.GetXaxis().SetTitle(xaxisTitle)
    background_TH1_.GetYaxis().SetTitle(yaxisTitle_main)
    background_TH1_.GetXaxis().SetLimits(massMin,massMax)
    background_TH1_.GetYaxis().SetRangeUser(minY,maxY)

    #draw objects
    #data_obs_TGraph_.Draw("A P E0")
    #background_TH1_.Draw("C SAME")
    background_TH1_.Draw("C")
    data_obs_TGraph_.Draw("P E0 SAME")

    #draw text
    pave_general = TPaveText(0.666772,0.794229,0.83557,0.940972,"NDC")
    pave_general.AddText("background fit")
    pave_general.SetFillColor(0)
    pave_general.SetLineColor(1)
    pave_general.SetFillStyle(0)
    pave_general.SetBorderSize(0)
    pave_general.SetTextFont(42)
    pave_general.SetTextSize(0.040)
    pave_general.SetTextAlign(12)
    pave_general.SetTextColor(1)
    pave_general.Draw("SAME")

    #draw text
    pave_sel = TPaveText(0.229489,0.0817972,0.464046,0.254608,"NDC")
    pave_sel.SetFillColor(0)
    pave_sel.SetBorderSize(0)
    pave_sel.SetFillStyle(0)

    if 'PF' in box:
        pave_sel.AddText(0.5,1.2,"Wide PF Jets")
    else:
        pave_sel.AddText(0.5,1.2,"Wide Calo Jets")

    pave_sel.AddText(0.5,0.5,str(massMin)+" < m_{jj} < "+str(massMax))
    pave_sel.AddText(0.5,0.,"|#eta| < 2.5, |#Delta#eta| < 1.3")
    pave_sel.Draw("SAME")

    pave_chi2 = TPaveText(0.229489,0.3,0.55,0.35,"NDC")
    pave_chi2.SetFillColor(0)
    pave_chi2.SetBorderSize(0)
    pave_chi2.SetFillStyle(0)
    pave_chi2.AddText(0.5, 0.0,
                      "#chi^{{2}} / ndf = {0:.1f} / {1:d} = {2:.1f}".format(
                          list_chi2AndNdf_[4], list_chi2AndNdf_[5],
                          list_chi2AndNdf_[4]/list_chi2AndNdf_[5]))
    pave_chi2.Draw("SAME")

    pave_fit = TPaveText(0.47,0.082,0.8,0.25,"NDC")
    pave_fit.SetFillColor(0)
    pave_fit.SetBorderSize(0)
    pave_fit.SetFillStyle(0)
    pave_fit.AddText(0.5, 0.8, "p0 = {0:.4g} #pm {1:.4g}".format(list_parameter_[0], list_parameter_[6]))
    pave_fit.AddText(0.5, 0.6, "p1 = {0:.3f} #pm {1:.3f}".format(list_parameter_[1], list_parameter_[7]))
    pave_fit.AddText(0.5, 0.4, "p2 = {0:.3f} #pm {1:.3f}".format(list_parameter_[2], list_parameter_[8]))
    pave_fit.AddText(0.5, 0.2, "p3 = {0:.3f} #pm {1:.3f}".format(list_parameter_[3], list_parameter_[9]))
    #pave_fit.AddText(0.5, 0.05, "m_{{eff}} = {0:.1f}".format(list_parameter_[4]))
    #pave_fit.AddText(0.5, 0.0, "#sigma_{{eff}} = {0:.1f}".format(list_parameter_[5]))
    pave_fit.Draw("SAME")

    # pave_toy = TPaveText(0.6,0.4,0.9,0.6,"NDC")
    # pave_toy.SetFillColor(0)
    # pave_toy.SetBorderSize(0)
    # pave_toy.SetFillStyle(0)
    # pave_toy.SetTextColor(2)
    # pave_toy.AddText(0.5, 0.0, "Toy MC (sbtoy1)")
    # pave_toy.Draw("SAME")

    #draw legend
    leg = TLegend(0.6564991,0.58,0.9203575,0.835812)
    leg.SetTextSize(0.03546853)
    leg.SetLineColor(0)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetMargin(0.35)
    leg.AddEntry(data_obs_TGraph_,"data" ,"EPL")
    leg.AddEntry(background_TH1_,"background","L")
    leg.Draw("SAME")

    #draw pad
    pad_1.RedrawAxis()
    pad_1.Update()
    pad_1.GetFrame().Draw()
    CMS_lumi.CMS_lumi(pad_1, iPeriod, iPos)


    #pad2 - residuals
    canvas.cd(2)
    pad_2 = canvas.GetPad(2)
    #pad_2.SetPad(0.01,0.02,0.99,0.27) #FIXME
    pad_2.SetPad(0.01,0.02,0.99,0.37)
    pad_2.SetBottomMargin(0.35)
    pad_2.SetRightMargin(0.05)
    pad_2.SetGridx()
    pad_2.SetGridy()


    if 'PF' in box:
        pad_2.SetLogx()



    vFrame2 = pad_2.DrawFrame(massMin, -range_residual, massMax, +range_residual)    
    vFrame2.SetTitle("")
    vFrame2.SetXTitle(xaxisTitle)
    vFrame2.GetXaxis().SetTitleSize(0.06)
    vFrame2.SetYTitle(yaxisTitle_secondary)
    vFrame2.GetYaxis().SetTitleSize(0.12)
    vFrame2.GetYaxis().SetTitleOffset(0.40)
    vFrame2.GetYaxis().SetLabelSize(0.05)
    vFrame2.GetXaxis().SetTitleSize(0.15)
    vFrame2.GetXaxis().SetTitleOffset(0.90)
    vFrame2.GetXaxis().SetLabelSize(0.06)

    #style residuals
    hist_fit_residual_vsMass_.GetXaxis().SetRangeUser(massMin,massMax)
    hist_fit_residual_vsMass_.GetYaxis().SetRangeUser(-range_residual,+range_residual)
    hist_fit_residual_vsMass_.GetYaxis().SetNdivisions(206,kFALSE)
    hist_fit_residual_vsMass_.SetLineWidth(0)
    hist_fit_residual_vsMass_.SetFillColor(2)
    hist_fit_residual_vsMass_.SetLineColor(1)
    hist_fit_residual_vsMass_.Draw("SAME HIST")


    if 'PF' in box:
        vFrame2.SetXTitle("Dijet Mass [TeV]")

        xLab = TLatex()
        xLab.SetTextAlign(22)
        xLab.SetTextFont(42)
        xLab.SetTextSize(2*0.05)

        xLab.DrawLatex(2000, -4, "2")
        xLab.DrawLatex(3000, -4, "3")
        xLab.DrawLatex(4000, -4, "4")
        xLab.DrawLatex(5000, -4, "5")
        xLab.DrawLatex(6000, -4, "6")
        xLab.DrawLatex(7000, -4, "7")
        xLab.DrawLatex(8000, -4, "8")


    line = TLine(massMin,0,massMax,0)
    line.Draw("")

    #============

    #write canvas
    canvas.SaveAs(outputLabel_+".root")
    canvas.SaveAs(outputLabel_+".pdf")



#==============================================================================



if __name__ == '__main__':
    main()
