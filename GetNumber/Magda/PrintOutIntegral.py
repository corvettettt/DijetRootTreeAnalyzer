from ROOT import *
fin1 = TFile('all.root')
fin2 = TFile('/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetNumber/Mine/all.root')

h1 = fin1.Get('Mjj_1530')
h2 = fin2.Get('Mjj_1530')

print h1.Integral()
print h2.Integral()
