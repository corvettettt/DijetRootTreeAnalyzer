from ROOT import *
import sys,os

VariableList = ['n_sv', 'nsv', 'sv_pt', 'sv_eta', 'sv_phi', 'sv_etarel', 'sv_phirel', 'sv_deltaR', 'sv_mass', 'sv_ntracks', 'sv_chi2', 'sv_ndf', 'sv_normchi2', 'sv_dxy', 'sv_dxyerr', 'sv_dxysig', 'sv_d3d', 'sv_d3derr', 'sv_d3dsig', 'sv_costhetasvpv', 'sv_enratio', 'npv', 'rho', 'ntrueInt', 'event_no', 'jet_no', 'gen_pt', 'Delta_gen_pt', 'isB', 'isGBB', 'isBB', 'isLeptonicB', 'isLeptonicB_C', 'isC', 'isGCC', 'isCC', 'isUD', 'isS', 'isG', 'isUndefined', 'genDecay', 'isPhysB', 'isPhysGBB', 'isPhysBB', 'isPhysLeptonicB', 'isPhysLeptonicB_C', 'isPhysC', 'isPhysGCC', 'isPhysCC', 'isPhysUD', 'isPhysS', 'isPhysG', 'isPhysUndefined', 'jet_pt', 'jet_corr_pt', 'jet_eta', 'jet_phi', 'jet_mass', 'jet_energy', 'jet_looseId', 'jet_qgl', 'QG_ptD', 'QG_axis2', 'QG_mult', 'y_multiplicity', 'y_charged_multiplicity', 'y_neutral_multiplicity', 'y_ptD', 'y_axis1', 'y_axis2', 'y_pt_dr_log', 'muons_number', 'electrons_number', 'muons_isLooseMuon', 'muons_isTightMuon', 'muons_isSoftMuon', 'muons_isHighPtMuon', 'muons_pt', 'muons_relEta', 'muons_relPhi', 'muons_energy', 'electrons_pt', 'electrons_relEta', 'electrons_relPhi', 'electrons_energy', 'gen_pt_Recluster', 'gen_pt_WithNu', 'Delta_gen_pt_Recluster', 'Delta_gen_pt_WithNu', 'pfCombinedInclusiveSecondaryVertexV2BJetTags', 'pfCombinedMVAV2BJetTags', 'pfDeepCSVJetTags_probb', 'pfDeepCSVJetTags_probbb', 'pfDeepCSVJetTags_probc', 'pfDeepCSVJetTags_probudsg', 'pfJetBProbabilityBJetTags', 'pfJetProbabilityBJetTags', 'softPFElectronBJetTags', 'softPFMuonBJetTags', 'n_Cpfcand', 'nCpfcand', 'Cpfcan_pt', 'Cpfcan_eta', 'Cpfcan_phi', 'Cpfcan_ptrel', 'Cpfcan_erel', 'Cpfcan_phirel', 'Cpfcan_etarel', 'Cpfcan_deltaR', 'Cpfcan_puppiw', 'Cpfcan_dxy', 'Cpfcan_dxyerrinv', 'Cpfcan_dxysig', 'Cpfcan_dz', 'Cpfcan_VTX_ass', 'Cpfcan_fromPV', 'Cpfcan_drminsv', 'Cpfcan_vertex_rho', 'Cpfcan_vertex_phirel', 'Cpfcan_vertex_etarel', 'Cpfcan_BtagPf_trackMomentum', 'Cpfcan_BtagPf_trackEta', 'Cpfcan_BtagPf_trackEtaRel', 'Cpfcan_BtagPf_trackPtRel', 'Cpfcan_BtagPf_trackPPar', 'Cpfcan_BtagPf_trackDeltaR', 'Cpfcan_BtagPf_trackPtRatio', 'Cpfcan_BtagPf_trackPParRatio', 'Cpfcan_BtagPf_trackSip3dVal', 'Cpfcan_BtagPf_trackSip3dSig', 'Cpfcan_BtagPf_trackSip2dVal', 'Cpfcan_BtagPf_trackSip2dSig', 'Cpfcan_BtagPf_trackDecayLen', 'Cpfcan_BtagPf_trackJetDistVal', 'Cpfcan_BtagPf_trackJetDistSig', 'Cpfcan_isMu', 'Cpfcan_isEl', 'Cpfcan_lostInnerHits', 'Cpfcan_numberOfPixelHits', 'Cpfcan_chi2', 'Cpfcan_quality', 'n_Npfcand', 'nNpfcand', 'Npfcan_pt', 'Npfcan_eta', 'Npfcan_phi', 'Npfcan_ptrel', 'Npfcan_erel', 'Npfcan_puppiw', 'Npfcan_phirel', 'Npfcan_etarel', 'Npfcan_deltaR', 'Npfcan_isGamma', 'Npfcan_HadFrac', 'Npfcan_drminsv', 'trackJetPt', 'jetNTracks', 'TagVarCSV_jetNSecondaryVertices', 'TagVarCSV_trackSumJetEtRatio', 'TagVarCSV_trackSumJetDeltaR', 'TagVarCSV_vertexCategory', 'TagVarCSV_trackSip2dValAboveCharm', 'TagVarCSV_trackSip2dSigAboveCharm', 'TagVarCSV_trackSip3dValAboveCharm', 'TagVarCSV_trackSip3dSigAboveCharm', 'n_TagVarCSV_jetNSelectedTracks', 'TagVarCSV_jetNSelectedTracks', 'TagVarCSVTrk_trackPtRel', 'TagVarCSVTrk_trackDeltaR', 'TagVarCSVTrk_trackPtRatio', 'TagVarCSVTrk_trackSip3dSig', 'TagVarCSVTrk_trackSip2dSig', 'TagVarCSVTrk_trackDecayLenVal', 'TagVarCSVTrk_trackJetDistVal', 'n_TagVarCSV_jetNTracksEtaRel', 'TagVarCSV_jetNTracksEtaRel', 'TagVarCSV_trackEtaRel', 'trackPParRatio', 'trackSip2dVal', 'trackSip3dVal', 'trackMomentum', 'trackEta', 'trackPPar', 'n_StoredVertices', 'NStoredVertices', 'TagVarCSV_vertexMass', 'TagVarCSV_vertexNTracks', 'TagVarCSV_vertexEnergyRatio', 'TagVarCSV_vertexJetDeltaR', 'TagVarCSV_flightDistance2dVal', 'TagVarCSV_flightDistance2dSig', 'TagVarCSV_flightDistance3dVal', 'TagVarCSV_flightDistance3dSig'] 

treename = 'deepntuplizer/tree'


sample={}
sample['bstar'] = { 
'0500':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_500GeV.root',
'1000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_1000GeV.root',
'2000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_2000GeV.root',
'3000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_3000GeV.root',
'4000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_4000GeV.root',
'5000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_5000GeV.root',
'6000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_6000GeV.root',
'7000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_7000GeV.root',
'8000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_8000GeV.root',
'9000':'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/BTV/bstar/bstar_9000GeV.root',
}

sample['RSG2bb'] = {
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

tchain = TChain(treename)
for i in ['RSG2bb','bstar']:
    for j,k in sample[i].items():
      tchain.Add(k)
      print k
NEntries = tchain.GetEntries()
print NEntries

Min={}
Max={}
for i in VariableList: 
  Min[i]=10000
  Max[i]=-10000

for sam in ['RSG2bb','bstar']:
  for mass,addr in sample[sam].items():
    tchain = TChain(treename)
    tchain.Add(addr,1000)
    for tt in progressbar(range(tchain.GetEntries()),sam+':'+mass+':'): 
      tchain.GetEntry(tt)
  
      for i in VariableList:
	if i !='TagVarCSV_trackEtaRel':
	  continue
	if 'Cpfcan_' in i:
	  for ind in range(tchain.n_Cpfcand):
	    value = getattr(tchain,i)[ind]
	   
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif 'muons_' in i and i != 'muons_number':
	  for ind in range(tchain.muons_number):
            value = getattr(tchain,i)[ind]
 
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif 'electrons_' in i and i != 'electrons_number':
          for ind in range(tchain.electrons_number):
	    value = getattr(tchain,i)[ind]
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif 'sv_' in i:
	  for ind in range(tchain.n_sv):
	    value = getattr(tchain,i)[ind]
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif 'Npfcan_' in i:
	  for ind in range(tchain.n_Npfcand):
            value = getattr(tchain,i)[ind]
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif i=='TagVarCSV_vertexMass' or i == 'TagVarCSV_vertexNTracks' or i == 'TagVarCSV_vertexEnergyRatio' or i == 'TagVarCSV_vertexJetDeltaR' or i =='TagVarCSV_flightDistance2dVal' or i =='TagVarCSV_flightDistance2dSig' or i == 'TagVarCSV_flightDistance3dVal' or i == 'TagVarCSV_flightDistance3dSig' :
          for ind in range(tchain.n_StoredVertices):
            value = getattr(tchain,i)[ind]
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif 'TagVarCSVTrk_' in i or i == 'trackPParRatio' or i=='trackSip2dVal' or i=='trackSip3dVal' or i=='trackMomentum' or i=='trackEta' or i=='trackPPar':
	  for ind in range(len(tchain.TagVarCSVTrk_trackPtRel)):
            value = getattr(tchain,i)[ind]
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	elif 'TagVarCSV_trackEtaRel' == i:
	  for ind in range(len(tchain.TagVarCSV_trackEtaRel)):
            value = getattr(tchain,i)[ind]
            if Min[i] >value:
              Min[i] = value 

            if Max[i] < value:
              Max[i] = value 

	else:
          if Min[i] > getattr(tchain,i):
            Min[i] = getattr(tchain,i)

          if Max[i] < getattr(tchain,i):
            Max[i] = getattr(tchain,i)

print '\n\n'
content = ''
for i in VariableList:
  content += i+'   '+str(Min[i])+'   '+str(Max[i])+'\n'

oo = open('maxmin.txt','w+')
oo.write(content)
oo.close()
