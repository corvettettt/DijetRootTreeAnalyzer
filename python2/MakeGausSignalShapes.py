from optparse import OptionParser
import ROOT as rt
import rootTools
from framework import Config
from array import *
import os
import sys

if __name__ == '__main__':
    
    parser = OptionParser()
    parser.add_option('-t','--type',dest="type",default="nom",type="string",
                  help="type of result")
    parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
                  help="Output directory to store results")

    (options,args) = parser.parse_args()

     
    if options.type=='nom':
        TYPE = ''
    else:
        TYPE = options.type.upper()
        
    if options.type=='nom':
        tfileOut = rt.TFile.Open('%s/ResonanceShapes_gaus_13TeV_CaloScouting_Spring15.root'%options.outDir,'recreate')
    else:
        tfileOut = rt.TFile.Open('%s/ResonanceShapes_gaus_13TeV_CaloScouting_Spring15_%s.root'%(options.outDir,TYPE),'recreate')
    tfileOut.cd()

    if options.type=='nom':
        res = 0.07
        scale = 1
    elif options.type=='jesUp':
        res = 0.07
        scale = 1.02
    elif options.type=='jesDown':
        res = 0.07
        scale = 0.98
    elif options.type=='jerUp':
        res = 1.1*0.07
        scale = 1
    elif options.type=='jerDown':
        res = 0.9*0.07
        scale = 1
        
    histos = []
    for mass in range(500,9050,50):
        
        h = rt.TH1D('h_gaus_%i'%mass,'gaus Resonance Shape',14000,0,14000)
        h.GetXaxis().SetTitle("Dijet Mass [GeV]")
        h.GetYaxis().SetTitle("Probability")

        for i in range(1,h.GetNbinsX()+1):
            int_ninfty_down = rt.Math.gaussian_cdf(scale*h.GetXaxis().GetBinLowEdge(i),res*scale*mass,mass)
            int_ninfty_up = rt.Math.gaussian_cdf(scale*h.GetXaxis().GetBinUpEdge(i),res*scale*mass,mass)
            h.SetBinContent(i,int_ninfty_up - int_ninfty_down)
        h.Scale(1.0/h.Integral())
        histos.append(h)
    tfileOut.cd()
    for h in histos:
        h.Write()
    tfileOut.Close()
        
        
