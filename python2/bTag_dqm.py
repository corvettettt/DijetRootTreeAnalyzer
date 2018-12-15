from optparse import OptionParser
from framework import Config
from rootTools import tdrstyle as setTDRStyle

import ROOT as rt
from array import array
import numpy as np
import sys, os, math

usage = """usage: python python/bTag_dqm.py -c config/bTag.cfg -b BTag2016_dqm"""


massBins_list = [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430, 10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000]


def customRebin(histo):
    massBins_list_actual = []
    massMin = histo.GetBinLowEdge(1)
    massMax = histo.GetBinLowEdge(histo.GetNbinsX())+histo.GetBinWidth(1)
    firstBin = -1
    lastBin = -1
    index_bin_boundary=-1
    for bin_boundary in massBins_list:
        index_bin_boundary = index_bin_boundary+1
        if (bin_boundary>=massMin and firstBin==-1 ):
            massMin = bin_boundary
            firstBin=1
            #print "FIRST BIN is "+str(massMin)
        if (bin_boundary>(massMax+0.0000000001) and lastBin==-1 ):
            massMax = massBins_list[index_bin_boundary-1]
            lastBin=1
            #print "LAST BIN is "+str(massMax)
        if (bin_boundary>=massMin and bin_boundary<=massMax):
            massBins_list_actual.append(bin_boundary)
    #print "===>>> Rebinning: ",histo.GetName(),massBins_list_actual
    massBins = array("d",massBins_list_actual)
    N_massBins = len(massBins)-1
    hNew = histo.Rebin(N_massBins, "hNew", massBins) 
    return hNew


def setBinning(histos):
    for k,h in histos.iteritems():
        if 'mjj' in k:
            hNew = customRebin(h)
            histos[k] = hNew
        elif 'pt' in k:
            h.Rebin(4)
        elif 'phi' in k:
            h.SetMinimum(0)


def setRecoStyle(histos):
    for k,h in histos.iteritems():
        h.SetMarkerColor(rt.kRed)
        h.SetLineColor(rt.kRed)

def setCaloStyle(histo):
    for k,h in histos.iteritems():
        h.SetMarkerColor(rt.kBlack)
        h.SetLineColor(rt.kBlack)

def computeRatio(h1,h2):

    h1.Sumw2()
    h2.Sumw2()

    ratio = rt.TH1F()

    xBuff = h1.GetXaxis().GetXbins().GetArray()
    xBuff.SetSize(h1.GetXaxis().GetNbins()+1)
    xArr = array('d',xBuff)
    if len(xArr) > 0:
        ratio = rt.TH1F("tmp","tmp",h1.GetXaxis().GetNbins(),xArr)
    else:
        ratio = rt.TH1F("tmp","tmp",h1.GetNbinsX(),h1.GetBinLowEdge(1),h1.GetBinLowEdge(h1.GetNbinsX())+h1.GetBinWidth(1))
        
    ratio.Sumw2()
    for bin in range(h1.GetNbinsX()):
        if h1.GetBinContent(bin+1) == 0 or h2.GetBinContent(bin+1) == 0:
            continue
        else:
            
            valh1 = h1.GetBinContent(bin+1)
            valh2 = h2.GetBinContent(bin+1)
            sigmah1 = h1.GetBinError(bin+1)
            sigmah2 = h2.GetBinError(bin+1)
            ratio.SetBinContent(bin+1,valh1/valh2)
            ratio.SetBinError(bin+1,math.sqrt((sigmah1/valh2)*(sigmah1/valh2) + (valh1*sigmah2/valh2/valh2)*(valh1*sigmah2/valh2/valh2)))


    return ratio



def simplePrint(histos, outFolder):
    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    for k,h in histos.iteritems():
        cc = rt.TCanvas();
        cc.SetGridx()
        cc.SetGridy()
        if ('mjj' in k or 'pt' in k) and not 'eff' in k:
            cc.SetLogy()

        h.Draw()

        #custom ranges
        rt.gPad.Update()
        if 'eff_mjj_btag0' in k:
            h.GetPaintedGraph().GetYaxis().SetRangeUser(0,1)
        elif 'eff_mjj_btag1' in k:
            h.GetPaintedGraph().GetYaxis().SetRangeUser(0,0.6)
        elif 'eff_mjj_btag2' in k:
            h.GetPaintedGraph().GetYaxis().SetRangeUser(0,0.1)


        cc.Print(outFolder+"/"+k+".pdf","pdf")




def overlayAndPrint(reco, calo, outFolder):
    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    for k,h in calo.iteritems():
        cc = rt.TCanvas();
        leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
        leg.AddEntry(h,"calo","L")
        leg.AddEntry(reco[k],"reco","L")


        #no ratio for efficiencies
        if 'eff' in k:
            cc.SetGridx()
            cc.SetGridy()
            h.Draw()
            reco[k].Draw("sames")
            leg.Draw("sames")

            rt.gPad.Update();
            graph = h.GetPaintedGraph()
            graph.SetMinimum(0)

            if graph.GetHistogram().GetMaximum() < reco[k].GetPaintedGraph().GetHistogram().GetMaximum():
                graph.SetMaximum(reco[k].GetPaintedGraph().GetHistogram().GetMaximum())
                rt.gPad.Update();


            cc.Print(outFolder+"/"+k+".pdf","pdf")
            continue


        #set Max and Min
        if h.GetMaximum() > reco[k].GetMaximum():
            h.GetYaxis().SetRangeUser(0,h.GetMaximum()+2000)
        else:
            h.GetYaxis().SetRangeUser(0,reco[k].GetMaximum()+2000)

        p1 = rt.TPad("p1","p1",0., 0.25, 1., 1.)
        p2 = rt.TPad("p2","p2",0., 0., 1., 0.25)
        p1.Draw()
        p2.Draw()

        #pad1
        p1.cd()
        p1.SetGridx()
        p1.SetGridy()

        h.Draw("HISTO,E")
        reco[k].Draw("HISTO,esames")
        leg.Draw("same")

        #pad2
        p2.cd()
        p2.SetGridx()
        p2.SetGridy()

        ratioHisto = computeRatio(h,reco[k])
        
        ratioHisto.GetYaxis().SetRangeUser(0., 2.);
        ratioHisto.Draw("P")

        line = rt.TF1("line", "1.", -1000000., 1000000.)
        line.SetLineWidth(2)
        line.SetLineColor(rt.kRed)
        line.Draw("same")

        cc.Print(outFolder+"/"+k+".pdf","pdf")
        ratioHisto.Delete()


def fillEfficiency(histoList):
    #PT
    eff_pt_j1_btag_tight = rt.TEfficiency(histoList['pt_j1_btag_tight'],histoList['pt_j1'])
    eff_pt_j1_btag_tight.SetName("eff_pt_j1_btag_tight")
    eff_pt_j2_btag_tight = rt.TEfficiency(histoList['pt_j2_btag_tight'],histoList['pt_j2'])
    eff_pt_j2_btag_tight.SetName("eff_pt_j2_btag_tight")
    eff_pt_j1_btag_medium = rt.TEfficiency(histoList['pt_j1_btag_medium'],histoList['pt_j1'])
    eff_pt_j1_btag_medium.SetName("eff_pt_j1_btag_medium")
    eff_pt_j2_btag_medium = rt.TEfficiency(histoList['pt_j2_btag_medium'],histoList['pt_j2'])
    eff_pt_j2_btag_medium.SetName("eff_pt_j2_btag_medium")
    histoList[eff_pt_j1_btag_tight.GetName()] = eff_pt_j1_btag_tight
    histoList[eff_pt_j2_btag_tight.GetName()] = eff_pt_j2_btag_tight
    histoList[eff_pt_j1_btag_medium.GetName()] = eff_pt_j1_btag_medium
    histoList[eff_pt_j2_btag_medium.GetName()] = eff_pt_j2_btag_medium
            
    #MJJ
    eff_mjj_btag0_tight = rt.TEfficiency(histoList['mjj_btag0_tight'],histoList['mjj'])
    eff_mjj_btag0_tight.SetName("eff_mjj_btag0_tight")
    eff_mjj_btag1_tight = rt.TEfficiency(histoList['mjj_btag1_tight'],histoList['mjj'])
    eff_mjj_btag1_tight.SetName("eff_mjj_btag1_tight")
    eff_mjj_btag2_tight = rt.TEfficiency(histoList['mjj_btag2_tight'],histoList['mjj'])
    eff_mjj_btag2_tight.SetName("eff_mjj_btag2_tight")
    histoList[eff_mjj_btag0_tight.GetName()] = eff_mjj_btag0_tight
    histoList[eff_mjj_btag1_tight.GetName()] = eff_mjj_btag1_tight
    histoList[eff_mjj_btag2_tight.GetName()] = eff_mjj_btag2_tight
    
    eff_mjj_btag0_medium = rt.TEfficiency(histoList['mjj_btag0_medium'],histoList['mjj'])
    eff_mjj_btag0_medium.SetName("eff_mjj_btag0_medium")
    eff_mjj_btag1_medium = rt.TEfficiency(histoList['mjj_btag1_medium'],histoList['mjj'])
    eff_mjj_btag1_medium.SetName("eff_mjj_btag1_medium")
    eff_mjj_btag2_medium = rt.TEfficiency(histoList['mjj_btag2_medium'],histoList['mjj'])
    eff_mjj_btag2_medium.SetName("eff_mjj_btag2_medium")
    histoList[eff_mjj_btag0_medium.GetName()] = eff_mjj_btag0_medium
    histoList[eff_mjj_btag1_medium.GetName()] = eff_mjj_btag1_medium
    histoList[eff_mjj_btag2_medium.GetName()] = eff_mjj_btag2_medium  
        
        


if __name__ == '__main__':

    ###################################################################
    parser = OptionParser(usage=usage)
    parser.add_option('-c','--config',dest="config",type="string",default="config/bTag.cfg",
                  help="Name of the config file to use")
    parser.add_option('-b','--box',dest="box", default="BTag2016_dqm",type="string",
                  help="box name")
    
    rt.RooMsgService.instance().setGlobalKillBelow(rt.RooFit.FATAL)

    (options,args) = parser.parse_args()

    cfg = Config.Config(options.config)
    box = options.box

    inputDataHistos     = cfg.getVariables(box,"inputDataHistos")
    outFolder           = cfg.getVariables(box,"outputFolder")
    
    ###################################################################

    #set style and plot
    rt.gROOT.SetBatch()
    setTDRStyle.setTDRStyle()

    inputDataFile = rt.TFile(inputDataHistos)
    names = [k.GetName() for k in inputDataFile.GetListOfKeys()]

    recoList = {}
    caloList = {}
    corrList = {}
    for hist in names:
        if 'caloVSreco' in hist:
            myTH1 = inputDataFile.Get(hist)
            myTH1.SetDirectory(0)
            corrList[hist.replace('_caloVSreco','')] = myTH1
        elif 'reco' in hist:
            myTH1 = inputDataFile.Get(hist)
            myTH1.SetDirectory(0)
            recoList[hist.replace('_reco','')] = myTH1
        elif 'calo' in hist:
            myTH1 = inputDataFile.Get(hist)
            myTH1.SetDirectory(0)
            caloList[hist.replace('_calo','')] = myTH1


    doCalo = len(caloList) > 0
    doReco = len(recoList) > 0

    if not doCalo and not doReco:
        print "no plots found"
        exit

    
    if doCalo:
        setBinning(caloList)
        fillEfficiency(caloList)
        setCaloStyle(caloList)

    if doReco:
        setBinning(recoList)
        fillEfficiency(recoList)
        setRecoStyle(recoList)


    if doCalo and doReco:
        overlayAndPrint(recoList,caloList,outFolder)
    elif doCalo:
        simplePrint(caloList,outFolder)
    elif doReco:
        simplePrint(recoList,outFolder)
    
    
    
