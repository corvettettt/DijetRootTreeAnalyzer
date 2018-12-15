from optparse import OptionParser
import ROOT as rt
import rootTools
from framework import Config
from array import *
import os
import random
import sys
import math
from scipy.integrate import quad
from itertools import *
from operator import *
from RunCombine import massIterable

def setStyle():
    rt.gStyle.SetOptStat(0)
    rt.gStyle.SetOptTitle(0)
    rt.gStyle.SetPaintTextFormat("1.2g")
    rt.gROOT.SetBatch()
    rt.RooMsgService.instance().setGlobalKillBelow(rt.RooFit.FATAL)

def getBiasHistos(varName,toyTree):        
    
    h = rt.TH1D('h_bias','h_bias',25,-4,4)
    ## toyTree.Draw('(muLoErr+muHiErr)/2.>>hErr(10000)')    
    ## hErr = rt.gPad.GetPrimitive("hErr")
    
    ## muErrLow = -1
    ## muErrHigh = 999999999
    ## try:
    ##     mean = hErr.GetMean()
    ##     mode = hErr.GetXaxis().GetBinCenter(hErr.GetMaximumBin())
    ##     rms = hErr.GetRMS()
    ##     nprobSum = int(2.0)
    ##     probSum = array("d",[0.,0.7])
    ##     q = array("d",[0,0])
    ##     hErr.GetQuantiles(nprobSum,q,probSum)
    ##     muErrLow = q[0]
    ##     muErrHigh = q[1]
    ## except:
    ##     pass
    
    toyTree.Project('h_bias','%s'%(varName),'(muHiErr+mu)<19&&(mu-muLoErr)>-19')

    return h

def getBiasDivRHistos(varName,toyTree):        
    
    h = rt.TH1D('h_bias','h_bias',25,-1.5,1.5)
    ## toyTree.Draw('(muLoErr+muHiErr)/2.>>hErr(10000)')    
    ## hErr = rt.gPad.GetPrimitive("hErr")
    
    ## muErrLow = -1
    ## muErrHigh = 999999999
    ## try:
    ##     mean = hErr.GetMean()
    ##     mode = hErr.GetXaxis().GetBinCenter(hErr.GetMaximumBin())
    ##     rms = hErr.GetRMS()
    ##     nprobSum = int(2.0)
    ##     probSum = array("d",[0.,0.7])
    ##     q = array("d",[0,0])
    ##     hErr.GetQuantiles(nprobSum,q,probSum)
    ##     muErrLow = q[0]
    ##     muErrHigh = q[1]
    ## except:
    ##     pass
    
    toyTree.Project('h_bias','%s'%(varName),'(muHiErr+mu)<19&&(mu-muLoErr)>-19')

    return h

def setHist(h_data,xTitle,yTitle,color=rt.kBlack):
    h_data.SetMarkerColor(color)
    h_data.SetLineColor(color)
    h_data.SetMarkerStyle(20)
    h_data.SetLineColor(color)
    h_data.GetXaxis().SetTitle(xTitle)
    h_data.GetYaxis().SetTitle(yTitle)
    #h_data.GetXaxis().SetLabelOffset(0.16)
    h_data.GetXaxis().SetLabelSize(0.05)
    h_data.GetYaxis().SetLabelSize(0.05)
    h_data.GetXaxis().SetTitleSize(0.06)
    h_data.GetYaxis().SetTitleSize(0.06)
    h_data.GetXaxis().SetTitleOffset(0.8)
    h_data.GetYaxis().SetTitleOffset(1)
    #h_data.SetMaximum(200)
    h_data.SetMaximum(2.*h_data.GetMaximum())
    #h_data.SetMinimum(2e-1)
    return h_data

    
def print1DBias(c,rootFile,h,func,printName,xTitle,yTitle,lumiLabel="",boxLabel="",plotLabel="",tLeg=None):

    #c.SetLogy(1)
    setHist(h,xTitle,yTitle)
    
    #h.SetLineWidth(2)    
    h.Draw("pe")
    if func!=None:
        #npoints = 1000
        #listx = []
        #listy = []
        #xmin = h.GetXaxis().GetXmin()
        #xmax = h.GetXaxis().GetXmax()
        #for ix in range(0,npoints+1):
        #    x = xmin+ix*(xmax-xmin)/npoints
        #    listx.append(x)
        #    listy.append(h.GetEntries()*func.Eval(x)/func.Integral(xmin,xmax))     
        #graph = rt.TGraph(npoints, array('d',listx), array('d',listy))
        #graph.SetLineColor(rt.kRed)
        #graph.SetLineWidth(2)
        #graph.Draw("same")
        h.Fit(func,"mle")
        #h.Fit(func,"")
        func.Draw("same")
    

        
    tLeg = rt.TLegend(0.55,0.6,0.89,0.89)
    tLeg.SetLineColor(rt.kWhite)
    tLeg.SetLineWidth(0)
    tLeg.SetFillStyle(0)
    tLeg.AddEntry(h,"#splitline{Pseudodata}{%s (%s GeV) #mu=%1.3f}"%(options.model, massPoint,rDict[int(massPoint)]),"lep")
    tLeg.AddEntry(func,"#splitline{Gaussian fit}{mean = %+1.2f, s.d. = %1.2f}"%(func.GetParameter(1),func.GetParameter(2)),"l")
            
    tLeg.Draw("same")

    l = rt.TLatex()
    l.SetTextAlign(11)
    l.SetTextSize(0.06)
    l.SetTextFont(62)
    l.SetNDC()
    l.DrawLatex(0.12,0.91,"CMS")
    l.SetTextSize(0.05)
    l.SetTextFont(52)
    l.DrawLatex(0.23,0.91,"Preliminary")
    l.SetTextFont(42)
    l.DrawLatex(0.62,0.91,"%s"%lumiLabel)
    l.SetTextFont(52)
    l.SetTextSize(0.045)

    pdf_dict = {'modexp':'5-par. mod. exp.',
                'atlas':'5-par. ATLAS/UA2',
                'fourparam':'4-par. dijet',
                'fiveparam':'5-par. dijet'
                }
    l.DrawLatex(0.15,0.82,'gen. pdf = %s'%pdf_dict[options.genPdf])
    l.DrawLatex(0.15,0.77,'fit pdf = %s'%pdf_dict[options.fitPdf])

    c.cd()
    
    c.Print(printName)
    c.Print(os.path.splitext(printName)[0]+'.C')
    cWrite = c.Clone(os.path.splitext(printName)[0].split('/')[-1])
    rootFile.cd()
    c.Write(os.path.splitext(printName)[0].split('/')[-1])

    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c','--config',dest="config",type="string",default="config/dijet_bias.config",
                  help="Name of the config file to use")
    parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
                  help="Output directory to store results")
    parser.add_option('-l','--lumi',dest="lumi", default=12910.,type="float",
                  help="integrated luminosity in pb^-1")
    parser.add_option('-b','--box',dest="box", default="CaloDijet2016",type="string",
                  help="box name")
    parser.add_option('-m','--model',dest="model", default="qq",type="string",
                  help="signal model name")
    parser.add_option('--mass',dest="mass", default='750',type="string",
                  help="mass of resonance")
    parser.add_option('-r',dest="r",default=1,type="float",
                  help="expect signal r value")
    parser.add_option('--gen-pdf',dest="genPdf", default="modexp", choices=['modexp','fourparam','fiveparam','atlas'],
                  help="pdf for generating")
    parser.add_option('--fit-pdf',dest="fitPdf", default="fourparam", choices=['modexp','fourparam','fiveparam','atlas'],
                  help="pdf for fitting")
    parser.add_option('--asymptotic-file',dest="asymptoticFile",default=None,type="string",
                  help="load asymptotic cross section results file")
    parser.add_option('--xsec',dest="xsec",default=10,type="float",
                  help="xsec for signal in pb (r = 1)")
    
    (options,args) = parser.parse_args()
     
    setStyle()
    
    box = options.box
    lumi = options.lumi
    cfg = Config.Config(options.config)


    xsecTree = None
    rDict = {}
    if options.asymptoticFile is not None:
        print "INFO: Input ref xsec file!"
        asymptoticRootFile = rt.TFile.Open(options.asymptoticFile,"READ")
        xsecTree = asymptoticRootFile.Get("xsecTree")        
        xsecTree.Draw('>>elist','','entrylist')
        elist = rt.gDirectory.Get('elist')
        entry = -1
        while True:
            entry = elist.Next()
            if entry == -1: break
            xsecTree.GetEntry(entry)
            rDict[int(eval('xsecTree.mass'))] = eval('xsecTree.xsecULExp_%s'%box)/options.xsec
    else:        
        for massPoint in massIterable(options.mass):   
            rDict[int(massPoint)] = options.r
    print rDict

    
    c = rt.TCanvas('c','c',500,400)    
    c.SetLeftMargin(0.12) 
    c.SetBottomMargin(0.12)
    rootFile = rt.TFile.Open(options.outDir + '/' + 'Plots_%s'%box + '.root','recreate')
    tdirectory = rootFile.GetDirectory(options.outDir)
    if tdirectory==None:
        rootFile.mkdir(options.outDir)
        tdirectory = rootFile.GetDirectory(options.outDir)
        
    dataString = "Sim. Data"
    eventsLabel = "Pseudodatasets"    
    x = array('d', cfg.getBinning(box)[0]) # mjj binning
    nBins = (len(x)-1)
    
    btagLabel = ""

    lumiLabel = "%.1f fb^{-1} (13 TeV)" % (lumi/1000.)
    boxLabel = ''    

    graph = rt.TGraphErrors(len(massIterable(options.mass)))
    graph_divr = rt.TGraphErrors(len(massIterable(options.mass)))
    histVsMass = rt.TH1D('histVsMass','histVsMass',100,int(massIterable(options.mass)[0])-100,int(massIterable(options.mass)[-1])+100)
    
    for i, massPoint in enumerate(massIterable(options.mass)):
        inputToyFile = '%s/mlfit%s_%s_lumi-%.3f_r-%.3f_%s_%s_%s.root'%(options.outDir,options.model,massPoint,(options.lumi/1000.),rDict[int(massPoint)],box,options.genPdf,options.fitPdf) 
        toyTree = rt.TChain("tree_fit_sb")
        toyTree.Add(inputToyFile)
        toyTree.Print()

        
        h_bias = getBiasHistos('(mu-%.3f)/((muLoErr+muHiErr)/2.)'%rDict[int(massPoint)],toyTree)
        h_bias_divr = getBiasDivRHistos('(mu-%.3f)/(%.3f)'%(rDict[int(massPoint)],rDict[int(massPoint)]),toyTree)
        
        
        gaus_func = rt.TF1("gaus_func","gaus(0)",-4,4)
        #gaus_func.SetParameter(0,100)
        gaus_func.SetParameter(0,20)
        gaus_func.SetParameter(1,0)
        gaus_func.SetParameter(2,1)
        print1DBias(c,tdirectory,h_bias,gaus_func,options.outDir+"/bias_%s_%s_lumi-%s_r-%s_%s_%s_%s.pdf"%(options.model,massPoint,('%.3f'%(options.lumi/1000.)).replace('.','p'),('%.3f'%rDict[int(massPoint)]).replace('.','p'),box,options.genPdf,options.fitPdf),"Bias (#hat{#mu} - #mu)/#sigma_{#mu}",eventsLabel,lumiLabel,boxLabel,'',None)

        graph.SetPoint(i, int(massPoint), 100.*gaus_func.GetParameter(1))
        #graph.SetPointError(i, 0, 100.*gaus_func.GetParameter(2))
        graph.SetPointError(i, 0, 100.*gaus_func.GetParError(1))

        
        gaus_func_divr = rt.TF1("gaus_func","gaus(0)",-1.5,1.5)
        #gaus_func.SetParameter(0,100)
        gaus_func_divr.SetParameter(0,20)
        gaus_func_divr.SetParameter(1,0)
        gaus_func_divr.SetParameter(2,0.5)
        print1DBias(c,tdirectory,h_bias_divr,gaus_func_divr,options.outDir+"/bias_divr_%s_%s_lumi-%s_r-%s_%s_%s_%s.pdf"%(options.model,massPoint,('%.3f'%(options.lumi/1000.)).replace('.','p'),('%.3f'%rDict[int(massPoint)]).replace('.','p'),box,options.genPdf,options.fitPdf),"Bias (#hat{#mu} - #mu)/#mu",eventsLabel,lumiLabel,boxLabel,'',None)
        
        graph_divr.SetPoint(i, int(massPoint), 100.*gaus_func_divr.GetParameter(1))
        #graph.SetPointError(i, 0, 100.*gaus_func.GetParameter(2))
        graph_divr.SetPointError(i, 0, 100.*gaus_func_divr.GetParError(1))

    histVsMass.Draw()
    histVsMass.SetMinimum(-300)
    histVsMass.SetMaximum(300)
    histVsMass.SetLineColor(rt.kBlue)
    histVsMass.SetLineStyle(2)
    histVsMass.SetYTitle("Mean bias [% of stat.+syst. unc. #sigma_{#mu}]")
    histVsMass.GetYaxis().SetTitleOffset(1)
    histVsMass.GetXaxis().SetTitleOffset(0.9)
    histVsMass.SetXTitle("%s resonance mass [GeV]"%options.model)
    histVsMass.GetXaxis().SetTitleSize(0.06)
    histVsMass.GetYaxis().SetTitleSize(0.06)
    histVsMass.GetXaxis().SetLabelSize(0.05)
    histVsMass.GetYaxis().SetLabelSize(0.05)
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.7)
    graph.Draw("pzsame")

    

    l = rt.TLatex()
    l.SetTextAlign(11)
    l.SetTextSize(0.06)
    l.SetTextFont(62)
    l.SetNDC()
    l.DrawLatex(0.12,0.91,"CMS")
    l.SetTextSize(0.05)
    l.SetTextFont(52)
    l.DrawLatex(0.23,0.91,"Preliminary")
    l.SetTextFont(42)
    l.DrawLatex(0.62,0.91,"%s"%lumiLabel)
    l.SetTextFont(52)
    l.SetTextSize(0.045)

    pdf_dict = {'modexp':'5-par. mod. exp.',
                'atlas':'5-par. ATLAS/UA2',
                'fourparam':'4-par. dijet',
                'fiveparam':'5-par. dijet'
                }
    l.DrawLatex(0.15,0.82,'gen. pdf = %s'%pdf_dict[options.genPdf])
    l.DrawLatex(0.15,0.77,'fit pdf = %s'%pdf_dict[options.fitPdf])
    

    c.Print("%s/biasVsMass_%s_lumi-%s_%s_%s_%s.pdf"%(options.outDir,options.model,('%.3f'%(options.lumi/1000.)).replace('.','p'),box,options.genPdf,options.fitPdf))
    c.Print("%s/biasVsMass_%s_lumi-%s_%s_%s_%s.C"%(options.outDir,options.model,('%.3f'%(options.lumi/1000.)).replace('.','p'),box,options.genPdf,options.fitPdf))
    printName = "%s/biasVsMass_%s_lumi-%s_%s_%s_%s"%(options.outDir,options.model,('%.3f'%(options.lumi/1000.)).replace('.','p'),box,options.genPdf,options.fitPdf)
    cWrite = c.Clone(os.path.splitext(printName)[0].split('/')[-1])
    tdirectory.cd()
    c.Write(os.path.splitext(printName)[0].split('/')[-1])

    c.Clear()
    histVsMass.Draw()    
    histVsMass.SetMinimum(-100)
    histVsMass.SetMaximum(100)
    histVsMass.SetYTitle("Mean bias [% of #mu]")
    histVsMass.SetXTitle("%s resonance mass [GeV]"%options.model)
    graph_divr.SetMarkerStyle(20)
    graph_divr.SetMarkerSize(0.7)
    graph_divr.Draw("pzsame")
    l = rt.TLatex()
    l.SetTextAlign(11)
    l.SetTextSize(0.06)
    l.SetTextFont(62)
    l.SetNDC()
    l.DrawLatex(0.12,0.91,"CMS")
    l.SetTextSize(0.05)
    l.SetTextFont(52)
    l.DrawLatex(0.23,0.91,"Preliminary")
    l.SetTextFont(42)
    l.DrawLatex(0.62,0.91,"%s"%lumiLabel)
    l.SetTextFont(52)
    l.SetTextSize(0.045)
    l.DrawLatex(0.15,0.82,'gen. pdf = %s'%pdf_dict[options.genPdf])
    l.DrawLatex(0.15,0.77,'fit pdf = %s'%pdf_dict[options.fitPdf])
    
    c.Print("%s/biasDivRVsMass_%s_lumi-%s_%s_%s_%s.pdf"%(options.outDir,options.model,('%.3f'%(options.lumi/1000.)).replace('.','p'),box,options.genPdf,options.fitPdf))
    c.Print("%s/biasDivRVsMass_%s_lumi-%s_%s_%s_%s.C"%(options.outDir,options.model,('%.3f'%(options.lumi/1000.)).replace('.','p'),box,options.genPdf,options.fitPdf))
    printName = "%s/biasDivRVsMass_%s_lumi-%s_%s_%s_%s"%(options.outDir,options.model,('%.3f'%(options.lumi/1000.)).replace('.','p'),box,options.genPdf,options.fitPdf)
    cWrite = c.Clone(os.path.splitext(printName)[0].split('/')[-1])
    tdirectory.cd()
    c.Write(os.path.splitext(printName)[0].split('/')[-1])
    
