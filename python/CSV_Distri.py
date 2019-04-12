from ROOT import *

import sys

SampleName = {}
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

  histo = {}

  for i in ['R2bb','R2qq','bstar']:
    histo[i]={}
    fout = TFile(i+'CSVDistri.root','recreate')
    tchain = TChain('rootTupleTree/tree')
    for j in ['0500','1000','2000','3000','4000','5000','6000','7000','8000','9000']:
      if i == 'R2qq' and j =='9000':
	continue
      tchain.Add(SampleName[i][j])
    Nen = tchain.GetEntries()

    for j in ['CSV','DeepJet','DeepCSV']:

  

      histo[i]['J1'+j] = TH1D('J1'+j,'J1'+j,15,0,1)
      histo[i]['J1'+j].SetTitle('%s distribution of leading AK4 Jet;Discriminator;# of Event'%j)

      histo[i]['J2'+j] = TH1D('J2'+j,'J2'+j,15,0,1)
      histo[i]['J2'+j].SetTitle('%s distribution of second leading AK4 Jet;Discriminator;# of Event'%j)

      histo[i]['J1b'+j] = TH1D('J1b'+j,'J1b'+j,15,0,1)
      histo[i]['J1b'+j].SetTitle('%s distribution of leading AK4 Jet if it\' a b;Discriminator;# of Event'%j)
    
      histo[i]['J2b'+j] = TH1D('J2b'+j,'J2b'+j,15,0,1)
      histo[i]['J2b'+j].SetTitle('%s distribution of second leading AK4 Jet  if it\' a b;Discriminator;# of Event'%j)

      histo[i]['J1c'+j] = TH1D('J1c'+j,'J1c'+j,15,0,1)
      histo[i]['J1c'+j].SetTitle('%s distribution of leading AK4 Jet if it\' a c;Discriminator;# of Event'%j)

      histo[i]['J2c'+j] = TH1D('J2c'+j,'J2c'+j,15,0,1)
      histo[i]['J2c'+j].SetTitle('%s distribution of second leading AK4 Jet  if it\' a c;Discriminator;# of Event'%j)

      histo[i]['J1udsg'+j] = TH1D('J1udsg'+j,'J1udsg'+j,15,0,1)
      histo[i]['J1udsg'+j].SetTitle('%s distribution of leading AK4 Jet if it\' a udsg;Discriminator;# of Event'%j)

      histo[i]['J2udsg'+j] = TH1D('J2udsg'+j,'J2udsg'+j,15,0,1)
      histo[i]['J2udsg'+j].SetTitle('%s distribution of second leading AK4 Jet  if it\' usdg;Discriminator;# of Event'%j)

    for j in progressbar(range(Nen)):
      tchain.GetEntry(j)
     
      if not (abs(tchain.deltaETAjj)<1.1       and
                abs(tchain.etaWJ_j1)<2.5       and
                abs(tchain.etaWJ_j2)<2.5  
	     ):
            continue

      for k in ['CSV','DeepJet','DeepCSV']:

        histo[i]['J1'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))
        histo[i]['J2'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))

        if tchain.jetHflavour_j1 == 5:
          histo[i]['J1b'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))
        if tchain.jetHflavour_j2 == 5:
          histo[i]['J2b'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))

        if tchain.jetHflavour_j1 == 4:
          histo[i]['J1c'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))
        if tchain.jetHflavour_j2 == 4:
          histo[i]['J2c'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))

        if tchain.jetHflavour_j1 == 0:
          histo[i]['J1udsg'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))
        if tchain.jetHflavour_j2 == 0:
          histo[i]['J2udsg'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))

      if tchain.pTAK4_j1 < tchain.pTAK4_j2:
        for k in ['CSV','DeepJet','DeepCSV']:
	  histo[i]['J1'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))
          histo[i]['J2'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))

	  if tchain.jetHflavour_j1 == 5:
            histo[i]['J1b'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))
          if tchain.jetHflavour_j2 == 5:
            histo[i]['J2b'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))

          if tchain.jetHflavour_j1 == 4:
            histo[i]['J1c'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))
          if tchain.jetHflavour_j2 == 4:
            histo[i]['J2c'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))

          if tchain.jetHflavour_j1 == 0:
            histo[i]['J1udsg'+k].Fill(getattr(tchain,'jet%sAK4_j2'%k))
          if tchain.jetHflavour_j2 == 0:
            histo[i]['J2udsg'+k].Fill(getattr(tchain,'jet%sAK4_j1'%k))


    for j in ['1','2']:
      for k in ['CSV','DeepJet','DeepCSV']:
        for l in ['','b','c','udsg']:
          histo[i]['J%s%s%s'%(j,l,k)].Write()

    fout.Close()
