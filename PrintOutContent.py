from ROOT import *
import sys

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



sampleNames_qg = {
500 :'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_0000GeV_reduced_skim.root',
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_1000GeV_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_2000GeV_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_3000GeV_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_4000GeV_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_5000GeV_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_6000GeV_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_7000GeV_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_8000GeV_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2qg_Dec_central/bstar2qg_9000GeV_reduced_skim.root',
                  }

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleNames_qq = {
1000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_1000GeV_reduced_skim.root',
2000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_2000GeV_reduced_skim.root',
3000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_3000GeV_reduced_skim.root',
4000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_4000GeV_reduced_skim.root',
5000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_5000GeV_reduced_skim.root',
6000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_6000GeV_reduced_skim.root',
7000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_7000GeV_reduced_skim.root',
8000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_8000GeV_reduced_skim.root',
9000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Dec_central/RSGraviton2qq_9000GeV_reduced_skim.root',

                  }

QCD = {
'200-300':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD200to300_reduced_skim.root',
'300-500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD300to500_reduced_skim.root',
'500-700':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD500to700_reduced_skim.root',
'700-1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD700to1000_reduced_skim.root',
'1000-1500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD1000to1500_reduced_skim.root',
'1500-2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD1500to2000_reduced_skim.root',
'2000-Inf':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD2000toInf_reduced_skim.root',

}
treeName = "rootTupleTree/tree"
sample = QCD

tchain = TChain(treeName)
for i,j in sample.items():
  tchain.Add(j)
nEntries = tchain.GetEntries()

type = {}

for i in progressbar(range(nEntries),'Mass'+": ", 40):
#for i in range(20000):
   this = []

   tchain.GetEntry(i)
  
   this.append(int(abs(tchain.jetpflavour_j1)))
   this.append(int(abs(tchain.jetpflavour_j2)))

   this.sort()

   if str(this) in type.keys():
     type[str(this)] +=1
   else:
     type[str(this)] =1

#if sample == sampleNames_qq:
#  print '[5,5]',type('[5,5]'),float(type('[5,5]'))/float(nEntries)
#else :
#  print '[5,21]',type('[5,21]'),float(type('[5,21]'))//float(nEntries)

print 'final state\tnumber\tPercerntage'
for i,j in type.items():
   print str(i)+'\t\t'+str(j)+'\t'+str(100*float(j)/float(nEntries))+'%'
