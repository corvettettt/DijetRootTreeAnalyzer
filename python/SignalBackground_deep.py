from ROOT import *
import math
from array import array

BG = '/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/inputs/Data_Rate_2017.root'
B = TFile(BG)

csv_list = [0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693] 
csv_list = [0.1522, 0.3,0.4941, 0.5803, 0.8, 0.8838]
L = [1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332,2500,2700,3000,3300,3600,3900,4400,4800,5200,5600,6000,7000,8000,9000]

gr={}
gr['0']={}
gr['1']={}
gr['le1']={}
gr['2']={}
for i in csv_list:
  gr['0'][i]={}
  gr['1'][i]={}
  gr['le1'][i]={}
  gr['2'][i]={}

for i in csv_list:
  Signal = 'signalHistos_bg_'+str(int(i*1000))+'.root' 
  S = TFile(Signal)

  rate_0 = S.Get('g_0btag_rate') 
  rate_le1 = S.Get('g_le1btag_rate')
  rate_1 = S.Get('g_1btag_rate')
  rate_2 = S.Get('g_2btag_rate')

  data_rate_0 = B.Get('DCSV0b_TagRate_'+str(int(float(i)*10000))) 
  data_rate_1 = B.Get('DCSV1b_TagRate_'+str(int(float(i)*10000)))
  data_rate_le1 = B.Get('DCSVle1b_TagRate_'+str(int(float(i)*10000)))
  data_rate_2 = B.Get('DCSV2b_TagRate_'+str(int(float(i)*10000)))

  x = []
  y_0 = []
  y_1 = []
  y_le1 = []
  y_2 = []

  for l in range(len(L)-1):
     mass = (L[l]+L[l+1])/2
     x.append((L[l]+L[l+1])/2)
     if data_rate_0.Eval(mass)==0:
       y_0.append(0)
     else:
       y_0.append(rate_0.Eval(mass)/math.sqrt(data_rate_0.Eval(mass)))

     if data_rate_1.Eval(mass)==0:
       y_1.append(0)
     else:
       y_1.append(rate_le1.Eval(mass)/math.sqrt(data_rate_1.Eval(mass)))

     if data_rate_le1.Eval(mass)==0:
       y_le1.append(0)
     else:
       y_le1.append(rate_1.Eval(mass)/math.sqrt(data_rate_le1.Eval(mass)))

     if 3200<mass<3400 :
       print mass,'   ', data_rate_le1.Eval(mass),'   ',rate_le1.Eval(mass)

     if data_rate_2.Eval(mass)==0:
       y_2.append(0)
     else:
       y_2.append(rate_2.Eval(mass)/math.sqrt(data_rate_2.Eval(mass)))


  gr['0'][i] = TGraph(len(x),array('d',x),array('d',y_0))
  gr['0'][i].SetLineColor(kBlack)
  gr['0'][i].SetLineWidth(2) 
  gr['1'][i] = TGraph(len(x),array('d',x),array('d',y_1))
  gr['1'][i].SetLineColor(kRed)
  gr['1'][i].SetLineWidth(2) 
  gr['le1'][i] = TGraph(len(x),array('d',x),array('d',y_le1))
  gr['le1'][i].SetLineColor(kGreen)
  gr['le1'][i].SetLineWidth(2) 
  gr['2'][i] = TGraph(len(x),array('d',x),array('d',y_2))
  gr['2'][i].SetLineColor(kBlue)
  gr['2'][i].SetLineWidth(2)  
 
  c1 = TCanvas()

  leg = TLegend(0.77, 0.70, 0.96, 0.89)
  leg.AddEntry(gr['0'][i],'0-tag','L')
  leg.AddEntry(gr['le1'][i],'le1-tag','L')
  leg.AddEntry(gr['1'][i],'1-tag','L')
  leg.AddEntry(gr['2'][i],'2-tag','L')

  gr['0'][i].Draw('APL')
  gr['0'][i].GetYaxis().SetRangeUser(0,4)
  gr['le1'][i].Draw("PL,sames")
  gr['1'][i].Draw("PL,sames")
  gr['2'][i].Draw("PL,sames")
  leg.Draw('same')

  c1.Print('RateOf'+str(int(i*1000))+'.pdf')

  c1.Close()
  S.Close()

for i in ['0','1','le1','2']:
  c1 = TCanvas()
  leg = TLegend(0.77, 0.50, 0.96, 0.89)
  index=0
  for j in csv_list:
     index +=1
     gr[i][j].SetLineColor(index)
     if index == 1:
       gr[i][j].Draw()
       gr[i][j].GetYaxis().SetRangeUser(0,4)
     else : 
       gr[i][j].Draw('PL,sames')
     leg.AddEntry(gr[i][j],'TagOf'+str(int(j*1000)),'L')
  leg.Draw('same')
  c1.Print('RateOf'+i+'bCategory.pdf')
  c1 = 0

