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


SampleName = {}
SampleName['bstar'] = {
'0500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ500GeV_reduced_skim.root',
'1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ1000GeV_reduced_skim.root',
'2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ2000GeV_reduced_skim.root',
'3000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ3000GeV_reduced_skim.root',
'4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ4000GeV_reduced_skim.root',
'5000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ5000GeV_reduced_skim.root',
'6000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ6000GeV_reduced_skim.root',
'7000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ7000GeV_reduced_skim.root',
'8000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ8000GeV_reduced_skim.root',
'9000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jet_central/bstar2JJ9000GeV_reduced_skim.root',
}

SampleName['R2qq'] = {
'0500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_500GeV_reduced_skim.root',
'1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_1000GeV_reduced_skim.root',
'2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_2000GeV_reduced_skim.root',
'3000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_3000GeV_reduced_skim.root',
'4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_4000GeV_reduced_skim.root',
'5000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_5000GeV_reduced_skim.root',
'6000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_6000GeV_reduced_skim.root',
'7000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_7000GeV_reduced_skim.root',
'8000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2QQ_Jet_central/R2QQ_8000GeV_reduced_skim.root',
}



SampleName['R2bb'] = {
'0500' : '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_500GeV_reduced_skim.root',
'1000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_1000GeV_reduced_skim.root',
'2000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_2000GeV_reduced_skim.root',
'3000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_3000GeV_reduced_skim.root',
'4000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_4000GeV_reduced_skim.root',
'5000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_5000GeV_reduced_skim.root',
'6000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_6000GeV_reduced_skim.root',
'7000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_7000GeV_reduced_skim.root',
'8000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_8000GeV_reduced_skim.root',
'9000': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_9000GeV_reduced_skim.root',


}

SampleName['bstar0p1'] = {
500: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/500GeV_reduced_skim.root',
1000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/1000GeV_reduced_skim.root',
2000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/2000GeV_reduced_skim.root',
3000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/3000GeV_reduced_skim.root',
4000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/4000GeV_reduced_skim.root',
5000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/5000GeV_reduced_skim.root',
6000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/6000GeV_reduced_skim.root',
7000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/7000GeV_reduced_skim.root',
8000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/8000GeV_reduced_skim.root',
9000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/9000GeV_reduced_skim.root',

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
sample = SampleName['bstar0p1']
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
