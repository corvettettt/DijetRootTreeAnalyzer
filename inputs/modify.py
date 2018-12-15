from ROOT import *

def ModifyHisto(histo):
  Nbin = histo.GetNbinsX()
  NewHisto = TH1D('','',10000,0,10000)
  for i in range(Nbin):
    if i <1530:
       NewHisto.SetBinContent(i,0)
    else:
       NewHisto.SetBinContent(i,histo.GetBinContent(i))  
  return NewHisto

Fin = TFile('JetHT_run2017_red_cert_scan_all.root')

Fout = TFile('New.root','recreate')

for i in Fin.GetListOfKeys():
  histo = Fin.Get(i.GetName())
  NewHisto = ModifyHisto(histo)
  NewHisto.Write(i.GetName())

Fin.Close()
Fout.Close()
