from optparse import OptionParser
import ROOT as rt
from rootTools import tdrstyle as setTDRStyle

import os
import sys

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-o','--dir',dest="outDir",default="./",type="string",
                  help="Output directory to store results")
    parser.add_option('-i','--input',dest="inputFile",default="./",type="string",
                  help="Input file containing numerator and denominator")
    parser.add_option('-n','--numerator',dest="numerator",type="string",
                  help="numerator for turnon")
    parser.add_option('-d','--denominator',dest="denominator",type="string",
                  help="denominator for turnon")


    (options,args) = parser.parse_args()
    

    rt.gROOT.SetBatch()
    setTDRStyle.setTDRStyle()
    
    inFile =  rt.TFile(options.inputFile)
    num = inFile.Get(options.numerator)
    den = inFile.Get(options.denominator)

    num.SetDirectory(0)
    den.SetDirectory(0)

    
    
    turnon = rt.TEfficiency(num,den)
    turnon.SetTitle("(PFHT800 && PFHT475)/PFHT475;Mjj [GeV];(PFHT800 && PFHT475)/PFHT475")

    cc = rt.TCanvas();
    cc.SetGridx()
    cc.SetGridy()
    turnon.Draw('AP')
    rt.gPad.Update()

    turnon.GetPaintedGraph().GetXaxis().SetRangeUser(500,3000);

    min = 800
    max = 2000
    f1 = rt.TF1("f1","[0]*TMath::Erf((x-[1])/[2])-[0]*TMath::Erf((-x-[1])/[2])",min,max)
    f1.SetParameters(0.5,900,150)
    f1.FixParameter(0,0.5)
    f1.SetLineColor(rt.kRed)

    turnon.Fit(f1,'r')
    print '0',f1.GetParameter(0)
    print '1',f1.GetParameter(1)
    print '2',f1.GetParameter(2)
    rt.gStyle.SetOptFit(0)

    

    cc.Print(options.outDir+"/turnon.pdf")
    cc.Print(options.outDir+"/turnon.C")
