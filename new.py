from ROOT import *

fin = TFile('/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/Bstar2bq_1000/bstar1000_20181010_021447/rootfile_list_bstar1000_20181010_021447_0_reduced_skim.root')#.Get('rootTupleTree/tree')

a = TTreeReader('rootTupleTree/tree',fin)

#mjj = TTreeReaderValue(a,'mjj')
mjj = TTreeReaderValue(float)(a,'mjj')

for i in mjj:
  print i
#print mjj[1]
