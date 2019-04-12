import ROOT as rt
from rootTools import tdrstyle as setTDRStyle
rt.gROOT.SetBatch()
setTDRStyle.setTDRStyle()

from ROOT import *
import math
import sys,os
treename = 'deepntuplizer/tree'

VariableList = ['n_sv','nsv','sv_pt','sv_phi','sv_etarel','sv_phirel','sv_deltaR','sv_mass','sv_ntracks','sv_chi2','sv_ndf','sv_normchi2','sv_dxy','sv_dxyerr','sv_dxysig','sv_d3d','sv_d3derr','sv_costhetasvpv','sv_enratio','npv','rho','ntreInt','event_no','jet_no','gen_pt','Delta_gen_pt','isB','isGBB','isBB','isLeptonicB','isLeptonicB_C','isC','isGCC','isCC','isUD','isS','isG','isUndefined','genDecay','isPhysB','isPhysGBB','isPhysBB','isPhysLeptonicB','isPhysLeptonicB_C','isPhysC','isPhysGCC','isPhysCC','isPhysUD','isPhysS','isPhysG','isPhysUndefined','jet_pt','jet_corr_pt','jet_eta','jet_phi','jet_mass','jet_energy','jet_looseID','jet_qgI','QG_ptD','QG_axis2','QG_mult','y_multiplicity','y_charged_multiplicity','y_neutral_multiplicity','y_ptD','y_axis1','y_axis2','y_pt_dr_log','muons_numbers','electrons_number','muons_isLooseMuon','muons_isTightMuon','muons_isSoftMuon','muons_isHighPtMuon','muons_pt','muons_relEta','muons_relPhi','muons_energy','electrons_pt','electrons_relEta','electrons_relPhi','electrons_energy','gen_pt_Recluster','gen_pt_WithNu','Delta_gen_pt_recluster','Delta_gen_pt_WithNu','nCpfcan','Cpf_can_pt','Cpfca_phi','Cpfcan_phi','cpfcan_ptrel','cpfcan_erel','Cpfcan_phirel','Cpfcan_etarel','Cpfcan_deltaR','Cpfcan_puppiw','Cpfcan_dxy','Cpfcan_dxyerrinv','Cpfcan_dxyig','Cpfcan_dz','Cpfcan_VTX_ass','Cpfcan_fromPV','Cpfcan_drminsv','Cpfcan_vertex_rho','Cpfcan_vertex_phirel','Cpfcan_vertex_etarel','Cpfcan_chi2','Cpfcan_quality','nNpfcand','Npfcan_pt','Npfcan_eta','Npfcan_phi','Npfcan_ptrel','Npfcan_erel','Npfcan_puppiw','Npfcan_phirel','Npfcan_etarel','Npfcan_deltaR','Npfcan_isGamma']

VariableList=['n_sv','nsv','sv_pt','sv_phi','sv_etarel','sv_phirel','sv_deltaR','sv_mass','sv_ntracks','sv_chi2','sv_ndf','sv_normchi2','sv_dxy','sv_dxyerr','sv_dxysig','sv_d3d','sv_d3derr','sv_costhetasvpv','sv_enratio','jet_pt','jet_corr_pt','jet_eta','jet_phi','jet_mass','jet_energy']

VariableList = ['n_sv','sv_pt','sv_phi','sv_eta','sv_deltaR','sv_mass','sv_ntracks','sv_chi2','jet_corr_pt','jet_eta','jet_phi','jet_mass','jet_energy']

VariableList = ['n_sv', 'nsv', 'sv_pt', 'sv_eta', 'sv_phi', 'sv_etarel', 'sv_phirel', 'sv_deltaR', 'sv_mass', 'sv_ntracks', 'sv_chi2', 'sv_ndf', 'sv_normchi2', 'sv_dxy', 'sv_dxyerr', 'sv_dxysig', 'sv_d3d', 'sv_d3derr', 'sv_d3dsig', 'sv_costhetasvpv', 'sv_enratio', 'npv', 'rho', 'ntrueInt', 'event_no', 'jet_no', 'gen_pt', 'Delta_gen_pt', 'isB', 'isGBB', 'isBB', 'isLeptonicB', 'isLeptonicB_C', 'isC', 'isGCC', 'isCC', 'isUD', 'isS', 'isG', 'isUndefined', 'genDecay', 'isPhysB', 'isPhysGBB', 'isPhysBB', 'isPhysLeptonicB', 'isPhysLeptonicB_C', 'isPhysC', 'isPhysGCC', 'isPhysCC', 'isPhysUD', 'isPhysS', 'isPhysG', 'isPhysUndefined', 'jet_pt', 'jet_corr_pt', 'jet_eta', 'jet_phi', 'jet_mass', 'jet_energy', 'jet_looseId', 'jet_qgl', 'QG_ptD', 'QG_axis2', 'QG_mult', 'y_multiplicity', 'y_charged_multiplicity', 'y_neutral_multiplicity', 'y_ptD', 'y_axis1', 'y_axis2', 'y_pt_dr_log', 'muons_number', 'electrons_number', 'muons_isLooseMuon', 'muons_isTightMuon', 'muons_isSoftMuon', 'muons_isHighPtMuon', 'muons_pt', 'muons_relEta', 'muons_relPhi', 'muons_energy', 'electrons_pt', 'electrons_relEta', 'electrons_relPhi', 'electrons_energy', 'gen_pt_Recluster', 'gen_pt_WithNu', 'Delta_gen_pt_Recluster', 'Delta_gen_pt_WithNu', 'pfCombinedInclusiveSecondaryVertexV2BJetTags', 'pfCombinedMVAV2BJetTags', 'pfDeepCSVJetTags_probb', 'pfDeepCSVJetTags_probbb', 'pfDeepCSVJetTags_probc', 'pfDeepCSVJetTags_probudsg', 'pfJetBProbabilityBJetTags', 'pfJetProbabilityBJetTags', 'softPFElectronBJetTags', 'softPFMuonBJetTags', 'n_Cpfcand', 'nCpfcand', 'Cpfcan_pt', 'Cpfcan_eta', 'Cpfcan_phi', 'Cpfcan_ptrel', 'Cpfcan_erel', 'Cpfcan_phirel', 'Cpfcan_etarel', 'Cpfcan_deltaR', 'Cpfcan_puppiw', 'Cpfcan_dxy', 'Cpfcan_dxyerrinv', 'Cpfcan_dxysig', 'Cpfcan_dz', 'Cpfcan_VTX_ass', 'Cpfcan_fromPV', 'Cpfcan_drminsv', 'Cpfcan_vertex_rho', 'Cpfcan_vertex_phirel', 'Cpfcan_vertex_etarel', 'Cpfcan_BtagPf_trackMomentum', 'Cpfcan_BtagPf_trackEta', 'Cpfcan_BtagPf_trackEtaRel', 'Cpfcan_BtagPf_trackPtRel', 'Cpfcan_BtagPf_trackPPar', 'Cpfcan_BtagPf_trackDeltaR', 'Cpfcan_BtagPf_trackPtRatio', 'Cpfcan_BtagPf_trackPParRatio', 'Cpfcan_BtagPf_trackSip3dVal', 'Cpfcan_BtagPf_trackSip3dSig', 'Cpfcan_BtagPf_trackSip2dVal', 'Cpfcan_BtagPf_trackSip2dSig', 'Cpfcan_BtagPf_trackDecayLen', 'Cpfcan_BtagPf_trackJetDistVal', 'Cpfcan_BtagPf_trackJetDistSig', 'Cpfcan_isMu', 'Cpfcan_isEl', 'Cpfcan_lostInnerHits', 'Cpfcan_numberOfPixelHits', 'Cpfcan_chi2', 'Cpfcan_quality', 'n_Npfcand', 'nNpfcand', 'Npfcan_pt', 'Npfcan_eta', 'Npfcan_phi', 'Npfcan_ptrel', 'Npfcan_erel', 'Npfcan_puppiw', 'Npfcan_phirel', 'Npfcan_etarel', 'Npfcan_deltaR', 'Npfcan_isGamma', 'Npfcan_HadFrac', 'Npfcan_drminsv', 'trackJetPt', 'jetNTracks', 'TagVarCSV_jetNSecondaryVertices', 'TagVarCSV_trackSumJetEtRatio', 'TagVarCSV_trackSumJetDeltaR', 'TagVarCSV_vertexCategory', 'TagVarCSV_trackSip2dValAboveCharm', 'TagVarCSV_trackSip2dSigAboveCharm', 'TagVarCSV_trackSip3dValAboveCharm', 'TagVarCSV_trackSip3dSigAboveCharm', 'n_TagVarCSV_jetNSelectedTracks', 'TagVarCSV_jetNSelectedTracks', 'TagVarCSVTrk_trackPtRel', 'TagVarCSVTrk_trackDeltaR', 'TagVarCSVTrk_trackPtRatio', 'TagVarCSVTrk_trackSip3dSig', 'TagVarCSVTrk_trackSip2dSig', 'TagVarCSVTrk_trackDecayLenVal', 'TagVarCSVTrk_trackJetDistVal', 'n_TagVarCSV_jetNTracksEtaRel', 'TagVarCSV_jetNTracksEtaRel', 'TagVarCSV_trackEtaRel', 'trackPParRatio', 'trackSip2dVal', 'trackSip3dVal', 'trackMomentum', 'trackEta', 'trackPPar', 'n_StoredVertices', 'NStoredVertices', 'TagVarCSV_vertexMass', 'TagVarCSV_vertexNTracks', 'TagVarCSV_vertexEnergyRatio', 'TagVarCSV_vertexJetDeltaR', 'TagVarCSV_flightDistance2dVal', 'TagVarCSV_flightDistance2dSig', 'TagVarCSV_flightDistance3dVal', 'TagVarCSV_flightDistance3dSig']
 


Sample={}
#Sample['bstar'] = { 
#'0500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_500GeV.root',
#'1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_1000GeV.root',
#'2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_2000GeV.root',
#'3000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_3000GeV.root',
#'4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_4000GeV.root',
#'5000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_5000GeV.root',
#'6000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_6000GeV.root',
#'7000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_7000GeV.root',
#'8000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_8000GeV.root',
#'9000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_9000GeV.root',
#}

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

Sample['RSG2qq'] = {
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

Sample['QCD'] = {
'200-300':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD200_300_reduced_skim.root',
'300-500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD300_500_reduced_skim.root',
'500-700':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD500_700_reduced_skim.root',
'700-1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD700_1000_reduced_skim.root',
'1000-1500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD1000_1500_reduced_skim.root',
'1500-2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD1500_2000_reduced_skim.root',
'2000-4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/QCD/QCD2000_Inf_reduced_skim.root',
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

Pt_Range = [30.0,200.0,400.0,600.0,800.0,1000.0,1400.0,1800.0,2200.0,2600.0,3000.0,3500.0,4000.0,5000.0]

def FillHisto(TCHAIN, HISTOLIST):
      for i in VariableList:
	if 'Cpfcan_' in i:
	  for ind in range(TCHAIN.n_Cpfcand):
	    value = getattr(TCHAIN,i)[ind]
	    HISTOLIST[i].Fill(value)

	elif 'muons_' in i and i != 'muons_number':
	  for ind in range(TCHAIN.muons_number):
            value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)
	elif 'electrons_' in i and i != 'electrons_number':
          for ind in range(TCHAIN.electrons_number):
	    value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)

	elif 'sv_' in i:
	  for ind in range(TCHAIN.n_sv):
	    value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)

	elif 'Npfcan_' in i:
	  for ind in range(TCHAIN.n_Npfcand):
            value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)

	elif i=='TagVarCSV_vertexMass' or i == 'TagVarCSV_vertexNTracks' or i == 'TagVarCSV_vertexEnergyRatio' or i == 'TagVarCSV_vertexJetDeltaR' or i =='TagVarCSV_flightDistance2dVal' or i =='TagVarCSV_flightDistance2dSig' or i == 'TagVarCSV_flightDistance3dVal' or i == 'TagVarCSV_flightDistance3dSig' :
          for ind in range(TCHAIN.n_StoredVertices):
            value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)

	elif 'TagVarCSVTrk_' in i or i == 'trackPParRatio' or i=='trackSip2dVal' or i=='trackSip3dVal' or i=='trackMomentum' or i=='trackEta' or i=='trackPPar':
	  for ind in range(len(TCHAIN.TagVarCSVTrk_trackPtRel)):
            value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)

	elif 'TagVarCSV_trackEtaRel' == i:
	  for ind in range(len(TCHAIN.TagVarCSV_trackEtaRel)):
            value = getattr(TCHAIN,i)[ind]
            HISTOLIST[i].Fill(value)

	else:
	    value = getattr(TCHAIN,i)
            HISTOLIST[i].Fill(value)
def ChangeValue(a,po):
  if (a<=0 and po =='up') or (a>=0 and po =='low'):
    return a*0.9
  if (a>=0 and po =='up') or (a<=0 and po =='low'):
    return a*1.1
  return 0


def MakeHisto(HISTOLIST,pre=''):
  INPUT = open('maxmin.txt') 
  temp = {}
  for i in VariableList: 
    temp[i]={}
    temp[i]['up'] = 0
    temp[i]['low']=0
  
  for i in INPUT.readlines():
    if not(i.split()[0] in VariableList):
      continue
    temp[i.split()[0]]['up'] = ChangeValue(float(i.split()[2]),'up')
    temp[i.split()[0]]['low'] = ChangeValue(float(i.split()[1]),'low')

  for i in VariableList:
    HISTOLIST[i] = TH1D(pre+i,pre+i,100,temp[i]['low'],temp[i]['up'])
    HISTOLIST[i].SetTitle(i)

#  return HISTOLIST

if __name__=='__main__':

  histo={}
  histoB={}
  histoC={}
  histoUDSG={}

  histo['all']={}
  histoB['all']={}
  histoC['all']={}
  histoUDSG['all']={}
  for i in Pt_Range[0:-1]:
    histo[i] = {}
    histoB[i] = {}
    histoC[i] = {} 
    histoUDSG[i] = {}

  MakeHisto(histo['all'],'all_')
  MakeHisto(histoB['all'],'allB_')
  MakeHisto(histoC['all'],'allC_')
  MakeHisto(histoUDSG['all'],'allUDSG_') 
  for i in Pt_Range[0:-1]:
    MakeHisto(histo[i],'pT'+str(int(i))+'_')
    MakeHisto(histoB[i],'pT'+str(int(i))+'B_')
    MakeHisto(histoC[i],'pT'+str(int(i))+'C_')
    MakeHisto(histoUDSG[i],'pT'+str(int(i))+'UDSG_')

  tchain = TChain(treename)
  for i in ['QCD']:
    for j,k in Sample[i].items():
      tchain = TChain(treename)
      tchain.Add(k,10000)

      for tt in progressbar(range(tchain.GetEntries()),i+':'+j+':'):
#  for tt in progressbar(range(1000),'Total'):

        tchain.GetEntry(tt) 
      
        FillHisto(tchain,histo['all'])
        if tchain.isB:
          FillHisto(tchain,histoB['all'])
        if tchain.isC:
          FillHisto(tchain,histoC['all'])
#    if tchain.isUD or tchain.isS or tchain.isG:
#      FillHisto(tchain,histoUDSG['all'])

        for ind,pT in enumerate(Pt_Range[0:-1]):
          if pT<tchain.jet_pt<Pt_Range[ind+1]:
            FillHisto(tchain,histo[pT])
            if tchain.isB:
              FillHisto(tchain,histoB[pT])
            if tchain.isC:
              FillHisto(tchain,histoC[pT])
#        if tchain.isUD or tchain.isS or tchain.isG:
#          FillHisto(tchain,histoUDSG[pT])

  outcome = TFile('out_QCD.root','recreate')
  for j in VariableList:
    for i in Pt_Range[0:-1]+['all']:
      histo[i][j].Write()
      histoB[i][j].Write()
      histoC[i][j].Write()
  outcome.Close()
    
  
