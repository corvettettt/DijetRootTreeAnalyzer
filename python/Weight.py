from optparse import OptionParser
from ROOT import *
import sys

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

if __name__=='__main__':
    #parser = OptionParser(usage=usage)
    #parser.add_option('-m','--model',dest="model",type="string",default="qq",
    #                  help="Name of the signal model")
    #(options,args) = parser.parse_args()
    #model   = options.model

    PASS = {}
    efficiency = {}
    for i in ['DeepCSV','CSV']:
      for j in ['M','T','L']:
        efficiency['tagged_%s_%s'%(i,j)] = TH2D('bTaggingEfficiency_%s_%s'%(i,j),'bTaggingEfficiency_%s_%s'%(i,j),100,0,7000,100,-3.14159,3.14159)
	PASS['tagged_%s_%s'%(i,j)] = TH2D('Passed_%s_%s'%(i,j),'Passed_%s_%s'%(i,j),100,0,7000,100,-3.14159,3.14159)

    #efficiency['untagged']=TH2D('','',100,0,9000,100,-3.14159,3.14159)
    ALL = TH2D('all','all',100,0,7000,100,-3.14159,3.14159)
    #efficiency['all']=TH2D('all','all',100,0,9000,100,-3.14159,3.14159)
 
    tchain = TChain('rootTupleTree/tree')
    for i,j in sampleName['qq'].items():
      tchain.Add(j)
    for i,j in sampleName['qg'].items():
      tchain.Add(j)
    for i in progressbar(range(tchain.GetEntries()), prefix="", size=60):
      tchain.GetEntry(i)
 
      for m in ['j1','j2']:
	if getattr(tchain,'jetpflavour_%s'%m) == 4 or getattr(tchain,'jetpflavour_%s'%m) == 5 :
	   continue
	ALL.Fill(getattr(tchain,'pTWJ_%s'%m),getattr(tchain,'etaAK4_%s'%m))
        for j in ['DeepCSV','CSV']:
          for k in ['M','T','L']:
            if getattr(tchain,'jet%sAK4_%s'%(j,m))>CSV_Value[j][k]:
	      PASS['tagged_%s_%s'%(j,k)].Fill(getattr(tchain,'pTWJ_%s'%m),getattr(tchain,'etaAK4_%s'%m))

    for i in ['DeepCSV','CSV']:
      for j in ['M','T','L']: 
	for m in range(100): 
	  for n in range(100):
             a = PASS['tagged_%s_%s'%(i,j)].GetBinContent(m,n)
             b = ALL.GetBinContent(m,n)
	     if b == 0 :
	       eff = 0
	     else:
	       eff = float(a)/float(b)
       	     efficiency['tagged_%s_%s'%(i,j)].SetBinContent(m,n,eff) 
    
    Fout = TFile('Efficiency_UDSG.root','recreate')
    for j in ['DeepCSV','CSV']:
      for k in ['M','T','L']:
	PASS['tagged_%s_%s'%(j,k)].Write()
        efficiency['tagged_%s_%s'%(j,k)].Write()
    ALL.Write()
    Fout.Close()
