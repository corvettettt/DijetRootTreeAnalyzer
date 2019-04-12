from ROOT import *
import sys,os
from optparse import OptionParser
SampleName = {}
SampleName['bstar0p1'] = {
500: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/500GeV_reduced_skim.root',
1000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/1000GeV_reduced_skim.root',
2000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/2000GeV_reduced_skim.root',
3000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/3000GeV_reduced_skim.root',
4000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/4000GeV_reduced_skim.root',
5000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/5000GeV_reduced_skim.root',
6000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/6000GeV_reduced_skim.root',
7000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/7000GeV_reduced_skim.root',
8000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/8000GeV_reduced_skim.root',
9000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg0p1_Jet_central/9000GeV_reduced_skim.root',

}

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
'0500': '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSG2BB_Jet_central/R2BB_500GeV_reduced_skim.root',
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


#SampleName[model].keys() = [1000,2000,3000,4000,5000,6000,7000,8000,9000]

CSV_Value={}
CSV_Value['DeepCSV'] = {
   'L':0.1522,
   'M':0.4941,
   'T':0.8001
}

CSV_Value['CSV'] = {
   'L':0.5803,
   'M':0.8838,
   'T':0.9693
}
CSV_Value['DeepJet'] = {
'L':0.0521,
'M':0.3033,
'T':0.7489,
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


if __name__=='__main__':

  parser = OptionParser()
  parser.add_option('-m','--model',dest="model",type="string",default="qq",help="Name of the signal model")
  (options,args) = parser.parse_args()
  model   = options.model

  histo = {}
  for i in SampleName[model].keys():
    histo[i] = {}
  for j in SampleName[model].keys():
    for i in ['j1','j2']:
      #for j in ['Eta','pT','Phi']
      histo[j]['h_pT_%s'%i] = TH1D('h_%s_pT_%s'%(j,i),'h_%s_pT_%s'%(j,i),50,0,5000)
      histo[j]['h_pT_%s'%i].SetTitle('%s Jet pT of %s Sample;pT(GeV);# of Event'%(i,j))
      histo[j]['h_Eta_%s'%i] = TH1D('h_%s_Eta_%s'%(j,i),'h_%s_Eta_%s'%(j,i),30,-3.14159,3.14159)
      histo[j]['h_Eta_%s'%i].SetTitle('%s Jet Eta of %s Sample;Eta;# of Event'%(i,j))
      histo[j]['h_Phi_%s'%i] = TH1D('h_%s_Phi_%s'%(j,i),'h_%s_Phi_%s'%(j,i),30,-3.14159,3.14159)
      histo[j]['h_Phi_%s'%i].SetTitle('%s Jet Phi of %s Sample;Phi;# of Event'%(i,j))
    histo[j]['h_DeltaPhi'] = TH1D('h_%s_DeltaPhi'%j,'h_%s_DeltaPhi'%j,30,0,3.2)
    histo[j]['h_DeltaPhi'].SetTitle('Delta Phi of %s sample;DeltaPhi;# of Event'%j)
    histo[j]['h_DeltaEta'] = TH1D('h_%s_DeltaEta'%j,'h_%s_DeltaEta'%j,30,0,4) 
    histo[j]['h_DeltaEta'].SetTitle('Delta Eta of %s sample;DeltaEta;# of Event'%j)
    histo[j]['h_pT'] = TH1D('h_pT_%s'%j,'h_pT_%s'%j,50,0,5000)
    histo[j]['h_pT'].SetTitle('Jet pT of %s GeV Sample;pT(GeV);# of Event'%j)
    histo[j]['h_Eta']= TH1D('h_Eta_%s'%j,'h_Eta_%s'%j,30,-3.14159,3.14159)
    histo[j]['h_Eta'].SetTitle('Jet Eta of %s Sample;Eta;# of Event'%j)
    histo[j]['h_Phi']= TH1D('h_Phi_%s'%j,'h_Phi_%s'%j,30,-3.14159,3.14159)
    histo[j]['h_Phi'].SetTitle('Jet Phi of %s Sample;Phi;# of Event'%j)
    histo[j]['h_Mass']= TH1D('h_Mass_%s'%j,'h_Mass_%s'%j,75,0,int(j)*1.5)
    histo[j]['h_Mass'].SetTitle('Invariant Mass of %s Sample;Mass(GeV);# of Event'%j)


    histo[j]['B'] = 0

  TreeName = 'rootTupleTree/tree'

  for i in SampleName[model].keys():
    tchain = TChain(TreeName)
    tchain.Add(SampleName[model][i])
    for j in progressbar(range(tchain.GetEntries()), str(i)+" : ", 40):
      
      tchain.GetEntry(j)

      if not (abs(tchain.deltaETAjj)<1.3       and
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

      for k in ['j1','j2']:

        if getattr(tchain,'jetpflavour_'+k) != 5:
          continue

	if tchain.pTAK4_j1 < tchain.pTAK4_j2:
          histo[i]['h_pT_%s'%(list(k)[0]+str(3-int(list(k)[1])))].Fill(getattr(tchain,'pTAK4_'+k))
          histo[i]['h_Eta_%s'%(list(k)[0]+str(3-int(list(k)[1])))].Fill(getattr(tchain,'etaAK4_'+k))
          histo[i]['h_Phi_%s'%(list(k)[0]+str(3-int(list(k)[1])))].Fill(getattr(tchain,'phiAK4_'+k))
	else:
          histo[i]['h_pT_%s'%k].Fill(getattr(tchain,'pTAK4_'+k))
          histo[i]['h_Eta_%s'%k].Fill(getattr(tchain,'etaAK4_'+k))
          histo[i]['h_Phi_%s'%k].Fill(getattr(tchain,'phiAK4_'+k))


        histo[i]['h_pT'].Fill(getattr(tchain,'pTAK4_'+k))
        if getattr(tchain,'jetpflavour_'+k) == 5:
          histo[i]['B'] +=1

      histo[i]['h_DeltaPhi'].Fill(tchain.deltaPHIjj)
      histo[i]['h_DeltaEta'].Fill(tchain.deltaETAjj)
      histo[i]['h_Mass'].Fill(tchain.mjj)

    histo[i]['Ratio'] = float(histo[i]['B'])/float(tchain.GetEntries())

  Ratio = TGraphAsymmErrors()

  Fout = TFile('L1L2_b_%s.root'%model,'recreate')
 
  tmp = {}

  for i in SampleName[model].keys():
    tmp[i]={}

  for k,j in enumerate(sorted(SampleName[model].keys())):
    for i in ['j1','j2']:
      tmp[j]['h_pT_%s'%i] = histo[j]['h_pT_%s'%i].Clone('h_%s_pT_%s'%(j,i))
      tmp[j]['h_pT_%s'%i].Scale(1/ histo[j]['h_pT_%s'%i].Integral())
      tmp[j]['h_pT_%s'%i].SetTitle('%s Jet pT of %s Sample;pT(GeV);# of Event'%(i,j))
      tmp[j]['h_pT_%s'%i].Write()
      tmp[j]['h_Eta_%s'%i]= histo[j]['h_Eta_%s'%i].Clone('h_%s_Eta_%s'%(j,i))
      tmp[j]['h_Eta_%s'%i].Scale(1/histo[j]['h_Eta_%s'%i].Integral())
      tmp[j]['h_Eta_%s'%i].SetTitle('%s Jet Eta of %s Sample;Eta;# of Event'%(i,j))
      tmp[j]['h_Eta_%s'%i].Write()
      tmp[j]['h_Phi_%s'%i]= histo[j]['h_Phi_%s'%i].Clone('h_%s_Phi_%s'%(j,i))
      tmp[j]['h_Phi_%s'%i].Scale(1/histo[j]['h_Phi_%s'%i].Integral())
      tmp[j]['h_Phi_%s'%i].SetTitle('%s Jet Phi of %s Sample;Phi;# of Event'%(i,j))
      tmp[j]['h_Phi_%s'%i].Write()


    tmp[j]['h_DeltaPhi'] = histo[j]['h_DeltaPhi'].Clone('h_%s_DeltaPhi'%j)
    tmp[j]['h_DeltaPhi'].Scale(1/histo[j]['h_DeltaPhi'].Integral())
    tmp[j]['h_DeltaPhi'].SetTitle('Delta Phi of %s sample;DeltaPhi;# of Event'%j)
    tmp[j]['h_DeltaPhi'].Write()

    tmp[j]['h_DeltaEta'] = histo[j]['h_DeltaEta'].Clone('h_%s_DeltaEta'%j)
    tmp[j]['h_DeltaEta'].Scale(1/histo[j]['h_DeltaEta'].Integral())
    tmp[j]['h_DeltaEta'].SetTitle('Delta Eta of %s sample;DeltaEta;# of Event'%j)
    tmp[j]['h_DeltaEta'].Write()

    tmp[j]['h_pT'] = histo[j]['h_pT'].Clone('h_pT_%s'%j)
    tmp[j]['h_pT'].Scale(1/ histo[j]['h_pT'].Integral())
    tmp[j]['h_pT'].SetTitle('Jet pT of %s Sample;pT(GeV);# of Event'%j)
    tmp[j]['h_pT'].Write()

    tmp[j]['h_Mass'] = histo[j]['h_Mass'].Clone('h_Mass_%s'%j)
    tmp[j]['h_Mass'].Scale(1/ histo[j]['h_pT'].Integral())
    tmp[j]['h_Mass'].SetTitle('Invariant Mass of %s Sample;Mass(GeV);# of Event'%j)
    tmp[j]['h_Mass'].Write()
    #tmp[j]['h_Eta']
    #tmp[j]['h_Eta']
    #tmp[j]['h_Eta']
    #tmp[j]['h_Eta']

    #tmp[j]['h_Phi']
    #tmp[j]['h_Phi']
    #tmp[j]['h_Phi']
    #tmp[j]['h_Phi']

    Ratio.SetPoint(k,float(j),histo[j]['Ratio'])
  Ratio.Write()
  Fout.Close()

