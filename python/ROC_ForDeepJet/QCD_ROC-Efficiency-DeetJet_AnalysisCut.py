import ROOT as rt
from rootTools import tdrstyle as setTDRStyle
rt.gROOT.SetBatch()
setTDRStyle.setTDRStyle()
import math


from ROOT import *
import os,sys
import collections

SampleName_Non = {}
SampleName = {}

SampleName['QCD'] = {
'0200-0300':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD200_300_reduced_skim.root',
'0300-0500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD300_500_reduced_skim.root',
'0500-0700':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD500_700_reduced_skim.root',
'0700-1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD700_1000_reduced_skim.root',
'1000-1500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD1000_1500_reduced_skim.root',
'1500-2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD1500_2000_reduced_skim.root',
'2000-4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD2000_Inf_reduced_skim.root',
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

CSV_Value ={}

CSV_Value['CSVv2'] =   [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9,0.95,0.9693,1]
CSV_Value['DeepCSV'] = [0,0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.55,0.6,0.65,0.7,0.75,0.8001,0.85,0.9,0.95,1]
CSV_Value['DeepJet'] = [0,0.0521,0.1,0.15,0.2,0.25,0.3033,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.7489,0.8,0.85,0.9,0.95,1]

Pt_Range = [30.0,200.0,400.0,600.0,800.0,1000.0,1400.0,1800.0,2200.0,2600.0,3000.0,3500.0,4000.0,5000.0]

def WriteEverything(dic,name = ''):
  for key,value in dic.items():
    if isinstance(value,dict):
      WriteEverything(value,name+'_'+str(key))
    else :
      value.Write(name+'_'+str(key))
  return

if __name__ == '__main__':

  treeName = "rootTupleTree/tree"

  Num = {}
  for sample in SampleName.keys()+['All']:
    Num[sample]={}
    ll = SampleName['QCD'].keys()
    for mass in ll+Pt_Range[0:-1]:
      Num[sample][mass]={}
      for flavor in ['b','c','udsg','uds','g']:
        Num[sample][mass][flavor] = {}
        Num[sample][mass][flavor]['total'] = 0
        for tagger in ['CSVv2','DeepCSV','DeepJet']:
          for discri in CSV_Value[tagger]:
            Num[sample][mass][flavor][tagger+'_'+str(discri)] = 0

  for sample,Dic in SampleName.items():
    for mass,add in collections.OrderedDict(sorted(Dic.items())).items():
      tchain = TChain(treeName)
      tchain.Add(add)

      print mass,' : ',add

      NEntries = tchain.GetEntries()
      if NEntries >400000:
	 NEntries = 400000
      for tt in progressbar(range(NEntries),'sample %s || Mass %s : '%(sample,mass)):
        tchain.GetEntry(tt)

        if not (abs(tchain.deltaETAjj)<1.1       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                #tchain.pTWJ_j1<6500              and
                tchain.pTWJ_j2>30                and
                #tchain.pTWJ_j2<6500              and

                #tchain.mjj > 1246                and
                #tchain.mjj < 14000               and

                tchain.PassJSON):
            continue

	for jet in ['j1','j2']:

	  for index,temp in enumerate(Pt_Range[0:-1]):
	    if Pt_Range[index]<=getattr(tchain,'pTAK4_'+jet)< Pt_Range[index+1]:
	      pT = Pt_Range[index]

  	  if getattr(tchain,'jetHflavour_'+jet) == 5:
	    flavor = 'b'  
          elif  getattr(tchain,'jetHflavour_'+jet) == 4:
	    flavor = 'c'
	  else:
	    flavor = 'udsg'

	  Num[sample][pT][flavor]['total'] += 1
	  Num['All'][pT][flavor]['total'] += 1

	  Num[sample][mass][flavor]['total'] += 1
	  Num['All'][mass][flavor]['total'] += 1
          for tagger in ['CSVv2','DeepCSV','DeepJet']:
	    for discri in CSV_Value[tagger]:
	      if getattr(tchain,WorkingPoint[tagger]['tag']+jet) > discri:
                Num[sample][mass][flavor][tagger+'_'+str(discri)] += 1
	        Num['All'][mass][flavor][tagger+'_'+str(discri)] += 1

		Num[sample][pT][flavor][tagger+'_'+str(discri)] += 1
                Num['All'][pT][flavor][tagger+'_'+str(discri)] += 1

	  if getattr(tchain,'jetpflavour_'+jet) == 21:
	    flavor = 'g'
	  elif getattr(tchain,'jetpflavour_'+jet) == 1 or getattr(tchain,'jetpflavour_'+jet) == 2 or getattr(tchain,'jetpflavour_'+jet) == 3:
	    flavor = 'uds'
	  else:
	    continue

	  Num[sample][pT][flavor]['total'] += 1
          Num['All'][pT][flavor]['total'] += 1
	  Num[sample][mass][flavor]['total'] += 1
          Num['All'][mass][flavor]['total'] += 1
	  for tagger in ['CSVv2','DeepCSV','DeepJet']:
            for discri in CSV_Value[tagger]:
	      if getattr(tchain,WorkingPoint[tagger]['tag']+jet) > discri:
	        Num[sample][mass][flavor][tagger+'_'+str(discri)] += 1
                Num['All'][mass][flavor][tagger+'_'+str(discri)] += 1
	        Num[sample][pT][flavor][tagger+'_'+str(discri)] += 1
                Num['All'][pT][flavor][tagger+'_'+str(discri)] += 1

  ratio = {}
  for sample in SampleName.keys():
    ratio[sample] = {}
    ll = SampleName[sample].keys()
    for mass in ll+Pt_Range[0:-1]:
      ratio[sample][mass] = {}
      for flavor in ['b','c','udsg']:
	ratio[sample][mass][flavor] = {}
        for tagger in ['CSVv2','DeepCSV','DeepJet']:
          ratio[sample][mass][flavor][tagger] = {}
          for index,discri in enumerate(CSV_Value[tagger]):
            numerator = Num[sample][mass][flavor][tagger+'_'+str(discri)]
            denominator = Num[sample][mass][flavor]['total']
            if denominator != 0:
              ratio[sample][mass][flavor][tagger][discri] = float(numerator)/float(denominator)
            else:
              ratio[sample][mass][flavor][tagger][discri] = 0

  for sample in SampleName.keys():
    ll = SampleName[sample].keys()
    for mass in ll+Pt_Range[0:-1]:
      for flavor in ['g','uds']:
	ratio[sample][mass][flavor] = {}
        for tagger in ['CSVv2','DeepCSV','DeepJet']:
	  ratio[sample][mass][flavor][tagger] = {}
	  for index,discri in enumerate(CSV_Value[tagger]):
	    numerator = Num[sample][mass][flavor][tagger+'_'+str(discri)]
	    denominator = Num[sample][mass][flavor]['total']
	    if denominator != 0:
	      ratio[sample][mass][flavor][tagger][discri] = float(numerator)/float(denominator)
            else:
              ratio[sample][mass][flavor][tagger][discri] = 0

  gr_dis = {}
  for sample in SampleName.keys(): 
    gr_dis[sample] = {}
    ll = SampleName[sample].keys()
    for mass in ll:
      gr_dis[sample][mass] = {}
      for flavor in ['g','uds','b','c','udsg']:
        gr_dis[sample][mass][flavor] = {}
        for tagger in ['CSVv2','DeepCSV','DeepJet']:
          gr_dis[sample][mass][flavor][tagger] = TGraph()
          if flavor == 'udsg':
  	    gr_dis[sample][mass][flavor][tagger].SetTitle('%s MisIdentify Probablity of Mass %sGeV %s sample;discriminator;MisIdentify Probablity'%(tagger,mass,sample))
  	  else:
  	    gr_dis[sample][mass][flavor][tagger].SetTitle('%s %s Tagging Efficiency of Mass %sGeV %s sample;discriminator;Tagging Efficiency of %s'%(tagger,flavor,mass,sample,flavor))
    	  for index,discri in enumerate(CSV_Value[tagger]):
            gr_dis[sample][mass][flavor][tagger].SetPoint(index,discri,ratio[sample][mass][flavor][tagger][discri])

  gr_mass = {}
  for sample in SampleName.keys():
    gr_mass[sample] = {}
    for flavor in ['g','uds','c','b','udsg']:
      gr_mass[sample][flavor]={}
      for tagger in ['CSVv2','DeepCSV','DeepJet']:
	gr_mass[sample][flavor][tagger]={}
	for WP in ['L','M','T']: 
	  gr_mass[sample][flavor][tagger][WP]= TGraph()
	  ll = SampleName[sample].keys()
	  if flavor == 'udsg':
	    gr_mass[sample][flavor][tagger][WP].SetTitle('%s WP %s MisIdentify Probablity of %s sample;Mass(GeV);MisIdentify Probablity'%(WP,tagger,sample))
	  if flavor == 'b':
            gr_mass[sample][flavor][tagger][WP].SetTitle('%s WP %s %s Tagging Efficiency of %s sample;Mass(GeV);Tagging Efficiency of %s'%(WP,tagger,flavor,sample,flavor)) 
          for index,mass in enumerate(sorted(ll)):
            gr_mass[sample][flavor][tagger][WP].SetPoint(index,(int(mass.split('-')[0])+int(mass.split('-')[1]))/2,ratio[sample][mass][flavor][tagger][WorkingPoint[tagger][WP]])
	    
  gr_pt = {}
  for sample in SampleName.keys():
    gr_pt[sample] = {}
    for flavor in ['g','uds','c','b','udsg']:
      gr_pt[sample][flavor] = {}
      for tagger in ['CSVv2','DeepCSV','DeepJet']:
        gr_pt[sample][flavor][tagger]={}
	for ind,pT in enumerate(Pt_Range[0:-1]): 
	  gr_pt[sample][flavor][tagger][pT]= TGraph()
	  if flavor != 'b':
	    gr_pt[sample][flavor][tagger][pT].SetTitle('%s MisIdentify Probablity of %s sample within pT %d ~ %d;discriminator;MisIdentify Probablity(%s jet)'%(tagger,sample,Pt_Range[ind],Pt_Range[ind+1],flavor))
	  if flavor == 'b':
	    gr_pt[sample][flavor][tagger][pT].SetTitle('%s %s Tagging Efficiency of %s sample within pT %d ~ %d;discriminator;Tagging Efficiency of %s'%(tagger,flavor,sample,Pt_Range[ind],Pt_Range[ind+1],flavor))
	  for index,discri in enumerate(CSV_Value[tagger]):
	    gr_pt[sample][flavor][tagger][pT].SetPoint(index,discri,ratio[sample][pT][flavor][tagger][discri])

  Fout = TFile('QCD_ROC_Efficiency_DeepJet_DeepCSV_CSVv2_AnalysisCut/NewDeep_ROC_Efficiency.root','recreate')
  WriteEverything(gr_dis,'dis')
  WriteEverything(gr_mass,'mass')  
  WriteEverything(gr_pt,'pt')
  Fout.Close()
