import ROOT as rt
from rootTools import tdrstyle as setTDRStyle
rt.gROOT.SetBatch()
setTDRStyle.setTDRStyle()
import math


from ROOT import *
import os,sys
import collections

SampleName={}

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

WorkingPoint = {}
WorkingPoint['CSVv2']={
'L':0.5803,
'M':0.8838,
'T':0.9693,
'tag' : 'jetCSVAK4_',
}
WorkingPoint['DeepCSV'] = {
'L':0.1522,
'M':0.4941,
'T':0.8001,
'tag' : 'jetDeepCSVAK4_',
}
WorkingPoint['DeepJet'] = {
'L':0.0521,
'M':0.3033,
'T':0.7489,
'tag' : 'jetDeepJetAK4_',
}

CSV_Value ={}

CSV_Value['CSVv2'] =   [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.5803,0.65,0.7,0.75,0.8,0.8838,0.9693]
CSV_Value['DeepCSV'] = [0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.55,0.6,0.65,0.7,0.75,0.8001,0.85,0.9]
CSV_Value['DeepJet'] = [0.0521,0.1,0.15,0.2,0.25,0.3033,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.7489,0.8,0.85,0.9]

Pt_Range = [30.0,200.0,400.0,600.0,800.0,1000.0,1400.0,1800.0,2200.0,2600.0,3000.0,3500.0,4000.0,5000.0]

def WriteEverything(dic,name = ''):
  for key,value in dic.items():
    if isinstance(value,dict):
      WriteEverything(value,name+'_'+str(key))
    else :
      value.Write(name+'_'+str(key))
  return

Fin = TFile('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/NewDeep_ROC_Efficiency.root')
Fout = TFile('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROC.root','recreate')

TP_mass = {}
for sample in SampleName.keys()+['All']:
  TP_mass[sample] = {}
  for tagger in ['CSVv2','DeepCSV','DeepJet']:
    TP_mass[sample][tagger] ={}
    for WP in ['L','M','T']:
      TP_mass[sample][tagger][WP] = TGraph()
      ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
      num = Fin.Get('mass_'+sample+'_b_'+tagger+'_'+WP).GetY()
      den = Fin.Get('mass_'+sample+'_udsg_'+tagger+'_'+WP).GetY()
      for index,mass in enumerate(sorted(ll)):
        if den[index] == 0:
          ratio = 0
        else:
          ratio = num[index]/math.sqrt(den[index])
        TP_mass[sample][tagger][WP].SetPoint(index,int(mass),ratio)


TP_pt = {}
for sample in SampleName.keys()+['All']:
  TP_pt[sample] = {}
  for tagger in ['CSVv2','DeepCSV','DeepJet']:
    TP_pt[sample][tagger] ={}
    for WP in ['L','M','T']:
      TP_pt[sample][tagger][WP] =  TGraph()

for index,pT in enumerate(Pt_Range[0:-1]):
  for tagger in ['CSVv2','DeepCSV','DeepJet']:
    for WP in ['L','M','T']:
      for sample in SampleName.keys()+['All']:
        num = Fin.Get('pt_'+sample+'_b_'+tagger+'_'+str(pT)).GetY()[CSV_Value[tagger].index(WorkingPoint[tagger][WP])]
	den = Fin.Get('pt_'+sample+'_udsg_'+tagger+'_'+str(pT)).GetY()[CSV_Value[tagger].index(WorkingPoint[tagger][WP])]

	if den == 0:
	  ratio = 0
	else:
	  ratio = num/math.sqrt(den)
	TP_pt[sample][tagger][WP].SetPoint(index,(Pt_Range[index]+Pt_Range[index+1])/2,ratio)

WriteEverything(TP_mass,'TP_mass')
WriteEverything(TP_pt,'TP_pt')

ROCg_mass = {}
for sample in SampleName.keys()+['All']:
  ROCg_mass[sample] = {}
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll: 
    ROCg_mass[sample][mass] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
       ROCg_mass[sample][mass][tagger] = TGraphAsymmErrors()
       ROCg_mass[sample][mass][tagger].SetTitle('%s ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (g jet)'%(tagger,mass,sample))
       Xaxis = Fin.Get('dis_'+sample+'_'+mass+'_b_'+tagger).GetY() 
       Yaxis = Fin.Get('dis_'+sample+'_'+mass+'_g_'+tagger).GetY()
       for index in range(len(CSV_Value[tagger])):
         ROCg_mass[sample][mass][tagger].SetPoint(index,Xaxis[index],Yaxis[index])


ROCg_pt = {}
for sample in SampleName.keys()+['All']:
  ROCg_pt[sample] = {}
  for index,pT in enumerate(Pt_Range[0:-1]):
    ROCg_pt[sample][pT] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
       ROCg_pt[sample][pT][tagger] = TGraphAsymmErrors()
       ROCg_pt[sample][pT][tagger].SetTitle('%s ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (g jet)'%(tagger,sample,Pt_Range[index],Pt_Range[index+1]))
       Xaxis = Fin.Get('pt_'+sample+'_b_'+tagger+'_'+str(pT)).GetY()     
       Yaxis = Fin.Get('pt_'+sample+'_g_'+tagger+'_'+str(pT)).GetY()
       for ind in range(len(CSV_Value[tagger])):
         ROCg_pt[sample][pT][tagger].SetPoint(ind,Xaxis[ind],Yaxis[ind])

ROCuds_mass = {}
for sample in SampleName.keys()+['All']:
  ROCuds_mass[sample] = {}
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll: 
    ROCuds_mass[sample][mass] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
       ROCuds_mass[sample][mass][tagger] = TGraphAsymmErrors()
       ROCuds_mass[sample][mass][tagger].SetTitle('%s ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (uds jet)'%(tagger,mass,sample))

       Xaxis = Fin.Get('dis_'+sample+'_'+mass+'_b_'+tagger).GetY()
       Yaxis = Fin.Get('dis_'+sample+'_'+mass+'_uds_'+tagger).GetY()
       for index in range(len(CSV_Value[tagger])):
         ROCuds_mass[sample][mass][tagger].SetPoint(index,Xaxis[index],Yaxis[index])

ROCuds_pt = {}
for sample in SampleName.keys()+['All']:
  ROCuds_pt[sample] = {}
  for ind,pT in enumerate(Pt_Range[0:-1]):
    ROCuds_pt[sample][pT] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
       ROCuds_pt[sample][pT][tagger] = TGraphAsymmErrors()
       ROCuds_pt[sample][pT][tagger].SetTitle('%s ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (uds jet)'%(tagger,sample,Pt_Range[ind],Pt_Range[ind+1]))
       Xaxis = Fin.Get('pt_'+sample+'_b_'+tagger+'_'+str(pT)).GetY()
       Yaxis = Fin.Get('pt_'+sample+'_uds_'+tagger+'_'+str(pT)).GetY()
       for index in range(len(CSV_Value[tagger])):
         ROCuds_pt[sample][pT][tagger].SetPoint(index,Xaxis[index],Yaxis[index])

ROCc_mass = {}
for sample in SampleName.keys()+['All']:
  ROCc_mass[sample] = {}
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll:
    ROCc_mass[sample][mass] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
       ROCc_mass[sample][mass][tagger] = TGraphAsymmErrors()
       ROCc_mass[sample][mass][tagger].SetTitle('%s ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (c jet)'%(tagger,mass,sample))
       Xaxis = Fin.Get('dis_'+sample+'_'+mass+'_b_'+tagger).GetY()
       Yaxis = Fin.Get('dis_'+sample+'_'+mass+'_c_'+tagger).GetY()
       for index in range(len(CSV_Value[tagger])):
         ROCc_mass[sample][mass][tagger].SetPoint(index,Xaxis[index],Yaxis[index])

ROCc_pt = {}
for sample in SampleName.keys()+['All']:
  ROCc_pt[sample] = {}
  for ind,pT in enumerate(Pt_Range[0:-1]):
    ROCc_pt[sample][pT] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
       ROCc_pt[sample][pT][tagger] = TGraphAsymmErrors()
       ROCc_pt[sample][pT][tagger].SetTitle('%s ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (c jet)'%(tagger,sample,Pt_Range[ind],Pt_Range[ind+1]))
       Xaxis = Fin.Get('pt_'+sample+'_b_'+tagger+'_'+str(pT)).GetY()
       Yaxis = Fin.Get('pt_'+sample+'_c_'+tagger+'_'+str(pT)).GetY()
       for index in range(len(CSV_Value[tagger])):
         ROCc_pt[sample][pT][tagger].SetPoint(index,Xaxis[index],Yaxis[index])

ROC_mass = {}
for sample in SampleName.keys()+['All']:
  ROC_mass[sample] = {}
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll:
    ROC_mass[sample][mass] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']: 
	 ROC_mass[sample][mass][tagger] = TGraphAsymmErrors()
	 ROC_mass[sample][mass][tagger].SetTitle('%s ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (udsg jet)'%(tagger,mass,sample))
         Xaxis = Fin.Get('dis_'+sample+'_'+mass+'_b_'+tagger).GetY()
         Yaxis = Fin.Get('dis_'+sample+'_'+mass+'_udsg_'+tagger).GetY()
         for index in range(len(CSV_Value[tagger])):
	   ROC_mass[sample][mass][tagger].SetPoint(index,Xaxis[index],Yaxis[index]) 

ROC_pt = {}
for sample in SampleName.keys()+['All']:
  ROC_pt[sample] = {}
  for ind,pT in enumerate(Pt_Range[0:-1]): 
    ROC_pt[sample][pT] = {}
    for tagger in ['CSVv2','DeepCSV','DeepJet']: 
       ROC_pt[sample][pT][tagger] = TGraphAsymmErrors()
       ROC_pt[sample][pT][tagger].SetTitle('%s ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (udsg jet)'%(tagger,sample,Pt_Range[ind],Pt_Range[ind+1]))
       Xaxis = Fin.Get('pt_'+sample+'_b_'+tagger+'_'+str(pT)).GetY()
       Yaxis = Fin.Get('pt_'+sample+'_udsg_'+tagger+'_'+str(pT)).GetY()
       for index in range(len(CSV_Value[tagger])):
         ROC_pt[sample][pT][tagger].SetPoint(index,Xaxis[index],Yaxis[index])

WriteEverything(ROC_mass,'ROC_mass')
WriteEverything(ROC_pt,'ROC_pt')
WriteEverything(ROCc_mass,'ROCc_mass')
WriteEverything(ROCc_pt,'ROCc_pt')
WriteEverything(ROCuds_mass,'ROCuds_mass')
WriteEverything(ROCuds_pt,'ROCuds_pt')
WriteEverything(ROCg_mass,'ROCg_mass')
WriteEverything(ROCg_pt,'ROCg_pt')


Fout.Close()
#Plotting

for sample in SampleName.keys()+['All']:
  for tagger in ['CSVv2','DeepCSV','DeepJet']:
    c = TCanvas()
    c.SetGridx()
    c.SetGridy() 
    leg = TLegend(0.7,0.75,0.9,0.9)
    for index,WP in enumerate(['L','M','T']):
      TP_mass[sample][tagger][WP].SetLineColor(index+1)
      TP_mass[sample][tagger][WP].SetMarkerColor(index+1)
      TP_mass[sample][tagger][WP].SetMarkerSize(0.5)
      leg.AddEntry(TP_mass[sample][tagger][WP],WP,'L')
      if WP =='L':
	  TP_mass[sample][tagger][WP].GetYaxis().SetRangeUser(0,10)
	  TP_mass[sample][tagger][WP].SetTitle('%s Tagging Porwer of %s sample;Mass(GeV);Tagging Power'%(tagger,sample))
 	  TP_mass[sample][tagger][WP].Draw()
      else:
	  TP_mass[sample][tagger][WP].Draw('same')
    leg.Draw('same')
    c.SetTitle('%s Tagging Porwer of %s sample'%(tagger,sample))
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/TaggingPower_Mass_%s_%s.pdf'%(tagger,sample))
    c.Close()

for sample in SampleName.keys()+['All']:
  for tagger in ['CSVv2','DeepCSV','DeepJet']:
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()
    leg = TLegend(0.7,0.75,0.9,0.9)
    for index,WP in enumerate(['L','M','T']):
      TP_pt[sample][tagger][WP].SetLineColor(index+1)
      TP_pt[sample][tagger][WP].SetMarkerColor(index+1)
      TP_pt[sample][tagger][WP].SetMarkerSize(0.5)
      leg.AddEntry(TP_pt[sample][tagger][WP],WP,'L')
      if WP =='L':
        TP_pt[sample][tagger][WP].GetYaxis().SetRangeUser(0,10)
        TP_pt[sample][tagger][WP].SetTitle('%s Tagging Porwer of %s sample;pT(GeV);Tagging Power'%(tagger,sample))
	TP_pt[sample][tagger][WP].SetTitle('%s Tagging Porwer of %s sample'%(tagger,sample))
        TP_pt[sample][tagger][WP].Draw()
      else:
        TP_pt[sample][tagger][WP].Draw('same')
    leg.Draw('same')
    c.SetTitle('%s Tagging Porwer of %s sample'%(tagger,sample))
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/TaggingPower_pT_%s_%s.pdf'%(tagger,sample))
    c.Close()

for sample in SampleName.keys()+['All']:
  for flavor in ['b','udsg','c','uds','g']:
    for tagger in ['CSVv2','DeepCSV','DeepJet']:
      c = TCanvas()
      c.SetGridx()
      c.SetGridy()
      leg = TLegend(0.7,0.75,0.9,0.9)
      for index,WP in enumerate(['L','M','T']):
	  working = Fin.Get('mass_'+sample+'_'+flavor+'_'+tagger+'_'+WP)
	  working.SetLineColor(index+1)
	  working.SetMarkerColor(index+1)
	  working.SetMarkerSize(0.5)
	  leg.AddEntry(working,WP,'L')
	  
	  if WP =='L':
	    working.GetYaxis().SetRangeUser(0,1)
	    if flavor == 'b':
              working.SetTitle('%s %s Tagging Efficiency of %s sample;Mass(GeV);Tagging Efficiency of %s'%(tagger,flavor,sample,flavor))
	    else :
	      working.SetTitle('%s MisIdentify Probability (%s jet) of %s sample;Mass(GeV);MisIdentify Probability (%s jet)'%(tagger,flavor,sample,flavor))
	    working.Draw()
	  else: 
	    working.Draw('same')
      leg.Draw('same')
      if flavor=='b':
 	   c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/bEffi_%s_%s.pdf'%(tagger,sample))
      else:
	   c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/%sMP_%s_%s.pdf'%(flavor,tagger,sample))
      c.Close()

for sample in SampleName.keys()+['All']:
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll:
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()

    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
	ROC_mass[sample][mass][tagger].SetLineColor(index+1)
	ROC_mass[sample][mass][tagger].SetMarkerColor(index+1) 
	ROC_mass[sample][mass][tagger].SetMarkerSize(0.5)
        if tagger == 'CSVv2':
	  ROC_mass[sample][mass][tagger].GetXaxis().SetRangeUser(0,1)
	  ROC_mass[sample][mass][tagger].GetYaxis().SetRangeUser(0.0001,1)
       
	  ROC_mass[sample][mass][tagger].SetTitle('ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (udsg jet)'%(mass,sample))
	  ROC_mass[sample][mass][tagger].Draw()
	else:
	  ROC_mass[sample][mass][tagger].Draw('same')
        leg.AddEntry(ROC_mass[sample][mass][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROC_%s_%s.pdf'%(sample,mass))
    c.Close()

for sample in SampleName.keys()+['All']:
  for ind,pT in enumerate(Pt_Range[0:-1]):
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()
    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROC_pt[sample][pT][tagger].SetLineColor(index+1)
      ROC_pt[sample][pT][tagger].SetMarkerColor(index+1)
      ROC_pt[sample][pT][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROC_pt[sample][pT][tagger].SetTitle('ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (udsg jet)'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
	ROC_pt[sample][pT][tagger].GetXaxis().SetRangeUser(0,1)
	ROC_pt[sample][pT][tagger].GetYaxis().SetRangeUser(0.0001,1)
        ROC_pt[sample][pT][tagger].Draw()
      else:
        ROC_pt[sample][pT][tagger].Draw('same')
      leg.AddEntry(ROC_pt[sample][pT][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROC_%s_Pt%d-%d.pdf'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
    c.Close()

for sample in SampleName.keys()+['All']:
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll:
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()

    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROCuds_mass[sample][mass][tagger].SetLineColor(index+1)
      ROCuds_mass[sample][mass][tagger].SetMarkerColor(index+1)
      ROCuds_mass[sample][mass][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROCuds_mass[sample][mass][tagger].GetXaxis().SetRangeUser(0,1)
        ROCuds_mass[sample][mass][tagger].GetYaxis().SetRangeUser(0.0001,1)

        ROCuds_mass[sample][mass][tagger].SetTitle('ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (uds jet)'%(mass,sample))
        ROCuds_mass[sample][mass][tagger].Draw()
      else:
        ROCuds_mass[sample][mass][tagger].Draw('same')
      leg.AddEntry(ROCuds_mass[sample][mass][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROCuds_%s_%s.pdf'%(sample,mass))
    c.Close()

for sample in SampleName.keys()+['All']:
  for ind,pT in enumerate(Pt_Range[0:-1]):
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()
    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROCuds_pt[sample][pT][tagger].SetLineColor(index+1)
      ROCuds_pt[sample][pT][tagger].SetMarkerColor(index+1)
      ROCuds_pt[sample][pT][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROCuds_pt[sample][pT][tagger].SetTitle('ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (uds jet)'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
        ROCuds_pt[sample][pT][tagger].GetXaxis().SetRangeUser(0,1)
        ROCuds_pt[sample][pT][tagger].GetYaxis().SetRangeUser(0.0001,1)
        ROCuds_pt[sample][pT][tagger].Draw()
      else:
        ROCuds_pt[sample][pT][tagger].Draw('same')
      leg.AddEntry(ROCuds_pt[sample][pT][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROCuds_%s_Pt%d-%d.pdf'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
    c.Close()

for sample in SampleName.keys()+['All']:
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll:
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()

    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROCg_mass[sample][mass][tagger].SetLineColor(index+1)
      ROCg_mass[sample][mass][tagger].SetMarkerColor(index+1)
      ROCg_mass[sample][mass][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROCg_mass[sample][mass][tagger].GetXaxis().SetRangeUser(0,1)
        ROCg_mass[sample][mass][tagger].GetYaxis().SetRangeUser(0.0001,1)

        ROCg_mass[sample][mass][tagger].SetTitle('ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (g jet)'%(mass,sample))
        ROCg_mass[sample][mass][tagger].Draw()
      else:
        ROCg_mass[sample][mass][tagger].Draw('same')
      leg.AddEntry(ROCg_mass[sample][mass][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROCg_%s_%s.pdf'%(sample,mass))
    c.Close()

for sample in SampleName.keys()+['All']:
  for ind,pT in enumerate(Pt_Range[0:-1]):
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()
    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROCg_pt[sample][pT][tagger].SetLineColor(index+1)
      ROCg_pt[sample][pT][tagger].SetMarkerColor(index+1)
      ROCg_pt[sample][pT][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROCg_pt[sample][pT][tagger].SetTitle('ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (g jet)'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
        ROCg_pt[sample][pT][tagger].GetXaxis().SetRangeUser(0,1)
        ROCg_pt[sample][pT][tagger].GetYaxis().SetRangeUser(0.0001,1)
        ROCg_pt[sample][pT][tagger].Draw()
      else:
        ROCg_pt[sample][pT][tagger].Draw('same')
      leg.AddEntry(ROCg_pt[sample][pT][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROCg_%s_Pt%d-%d.pdf'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
    c.Close()


for sample in SampleName.keys()+['All']:
  ll = SampleName['R2bb'].keys() if sample=='All' else SampleName[sample].keys()
  for mass in ll: 
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()
    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROCc_mass[sample][mass][tagger].SetLineColor(index+1)
      ROCc_mass[sample][mass][tagger].SetMarkerColor(index+1) 
      ROCc_mass[sample][mass][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROCc_mass[sample][mass][tagger].GetXaxis().SetRangeUser(0,1)
        ROCc_mass[sample][mass][tagger].GetYaxis().SetRangeUser(0.0001,1)
  
        ROCc_mass[sample][mass][tagger].SetTitle('ROC plot of %sGeV %s sample;b Tagging Efficiency;MisIdentify Probablity (c jet)'%(mass,sample))
        ROCc_mass[sample][mass][tagger].Draw()
      else:
        ROCc_mass[sample][mass][tagger].Draw('same')
      leg.AddEntry(ROCc_mass[sample][mass][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROCc_%s_%s.pdf'%(sample,mass))
    c.Close()

for sample in SampleName.keys()+['All']:
  for ind,pT in enumerate(Pt_Range[0:-1]):
    c = TCanvas()
    c.SetGridx()
    c.SetGridy()
    leg = TLegend(0.7,0.1,0.9,0.25)
    for index,tagger in enumerate(['CSVv2','DeepCSV','DeepJet']):
      ROCc_pt[sample][pT][tagger].SetLineColor(index+1)
      ROCc_pt[sample][pT][tagger].SetMarkerColor(index+1)
      ROCc_pt[sample][pT][tagger].SetMarkerSize(0.5)
      if tagger == 'CSVv2':
        ROCc_pt[sample][pT][tagger].SetTitle('ROC plot of %s sample within pT %d ~ %d;b Tagging Efficiency;MisIdentify Probablity (c jet)'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
        ROCc_pt[sample][pT][tagger].GetXaxis().SetRangeUser(0,1)
        ROCc_pt[sample][pT][tagger].GetYaxis().SetRangeUser(0.0001,1)
        ROCc_pt[sample][pT][tagger].Draw()
      else:
        ROCc_pt[sample][pT][tagger].Draw('same')
      leg.AddEntry(ROCc_pt[sample][pT][tagger],tagger,'l')
    leg.Draw('same')
    c.SetLogy()
    c.Print('ROC_Efficiency_DeepJet_DeepCSV_CSVv2/ROCc_%s_Pt%d-%d.pdf'%(sample,Pt_Range[ind],Pt_Range[ind+1]))
    c.Close()


#////////////////////////////


