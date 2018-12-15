from optparse import OptionParser
from framework import Config
import ROOT as rt
import sys




usage = """usage: python python/bTag_analysis.py -c config/bTag_analysis.cfg -b BTag2016"""


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

    loose = cfg.getVariables(box,"loose")
    medium = cfg.getVariables(box,"medium")

    ###################################################################

    print treeName
    tchain = rt.TChain(treeName)
    for i, line in enumerate(inputData):
        tchain.Add(line)


    nEntries = tchain.GetEntries()
    print 'Number of entries: ', nEntries

    # Book histos
    histo_mjj = rt.TH1F("mjj","",10000,0,10000)
    histo_mjj_btag0_loose = rt.TH1F("mjj_btag0_loose","",10000,0,10000)
    histo_mjj_btag1_loose = rt.TH1F("mjj_btag1_loose","",10000,0,10000)
    histo_mjj_btag2_loose = rt.TH1F("mjj_btag2_loose","",10000,0,10000)
    histo_mjj_btag0_medium = rt.TH1F("mjj_btag0_medium","",10000,0,10000)
    histo_mjj_btag1_medium = rt.TH1F("mjj_btag1_medium","",10000,0,10000)
    histo_mjj_btag2_medium = rt.TH1F("mjj_btag2_medium","",10000,0,10000)
    

    #loop over entries
    for i in xrange(nEntries):
        if i%100000 == 0:
            print "analyzing event: ",i

        tchain.GetEntry(i)

        #implement analysis
#        if not (tchain.passHLT_CaloScoutingHT250 and
        if not (tchain.passHLT_PFHT800           and
                abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and
                tchain.pTWJ_j1>60                and
                tchain.pTWJ_j2>30                and
                tchain.PassJSON):
            continue


        #fill histograms
        histo_mjj.Fill(tchain.mjj)
    

        njetsl=0
        njetsm=0 
    
        if tchain.jetCSVAK4_j1 > loose:
            njetsl+=1
        if tchain.jetCSVAK4_j2 > loose:
            njetsl+=1
                
        if tchain.jetCSVAK4_j1 > medium:
            njetsm+=1
        if tchain.jetCSVAK4_j2 > medium:
            njetsm+=1
            
            
        if njetsl == 1:
            histo_mjj_btag1_loose.Fill(tchain.mjj)
        elif njetsl == 2:
            histo_mjj_btag2_loose.Fill(tchain.mjj)
        else:
            histo_mjj_btag0_loose.Fill(tchain.mjj)

        if njetsm == 1:
            histo_mjj_btag1_medium.Fill(tchain.mjj)
        elif njetsm == 2:
            histo_mjj_btag2_medium.Fill(tchain.mjj)
        else:
            histo_mjj_btag0_medium.Fill(tchain.mjj)
 
    #end loop


    rt.gROOT.SetBatch(rt.kTRUE)

    #Create ROOT file
    rootFile = rt.TFile(outFile, 'recreate')
    histo_mjj.GetXaxis().SetTitle('mjj [GeV]')
    histo_mjj.Write()
    histo_mjj_btag0_loose.Write()
    histo_mjj_btag1_loose.Write()
    histo_mjj_btag2_loose.Write() 
    histo_mjj_btag0_medium.Write() 
    histo_mjj_btag1_medium.Write() 
    histo_mjj_btag2_medium.Write()
    
    
    
    rootFile.Close()
