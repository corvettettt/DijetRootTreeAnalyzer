from optparse import OptionParser
import ROOT as rt
import rootTools
from framework import Config
from array import *
import os
import sys

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-o','--output',dest="output",default="./",type="string",
                  help="Output ROOT file to store output histograms")
    parser.add_option('-l','--list',dest="list", default="lists/testlist.txt",type="string",
                  help="test list")
    parser.add_option('--no-corr',dest="noCorr",default=False,action='store_true',
                  help="no bias correction")

    (options,args) = parser.parse_args()
    corr = ''
    if options.noCorr:
        corr = '_noCorr'

    tchain = rt.TChain('rootTupleTree/tree')
    tchain.SetBranchStatus('*',0)
    tchain.SetBranchStatus('mjj%s'%corr,1)
    tchain.SetBranchStatus('passHLT_CaloScoutingHT250',1)
    tchain.SetBranchStatus('event',1)
    tchain.SetBranchStatus('lumi',1)
    tchain.SetBranchStatus('run',1)
    tchain.SetBranchStatus('PassJSON',1)
    tchain.SetBranchStatus('deltaETAjj',1)
    tchain.SetBranchStatus('deltaPHIjj',1)
    tchain.SetBranchStatus('phiWJ_j1',1)
    tchain.SetBranchStatus('phiWJ_j2',1)
    tchain.SetBranchStatus('etaWJ_j1',1)
    tchain.SetBranchStatus('etaWJ_j2',1)
    tchain.SetBranchStatus('pTWJ_j1%s'%corr,1)
    tchain.SetBranchStatus('pTWJ_j2%s'%corr,1)
    
    h_mjj_1GeVbin = rt.TH1D('h_mjj_HLTpass_HT250_1GeVbin','h_mjj_HLTpass_HT250_1GeVbin',14000,0,14000)
    h_deltaETAjj = rt.TH1D('h_deltaETAjj_HLTpass_HT250','h_deltaETAjj_HLTpass_HT250',1000,0,5)
    h_deltaPHIjj = rt.TH1D('h_deltaPHIjj_HLTpass_HT250','h_deltaPHIjj_HLTpass_HT250',1000,0,4)
    h_etaWJ_j1 = rt.TH1D('h_etaWJ_j1_HLTpass_HT250','h_etaWJ_j1_HLTpass_HT250',1000,-5,5)
    h_etaWJ_j2 = rt.TH1D('h_etaWJ_j2_HLTpass_HT250','h_etaWJ_j2_HLTpass_HT250',1000,-5,5)
    h_phiWJ_j1 = rt.TH1D('h_phiWJ_j1_HLTpass_HT250','h_phiWJ_j1_HLTpass_HT250',1000,-4,4)
    h_phiWJ_j2 = rt.TH1D('h_phiWJ_j2_HLTpass_HT250','h_phiWJ_j2_HLTpass_HT250',1000,-4,4)
    h_pTWJ_j1 = rt.TH1D('h_pTWJ_j1_HLTpass_HT250','h_pTWJ_j1_HLTpass_HT250',10000,0,10000)
    h_pTWJ_j2 = rt.TH1D('h_pTWJ_j2_HLTpass_HT250','h_pTWJ_j2_HLTpass_HT250',10000,0,10000)    
    
    cut = 'passHLT_CaloScoutingHT250&&abs(deltaETAjj)<1.3&&abs(etaWJ_j1)<2.5&&abs(etaWJ_j2)<2.5&&pTWJ_j1%s>60&&pTWJ_j2%s>30&&PassJSON'%(corr,corr)
    
    histoExpr = { h_mjj_1GeVbin: 'mjj%s'%corr, 
                  h_deltaETAjj: 'deltaETAjj',
                  h_deltaPHIjj: 'deltaPHIjj',
                  h_etaWJ_j1: 'etaWJ_j1',
                  h_etaWJ_j2: 'etaWJ_j2',
                  h_phiWJ_j1: 'phiWJ_j1',
                  h_phiWJ_j2: 'phiWJ_j2',
                  h_pTWJ_j1: 'pTWJ_j1%s'%corr,
                  h_pTWJ_j2: 'pTWJ_j2%s'%corr
                }
    
    f = open(options.list)
    for i, line in enumerate(f):
        print line.replace('\n','')
        tchain.Add(line.replace('\n',''))

    def project(tree, h, var, cut):
        print 'projecting var: %s, cut: %s from tree: %s into hist: %s'%(var, cut, tree.GetName(), h.GetName())
        tree.Project(h.GetName(),var,cut)

    for hist,var in histoExpr.iteritems():
        if var!='mjj%s'%corr: continue
        project(tchain, hist, var, cut)
    
    #tchain.Draw('>>elist',cut+"&&mjj>1000",'entrylist')
        
    #elist = rt.gDirectory.Get('elist')    
    #entry = -1
    #print "run lumi event mjj pT1 pT2 file" 
    #while True:
    #    entry = elist.Next()
    #    if entry == -1: break
    #    tchain.GetEntry(entry)
    #    curFile = tchain.GetCurrentFile()
    #    print tchain.run, tchain.lumi, tchain.event, tchain.mjj, tchain.pTWJ_j1, tchain.pTWJ_j2, curFile.GetName()

    output = rt.TFile(options.output,'recreate')
    output.cd()
    for h in histoExpr:
        h.Write()
    output.Close()
