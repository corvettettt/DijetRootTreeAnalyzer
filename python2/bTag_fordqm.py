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
    ptRange = [100,0,1000]
    mjjRange = [150,500,2000]
    etaRange = [100,-3.5,3.5]
    csvRange = [20,0,1]
    
    allHistos = []

    ##calo
    h_csv_j1_calo = rt.TH1F("csv_j1_calo","",csvRange[0],csvRange[1],csvRange[2])
    h_csv_j2_calo = rt.TH1F("csv_j2_calo","",csvRange[0],csvRange[1],csvRange[2])

    h_mjj_calo = rt.TH1F("mjj_calo","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag0_tight_calo = rt.TH1F("mjj_btag0_tight_calo","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag1_tight_calo = rt.TH1F("mjj_btag1_tight_calo","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag2_tight_calo = rt.TH1F("mjj_btag2_tight_calo","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag0_medium_calo = rt.TH1F("mjj_btag0_medium_calo","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag1_medium_calo = rt.TH1F("mjj_btag1_medium_calo","",mjjRange[0],mjjRange[1],mjjRange[2])
    h_mjj_btag2_medium_calo = rt.TH1F("mjj_btag2_medium_calo","",mjjRange[0],mjjRange[1],mjjRange[2])

    h_pt_j1_calo = rt.TH1F("pt_j1_calo","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j2_calo = rt.TH1F("pt_j2_calo","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j1_btag_tight_calo = rt.TH1F("pt_j1_btag_tight_calo","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j2_btag_tight_calo = rt.TH1F("pt_j2_btag_tight_calo","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j1_btag_medium_calo = rt.TH1F("pt_j1_btag_medium_calo","",ptRange[0],ptRange[1],ptRange[2])
    h_pt_j2_btag_medium_calo = rt.TH1F("pt_j2_btag_medium_calo","",ptRange[0],ptRange[1],ptRange[2])

    h_eta_j1_calo = rt.TH1F("eta_j1_calo","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j2_calo = rt.TH1F("eta_j2_calo","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j1_btag_tight_calo = rt.TH1F("eta_j1_btag_tight_calo","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j2_btag_tight_calo = rt.TH1F("eta_j2_btag_tight_calo","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j1_btag_medium_calo = rt.TH1F("eta_j1_btag_medium_calo","",etaRange[0],etaRange[1],etaRange[2])
    h_eta_j2_btag_medium_calo = rt.TH1F("eta_j2_btag_medium_calo","",etaRange[0],etaRange[1],etaRange[2])

    allHistos.extend([h_csv_j1_calo,h_csv_j2_calo])
    allHistos.extend([h_mjj_calo,h_mjj_btag0_tight_calo,h_mjj_btag1_tight_calo,h_mjj_btag2_tight_calo,h_mjj_btag0_medium_calo,h_mjj_btag1_medium_calo,h_mjj_btag2_medium_calo])
    allHistos.extend([h_pt_j1_calo,h_pt_j2_calo,h_pt_j1_btag_tight_calo,h_pt_j2_btag_tight_calo,h_pt_j1_btag_medium_calo,h_pt_j2_btag_medium_calo])
    allHistos.extend([h_eta_j1_calo,h_eta_j2_calo,h_eta_j1_btag_tight_calo,h_eta_j2_btag_tight_calo,h_eta_j1_btag_medium_calo,h_eta_j2_btag_medium_calo])


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


    allHistos.extend([h_csv_j1_reco,h_csv_j2_reco])
    allHistos.extend([h_mjj_reco,h_mjj_btag0_tight_reco,h_mjj_btag1_tight_reco,h_mjj_btag2_tight_reco,h_mjj_btag0_medium_reco,h_mjj_btag1_medium_reco,h_mjj_btag2_medium_reco])
    allHistos.extend([h_pt_j1_reco,h_pt_j2_reco,h_pt_j1_btag_tight_reco,h_pt_j2_btag_tight_reco,h_pt_j1_btag_medium_reco,h_pt_j2_btag_medium_reco])
    allHistos.extend([h_eta_j1_reco,h_eta_j2_reco,h_eta_j1_btag_tight_reco,h_eta_j2_btag_tight_reco,h_eta_j1_btag_medium_reco,h_eta_j2_btag_medium_reco])



    ##calo vs reco
    h_csv_j1_caloVSreco = rt.TH2F("h_csv_j1_caloVSreco","",csvRange[0],csvRange[1],csvRange[2],csvRange[0],csvRange[1],csvRange[2])
    h_csv_j2_caloVSreco = rt.TH2F("h_csv_j2_caloVSreco","",csvRange[0],csvRange[1],csvRange[2],csvRange[0],csvRange[1],csvRange[2])



    for h in allHistos:
        if 'mjj' in h.GetName():
            h.GetXaxis().SetTitle("Mjj [GeV]")
        elif 'pt' in h.GetName():
            h.GetXaxis().SetTitle("Pt [GeV]")
        elif 'eta' in h.GetName():
            h.GetXaxis().SetTitle("Eta")
        elif 'csv' in h.GetName():
            h.GetXaxis().SetTitle("CSV")

        






    #loop over entries
    for i in xrange(nEntries):
        if i%100000 == 0:
            print "analyzing event: ",i

        tchain.GetEntry(i)

        #implement analysis
        if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and
                tchain.pTWJ_j1>60                and
                tchain.pTWJ_j2>30                and
                tchain.PassJSON):
            continue



        caloJet1 = rt.TLorentzVector()
        caloJet2 = rt.TLorentzVector()
        caloJet1.SetPtEtaPhiM(tchain.pTWJ_j1,tchain.etaWJ_j1,tchain.phiWJ_j1,tchain.massWJ_j1)
        caloJet2.SetPtEtaPhiM(tchain.pTWJ_j2,tchain.etaWJ_j2,tchain.phiWJ_j2,tchain.massWJ_j2)
        caloJets = [caloJet1,caloJet2]
        caloCSV = [tchain.jetCSVAK4_j1,tchain.jetCSVAK4_j2]
        caloMjj = (caloJets[0]+caloJets[1]).M()

        recoJet1 = rt.TLorentzVector()
        recoJet2 = rt.TLorentzVector()
        recoJet1.SetPtEtaPhiM(tchain.pTWJ_recoj1,tchain.etaWJ_recoj1,tchain.phiWJ_recoj1,tchain.massWJ_recoj1)
        recoJet2.SetPtEtaPhiM(tchain.pTWJ_recoj2,tchain.etaWJ_recoj2,tchain.phiWJ_recoj2,tchain.massWJ_recoj2)
        recoJets = [recoJet1,recoJet2]
        recoCSV = [tchain.jetCSVAK4_recoj1,tchain.jetCSVAK4_recoj2]
        recoMjj = (recoJets[0]+recoJets[1]).M()

        #matching
        if caloJets[0].DeltaR(recoJets[0]) > caloJets[0].DeltaR(recoJets[1]):
            recoJets.reverse()
            recoCSV.reverse()
        
        #apply threshold on dR
        if caloJets[0].DeltaR(recoJets[0]) > dR or caloJets[1].DeltaR(recoJets[1]) > dR:
            continue;
            

        #fill histograms
        h_mjj_calo.Fill(caloMjj)
        h_mjj_reco.Fill(recoMjj)

        h_pt_j1_calo.Fill(caloJets[0].Pt())
        h_pt_j2_calo.Fill(caloJets[1].Pt())
        h_eta_j1_calo.Fill(caloJets[0].Eta())
        h_eta_j2_calo.Fill(caloJets[1].Eta())
    
        h_pt_j1_reco.Fill(recoJets[0].Pt())
        h_pt_j2_reco.Fill(recoJets[1].Pt())
        h_eta_j1_reco.Fill(recoJets[0].Eta())
        h_eta_j2_reco.Fill(recoJets[1].Eta())
    
        h_csv_j1_calo.Fill(caloCSV[0])
        h_csv_j2_calo.Fill(caloCSV[1])
        h_csv_j1_reco.Fill(recoCSV[0])
        h_csv_j2_reco.Fill(recoCSV[1])



        #correlation
        h_csv_j1_caloVSreco.Fill(recoCSV[0],caloCSV[0])
        h_csv_j2_caloVSreco.Fill(recoCSV[1],caloCSV[1])


        #calo j1
        n_jets_t_calo = 0
        n_jets_t_reco = 0
        n_jets_m_calo = 0
        n_jets_m_reco = 0

        if caloCSV[0] > tight:
            n_jets_t_calo+=1
            h_pt_j1_btag_tight_calo.Fill(caloJets[0].Pt())
            h_eta_j1_btag_tight_calo.Fill(caloJets[0].Eta())
        if caloCSV[0] > medium:
            n_jets_m_calo+=1
            h_pt_j1_btag_medium_calo.Fill(caloJets[0].Pt())
            h_eta_j1_btag_medium_calo.Fill(caloJets[0].Eta())
        #calo j2
        if caloCSV[1] > tight:
            n_jets_t_calo+=1
            h_pt_j2_btag_tight_calo.Fill(caloJets[1].Pt())
            h_eta_j2_btag_tight_calo.Fill(caloJets[1].Eta())
        if caloCSV[1] > medium:
            n_jets_m_calo+=1
            h_pt_j2_btag_medium_calo.Fill(caloJets[1].Pt())
            h_eta_j2_btag_medium_calo.Fill(caloJets[1].Eta())



        #reco j1
        if recoCSV[0] > tight:
            n_jets_t_reco+=1
            h_pt_j1_btag_tight_reco.Fill(recoJets[0].Pt())
            h_eta_j1_btag_tight_reco.Fill(recoJets[0].Eta())
        if recoCSV[0] > medium:
            n_jets_m_reco+=1
            h_pt_j1_btag_medium_reco.Fill(recoJets[0].Pt())
            h_eta_j1_btag_medium_reco.Fill(recoJets[0].Eta())
        #reco j2
        if recoCSV[1] > tight:
            n_jets_t_reco+=1
            h_pt_j2_btag_tight_reco.Fill(recoJets[1].Pt())
            h_eta_j2_btag_tight_reco.Fill(recoJets[1].Eta())
        if recoCSV[1] > medium:
            n_jets_m_reco+=1
            h_pt_j2_btag_medium_reco.Fill(recoJets[1].Pt())
            h_eta_j2_btag_medium_reco.Fill(recoJets[1].Eta())


            
        if n_jets_t_calo == 1:
            h_mjj_btag1_tight_calo.Fill(caloMjj)
        elif n_jets_t_calo == 2:
            h_mjj_btag2_tight_calo.Fill(caloMjj)
        else:
            h_mjj_btag0_tight_calo.Fill(caloMjj)

        if n_jets_t_reco == 1:
            h_mjj_btag1_tight_reco.Fill(recoMjj)
        elif n_jets_t_reco == 2:
            h_mjj_btag2_tight_reco.Fill(recoMjj)
        else:
            h_mjj_btag0_tight_reco.Fill(recoMjj)

        if n_jets_m_calo == 1:
            h_mjj_btag1_medium_calo.Fill(caloMjj)
        elif n_jets_m_calo == 2:
            h_mjj_btag2_medium_calo.Fill(caloMjj)
        else:
            h_mjj_btag0_medium_calo.Fill(caloMjj)

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

    h_csv_j1_caloVSreco.Write()
    h_csv_j2_caloVSreco.Write()

    h_csv_j1_calo.Write()
    h_csv_j2_calo.Write()
    h_csv_j1_reco.Write()
    h_csv_j2_reco.Write()

    #calo
    h_mjj_calo.Write()
    h_mjj_btag0_tight_calo.Write()
    h_mjj_btag1_tight_calo.Write()
    h_mjj_btag2_tight_calo.Write()
    h_mjj_btag0_medium_calo.Write()
    h_mjj_btag1_medium_calo.Write()
    h_mjj_btag2_medium_calo.Write()

    h_pt_j1_btag_tight_calo.Write()   
    h_pt_j2_btag_tight_calo.Write()   
    h_pt_j1_btag_medium_calo.Write()   
    h_pt_j2_btag_medium_calo.Write()   
    h_pt_j1_calo.Write()
    h_pt_j2_calo.Write()
    h_eta_j1_btag_tight_calo.Write()   
    h_eta_j2_btag_tight_calo.Write()   
    h_eta_j1_btag_medium_calo.Write()   
    h_eta_j2_btag_medium_calo.Write()   
    h_eta_j1_calo.Write()
    h_eta_j2_calo.Write()
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
    



    rootFile.Close()
