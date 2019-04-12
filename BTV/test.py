from ROOT import * 
Sample = {}
Sample['RSG2bb'] = {
'0500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_500GeV.root',
'1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_1000GeV.root',
'2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_2000GeV.root',
'3000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_3000GeV.root',
'4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_4000GeV.root',
'5000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_5000GeV.root',
'6000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_6000GeV.root',
'7000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_7000GeV.root',
'8000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_8000GeV.root',
'9000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/RSG2bb/RSG2bb_9000GeV.root',
}

for i,j in Sample['RSG2bb'].items():
  tchain = TChain('deepntuplizer/tree')
  tchain.Add(j)
  print i,'  ',tchain.GetEntries()
