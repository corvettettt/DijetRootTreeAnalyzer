import ROOT as rt
import math as math
import sys, os
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
sampleNames_qq = {
#1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/1000GeV_reduced_skim.root',
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/test_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/2000GeV_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/3000GeV_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/4000GeV_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/5000GeV_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/6000GeV_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/7000GeV_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/8000GeV_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ/9000GeV_reduced_skim.root',
                  }

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleNames_qg = { 
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_1000_20180701_054551_0_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_2000_20180701_054603_0_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_3000_20180701_054616_0_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_4000_20180701_054628_0_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_5000_20180701_054641_0_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_6000_20180701_054653_0_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_7000_20180701_054706_0_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_8000_20180701_054718_0_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_9000_20180701_054731_0_reduced_skim.root',

                  }


CSV_Value = [0.1,0.15,0.2219,0.3,0.35,0.4,0.45,0.5, 0.5426,0.6, 0.6324,0.7,0.75,0.8, 0.8484, 0.8958, 0.9535]

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleNames_gg = {
                  1000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/1000GeV_reduced_skim.root',
    #              2000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/2000GeV_reduced_skim.root',
    #              3000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/3000GeV_reduced_skim.root',
    #              4000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/4000GeV_reduced_skim.root',
    #              5000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/5000GeV_reduced_skim.root',
    #              6000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/6000GeV_reduced_skim.root',
    #              7000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/7000GeV_reduced_skim.root',
    #              8000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/8000GeV_reduced_skim.root',
    #              9000 : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BstarToJJ/bstar/9000GeV_reduced_skim.root'
                  }

treeName = "rootTupleTree/tree"
massRange  = {#500: [75,0,1500],
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



def progressbar(it, prefix="", size=60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()



def QuaInter(F):
  def Func(x):
     z = 0
     mass = [1000.0,2000.0,3000.0,4000.0,5000.0,6000.0,7000.0,8000.0,9000.0]
     for i in mass:
        term = 1.0
        for j in [y for y in mass if y!=i]:
           term = (float(x)-float(j))/(float(i)-float(j))*term
        z=z+term*F.Eval(i)
     return  z
  return Func

def Do_Inter(Rate):
  mass = [1000.0,2000.0,3000.0,4000.0,5000.0,6000.0,7000.0,8000.0,9000.0]
  Inter = QuaInter (Rate)
  Return_plot = rt.TGraphAsymmErrors()
  num = -1
  for M in range(1000,9000,100):
     num=num+1
     Return_plot.SetPoint(num,M,Inter(M))
  return Return_plot

def bookAndFill(mass,sample,flavour):
 
#[0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.46,0.5,0.55,0.5803,0.60,0.65,0.70,0.75,0.8,0.85,0.8838,0.9,0.935,0.95,0.9693]#[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.46,0.5,0.55,0.60,0.65,0.70,0.75,0.8,0.85,0.9,0.935,0.95]
#    CSV_Value=[0.5,0.6,0.7,0.8,0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94,0.95,0.96]
    #CSV_Value=[0.82,0.84,0.86,0.88]#0.5,0.6,0.7,0.8,0.85,0.9,0.91,0.93,0.95,0.97]

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

    for i in progressbar(range(nEntries), "Mass "+str(mass)+": ", 40):
        tchain.GetEntry(i)


        #select flavour
        if (flavour == "bb" and (tchain.jetHflavour_j1 != 5 or tchain.jetHflavour_j2 != 5)):
            continue
        elif (flavour == "cc" and (tchain.jetHflavour_j1 != 4 or tchain.jetHflavour_j2 != 4)):
            continue
        elif (flavour == "qq" and (tchain.jetHflavour_j1 == 4 or tchain.jetHflavour_j1 == 5 or tchain.jetHflavour_j2 == 4 or tchain.jetHflavour_j2 == 5  )):
            continue
        elif (flavour == "bg" and (tchain.jetHflavour_j1 != 5 and tchain.jetHflavour_j2 != 5  )):
            continue
	for i in CSV_Value:
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

           NBjet=0
 	   if tchain.jetCSVAK4_j1>i:
	      NBjet = NBjet + 1
           if tchain.jetCSVAK4_j2>i:
              NBjet = NBjet + 1
	
           if NBjet == 0:
              #hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj,tchain.evtBweight_m)
              hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj)
              hDict[i]["h_weight_0b"].Fill(tchain.evtBweight_m)
           if NBjet == 1:
              #hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj,tchain.evtBweight_m)
              hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj)
              hDict[i]["h_weight_1b"].Fill(tchain.evtBweight_m)
           if NBjet == 2:
              #hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj,tchain.evtBweight_m)
              hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj)
              hDict[i]["h_weight_2b"].Fill(tchain.evtBweight_m)
	   if NBjet > 0:
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
    (options,args) = parser.parse_args()
    flavour = options.flavour
    model   = options.model

    print "selected flavour:",flavour
    print "signal model    :",model
    ###################################################################


    # book histos and graphs
    mDict = {}
    sampleNames = {}

    # loop over the MC samples
    if (model == "qq"):
        sampleNames = sampleNames_qq
    elif (model == "qg"):
        sampleNames = sampleNames_qg
    elif (model == "gg"):
        sampleNames = sampleNames_gg
    else:
        print "model unknown"
        exit

    for mass, sample in sorted(sampleNames.iteritems()):
        mDict[mass] = bookAndFill(mass,sample,flavour)
        



    #Create ROOT file and save plain histos
    outName = "signalHistos_"+flavour
    outFolder = "signalHistos_"+flavour+'_Oct_For2016Scan_CSVv2_2'

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
    for i in CSV_Value:
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
      for i in CSV_Value: 
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
     
    for i in CSV_Value:
      rootFile = rt.TFile(outFolder+"/"+outName+"_"+str(int(i*1000))+".root", 'recreate')
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

        h1.Print(outFolder+"/shapes_"+str(mass)+"_"+flavour+"_"+str(int(i*1000))+".pdf")

        for n,h in mDict[mass][i].iteritems():
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


    for i in CSV_Value:
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

       g_1btag_rate_Q.SetTitle('Tagging Rate of CSVv2='+str(i)+';Mass (GeV);Tagging Rate') 
       g_1btag_rate_Q.Draw("APL")
       g_1btag_rate_Q.GetYaxis().SetRangeUser(0,1)
       g_2btag_rate_Q.Draw("PL,sames")
       g_le1btag_rate_Q.Draw("PL,sames")
   
       leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
       leg.AddEntry(g_1btag_rate_Q,"1-tag","L")
       leg.AddEntry(g_2btag_rate_Q,"2-tag","L")
       leg.AddEntry(g_le1btag_rate_Q,"ge1-tag","L")
       leg.Draw("same")
   
       c1.Print(outFolder+"/tagRate_"+flavour+"_"+str(int(i*1000))+".pdf")
   
   
       # close file
       #raw_input("Press Enter to continue...")
   
   
