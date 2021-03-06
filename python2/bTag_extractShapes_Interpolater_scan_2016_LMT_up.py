import ROOT as rt
import math as math
import sys, os
from optparse import OptionParser
from rootTools import tdrstyle as setTDRStyle
import glob


#to import samples names
from bTag_signalStudies_scan_deep_2016_LMT_up import *

usage = """usage: python python/bTag_extractShapes.py -e none -m qq"""



def makeShape(mass, sample, model):


    LIST=['Nominal','JER','JESUP','JESDOWN']

    #book histo
    myHisto = {}
    for i in LIST: 
       myHisto[i] = rt.TH1F("h_"+model+"_Spring16_M"+str(mass)+"_Mjj_"+i,  "h_"+model+"_Spring16_M"+str(mass)+"_Mjj_"+i, 75, 0., 1.5 )

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

	Mjj = {}

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


	Mjj['Nominal'] = tchain.mjj
	Mjj['JER'] = tchain.mjj #* (1.0 + 0.1 * recoFunc.Eval(tchain.mjj)*ran)
	Mjj['JESUP'] = tchain.mjj #* (1.0 + jesUp)# * (1.0 + smearFunc.Eval(Mjj) * ran)
	Mjj['JESDOWN'] = tchain.mjj #* (1.0 + jesDown)# * (1.0 + smearFunc.Eval(Mjj) * ran)

	for i in LIST:
          myHisto[i].Fill(Mjj[i]/mass)

    for i in LIST:
       myHisto[i].Scale(1./myHisto[i].GetEntries())
 
    return myHisto



def scaleShape(mass, histo, g_eff):
  if g_eff =='Non':
    histo_tmp = rt.TH1F('tmp'+str(mass),'tmp'+str(mass), 75, 0., 1.5)
    sFactor = 1
    histo.Copy(histo_tmp)
    histo_tmp.Scale(sFactor)
    return histo_tmp
  else:
    histo_tmp = rt.TH1F('tmp'+str(mass)+str(int(g_eff.Eval(mass)*100)),'tmp'+str(mass)+str(int(g_eff.Eval(mass)*100)), 75, 0., 1.5)
    sFactor = g_eff.Eval(mass)
    histo.Copy(histo_tmp)
    histo_tmp.Scale(sFactor)

    return histo_tmp

if __name__ == '__main__':

    rt.gROOT.SetBatch()
    setTDRStyle.setTDRStyle()
    ###################################################################                                                                                                                                         
    parser = OptionParser(usage=usage)
    parser.add_option('-m','--model',dest="model",type="string",default="qq",
                      help="Name of the signal model")
    parser.add_option('-e','--eff',dest="eff",type="string",default="signalHistos_bb/signalHistos_bb.root",
                      help="file containing the b-tag eff plot")
    parser.add_option('-c','--cate',dest="cate",type="string",default="le1b",
                      help="category 0b/1b/2b/le1b/Non")
    (options,args) = parser.parse_args()
    model   = options.model
    cate    = options.cate
    effFile = options.eff

    print "signal model    :",model
    ###################################################################                                                                                                                                        

    #outFile


    LIST=['Nominal']
    CSV_Value = ['L','M','T']
#    CSV_Value = [0.1,0.15,0.2219,0.3,0.35,0.4,0.45,0.5, 0.5426,0.6, 0.6324,0.7,0.75,0.8, 0.8484, 0.8958, 0.9535]
#[0.1,0.15,0.2,0.3,0.35,0.45,0.5,0.5803,0.65,0.75,0.8,0.8838,0.9,0.9693]
    #CSV_Value=[0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.46,0.5,0.55,0.5803,0.60,0.65,0.70,0.75,0.8,0.85,0.8838,0.9,0.935,0.95,0.9693]#[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.46,0.5,0.55,0.60,0.65,0.70,0.75,0.8,0.85,0.9,0.935,0.95]
    histo={}

    if (model == "qq"):
      sampleNames = sampleNames_qq
      flavor = 'bb'
    elif (model == "qg"):
      flavor = 'bg'
      sampleNames = sampleNames_qg
    elif (model == "gg"):
      sampleNames = sampleNames_gg
    else:
      print "model unknown"


    if model=='qq':
      outFolder = effFile
    elif model=='qg':
      outFolder = effFile

    for mass, sample in sorted(sampleNames.iteritems()):
       histo[mass] = makeShape(mass,sample,model)

    for i in CSV_Value :

      if model == 'qg':
        effFile = rt.TFile(options.eff+'/signalHistos_bg_'+i+'.root')  
      if model == 'qq':
	effFile = rt.TFile(options.eff+'/signalHistos_bb_'+i+'.root')  
      for Type in LIST:
	rootFile = rt.TFile(outFolder+"/ResonanceShapes_"+model+"_"+flavor+"_13TeV_Spring16_"+i+'_'+Type+".root", 'recreate')
        for mass, sample in sorted(sampleNames.iteritems()):  
          if cate=='Non':
            g_eff = 'Non'
	    histo_scaled=scaleShape(mass, histo[mass][Type], g_eff)
	    histo_scaled.Write()
          else:
            if (model == "qq"):
              g_eff = effFile.Get("g_"+cate+"tag_rate")
            elif (model == "qg"):
              g_eff = effFile.Get("g_"+cate+"tag_rate")
            else:
              print "model unknown"
              exit
            histo_scaled=scaleShape(mass, histo[mass][Type], g_eff)
            histo_scaled.Write()
 	rootFile.Close() 
  
