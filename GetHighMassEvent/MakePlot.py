from ROOT import *
import array
csv_list =  [0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8001,0.8838,0.9693]#[0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693] 

L = [1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152]

F=TFile('/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/inputs/JetHT_run2017_red_cert_scan.root')

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
      for i in ['0','le1','2','1']:
        for k in ['CSV','DCSV']:
          y[k][i][j]=[]

All = F.Get('total')

x=[]
for i in range(len(L)-1):
  x.append((L[i]+L[i+1])/2)
  for j in ['CSV','DCSV']:
    for k in ['0','le1','2','1']:
      for m in csv_list:
        if All.GetBinContent(i)==0:
	  y[j][k][m].append(0)
	  continue
  	y[j][k][m].append(h_mjj[j][k][m].GetBinContent(i)/All.GetBinContent(i))

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
    gr[i]['0'][k].Draw("APL")
    gr[i]['0'][k].GetYaxis().SetRangeUser(0,1)
    gr[i]['le1'][k].Draw("PL,sames")
    gr[i]['1'][k].Draw("PL,sames")
    gr[i]['2'][k].Draw("PL,sames")

    leg = TLegend(0.87, 0.80, 0.96, 0.89)
    leg.AddEntry(gr[i]['0'][k],'0-tag',"L")
    leg.AddEntry(gr[i]['1'][k],"1-tag","L")
    leg.AddEntry(gr[i]['2'][k],"2-tag","L")
    leg.AddEntry(gr[i]['le1'][k],"le1-tag","L")
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

