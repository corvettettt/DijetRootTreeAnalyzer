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
    parser.add_option('-m','--model',dest="model",default="gg",type="string",
                  help="model")
    parser.add_option('-d','--outdir',dest="outDir",default="./",type="string",
                  help="Output directory to store output histograms")

    (options,args) = parser.parse_args()
    if options.type=='nom':
        TYPE = ''
    else:
        TYPE = options.type.upper()

    if options.model=='gg':
        title = 'RSGgg'
    elif options.model=='qq':
        title = 'RSGqq'
    elif options.model=='qg':
        title = 'QstarToJJ'

    #production = ['CaloScouting','Spring15']
    production = ['CaloScouting','Spring16']
    #production = ['Spring16']
    

    histos = []
    for f in args:
        mass = int(f.split('.root')[0].split('_')[-1])
        tfileIn = rt.TFile.Open(f)
        h = tfileIn.Get('h_mjj_ratio_%s'%options.type)
        h.SetName('h_%s_%s%s_M%i_WJ'%(title,''.join(production),TYPE,mass))
        h.SetTitle('Mjj_WJ/M')
        h.SetDirectory(0)
        histos.append(h)

    
    if options.type=='nom':
        tfileOut = rt.TFile.Open('%s/InputShapes_%s_%s.root'%(options.outDir,title,'_'.join(production)),'recreate')
    else:
        tfileOut = rt.TFile.Open('%s/InputShapes_%s_%s_%s.root'%(options.outDir,title,'_'.join(production),TYPE),'recreate')
    tfileOut.cd()
    for h in histos:
        h.Write()
    tfileOut.Close()
        
        
