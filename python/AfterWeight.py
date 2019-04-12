from ROOT import *
import sys,os
from optparse import OptionParser

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

def progressbar(it, prefix="", size=60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i)
    sys.stdout.write("\n")
    sys.stdout.flush()

CSV_Value={}
CSV_Value['CSV'] = {
   'L':0.5803,
   'M':0.8838,
   'T':0.9693
}

CSV_Value['DeepCSV'] = {
   'L':0.1522,
   'M':0.4941,
   'T':0.8001
}

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
    tchain = rt.TChain(treeName)
    tchain.Add(sample)
    nEntries = tchain.GetEntries()

    for i in progressbar(range(nEntries), "Mass "+str(mass)+": ", 40):
        tchain.GetEntry(i)

        for i in CSV_Value:
           hDict[i]["h_mass_all"].Fill(tchain.mjj)

           if (flavour == "bb" and (tchain.jetHflavour_j1 != 5 or tchain.jetHflavour_j2 != 5)):
             continue

           if not (abs(tchain.deltaETAjj)<1.1       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                tchain.pTWJ_j2>30                and

                tchain.PassJSON):
            continue

           hDict[i]["h_mass_passed"].Fill(tchain.mjj)

           NBjet=0
           if tchain.jetDeepCSVAK4_j1>i:
              NBjet = NBjet + 1
           if tchain.jetDeepCSVAK4_j2>i:
              NBjet = NBjet + 1

           if NBjet == 0:
              hDict[i]["h_mass_passed_0b"].Fill(tchain.mjj)
           if NBjet == 1:
              #hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj,tchain.evtBweight_m)
              hDict[i]["h_mass_passed_1b"].Fill(tchain.mjj)
           if NBjet == 2:
              #hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj,tchain.evtBweight_m)
              hDict[i]["h_mass_passed_2b"].Fill(tchain.mjj)
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

    for mass, sample in sorted(sampleName[model].iteritems()):
        mDict[mass] = bookAndFill(mass,sample,flavour)

