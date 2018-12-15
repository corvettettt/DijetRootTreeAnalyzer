import ROOT as rt
import os.path
import sys, glob, re
from array import *
from optparse import OptionParser

from Plot1DLimit import getHybridCLsArrays, setstyle

if __name__ == '__main__':

    rt.gROOT.SetBatch()
    directory = {'gg':'Limits/gg/',
                 'qg':'Limits/qg/',
                 'qq':'Limits/qq/',
                 'gaus':'Limits/gaus/',
                 'gaus10':'Limits/gaus10/',
                 'gg_nosys':'Limits/gg_nosys/',
                 'qg_nosys':'Limits/qg_nosys/',
                 'qq_nosys':'Limits/qq_nosys/',
                 'gaus_nosys':'Limits/gaus_nosys/',
                 'gaus10_nosys':'Limits/gaus10_nosys/'}

    Box  = 'CaloDijet2016'
    #Box  = 'PFDijet2016'
    lumi = 12.910
    
    models = ['gaus10']

    box = Box.lower()

    observed = {}
    expected = {}

    gr_expectedLimitRatio  = {}
    expectedLimitRatio  = {}
    
    gr_observedLimitRatio  = {}
    observedLimitRatio  = {}
    
    
    for model in models:
        gluinoMassArray, gluinoMassArray_er, observedLimit, observedLimit_er, expectedLimit, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma = getHybridCLsArrays(directory[model], model, Box, False)
        observed[model] = observedLimit
        expected[model] = expectedLimit
        
        gluinoMassArray, gluinoMassArray_er, observedLimit_nosys, observedLimit_er, expectedLimit_nosys, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma = getHybridCLsArrays(directory[model+'_nosys'], model, Box, False)
        observed[model+'_nosys'] = observedLimit_nosys
        expected[model+'_nosys'] = expectedLimit_nosys

        expectedLimitRatio[model] = array('d',[num/denom for num, denom in zip(expected[model],expected[model+'_nosys'])])
        observedLimitRatio[model] = array('d',[num/denom for num, denom in zip(observed[model],observed[model+'_nosys'])])
        
        nPoints = len(gluinoMassArray)
        gr_expectedLimitRatio[model] = rt.TGraph(nPoints, gluinoMassArray, expectedLimitRatio[model])
        gr_expectedLimitRatio[model].SetLineWidth(3)
        gr_expectedLimitRatio[model].SetLineStyle(2)

        
        gr_observedLimitRatio[model] = rt.TGraph(nPoints, gluinoMassArray, observedLimitRatio[model])
        gr_observedLimitRatio[model].SetMarkerColor(1)
        gr_observedLimitRatio[model].SetMarkerStyle(22)
        gr_observedLimitRatio[model].SetMarkerSize(0.6)
        gr_observedLimitRatio[model].SetLineWidth(3)
        gr_observedLimitRatio[model].SetLineColor(rt.kBlack)
        gr_observedLimitRatio[model].SetMarkerStyle(20)
        
        setstyle()
        rt.gStyle.SetOptStat(0)
        c = rt.TCanvas("c","c",500,400)

        h_limit = rt.TMultiGraph()
        h_limit.Add(gr_expectedLimitRatio[model])
        h_limit.Add(gr_observedLimitRatio[model])
        
        h_limit.SetTitle(" ;Resonance Mass m_{X} [GeV]; Limit ratio (stat.+syst. / stat.-only)")
        
        
        h_limit.Draw("a3")
        if 'PF' in Box:
            h_limit.GetXaxis().SetLimits(1600,7500)
        else:
            h_limit.GetXaxis().SetLimits(600,1600)
        h_limit.SetMaximum(10)
        h_limit.SetMinimum(0)
            
        h_limit.Draw("a3")
        gr_expectedLimitRatio[model].Draw("csame")
        gr_observedLimitRatio[model].Draw("lpsame")
        

        
        l = rt.TLatex()
        l.SetTextAlign(11)
        l.SetTextSize(0.05)
        l.SetNDC()
        l.SetTextFont(62)
        l.DrawLatex(0.17,0.92,"CMS")
        
        l.SetTextFont(52)
        l.DrawLatex(0.26,0.92,"Preliminary")
        l.SetTextFont(42)
        #l.DrawLatex(0.65,0.92,"%.0f pb^{-1} (13 TeV)"%(options.lumi*1000))
        l.DrawLatex(0.68,0.92,"%.1f fb^{-1} (13 TeV)"%(lumi))

        
    
        if model=="gg":
            l.DrawLatex(0.3,0.8,"gg #rightarrow X #rightarrow jj")
        elif model=="qg":        
            l.DrawLatex(0.3,0.8,"qg #rightarrow X #rightarrow jj")
        elif model=="qq":
            l.DrawLatex(0.3,0.8,"qq #rightarrow X #rightarrow jj")
        elif model=="gaus":
            l.DrawLatex(0.24,0.8,"Gaussian, 7% width")
        elif model=="gaus10":
            l.DrawLatex(0.22,0.8,"Gaussian, 10% width")



            

        c.SetGridy()
        #leg = rt.TLegend(0.55,0.79,0.92,0.87)
        leg = rt.TLegend(0.55,0.74,0.92,0.87)
        leg.SetTextFont(42)
        leg.SetFillColor(rt.kWhite)
        leg.SetLineColor(rt.kWhite)
        leg.AddEntry(gr_observedLimitRatio[model], "Observed","lp")
        leg.AddEntry(gr_expectedLimitRatio[model], "Expected","l")
            
        leg.Draw("SAME")
            

        c.SaveAs("Limits/limitRatio_freq_"+model+"_"+box+".pdf")
        c.SaveAs("Limits/limitRatio_freq_"+model+"_"+box+".C")
