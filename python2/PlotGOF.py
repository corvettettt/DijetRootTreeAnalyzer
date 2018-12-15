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


def setStyle():
    rt.gStyle.SetOptStat(0)
    rt.gStyle.SetOptTitle(0)
    rt.gStyle.SetPaintTextFormat("1.2g")
    rt.gROOT.SetBatch()
    rt.RooMsgService.instance().setGlobalKillBelow(rt.RooFit.FATAL)

def getGOFHistos(varName,toyTree):
    toyTree.GetEntry(0)
    var_data = eval('toyTree.%s_%s'%(varName,box))
        
    toyTree.Draw('%s>>htest%s'%('%s_%s'%(varName,box),'%s_%s'%(varName,box)))
    htemp = rt.gPad.GetPrimitive("htest%s"%('%s_%s'%(varName,box)))
    rms = htemp.GetRMS()
    mean = htemp.GetMean()
    
    xmax = max(mean+3.*rms,var_data+1)
    #xmax = 60
    xmax = 100
    
    xmin = int(max(0,htemp.GetXaxis().GetXmin()))
    xmin = 0
    #xmin = 10
    
    h = rt.TH1D('h_%s'%varName,'h_%s'%varName,70,xmin,xmax)
    h_cut = rt.TH1D('h_%s_cut'%varName,'h_%s_cut'%varName,70,xmin,xmax)
    toyTree.Project('h_%s'%varName,'%s_%s'%(varName,box))
    toyTree.Project('h_%s_cut'%varName,'%s_%s'%(varName,box),'%s_%s>%f'%(varName,box,var_data))

    return h, h_cut, var_data

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
    h_data.GetXaxis().SetTitleSize(0.05)
    h_data.GetYaxis().SetTitleSize(0.05)
    #h_data.GetXaxis().SetTitleOffset(0.8)
    #h_data.GetYaxis().SetTitleOffset(0.7)
    h_data.SetMaximum(pow(h_data.GetMaximum(),1.7))
    h_data.SetMinimum(2e-1)
    return h_data

    
def print1DGOF(c,rootFile,h,h_cut,func,chi2_data,printName,xTitle,yTitle,lumiLabel="",boxLabel="",plotLabel="",isData=False,tLeg=None):

    c.SetLogy(1)
    setHist(h,xTitle,yTitle)
    
    #h.SetLineWidth(2)    
    h.Draw("pe")
    h_cut.SetLineColor(rt.kViolet-10)
    h_cut.SetFillColor(rt.kViolet-10)
    h_cut.Draw("histsame")
    h.Draw("pesame")
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
        func.Draw("same")
    
    pvalue = h_cut.Integral(0,h_cut.GetNbinsX()+1)/h.Integral(0,h.GetNbinsX()+1)
    for i in range(1,h_cut.GetNbinsX()+1):
        if h_cut.GetXaxis().GetBinLowEdge(i) < chi2_data:
            h_cut.SetBinContent(i,0)
    
    tlineObs = rt.TArrow(chi2_data,0,chi2_data,h.GetBinContent(h.GetMaximumBin()),0.04,"<")
    tlineObs.SetLineColor(rt.kBlack)
    tlineObs.SetLineWidth(4)
    tlineObs.Draw()

        
    tLeg = rt.TLegend(0.6,0.6,0.89,0.89)
    tLeg.SetLineColor(rt.kWhite)
    tLeg.SetLineWidth(0)
    tLeg.SetFillStyle(0)
    tLeg.AddEntry(h,"toy data","lep")
    tLeg.AddEntry(tlineObs,"observed = %.1f"%chi2_data,"l")
    tLeg.AddEntry(h_cut,"p-value = %.2f"%(pvalue),"f")
    tLeg.AddEntry(func,"chisq fit, ndf = %.1f #pm %.1f"%(func.GetParameter(1),func.GetParError(1)),"l")
            
    tLeg.Draw("same")

    l = rt.TLatex()
    l.SetTextAlign(11)
    l.SetTextSize(0.06)
    l.SetTextFont(62)
    l.SetNDC()
    l.DrawLatex(0.12,0.91,"CMS")
    l.SetTextSize(0.05)
    l.SetTextFont(52)
    if isData:
        l.DrawLatex(0.23,0.91,"Preliminary")
    else:
        l.DrawLatex(0.23,0.91,"Simulation")
    l.SetTextFont(42)
    l.DrawLatex(0.62,0.91,"%s"%lumiLabel)
    l.SetTextFont(52)
    l.SetTextSize(0.045)
    l.DrawLatex(0.2,0.82,boxLabel)
    l.DrawLatex(0.3,0.77,plotLabel)

    c.cd()
    
    c.Print(printName)
    c.Print(os.path.splitext(printName)[0]+'.C')
    cWrite = c.Clone(os.path.splitext(printName)[0].split('/')[-1])
    rootFile.cd()
    c.Write(os.path.splitext(printName)[0].split('/')[-1])

    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c','--config',dest="config",type="string",default="config/run2.config",
                  help="Name of the config file to use")
    parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
                  help="Output directory to store results")
    parser.add_option('-l','--lumi',dest="lumi", default=3000.,type="float",
                  help="integrated luminosity in pb^-1")
    parser.add_option('-b','--box',dest="box", default="MultiJet",type="string",
                  help="box name")
    parser.add_option('-t','--input-toy-file',dest="inputToyFile", default=None,type="string",
                  help="input toy file")
    parser.add_option('--data',dest="isData", default=False,action='store_true',
                  help="changes plots for data")
    parser.add_option('--fit-region',dest="fitRegion",default="Full",type="string",
                  help="Fit region")
    
    (options,args) = parser.parse_args()
     
    setStyle()
    
    box = options.box
    lumi = options.lumi
    cfg = Config.Config(options.config)
    fitRegion = options.fitRegion

    
    toyTree = None
    if options.inputToyFile is not None:
        toyFiles = options.inputToyFile.split(',')
        toyTree = rt.TChain("myTree")
        for toyFile in toyFiles:
            toyTree.Add(toyFile)
    
    c = rt.TCanvas('c','c',500,400)    
    c.SetLeftMargin(0.12) 
    c.SetBottomMargin(0.12)
    rootFile = rt.TFile.Open(options.outDir + '/' + 'Plots_%s'%box + '.root','recreate')
    tdirectory = rootFile.GetDirectory(options.outDir)
    if tdirectory==None:
        rootFile.mkdir(options.outDir)
        tdirectory = rootFile.GetDirectory(options.outDir)

    if options.isData:
        dataString = "Data"
    else:
        dataString = "Sim. Data"

    eventsLabel = "Toy Datasets"
    
    x = array('d', cfg.getBinning(box)[0]) # mjj binning
    nBins = (len(x)-1)
        
    h_n2llr, h_n2llr_cut, n2llr_data = getGOFHistos('n2llr',toyTree)
    h_chi2p, h_chi2p_cut, chi2p_data = getGOFHistos('chi2p',toyTree)       
    h_chi2, h_chi2_cut, chi2_data = getGOFHistos('chi2',toyTree)            
    h_chi2non0, h_chi2non0_cut, chi2non0_data = getGOFHistos('chi2non0',toyTree)            
    
    btagLabel = ""

    lumiLabel = "%.1f fb^{-1} (13 TeV)" % (lumi/1000.)
    boxLabel = ''

    chi2_func = rt.TF1('chisqpdf','[0]*ROOT::Math::chisquared_pdf(x,[1])',0,100)
    chi2_func.SetParameter(0,toyTree.GetEntries())
    chi2_func.SetParameter(1,50)
    
    
    print1DGOF(c,tdirectory,h_n2llr,h_n2llr_cut,chi2_func,n2llr_data,options.outDir+"/gof_n2llr_%s.pdf"%box,"-2 log #lambda",eventsLabel,lumiLabel,boxLabel,'',options.isData,None)
    print1DGOF(c,tdirectory,h_chi2p,h_chi2p_cut,chi2_func,chi2p_data,options.outDir+"/gof_chi2p_%s.pdf"%box,"#chi^{2}_{p}",eventsLabel,lumiLabel,boxLabel,'',options.isData,None)
    print1DGOF(c,tdirectory,h_chi2,h_chi2_cut,chi2_func,chi2_data,options.outDir+"/gof_chi2_%s.pdf"%box,"#chi^{2}",eventsLabel,lumiLabel,boxLabel,'',options.isData,None)
    print1DGOF(c,tdirectory,h_chi2non0,h_chi2non0_cut,chi2_func,chi2non0_data,options.outDir+"/gof_chi2non0_%s.pdf"%box,"#chi^{2}",eventsLabel,lumiLabel,boxLabel,'',options.isData,None)
    
 
