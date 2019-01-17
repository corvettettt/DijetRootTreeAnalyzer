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
sampleNames_qq={}
sampleNames_qq['central'] = {
1000:
2000:
3000:
4000:
5000:
6000:
7000:
8000:
9000:
                 }
sampleNames_qq['up'] = {
1000:
2000:
3000:
4000:
5000:
6000:
7000:
8000:
9000:
                 }
sampleNames_qq['down'] = {
1000:
2000:
3000:
4000:
5000:
6000:
7000:
8000:
9000:
                 }


sampleNames_qg={} 
sampleNames_qg['central'] = {
500:
1000:
2000:
3000:
4000:
5000:
6000:
7000:
8000:
9000:
                 }
sampleNames_qg['up'] = {
500:
1000:
2000:
3000:
4000:
5000:
6000:
7000:
8000:
9000:
                 }
sampleNames_qg['down'] = {
500:
1000:
2000:
3000:
4000:
5000:
6000:
7000:
8000:
9000:
                 }

CSV_Value = {
   'L':0.2219,
   'M':0.6324,
   'T':0.8958
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
def bookAndFill(mass,sample,flavour):
 
#    CSV_Value = [0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693] 
#[0.05,0.1,0.15,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5,0.55,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9,0.95,0.9693] 
#    CSV_Value=[0.5,0.6,0.7,0.8,0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94,0.95,0.96]
    #CSV_Value=[0.82,0.84,0.86,0.88]#0.5,0.6,0.7,0.8,0.85,0.9,0.91,0.93,0.95,0.97]

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

    for i in progressbar(range(nEntries), "Mass "+str(mass)+": ", 40):
        tchain.GetEntry(i)


	for i,j in CSV_Value.items():
           hDict[i]["h_mass_all"].Fill(tchain.mjj)
        
        #implement analysis
           if not (abs(tchain.deltaETAjj)<1.3       and
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

           SFs = []
           if tchain.jetDeepCSVAK4_j1>j:
             SFs.append(getattr(tchain,'DeepSF_%s_j1'%i.low()))
           if tchain.jetDeepCSVAK4_j2>j:
             SFs.append(getattr(tchain,'DeepSF_%s_j2'%i.low()))

           #hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj,tchain.evtBweight_m)
           hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj,bWeight(SFs,0))

           hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj,bWeight(SFs,1))

           hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj,bWeight(SFs,2))

           hDict[i]["h_mass_passed_le1b"].Fill(tchain.mjj,bWeight(SFs,1))
           hDict[i]["h_mass_passed_le1b"].Fill(tchain.mjj,bWeight(SFs,2))

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

    if model =='qq':
      massRange[500]= [75,0,1500]

#    CSV_Value = [0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693]

    # book histos and graphs
    mDict = {}
    sampleNames = {}

    # loop over the MC samples
    if (model == "qq"):
        sampleNames = sampleNames_qq[su]
    elif (model == "qg"):
        sampleNames = sampleNames_qg[su]
    else:
        print "model unknown"
        exit

    for mass, sample in sorted(sampleNames.iteritems()):
        mDict[mass] = bookAndFill(mass,sample,flavour)
        



    #Create ROOT file and save plain histos
    outName = "signalHistos_"+flavour
    outFolder = "signalHistos_"+flavour+'_Dec_For2016Scan_deep_'+su

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
 
       g_0btag_rate_Q.Draw("APL")
       g_0btag_rate_Q.GetYaxis().SetRangeUser(0,1)
       g_1btag_rate_Q.Draw("PL,sames")
       g_2btag_rate_Q.Draw("PL,sames")
       g_le1btag_rate_Q.Draw("PL,sames")
   
       leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
       leg.AddEntry(g_0btag_rate_Q,"0-tag","L")
       leg.AddEntry(g_1btag_rate_Q,"1-tag","L")
       leg.AddEntry(g_2btag_rate_Q,"2-tag","L")
       leg.AddEntry(g_le1btag_rate_Q,"le1-tag","L")
       leg.Draw("same")
   
       c1.Print(outFolder+"/tagRate_"+flavour+"_"+i+".pdf")
   
   
       # close file
       #raw_input("Press Enter to continue...")
   
   
