from ROOT import * 
import sys, os
import array

def SumBins(plot,xlow,xhigh):
  total = 0
  for i in range(int(xlow),int(xhigh),1):
     total += plot.GetBinContent(i)
     #print plot.GetBinContent(i)
  return float(total)

csv_list =[0.8838]#  [0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8001,0.8838,0.9693]#[0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693] 

L = [1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332,2500,2700,3000,3300,3600,3900,4400,4800,5200,5600,6000,6500,7000,7500,8000]


F=TFile('/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/inputs/JetHT_run2017_red_cert_scan_all.root')

h_mjj={}
y={}
h_mjj['CSV']={}
h_mjj['DCSV']={}
y['CSV']={}
y['DCSV']={}
for i in ['0','le1','2','1']:
  h_mjj['CSV'][i]={}
  h_mjj['DCSV'][i]={}
  y['CSV'][i]={}
  y['DCSV'][i]={}
for j in csv_list:
      h_mjj['CSV']['0'][j]=F.Get('h_mass_passed_0b_CSVv2_'+str(j*1000))
      h_mjj['CSV']['le1'][j]=F.Get('h_mass_passed_le1b_CSVv2_'+str(j*1000))
      h_mjj['CSV']['1'][j]=F.Get('h_mass_passed_1b_CSVv2_'+str(j*1000))
      h_mjj['CSV']['2'][j]=F.Get('h_mass_passed_2b_CSVv2_'+str(j*1000))
      h_mjj['DCSV']['0'][j]=F.Get('h_mass_passed_0b_DeepCSV_'+str(j*1000))
      h_mjj['DCSV']['le1'][j]=F.Get('h_mass_passed_le1b_DeepCSV_'+str(j*1000))
      h_mjj['DCSV']['1'][j]=F.Get('h_mass_passed_1b_DeepCSV_'+str(j*1000))
      h_mjj['DCSV']['2'][j]=F.Get('h_mass_passed_2b_DeepCSV_'+str(j*1000))
      print h_mjj['DCSV']['2'][j]
      print h_mjj['DCSV']['le1'][j]
      print h_mjj['CSV']['1'][j]
      for i in ['0','le1','2','1']:
        for k in ['CSV','DCSV']:
          y[k][i][j]=[]

All = F.Get('total')

HighestPoint = {}
for i in csv_list:
  HighestPoint[i] = {}
  for j in ['CSV','DCSV']:
    HighestPoint[i][j]=0
x=[]
for i in range(len(L)-1):
  x.append((L[i]+L[i+1])/2)
  for j in ['CSV','DCSV']:
    for k in ['0','le1','2','1']:
      for m in csv_list:
        if SumBins(All,L[i],L[i+1])==0:
	  y[j][k][m].append(0)
	  continue
  	y[j][k][m].append(SumBins(h_mjj[j][k][m],L[i],L[i+1])/SumBins(All,L[i],L[i+1]))

	if not k=='0':
	  if SumBins(h_mjj[j][k][m],L[i],L[i+1])/SumBins(All,L[i],L[i+1]) > HighestPoint[m][j]:
	    HighestPoint[m][j] = SumBins(h_mjj[j][k][m],L[i],L[i+1])/SumBins(All,L[i],L[i+1])

x_a=array.array('d',x)
y_a={}
gr={}
for i in ['CSV','DCSV']:
  y_a[i]={}
  gr[i]={}
  for j in ['0','le1','2','1']:
    y_a[i][j]={}
    gr[i][j]={}
    for k in csv_list:
      y_a[i][j][k] = array.array('d',y[i][j][k])
      gr[i][j][k] = TGraph(len(x_a),x_a,y_a[i][j][k])

for i in ['CSV','DCSV']:
  for k in csv_list:
    gr[i]['0'][k].SetLineColor(kBlack)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['1'][k].SetLineColor(kRed)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['le1'][k].SetLineColor(kGreen)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['2'][k].SetLineColor(kBlue)
    gr[i]['0'][k].SetLineWidth(2)
    c1 = TCanvas()
    gr[i]['le1'][k].Draw("APL")
    gr[i]['le1'][k].SetTitle('')
    gr[i]['le1'][k].GetXaxis().SetTitle('Resonance Mass(GeV)')
    gr[i]['le1'][k].GetYaxis().SetTitle('Tagging Efficiency')
 
    gr[i]['le1'][k].GetYaxis().SetRangeUser(0,1.05*HighestPoint[k][i])
    
    gr[i]['1'][k].Draw("PL,sames")
    gr[i]['2'][k].Draw("PL,sames")

    leg = TLegend(0.80, 0.75, 0.96, 0.89)
    leg.AddEntry(gr[i]['1'][k],"1-tag","L")
    leg.AddEntry(gr[i]['2'][k],"2-tag","L")
    leg.AddEntry(gr[i]['le1'][k],"ge1-tag","L")
    leg.Draw("same")

    c1.Print(i+'TagRate'+str(int(float(k)*1000))+".pdf")

Fout = TFile("Data_Rate.root","recreate")

for i in ['CSV','DCSV']:
  for k in csv_list:
    gr[i]['0'][k].Write(i+'0b_TagRate_'+str(int(float(k)*10000)))
    gr[i]['1'][k].Write(i+'1b_TagRate_'+str(int(float(k)*10000)))
    gr[i]['le1'][k].Write(i+'le1b_TagRate_'+str(int(float(k)*10000)))
    gr[i]['2'][k].Write(i+'2b_TagRate_'+str(int(float(k)*10000)))

Fout.Close()

