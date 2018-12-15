from optparse import OptionParser
from framework import Config
import ROOT as rt
import math as math
import sys




usage = """usage: python python/bTag_fordqm.py -c config/bTag.cfg -b BTag2016_fordqm"""



def deltaR2( e1, p1, e2, p2):
    de = e1 - e2
    dp = deltaPhi(p1, p2)
    return de*de + dp*dp


def deltaR( *args ):
    return math.sqrt( deltaR2(*args) )


def deltaPhi( p1, p2):
    '''Computes delta phi, handling periodic limit conditions.'''
    res = p1 - p2
    while res > math.pi:
        res -= 2*math.pi
    while res < -math.pi:
        res += 2*math.pi
    return res



if __name__ == '__main__':
    ###################################################################
    parser = OptionParser(usage=usage)
    parser.add_option('-c','--config',dest="config",type="string",default="config/bTag_analysis.cfg",
                  help="Name of the config file to use")
    parser.add_option('-b','--box',dest="box", default="BTag2016",type="string",
                  help="box name")

    rt.RooMsgService.instance().setGlobalKillBelow(rt.RooFit.FATAL)

    (options,args) = parser.parse_args()
    
    cfg = Config.Config(options.config)
    box = options.box

    inputData       = cfg.getVariables(box,"inputDataNtu")
    treeName        = cfg.getVariables(box,"treeName")
    outFile         = cfg.getVariables(box,"outFile")

    tight = cfg.getVariables(box,"tight")
    medium = cfg.getVariables(box,"medium")
    dR = cfg.getVariables(box,"deltaR")
    
    ###################################################################

    print treeName
    tchain = rt.TChain(treeName)
    for i, line in enumerate(inputData):
        tchain.Add(line)


    nEntries = tchain.GetEntries()
    print 'Number of entries: ', nEntries

    # Book histos
             #bins,min,max
    ptRange = [400,0,4000]
    mjjRange = [750,500,8000]
    etaRange = [1000,-3.5,3.5]
    phiRange = [360,-3.1415,3.1415]
    csvRange = [100,0,1]
    
    allHistos = []

    ##reco
    h_csv_j1_reco = rt.TH1F("csv_j1_reco","",csvRange[0],csvRange[1],csvRange[2])
    h_csv_j2_reco = rt.TH1F("csv_j2_reco","",csvRange[0],csvRange[1],csvRange[2])

    h_mjj_reco = rt.TH1F("mjj_reco","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag0_tight_reco = rt.TH1F("mjj_btag0_tight_reco","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag1_tight_reco = rt.TH1F("mjj_btag1_tight_reco","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag2_tight_reco = rt.TH1F("mjj_btag2_tight_reco","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag0_medium_reco = rt.TH1F("mjj_btag0_medium_reco","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag1_medium_reco = rt.TH1F("mjj_btag1_medium_reco","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag2_medium_reco = rt.TH1F("mjj_btag2_medium_reco","",mjjRange[0],mjjRange[1],mjjRange[2])

    h_pt_j1_reco = rt.TH1F("pt_j1_reco","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j2_reco = rt.TH1F("pt_j2_reco","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j1_btag_tight_reco = rt.TH1F("pt_j1_btag_tight_reco","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j2_btag_tight_reco = rt.TH1F("pt_j2_btag_tight_reco","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j1_btag_medium_reco = rt.TH1F("pt_j1_btag_medium_reco","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j2_btag_medium_reco = rt.TH1F("pt_j2_btag_medium_reco","",ptRange[0],ptRange[1],ptRange[2])

    h_eta_j1_reco = rt.TH1F("eta_j1_reco","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j2_reco = rt.TH1F("eta_j2_reco","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j1_btag_tight_reco = rt.TH1F("eta_j1_btag_tight_reco","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j2_btag_tight_reco = rt.TH1F("eta_j2_btag_tight_reco","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j1_btag_medium_reco = rt.TH1F("eta_j1_btag_medium_reco","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j2_btag_medium_reco = rt.TH1F("eta_j2_btag_medium_reco","",etaRange[0],etaRange[1],etaRange[2])

    h_phi_j1_reco = rt.TH1F("phi_j1_reco","",phiRange[0],phiRange[1],phiRange[2])
    h_phi_j2_reco = rt.TH1F("phi_j2_reco","",phiRange[0],phiRange[1],phiRange[2])
    h_phi_j1_btag_tight_reco = rt.TH1F("phi_j1_btag_tight_reco","",phiRange[0],phiRange[1],phiRange[2])
    h_phi_j2_btag_tight_reco = rt.TH1F("phi_j2_btag_tight_reco","",phiRange[0],phiRange[1],phiRange[2])
    h_phi_j1_btag_medium_reco = rt.TH1F("phi_j1_btag_medium_reco","",phiRange[0],phiRange[1],phiRange[2])
    h_phi_j2_btag_medium_reco = rt.TH1F("phi_j2_btag_medium_reco","",phiRange[0],phiRange[1],phiRange[2])


    allHistos.extend([h_csv_j1_reco,h_csv_j2_reco])
    allHistos.extend([h_mjj_reco,h_mjj_btag0_tight_reco,h_mjj_btag1_tight_reco,h_mjj_btag2_tight_reco,h_mjj_btag0_medium_reco,h_mjj_btag1_medium_reco,h_mjj_btag2_medium_reco])
    allHistos.extend([h_pt_j1_reco,h_pt_j2_reco,h_pt_j1_btag_tight_reco,h_pt_j2_btag_tight_reco,h_pt_j1_btag_medium_reco,h_pt_j2_btag_medium_reco])
    allHistos.extend([h_eta_j1_reco,h_eta_j2_reco,h_eta_j1_btag_tight_reco,h_eta_j2_btag_tight_reco,h_eta_j1_btag_medium_reco,h_eta_j2_btag_medium_reco])
    allHistos.extend([h_phi_j1_reco,h_phi_j2_reco,h_phi_j1_btag_tight_reco,h_phi_j2_btag_tight_reco,h_phi_j1_btag_medium_reco,h_phi_j2_btag_medium_reco])




    for h in allHistos:
        if 'mjj' in h.GetName():
            h.GetXaxis().SetTitle("Mjj [GeV]")
        elif 'pt' in h.GetName():
            h.GetXaxis().SetTitle("Pt [GeV]")
        elif 'eta' in h.GetName():
            h.GetXaxis().SetTitle("Eta")
        elif 'phi' in h.GetName():
            h.GetXaxis().SetTitle("Phi")
        elif 'csv' in h.GetName():
            h.GetXaxis().SetTitle("CSV")

        






    #loop over entries
    for i in xrange(nEntries):
    #for i in xrange(300000):
        if i%100000 == 0:
            print "analyzing event: ",i

        tchain.GetEntry(i)

        #implement analysis
        if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                tchain.pTWJ_j1<6500              and
                tchain.pTWJ_j2>30                and
                tchain.pTWJ_j2<6500              and

                tchain.mjj > 1246                and
                tchain.mjj < 14000               and
                
                tchain.PassJSON):
            continue



        recoJet1 = rt.TLorentzVector()
        recoJet2 = rt.TLorentzVector()
        recoJet1.SetPtEtaPhiM(tchain.pTWJ_j1,tchain.etaWJ_j1,tchain.phiWJ_j1,tchain.massWJ_j1)
        recoJet2.SetPtEtaPhiM(tchain.pTWJ_j2,tchain.etaWJ_j2,tchain.phiWJ_j2,tchain.massWJ_j2)
        recoJets = [recoJet1,recoJet2]
        recoCSV = [tchain.jetCSVAK4_j1,tchain.jetCSVAK4_j2]
        recoMjj = (recoJets[0]+recoJets[1]).M()

        #fill histograms
        h_mjj_reco.Fill(recoMjj)

        h_pt_j1_reco.Fill(recoJets[0].Pt())
        h_pt_j2_reco.Fill(recoJets[1].Pt())
        h_eta_j1_reco.Fill(recoJets[0].Eta())
        h_eta_j2_reco.Fill(recoJets[1].Eta())
        h_phi_j1_reco.Fill(recoJets[0].Phi())
        h_phi_j2_reco.Fill(recoJets[1].Phi())
    
        h_csv_j1_reco.Fill(recoCSV[0])
        h_csv_j2_reco.Fill(recoCSV[1])

        n_jets_t_reco = 0
        n_jets_m_reco = 0


        #reco j1
        if recoCSV[0] > tight:
            n_jets_t_reco+=1
            h_pt_j1_btag_tight_reco.Fill(recoJets[0].Pt())
            h_eta_j1_btag_tight_reco.Fill(recoJets[0].Eta())
            h_phi_j1_btag_tight_reco.Fill(recoJets[0].Phi())
        if recoCSV[0] > medium:
            n_jets_m_reco+=1
            h_pt_j1_btag_medium_reco.Fill(recoJets[0].Pt())
            h_eta_j1_btag_medium_reco.Fill(recoJets[0].Eta())
            h_phi_j1_btag_medium_reco.Fill(recoJets[0].Phi())
        #reco j2
        if recoCSV[1] > tight:
            n_jets_t_reco+=1
            h_pt_j2_btag_tight_reco.Fill(recoJets[1].Pt())
            h_eta_j2_btag_tight_reco.Fill(recoJets[1].Eta())
            h_phi_j2_btag_tight_reco.Fill(recoJets[1].Phi())
        if recoCSV[1] > medium:
            n_jets_m_reco+=1
            h_pt_j2_btag_medium_reco.Fill(recoJets[1].Pt())
            h_eta_j2_btag_medium_reco.Fill(recoJets[1].Eta())
            h_phi_j2_btag_medium_reco.Fill(recoJets[1].Phi())


            
        if n_jets_t_reco == 1:
            h_mjj_btag1_tight_reco.Fill(recoMjj)
        elif n_jets_t_reco == 2:
            h_mjj_btag2_tight_reco.Fill(recoMjj)
        else:
            h_mjj_btag0_tight_reco.Fill(recoMjj)


        if n_jets_m_reco == 1:
            h_mjj_btag1_medium_reco.Fill(recoMjj)
        elif n_jets_m_reco == 2:
            h_mjj_btag2_medium_reco.Fill(recoMjj)
        else:
            h_mjj_btag0_medium_reco.Fill(recoMjj)



             
    #end loop


    rt.gROOT.SetBatch(rt.kTRUE)

    #Create ROOT file
    rootFile = rt.TFile(outFile, 'recreate')

    h_csv_j1_reco.Write()
    h_csv_j2_reco.Write()

    #reco    
    h_mjj_reco.Write()
    h_mjj_btag0_tight_reco.Write()
    h_mjj_btag1_tight_reco.Write()
    h_mjj_btag2_tight_reco.Write()
    h_mjj_btag0_medium_reco.Write()
    h_mjj_btag1_medium_reco.Write()
    h_mjj_btag2_medium_reco.Write()

    h_pt_j1_btag_tight_reco.Write()   
    h_pt_j2_btag_tight_reco.Write()   
    h_pt_j1_btag_medium_reco.Write()   
    h_pt_j2_btag_medium_reco.Write()   
    h_pt_j1_reco.Write()
    h_pt_j2_reco.Write()
    h_eta_j1_btag_tight_reco.Write()   
    h_eta_j2_btag_tight_reco.Write()   
    h_eta_j1_btag_medium_reco.Write()   
    h_eta_j2_btag_medium_reco.Write()   
    h_eta_j1_reco.Write()
    h_eta_j2_reco.Write()
    h_phi_j1_btag_tight_reco.Write()   
    h_phi_j2_btag_tight_reco.Write()   
    h_phi_j1_btag_medium_reco.Write()   
    h_phi_j2_btag_medium_reco.Write()   
    h_phi_j1_reco.Write()
    h_phi_j2_reco.Write()
    



    rootFile.Close()
