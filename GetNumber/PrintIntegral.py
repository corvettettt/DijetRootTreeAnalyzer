from ROOT import *

f1 = TFile('Mine/all.root')
f2 = TFile('GetMassMagda/all.root')

gr1 =  f1.Get('Mjj_1530')
gr2 = f2.Get('Mjj_1530')

print gr1.Integral()
print gr2.Integral()
