import ROOT as rt
import math as math
import sys, os
from bTag_signalStudies import *
from optparse import OptionParser
from rootTools import tdrstyle as setTDRStyle

### plots for signals ###
# tagging rate vs mass for signals (b, udcs, g)
# scale factors vs mass for signals with uncertainty
# selections acceptance vs mass for signals
# shape comparison before and after b-tag selection (normalized to 1)

usage = """usage: python python/bTag_signalStudies.py -f bb -m qq"""

#eosPrefix = "root://eoscms.cern.ch//eos/cms"
#eosPath = "/store/group/phys_exotica/dijet/Dijet13TeV/deguio/fall16_red_MC/RSGravitonToQuarkQuark_kMpl01_Spring16_20161201_145940/"
eosPrefix = ""
eosPath = "/tmp/TylerW/"
sampleNames_qg={}
sampleNames_qg = {
500:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ500GeV_reduced_skim.root',
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ1000GeV_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ2000GeV_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ3000GeV_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ4000GeV_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ5000GeV_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ6000GeV_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ7000GeV_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ8000GeV_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ9000GeV_reduced_skim.root',
                  }


#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleNames_qq = {}
sampleNames_qq = {
500:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_500GeV_reduced_skim.root',
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_1000GeV_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_2000GeV_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_3000GeV_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_4000GeV_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_5000GeV_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_6000GeV_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_7000GeV_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_8000GeV_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_9000GeV_reduced_skim.root',
                  }

CSV_Value = [0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.8838,0.9,0.9693] 


treeName = "rootTupleTree/tree"
massRange  = {500: [75,0,1500],
              1000: [50,0,2000],
              2000: [50,0,5000],
              3000: [50,0,5000],
              4000: [35,0,7000],
              5000: [35,0,8000],
              6000: [30,0,9000],
              7000: [20,0,10000],
              8000: [20,0,12000],
              9000: [20,0,12000]
              }


def bookAndFill(mass,sample,flavour):
    #book histos
    hDict={}
    for i in CSV_Value:
      hDict[i] = {}
 
    for i in CSV_Value:
      prefix = str(mass)+"_"+str(int(i*1000))
      hDict[i]["h_mass_all"]    = rt.TH1F(prefix+"_mass_all",   prefix+"_mass_all",   massRange[mass][0],massRange[mass][1],massRange[mass][2])
      hDict[i]["h_mass_passed"] = rt.TH1F(prefix+"_mass_passed_deepCSV",prefix+"_mass_passed_deepCSV",massRange[mass][0],massRange[mass][1],massRange[mass][2])
      hDict[i]["h_mass_passed"].SetLineColor(rt.kOrange+8)
      hDict[i]["h_mass_passed"].SetMarkerColor(rt.kOrange+8)
      hDict[i]["h_mass_passed"].SetLineWidth(3)
      hDict[i]["h_mass_passed"].GetXaxis().SetTitle("Resonance Mass [GeV]")


      hDict[i]["h_mass_passed_0b"] = rt.TH1F(prefix+"_mass_passed_deepCSV_0b",prefix+"_mass_passed_deepCSV_0b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
      hDict[i]["h_mass_passed_0b"].SetMarkerSize(0.5)
  
      hDict[i]["h_mass_passed_1b"] = rt.TH1F(prefix+"_mass_passed_deepCSV_1b",prefix+"_mass_passed_deepCSV_1b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
      hDict[i]["h_mass_passed_1b"].SetLineColor(rt.kRed)
      hDict[i]["h_mass_passed_1b"].SetMarkerColor(rt.kRed)
      hDict[i]["h_mass_passed_1b"].SetMarkerSize(0.5)
    
      hDict[i]["h_mass_passed_2b"] = rt.TH1F(prefix+"_mass_passed_deepCSV_2b",prefix+"_mass_passed_deepCSV_2b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
      hDict[i]["h_mass_passed_2b"].SetLineColor(rt.kBlue)
      hDict[i]["h_mass_passed_2b"].SetMarkerColor(rt.kBlue)
      hDict[i]["h_mass_passed_2b"].SetMarkerSize(0.5)

      hDict[i]["h_mass_passed_le1b"] = rt.TH1F(prefix+"_mass_passed_deepCSV_le1b",prefix+"_mass_passed_deepCSV_le1b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
      hDict[i]["h_mass_passed_le1b"].SetLineColor(rt.kGreen)
      hDict[i]["h_mass_passed_le1b"].SetMarkerColor(rt.kGreen)
      hDict[i]["h_mass_passed_le1b"].SetMarkerSize(0.5)

      hDict[i]["h_weight_0b"] = rt.TH1F(prefix+"_weight_0b",prefix+"_weight_0b",2000,0.,2.)
      hDict[i]["h_weight_1b"] = rt.TH1F(prefix+"_weight_1b",prefix+"_weight_1b",2000,0.,2.)
      hDict[i]["h_weight_2b"] = rt.TH1F(prefix+"_weight_2b",prefix+"_weight_2b",2000,0.,2.)



    #loop over the tree and fill the histos
    tchain = rt.TChain(treeName)
    tchain.Add(sample)
    nEntries = tchain.GetEntries()

    for k in progressbar(range(nEntries), "Mass "+str(mass)+": ", 40):
        tchain.GetEntry(k)

        #implement analysis
	for i in CSV_Value:
           hDict[i]["h_mass_all"].Fill(tchain.mjj)
        
           hDict[i]["h_mass_passed"].Fill(tchain.mjj)

           if not (abs(tchain.deltaETAjj)<1.1       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                #tchain.pTWJ_j1<6500              and
                tchain.pTWJ_j2>30                and
                #tchain.pTWJ_j2<6500              and

                #tchain.mjj > 1246                and
                #tchain.mjj < 14000               and

                tchain.PassJSON):
             continue

	   Npass = 0
 	   if tchain.jetCSVAK4_j1>i:
	     Npass+=1
           if tchain.jetCSVAK4_j2>i:
 	     Npass+=1
  
	   if Npass ==0:
             hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj)
           if Npass ==1:
             hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj)
           if Npass ==2:
             hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj)
           if Npass >0:
	     hDict[i]["h_mass_passed_le1b"].Fill(tchain.mjj)


    return hDict



if __name__ == '__main__':

    rt.gROOT.SetBatch()
    setTDRStyle.setTDRStyle()
    ###################################################################
    parser = OptionParser(usage=usage)
    parser.add_option('-f','--flavour',dest="flavour",type="string",default="none",
                      help="Name of the signal flavour")
    parser.add_option('-m','--model',dest="model",type="string",default="qq",
                      help="Name of the signal model")
    parser.add_option('-s','--su',dest='su',type = 'string',default='central',help='central/up/down')

    (options,args) = parser.parse_args()
    flavour = options.flavour
    model   = options.model
    su = options.su


    print "selected flavour:",flavour
    print "signal model    :",model
    ###################################################################

#    CSV_Value = [0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693]

    # book histos and graphs
    mDict = {}
    sampleNames = {}

    # loop over the MC samples
    if (model == "qq"):
        sampleNames = sampleNames_qq
    elif (model == "qg"):
        sampleNames = sampleNames_qg
    else:
        print "model unknown"
        exit

    for mass, sample in sorted(sampleNames.iteritems()):
        mDict[mass] = bookAndFill(mass,sample,flavour)

    #Create ROOT file and save plain histos
    outName = "signalHistos_"+flavour
    outFolder = "signalHistos_"+flavour+'_Mar_For2017Scan_CSVv2'

    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    if (flavour == "none"):
        outName = ("ResonanceShapes_%s_13TeV_Spring16.root"%model)

    g_an_acc={}
    g_mtbtag_rate={}
    g_1btag_rate={}
    g_2btag_rate={}
    g_le1btag_rate={}
    g_0btag_weight={}
    g_1btag_weight={}
    g_2btag_weight={}

    #make analysis vs mass
    for i in CSV_Value:
      g_an_acc[i]    = rt.TGraphAsymmErrors()
  
      g_mtbtag_rate[i] = rt.TGraphAsymmErrors()
      g_mtbtag_rate[i].SetTitle("g_mtbtag_rate;Resonance Mass [GeV];Tagging Rate")
      g_mtbtag_rate[i].SetLineWidth(2)
      g_1btag_rate[i] = rt.TGraphAsymmErrors()
      g_1btag_rate[i].SetMarkerColor(rt.kRed)
      g_1btag_rate[i].SetLineColor(rt.kRed)
      g_1btag_rate[i].SetLineWidth(2)
      g_2btag_rate[i] = rt.TGraphAsymmErrors()
      g_2btag_rate[i].SetMarkerColor(rt.kBlue)
      g_2btag_rate[i].SetLineColor(rt.kBlue)
      g_2btag_rate[i].SetLineWidth(2)
 
      g_le1btag_rate[i] = rt.TGraphAsymmErrors()
      g_le1btag_rate[i].SetMarkerColor(rt.kGreen)
      g_le1btag_rate[i].SetLineColor(rt.kGreen)
      g_le1btag_rate[i].SetLineWidth(2)
 
      g_0btag_weight[i] = rt.TGraphAsymmErrors()
      g_1btag_weight[i] = rt.TGraphAsymmErrors()
      g_2btag_weight[i] = rt.TGraphAsymmErrors()
  

    bin=0 
    for mass,hDict in sorted(mDict.iteritems()):
      for i in CSV_Value: 


        num = hDict[i]["h_mass_passed"].GetSumOfWeights()
        den = hDict[i]["h_mass_all"].GetSumOfWeights()
        #g_an_acc.SetPoint(bin,mass,num/den)  #wrong. the reduced ntuples have already the selection implemented

        num = hDict[i]["h_mass_passed_1b"].GetSumOfWeights()
        g_1btag_rate[i].SetPoint(bin,mass,num/den)

        num = hDict[i]["h_mass_passed_2b"].GetSumOfWeights()
        g_2btag_rate[i].SetPoint(bin,mass,num/den)

	num = hDict[i]["h_mass_passed_le1b"].GetSumOfWeights()
	g_le1btag_rate[i].SetPoint(bin,mass,num/den)
      bin += 1       

    for i in CSV_Value: 
      rootFile = rt.TFile(outFolder+"/"+outName+"_"+str(int(i*1000))+".root", 'recreate')
      for mass,hDict in sorted(mDict.iteritems()):
        # shape comparison 0 btag
        h1 = rt.TCanvas()
        h1.SetGridx()
        h1.SetGridy()
        h1.cd()  

        hDict[i]["h_mass_passed"].DrawNormalized()
        hDict[i]["h_mass_passed_1b"].DrawNormalized("sames")
        hDict[i]["h_mass_passed_2b"].DrawNormalized("sames")

        leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
        leg.AddEntry(hDict[i]["h_mass_passed"],"untagged","L")
        leg.AddEntry(hDict[i]["h_mass_passed_1b"],"1-tag","P")
        leg.AddEntry(hDict[i]["h_mass_passed_2b"],"2-tag","P")
        leg.Draw("same")

        h1.Print(outFolder+"/shapes_"+str(mass)+"_"+flavour+"_"+str(int(i*1000))+".pdf")

        for n,h in hDict[i].items():
            h.Write()
      g_an_acc[i].Write("g_an_acc")
      g_1btag_rate_Q=Do_Inter(g_1btag_rate[i])
      g_2btag_rate_Q=Do_Inter(g_2btag_rate[i])
      g_le1btag_rate_Q=Do_Inter(g_le1btag_rate[i])


#        g_0btag_rate_Q.Write("g_0btag_rate")
#        g_1btag_rate_Q.Write("g_1btag_rate")
      g_1btag_rate_Q.SetMarkerColor(rt.kRed)
      g_1btag_rate_Q.SetLineColor(rt.kRed)
      g_1btag_rate_Q.SetLineWidth(2)
#        g_2btag_rate_Q.Write("g_2btag_rate")
      g_2btag_rate_Q.SetMarkerColor(rt.kBlue)
      g_2btag_rate_Q.SetLineColor(rt.kBlue)
      g_2btag_rate_Q.SetLineWidth(2)

      g_le1btag_rate_Q.SetMarkerColor(rt.kGreen)
      g_le1btag_rate_Q.SetLineColor(rt.kGreen)
      g_le1btag_rate_Q.SetLineWidth(2)

      g_1btag_rate_Q.Write("g_1btag_rate")
      g_2btag_rate_Q.Write("g_2btag_rate")
      g_le1btag_rate_Q.Write("g_le1btag_rate")


      rootFile.Close()


    for i in CSV_Value:
       # Draw and print
       # tagging rate vs mass
       c1 = rt.TCanvas()
       c1.SetGridx()
       c1.SetGridy()
       c1.cd()

       
       g_1btag_rate_Q=Do_Inter(g_1btag_rate[i])
       g_2btag_rate_Q=Do_Inter(g_2btag_rate[i])
       g_le1btag_rate_Q=Do_Inter(g_le1btag_rate[i])


       g_1btag_rate_Q.SetMarkerColor(rt.kRed)
       g_1btag_rate_Q.SetLineColor(rt.kRed)
       g_1btag_rate_Q.SetLineWidth(2)
       #g_1btag_rate_Q.Write("g_1btag_rate")

       g_2btag_rate_Q.SetMarkerColor(rt.kBlue)
       g_2btag_rate_Q.SetLineColor(rt.kBlue)
       g_2btag_rate_Q.SetLineWidth(2)
       #g_2btag_rate_Q.Write("g_2btag_rate")

       g_le1btag_rate_Q.SetMarkerColor(rt.kGreen)
       g_le1btag_rate_Q.SetLineColor(rt.kGreen)
       g_le1btag_rate_Q.SetLineWidth(2)
       #g_le1btag_rate_Q.Write("g_le1btag_rate")
 
       g_1btag_rate_Q.Draw("APL")
       g_1btag_rate_Q.GetYaxis().SetRangeUser(0,1)
       g_2btag_rate_Q.Draw("PL,sames")
       g_le1btag_rate_Q.Draw("PL,sames")
   
       leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
       leg.AddEntry(g_1btag_rate_Q,"1-tag","L")
       leg.AddEntry(g_2btag_rate_Q,"2-tag","L")
       leg.AddEntry(g_le1btag_rate_Q,"le1-tag","L")
       leg.Draw("same")
   
       c1.Print(outFolder+"/tagRate_"+flavour+"_"+str(int(i*1000))+".pdf")
   
   
       # close file
       #raw_input("Press Enter to continue...")
   
   
