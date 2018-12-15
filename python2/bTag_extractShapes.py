import ROOT as rt
import math as math
import sys, os
from optparse import OptionParser
from rootTools import tdrstyle as setTDRStyle

#to import samples names
from bTag_signalStudies import *

usage = """usage: python python/bTag_extractShapes.py -e none -m qq"""



def makeShape(mass, sample, model):

    #book histo
    myHisto = rt.TH1F("h_"+model+"_"+str(mass),  "h_"+model+"_"+str(mass), 1400, 0., 14000. )


    #loop over the tree and fill the histos
    tchain = rt.TChain(treeName)
    tchain.Add(sample)
    nEntries = tchain.GetEntries()

    for i in progressbar(range(nEntries), "Mass "+str(mass)+": ", 40):
        tchain.GetEntry(i)


        #select bb events at gen level
        if (model == 'qq' and (tchain.jetHflavour_j1 != 5 or tchain.jetHflavour_j2 != 5)):
            continue
        if (model == 'qg' and (tchain.jetHflavour_j1 != 5 and tchain.jetHflavour_j2 != 5)):
            continue

        myHisto.Fill(tchain.mjj)


    myHisto.Scale(1./myHisto.GetEntries())
    return myHisto



def scaleShape(mass, histo, g_eff):
    sFactor = g_eff.Eval(mass)
    histo.Scale(sFactor)



if __name__ == '__main__':

    rt.gROOT.SetBatch()
    setTDRStyle.setTDRStyle()
    ###################################################################                                                                                                                                         
    parser = OptionParser(usage=usage)
    parser.add_option('-m','--model',dest="model",type="string",default="qq",
                      help="Name of the signal model")
    parser.add_option('-e','--eff',dest="eff",type="string",default="signalHistos_bb/signalHistos_bb.root",
                      help="file containing the b-tag eff plot")
    (options,args) = parser.parse_args()
    model   = options.model

    effFile = rt.TFile(options.eff)

    print "signal model    :",model
    ###################################################################                                                                                                                                        

    #outFile
    rootFile = rt.TFile("ResonanceShapes_"+model+"_bb_13TeV_Spring16.root", 'recreate') 

    # loop over the MC samples
    if (model == "qq"):
        sampleNames = sampleNames_qq
        g_eff = effFile.Get("g_2btag_rate")

    elif (model == "qg"):
        sampleNames = sampleNames_qg
        g_eff = effFile.Get("g_1btag_rate")

    elif (model == "gg"):
        sampleNames = sampleNames_gg
    else:
        print "model unknown"
        exit

    for mass, sample in sorted(sampleNames.iteritems()):
        histo = makeShape(mass,sample,model)
        #scale the shape to take into account the bTag eff
        scaleShape(mass, histo, g_eff)
        histo.Write()


    rootFile.Close()
