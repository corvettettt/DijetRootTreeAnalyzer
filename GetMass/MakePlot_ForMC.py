import ROOT as rt
from rootTools import tdrstyle as setTDRStyle
rt.gROOT.SetBatch()
setTDRStyle.setTDRStyle()

from ROOT import * 
import sys, os
import array
from optparse import OptionParser

def SumBins(plot,xlow,xhigh):
  total = 0
  for i in range(int(xlow),int(xhigh),1):
     total += plot.GetBinContent(i)
     #print plot.GetBinContent(i)
  return float(total)

csv_list = [0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.9,0.9693]

#L = [1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332,2500,2700,3000,3300,3600,3900,4400,4800,5200,5600,6000,6500,7000,7500,8000]
L = [1530, 1730, 1930,2130, 2300,2500,2700,3000,3300,3600,3900,4400,4800,5200,5600,6000,7000]

parser = OptionParser()
parser.add_option('-i','--Input',dest="Input",type="string",default="none",help="Name of the signal flavour")
parser.add_option('-o','--Output',dest="Output",type="string",default="non",help="Name of the signal model")
(options,args) = parser.parse_args()
Input = options.Input
Output  = options.Output
F = TFile(Input)

h_mjj={}
y={}
h_mjj['CSV']={}
h_mjj['DCSV']={}
h_mjj['DeepJet'] = {}
y['CSV']={}
y['DCSV']={}
y['DeepJet'] = {}
for i in ['0','le1','2','1']:
  h_mjj['CSV'][i]={}
  h_mjj['DCSV'][i]={}
  h_mjj['DeepJet'][i]={}
  y['CSV'][i]={}
  y['DCSV'][i]={}
  y['DeepJet'][i] = {}

h_mjj['CSV']['mt'] = F.Get('h_mass_passed_mt_CSVv2')
h_mjj['DeepJet']['mt'] =F.Get('h_mass_passed_mt_DeepJet')
h_mjj['DCSV']['mt'] =F.Get('h_mass_passed_mt_DeepCSV')
y['CSV']['mt'] = []
y['DeepJet']['mt'] = []
y['DCSV']['mt'] =[]



for j in csv_list:
      h_mjj['CSV']['0'][j]=F.Get('h_mass_passed_0b_CSVv2_'+str(j*1000))
      h_mjj['CSV']['le1'][j]=F.Get('h_mass_passed_le1b_CSVv2_'+str(j*1000))
      h_mjj['CSV']['1'][j]=F.Get('h_mass_passed_1b_CSVv2_'+str(j*1000))
      h_mjj['CSV']['2'][j]=F.Get('h_mass_passed_2b_CSVv2_'+str(j*1000))

      h_mjj['DCSV']['0'][j]=F.Get('h_mass_passed_0b_DeepCSV_'+str(j*1000))
      h_mjj['DCSV']['le1'][j]=F.Get('h_mass_passed_le1b_DeepCSV_'+str(j*1000))
      h_mjj['DCSV']['1'][j]=F.Get('h_mass_passed_1b_DeepCSV_'+str(j*1000))
      h_mjj['DCSV']['2'][j]=F.Get('h_mass_passed_2b_DeepCSV_'+str(j*1000))

      
      h_mjj['DeepJet']['0'][j]=F.Get('h_mass_passed_0b_DeepJet_'+str(j*1000))
      h_mjj['DeepJet']['le1'][j]=F.Get('h_mass_passed_le1b_DeepJet_'+str(j*1000))
      h_mjj['DeepJet']['1'][j]=F.Get('h_mass_passed_1b_DeepJet_'+str(j*1000))
      h_mjj['DeepJet']['2'][j]=F.Get('h_mass_passed_2b_DeepJet_'+str(j*1000))


      for i in ['0','le1','2','1']:
        for k in ['CSV','DCSV','DeepJet']:
          y[k][i][j]=[]

All = F.Get('total')

HighestPoint = {}
for i in csv_list:
  HighestPoint[i] = {}
  for j in ['CSV','DCSV','DeepJet']:
    HighestPoint[i][j]=0
x=[]

for i in range(len(L)-1):
  x.append((L[i]+L[i+1])/2)
  for j in ['CSV','DCSV','DeepJet']:
    for k in ['0','le1','2','1']:
      for m in csv_list:
        if SumBins(All,L[i],L[i+1])==0:
	  y[j][k][m].append(0)
	  continue
  	y[j][k][m].append(SumBins(h_mjj[j][k][m],L[i],L[i+1])/SumBins(All,L[i],L[i+1]))

	if not k=='0':
	  if SumBins(h_mjj[j][k][m],L[i],L[i+1])/SumBins(All,L[i],L[i+1]) > HighestPoint[m][j]:
	    HighestPoint[m][j] = SumBins(h_mjj[j][k][m],L[i],L[i+1])/SumBins(All,L[i],L[i+1])


for i in range(len(L)-1):
  for j in ['CSV','DCSV','DeepJet']:
    k = 'mt'
    if SumBins(All,L[i],L[i+1])==0:
      y[j][k].append(0)
      continue
    y[j][k].append(SumBins(h_mjj[j][k],L[i],L[i+1])/SumBins(All,L[i],L[i+1]))

x_a=array.array('d',x)
print x_a
y_a={}
gr={}
for i in ['CSV','DCSV','DeepJet']:
  y_a[i]={}
  gr[i]={}
  y_a[i]['mt'] = array.array('d',y[i]['mt'])
  gr[i]['mt']  = TGraph(len(x_a),x_a,y_a[i]['mt'])
  for j in ['0','le1','2','1']:
    y_a[i][j]={}
    gr[i][j]={}
    for k in csv_list:
      y_a[i][j][k] = array.array('d',y[i][j][k])
      gr[i][j][k] = TGraph(len(x_a),x_a,y_a[i][j][k])

for i in ['CSV','DCSV','DeepJet']:
  for k in csv_list:
    gr[i]['0'][k].SetLineColor(kBlack)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['1'][k].SetLineColor(kRed)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['le1'][k].SetLineColor(kGreen)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['2'][k].SetLineColor(kBlue)
    gr[i]['0'][k].SetLineWidth(2)
    gr[i]['mt'].SetLineColor(kOrange)
    gr[i]['mt'].SetLineWidth(2)

    c1 = TCanvas()
    gr[i]['le1'][k].Draw("APL")
    gr[i]['le1'][k].SetTitle('')
    gr[i]['le1'][k].GetXaxis().SetTitle('Resonance Mass(GeV)')
    gr[i]['le1'][k].GetYaxis().SetTitle('MisIdentify Rate')
 
    gr[i]['le1'][k].GetYaxis().SetRangeUser(0,1.05*HighestPoint[k][i])
    gr[i]['mt'].Draw('PL,sames')
    gr[i]['1'][k].Draw("PL,sames")
    gr[i]['2'][k].Draw("PL,sames")

    leg = TLegend(0.80, 0.75, 0.96, 0.89)
    leg.AddEntry(gr[i]['1'][k],"1-tag","L")
    leg.AddEntry(gr[i]['2'][k],"2-tag","L")
    leg.AddEntry(gr[i]['le1'][k],"ge1-tag","L")
    leg.AddEntry(gr[i]['mt'],'mt-tag','L')
    leg.Draw("same")

    c1.Print(Output+'/'+i+'TagRate'+str(int(float(k)*1000))+".pdf")

Fout = TFile(Output+'/TaggingRate.root',"recreate")

for i in ['CSV','DCSV','DeepJet']:
  gr[i]['mt'].Write(i+'mt_TagRate')
  for k in csv_list:
    gr[i]['0'][k].Write(i+'0b_TagRate_'+str(int(float(k)*10000)))
    gr[i]['1'][k].Write(i+'1b_TagRate_'+str(int(float(k)*10000)))
    gr[i]['le1'][k].Write(i+'le1b_TagRate_'+str(int(float(k)*10000)))
    gr[i]['2'][k].Write(i+'2b_TagRate_'+str(int(float(k)*10000)))
Fout.Close()

