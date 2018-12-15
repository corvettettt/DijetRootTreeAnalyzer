import ROOT as rt
import math as math
import sys, os
from optparse import OptionParser
from rootTools import tdrstyle as setTDRStyle

#to import samples names
from bTag_signalStudies_le1_K import *

usage = """usage: python python/bTag_extractShapes.py -e none -m qq"""



def makeShape(mass, sample, model):
    myHisto={}

    #book histo
    myHisto['Norminal'] = rt.TH1F("h_"+model+"_Spring16_M"+str(mass)+"_Mjj_Norminal",  "h_"+model+"_Spring16_M"+str(mass)+"_Mjj_Norminal", 75, 0., 1.5 )
    myHisto['JER'] = rt.TH1F("h_"+model+"_Spring16_M"+str(mass)+"_Mjj_JER",  "h_"+model+"_Spring16_M"+str(mass)+"_Mjj_JER", 75, 0., 1.5 ) 
    myHisto['JESUP'] = rt.TH1F("h_"+model+"_Spring16_M"+str(mass)+"_Mjj_JESUP",  "h_"+model+"_Spring16_M"+str(mass)+"_Mjj_JESUP", 75, 0., 1.5 ) 
    myHisto['JESDOWN'] = rt.TH1F("h_"+model+"_Spring16_M"+str(mass)+"_Mjj_JESDOWN",  "h_"+model+"_Spring16_M"+str(mass)+"_Mjj_JESDOWN", 75, 0., 1.5 )


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

	MJJ = tchain.mjj

	hltP0=2.441
	hltP1=0
	recoP0=2.077
	recoP1=0
	jerUp=0.1
	jerDown=-0.1
	jes=0
	jesUp=0.02
	jesDown=-0.02

	hltFunc = rt.TF1("hltFunc","sqrt([0]*[0]/x+[1]*[1])",0,14000)
	hltFunc.SetParameter(0,hltP0)
	hltFunc.SetParameter(1,hltP1)

	recoFunc= rt.TF1("recoFunc","sqrt([0]*[0]/x+[1]*[1])",0,14000)
	recoFunc.SetParameter(0,recoP0)
	recoFunc.SetParameter(1,recoP1)

	smearFunc=rt.TF1("smearFunc","(recoFunc)*sqrt(hltFunc*hltFunc/recoFunc/recoFunc-1.0)",0,14000)

	smearJerUpFunc=rt.TF1("smearJerUpFunc","(recoFunc)*sqrt(pow(hltFunc + [0]*recoFunc,2.0)/recoFunc/recoFunc-1.0)",0,14000)
	smearJerUpFunc.SetParameter(0,jerUp)

	smearJerDownFunc=rt.TF1("smearJerDownFunc","(recoFunc)*sqrt(pow(hltFunc + [0]*recoFunc,2.0)/recoFunc/recoFunc-1.0)",0,14000)
	smearJerDownFunc.SetParameter(0,jerDown)

	r=rt.TRandom3()
	ran=r.Gaus()

	Mjj={}
	Mjj['Norminal'] = MJJ
	Mjj['JER'] = MJJ * (1.0 + 0.1 * recoFunc.Eval(MJJ)*ran)
	Mjj['JESUP'] = MJJ * (1.0 + jesUp)# * (1.0 + smearFunc.Eval(Mjj) * ran)
	Mjj['JESDOWN'] = MJJ * (1.0 + jesDown)# * (1.0 + smearFunc.Eval(Mjj) * ran)

        myHisto['Norminal'].Fill(Mjj['Norminal']/mass)
        myHisto['JER'].Fill(Mjj['JER']/mass)
        myHisto['JESUP'].Fill(Mjj['JESUP']/mass)
        myHisto['JESDOWN'].Fill(Mjj['JESDOWN']/mass)

    myHisto['Norminal'].Scale(1./myHisto['Norminal'].GetEntries())
    myHisto['JER'].Scale(1./myHisto['JER'].GetEntries())
    myHisto['JESDOWN'].Scale(1./myHisto['JESDOWN'].GetEntries())
    myHisto['JESUP'].Scale(1./myHisto['JESUP'].GetEntries())

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
    parser.add_option('-e','--eff',dest="eff",type="string",default="signalHistos_bb/",
                      help="file containing the b-tag eff plot")
    (options,args) = parser.parse_args()
    model   = options.model

    effFile = rt.TFile(options.eff)

    print "signal model    :",model
    ###################################################################                                                                                                                                        
    LIST=['Norminal','JESUP','JER','JESDOWN']

    #outFile

    # loop over the MC samples
    if (model == "qq"):
        sampleNames = sampleNames_qq
        g_eff = effFile.Get("g_le1btag_rate")

    elif (model == "qg"):
        sampleNames = sampleNames_qg
        g_eff = effFile.Get("g_le1btag_rate")

    elif (model == "gg"):
        sampleNames = sampleNames_gg
    else:
        print "model unknown"
        exit


    histo= {} 
    for mass, sample in sorted(sampleNames.iteritems()):
        histo[mass] = makeShape(mass,sample,model)
        #scale the shape to take into account the bTag eff

    for Type in LIST:
      rootFile = rt.TFile(effFile+"/ResonanceShapes_"+model+"_bb_13TeV_Spring16_"+Type+"_Inter.root", 'recreate')
      for mass, sample in sorted(sampleNames.iteritems()):
        scaleShape(mass, histo[mass][Type], g_eff)
	histo[mass][Type].Write()
      rootFile.Close()
