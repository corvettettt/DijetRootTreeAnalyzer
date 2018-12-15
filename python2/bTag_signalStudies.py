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
eosPath = "/tmp/deguio/"
sampleNames_qq = {#500: eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_500_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  #750:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_750_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  1000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  #2000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_2000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  3000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_3000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  4000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  5000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_5000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  6000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_6000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  7000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_7000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  8000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_8000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  9000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root"
                  }

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleNames_qg = {500:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_500_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  750:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_750_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  1000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_1000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  2000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_2000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  3000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_3000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  4000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_4000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  5000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_5000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  6000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_6000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  7000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_7000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  8000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_8000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root",
                  9000:  eosPrefix+eosPath+"rootfile_QstarToJJ_M_9000_TuneCUETP8M1_13TeV_pythia8_QstarToJJ_TuneCUETP8M1_13TeV_pythia8_20170115_213938_0_reduced_skim.root"
                  }

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleNames_gg = {#500: eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_500_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  #750:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_750_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  1000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  #2000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_2000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  3000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_3000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  4000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  5000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_5000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  6000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_6000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  7000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_7000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  8000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_8000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root",
                  9000:  eosPrefix+eosPath+"rootfile_RSGravitonToQuarkQuark_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8_RSGravitonToQuarkQuark_kMpl01_Spring16_20161214_115751_0_reduced_skim.root"
                  }

treeName = "rootTupleTree/tree"
massRange  = {500: [75,0,1500],
              750: [75,0,1500],
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




def bookAndFill(mass,sample,flavour):
    
    #book histos
    hDict = {}

    prefix = str(mass)
    hDict["h_mass_all"]    = rt.TH1F(prefix+"_mass_all",   prefix+"_mass_all",   massRange[mass][0],massRange[mass][1],massRange[mass][2])
    hDict["h_mass_passed"] = rt.TH1F(prefix+"_mass_passed",prefix+"_mass_passed",massRange[mass][0],massRange[mass][1],massRange[mass][2])
    hDict["h_mass_passed"].SetLineColor(rt.kOrange+8)
    hDict["h_mass_passed"].SetMarkerColor(rt.kOrange+8)
    hDict["h_mass_passed"].SetLineWidth(3)
    hDict["h_mass_passed"].GetXaxis().SetTitle("Resonance Mass [GeV]")

    hDict["h_mass_passed_0b"] = rt.TH1F(prefix+"_mass_passed_0b",prefix+"_mass_passed_0b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
    hDict["h_mass_passed_0b"].SetMarkerSize(0.5)

    hDict["h_mass_passed_1b"] = rt.TH1F(prefix+"_mass_passed_1b",prefix+"_mass_passed_1b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
    hDict["h_mass_passed_1b"].SetLineColor(rt.kRed)
    hDict["h_mass_passed_1b"].SetMarkerColor(rt.kRed)
    hDict["h_mass_passed_1b"].SetMarkerSize(0.5)
    
    hDict["h_mass_passed_2b"] = rt.TH1F(prefix+"_mass_passed_2b",prefix+"_mass_passed_2b",massRange[mass][0],massRange[mass][1],massRange[mass][2])
    hDict["h_mass_passed_2b"].SetLineColor(rt.kBlue)
    hDict["h_mass_passed_2b"].SetMarkerColor(rt.kBlue)
    hDict["h_mass_passed_2b"].SetMarkerSize(0.5)

    hDict["h_weight_0b"] = rt.TH1F(prefix+"_weight_0b",prefix+"_weight_0b",2000,0.,2.)
    hDict["h_weight_1b"] = rt.TH1F(prefix+"_weight_1b",prefix+"_weight_1b",2000,0.,2.)
    hDict["h_weight_2b"] = rt.TH1F(prefix+"_weight_2b",prefix+"_weight_2b",2000,0.,2.)



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

        hDict["h_mass_all"].Fill(tchain.mjj)
        
        #implement analysis
        if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                tchain.pTWJ_j1<6500              and
                tchain.pTWJ_j2>30                and
                tchain.pTWJ_j2<6500              and

                #tchain.mjj > 1246                and
                #tchain.mjj < 14000               and
                
                tchain.PassJSON):
            continue


        hDict["h_mass_passed"].Fill(tchain.mjj)
        
        if tchain.nBjets_m == 0:
            #hDict["h_mass_passed_0b"].Fill(tchain.mjj,tchain.evtBweight_m)
            hDict["h_mass_passed_0b"].Fill(tchain.mjj)
            hDict["h_weight_0b"].Fill(tchain.evtBweight_m)
        elif tchain.nBjets_m == 1:
            #hDict["h_mass_passed_1b"].Fill(tchain.mjj,tchain.evtBweight_m)
            hDict["h_mass_passed_1b"].Fill(tchain.mjj)
            hDict["h_weight_1b"].Fill(tchain.evtBweight_m)
        elif tchain.nBjets_m == 2:
            #hDict["h_mass_passed_2b"].Fill(tchain.mjj,tchain.evtBweight_m)
            hDict["h_mass_passed_2b"].Fill(tchain.mjj)
            hDict["h_weight_2b"].Fill(tchain.evtBweight_m)
            

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
    outName = "signalHistos_"+flavour+".root"
    outFolder = "signalHistos_"+flavour

    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    if (flavour == "none"):
        outName = ("ResonanceShapes_%s_13TeV_Spring16.root"%model)

    rootFile = rt.TFile(outFolder+"/"+outName, 'recreate')


    #make analysis vs mass
    g_an_acc    = rt.TGraphAsymmErrors()

    g_0btag_rate = rt.TGraphAsymmErrors()
    g_0btag_rate.SetTitle("g_0btag_rate;Resonance Mass [GeV];Tagging Rate")
    g_0btag_rate.SetLineWidth(2)
    g_1btag_rate = rt.TGraphAsymmErrors()
    g_1btag_rate.SetMarkerColor(rt.kRed)
    g_1btag_rate.SetLineColor(rt.kRed)
    g_1btag_rate.SetLineWidth(2)
    g_2btag_rate = rt.TGraphAsymmErrors()
    g_2btag_rate.SetMarkerColor(rt.kBlue)
    g_2btag_rate.SetLineColor(rt.kBlue)
    g_2btag_rate.SetLineWidth(2)

    g_0btag_weight = rt.TGraphAsymmErrors()
    g_1btag_weight = rt.TGraphAsymmErrors()
    g_2btag_weight = rt.TGraphAsymmErrors()


    
    bin = 0
    for mass,hDict in sorted(mDict.iteritems()):
        
        num = hDict["h_mass_passed"].GetSumOfWeights()
        den = hDict["h_mass_all"].GetSumOfWeights()
        #g_an_acc.SetPoint(bin,mass,num/den)  #wrong. the reduced ntuples have already the selection implemented

        num = hDict["h_mass_passed_0b"].GetSumOfWeights()
        den = hDict["h_mass_passed"].GetSumOfWeights()
        g_0btag_rate.SetPoint(bin,mass,num/den)
        g_0btag_weight.SetPoint(bin,mass,hDict["h_weight_0b"].GetMean())

        num = hDict["h_mass_passed_1b"].GetSumOfWeights()
        g_1btag_rate.SetPoint(bin,mass,num/den)
        g_1btag_weight.SetPoint(bin,mass,hDict["h_weight_1b"].GetMean())

        num = hDict["h_mass_passed_2b"].GetSumOfWeights()
        g_2btag_rate.SetPoint(bin,mass,num/den)
        g_2btag_weight.SetPoint(bin,mass,hDict["h_weight_2b"].GetMean())
       
        # shape comparison 0 btag
        h1 = rt.TCanvas()
        h1.SetGridx()
        h1.SetGridy()
        h1.cd()  

        hDict["h_mass_passed"].DrawNormalized()
        hDict["h_mass_passed_0b"].DrawNormalized("sames")
        hDict["h_mass_passed_1b"].DrawNormalized("sames")
        hDict["h_mass_passed_2b"].DrawNormalized("sames")

        leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
        leg.AddEntry(hDict["h_mass_passed"],"untagged","L")
        leg.AddEntry(hDict["h_mass_passed_0b"],"0-tag","P")
        leg.AddEntry(hDict["h_mass_passed_1b"],"1-tag","P")
        leg.AddEntry(hDict["h_mass_passed_2b"],"2-tag","P")
        leg.Draw("same")


        h1.Print(outFolder+"/shapes_"+str(mass)+"_"+flavour+".pdf")

        bin += 1
        for n,h in hDict.iteritems():
            h.Write()




    g_an_acc.Write("g_an_acc")

    g_0btag_rate.Write("g_0btag_rate")
    g_1btag_rate.Write("g_1btag_rate")
    g_2btag_rate.Write("g_2btag_rate")

    g_0btag_weight.Write("g_0btag_weight")
    g_1btag_weight.Write("g_1btag_weight")
    g_2btag_weight.Write("g_2btag_weight")

    # Draw and print
    # tagging rate vs mass
    c1 = rt.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.cd()

    g_0btag_rate.Draw("APL")
    g_0btag_rate.GetYaxis().SetRangeUser(0,1)
    g_1btag_rate.Draw("PL,sames")
    g_2btag_rate.Draw("PL,sames")

    leg = rt.TLegend(0.87, 0.80, 0.96, 0.89)
    leg.AddEntry(g_0btag_rate,"0-tag","L")
    leg.AddEntry(g_1btag_rate,"1-tag","L")
    leg.AddEntry(g_2btag_rate,"2-tag","L")
    leg.Draw("same")

    c1.Print(outFolder+"/tagRate_"+flavour+".pdf")


    # close file
    #raw_input("Press Enter to continue...")
    rootFile.Close()


