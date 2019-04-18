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

sampleName = {}

sampleName['qg'] = {
500: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_500GeV_reduced_skim.root',
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_1000GeV_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_2000GeV_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_3000GeV_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_4000GeV_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_5000GeV_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_6000GeV_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_7000GeV_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_8000GeV_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_9000GeV_reduced_skim.root',
                  }

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleName['qq'] = {
1000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG1000GeV_reduced_skim.root',
2000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG2000GeV_reduced_skim.root',
3000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG3000GeV_reduced_skim.root',
4000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG4000GeV_reduced_skim.root',
5000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG5000GeV_reduced_skim.root',
6000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG6000GeV_reduced_skim.root',
7000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG7000GeV_reduced_skim.root',
8000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG8000GeV_reduced_skim.root',
9000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG9000GeV_reduced_skim.root',
                  }


CSV_Value = {
   'L':0.5803,
   'M':0.8838,
   'T':0.9693
}


treeName = "rootTupleTree/tree"
massRange  = {500: [75,0,1500],
              #750: [75,0,1500],
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

Effi={}
Effi['B'] = rt.TFile('/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/python/Efficiency_B.root')
Effi['C'] = rt.TFile('/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/python/Efficiency_C.root')
Effi['UDSG'] = rt.TFile('/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/python/Efficiency_UDSG.root')
def GetEfficiency(pT,Eta,WP,flavor):
  tag = 'CSV'
  n_pt = int(pT/70.0)
  n_eta = int((Eta+3.14159)/(3.14159*2/100.0))
  if flavor ==5 :
    do = 'B'
  elif flavor ==4 :
    do = 'C'
  else:
    do = 'UDSG'
  histo = Effi[do].Get('bTaggingEfficiency_%s_%s'%(tag,WP))
  Eff = histo.GetBinContent(n_pt,n_eta)
  if Eff ==1 :
     return 0.999
  if Eff ==0:
     return 0.001
  return Eff


def bookAndFill(mass,sample,flavour):
    #book histos
    hDict={}
    for i,j in CSV_Value.items():
      hDict[i] = {}

    
    for i,j in CSV_Value.items():
      prefix = str(mass)+"_"+i
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

	for i,j in CSV_Value.items():
           hDict[i]["h_mass_all"].Fill(tchain.mjj)
        
           if model == 'qq':
             if not ( abs(tchain.jetHflavour_j1) == 5 and abs(tchain.jetHflavour_j2) == 5):
               continue

           #implement analysis
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


           hDict[i]["h_mass_passed"].Fill(tchain.mjj)

           P_MC_1=1
           P_MC_2=1
           P_DATA_1=1
           P_DATA_2=1
           nbtag = 0

           if tchain.jetCSVAK4_j1>j:
             nbtag+=1
             P_MC_1 = GetEfficiency(tchain.pTWJ_j1,tchain.etaWJ_j1,i,abs(tchain.jetpflavour_j1))
             P_DATA_1 =  GetEfficiency(tchain.pTWJ_j1,tchain.etaWJ_j1,i,abs(tchain.jetpflavour_j1)) * getattr(tchain,'CSVv2SF_%s_j1'%i.lower())
           else:
             P_MC_1 = 1 - GetEfficiency(tchain.pTWJ_j1,tchain.etaWJ_j1,i,abs(tchain.jetpflavour_j1))
             P_DATA_1 = 1 - GetEfficiency(tchain.pTWJ_j1,tchain.etaWJ_j1,i,abs(tchain.jetpflavour_j1)) * getattr(tchain,'CSVv2SF_%s_j1'%i.lower())
#             SFs.append(getattr(tchain,'CSVv2SF_%s_j1'%i.lower()))
           if tchain.jetCSVAK4_j2>j:
             nbtag+=1
             P_MC_2 = GetEfficiency(tchain.pTWJ_j2,tchain.etaWJ_j2,i,abs(tchain.jetpflavour_j2))
             P_DATA_2 = GetEfficiency(tchain.pTWJ_j2,tchain.etaWJ_j2,i,abs(tchain.jetpflavour_j2)) * getattr(tchain,'CSVv2SF_%s_j2'%i.lower())
           else:
             P_MC_2 = 1 - GetEfficiency(tchain.pTWJ_j2,tchain.etaWJ_j2,i,abs(tchain.jetpflavour_j2))
             P_DATA_2 = 1 - GetEfficiency(tchain.pTWJ_j2,tchain.etaWJ_j2,i,abs(tchain.jetpflavour_j2)) * getattr(tchain,'CSVv2SF_%s_j2'%i.lower())
#             SFs.append(getattr(tchain,'CSVv2SF_%s_j2'%i.lower()))

           #hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj,tchain.evtBweight_m)
           Weight = P_DATA_1*P_DATA_2/P_MC_1/P_MC_2

           if Weight >2:
             print ''
             print GetEfficiency(tchain.pTWJ_j1,tchain.etaWJ_j1,i,abs(tchain.jetpflavour_j1))
             print 'pT:',tchain.pTWJ_j1,'\tEta',tchain.etaWJ_j1,'\tFlavor:',tchain.jetpflavour_j1
             print GetEfficiency(tchain.pTWJ_j2,tchain.etaWJ_j2,i,abs(tchain.jetpflavour_j2))
             print 'pT:',tchain.pTWJ_j2,'\tEta',tchain.etaWJ_j2,'\tFlavor:',tchain.jetpflavour_j2
             print 'Passed:',nbtag
             print i,':',Weight
             print

           if Weight > 10:
             continue



           if nbtag == 0:
             hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj,Weight)
           if nbtag == 1:
             hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj,Weight)
           if nbtag == 2:
             hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj,Weight)
           if nbtag > 0:
             hDict[i]["h_mass_passed_le1b"].Fill(tchain.mjj,Weight)

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

    for mass, sample in sorted(sampleName[model].iteritems()):
        mDict[mass] = bookAndFill(mass,sample,flavour)

    #Create ROOT file and save plain histos
    outName = "signalHistos_"+flavour
    outFolder = "signalHistos_"+flavour+'_Jan_For2017Scan_CSVv2_1a'

    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    if (flavour == "none"):
        outName = ("ResonanceShapes_%s_13TeV_Spring16.root"%model)

    g_an_acc={}
    g_0btag_rate={}
    g_1btag_rate={}
    g_2btag_rate={}
    g_le1btag_rate={}
    g_0btag_weight={}
    g_1btag_weight={}
    g_2btag_weight={}

    #make analysis vs mass
    for i,j in CSV_Value.items():
      g_an_acc[i]    = rt.TGraphAsymmErrors()
  
      g_0btag_rate[i] = rt.TGraphAsymmErrors()
      g_0btag_rate[i].SetTitle("g_0btag_rate;Resonance Mass [GeV];Tagging Rate")
      g_0btag_rate[i].SetLineWidth(2)
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
      for i,j in CSV_Value.items(): 
        num = hDict[i]["h_mass_passed"].GetSumOfWeights()
        den = hDict[i]["h_mass_all"].GetSumOfWeights()
        #g_an_acc.SetPoint(bin,mass,num/den)  #wrong. the reduced ntuples have already the selection implemented

        num = hDict[i]["h_mass_passed_0b"].GetSumOfWeights()
        den = hDict[i]["h_mass_passed"].GetSumOfWeights()
        g_0btag_rate[i].SetPoint(bin,mass,num/den)
        g_0btag_weight[i].SetPoint(bin,mass,hDict[i]["h_weight_0b"].GetMean())
        num = hDict[i]["h_mass_passed_1b"].GetSumOfWeights()
        g_1btag_rate[i].SetPoint(bin,mass,num/den)
        g_1btag_weight[i].SetPoint(bin,mass,hDict[i]["h_weight_1b"].GetMean())

        num = hDict[i]["h_mass_passed_2b"].GetSumOfWeights()
        g_2btag_rate[i].SetPoint(bin,mass,num/den)
        g_2btag_weight[i].SetPoint(bin,mass,hDict[i]["h_weight_2b"].GetMean())

	num = hDict[i]["h_mass_passed_le1b"].GetSumOfWeights()
	g_le1btag_rate[i].SetPoint(bin,mass,num/den)
      bin += 1       
    for i,j in CSV_Value.items(): 
      rootFile = rt.TFile(outFolder+"/"+outName+"_"+i+".root", 'recreate')
      for mass,hDict in sorted(mDict.iteritems()):
        # shape comparison 0 btag
        h1 = rt.TCanvas()
        h1.SetGridx()
        h1.SetGridy()
        h1.cd()  

        hDict[i]["h_mass_passed"].DrawNormalized()
        hDict[i]["h_mass_passed_0b"].DrawNormalized("sames")
        hDict[i]["h_mass_passed_1b"].DrawNormalized("sames")
        hDict[i]["h_mass_passed_2b"].DrawNormalized("sames")

        leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
        leg.AddEntry(hDict[i]["h_mass_passed"],"untagged","L")
        leg.AddEntry(hDict[i]["h_mass_passed_0b"],"0-tag","P")
        leg.AddEntry(hDict[i]["h_mass_passed_1b"],"1-tag","P")
        leg.AddEntry(hDict[i]["h_mass_passed_2b"],"2-tag","P")
        leg.Draw("same")

        h1.Print(outFolder+"/shapes_"+str(mass)+"_"+flavour+"_"+i+".pdf")

        for n,h in hDict[i].items():
            h.Write()
      g_an_acc[i].Write("g_an_acc")
      g_0btag_rate_Q=Do_Inter(g_0btag_rate[i])
      g_1btag_rate_Q=Do_Inter(g_1btag_rate[i])
      g_2btag_rate_Q=Do_Inter(g_2btag_rate[i])
      g_le1btag_rate_Q=Do_Inter(g_le1btag_rate[i])


#        g_0btag_rate_Q.Write("g_0btag_rate")
      g_0btag_rate_Q.SetLineWidth(2)
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

      g_0btag_rate_Q.Write("g_0btag_rate")
      g_1btag_rate_Q.Write("g_1btag_rate")
      g_2btag_rate_Q.Write("g_2btag_rate")
      g_le1btag_rate_Q.Write("g_le1btag_rate")

      g_0btag_weight[i].Write("g_0btag_weight")
      g_1btag_weight[i].Write("g_1btag_weight")
      g_2btag_weight[i].Write("g_2btag_weight")

      rootFile.Close()


    for i,j in CSV_Value.items():
       # Draw and print
       # tagging rate vs mass
       c1 = rt.TCanvas()
       c1.SetGridx()
       c1.SetGridy()
       c1.cd()

       
       g_0btag_rate_Q=Do_Inter(g_0btag_rate[i])
       g_1btag_rate_Q=Do_Inter(g_1btag_rate[i])
       g_2btag_rate_Q=Do_Inter(g_2btag_rate[i])
       g_le1btag_rate_Q=Do_Inter(g_le1btag_rate[i])

       g_0btag_rate_Q.SetLineWidth(2)
       #g_0btag_rate_Q.Write("g_0btag_rate")

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
   
       c1.Print(outFolder+"/tagRate_"+flavour+"_"+i+".pdf")
   
   
       # close file
       #raw_input("Press Enter to continue...")
   
   