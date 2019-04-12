import ROOT as rt
from rootTools import tdrstyle as setTDRStyle
rt.gROOT.SetBatch()
setTDRStyle.setTDRStyle()

from ROOT import *
import math
import sys,os
import array

VariableList = ['n_sv', 'nsv', 'sv_pt', 'sv_eta', 'sv_phi', 'sv_etarel', 'sv_phirel', 'sv_deltaR', 'sv_mass', 'sv_ntracks', 'sv_chi2', 'sv_ndf', 'sv_normchi2', 'sv_dxy', 'sv_dxyerr', 'sv_dxysig', 'sv_d3d', 'sv_d3derr', 'sv_d3dsig', 'sv_costhetasvpv', 'sv_enratio', 'npv', 'rho', 'ntrueInt', 'event_no', 'jet_no', 'gen_pt', 'Delta_gen_pt', 'isB', 'isGBB', 'isBB', 'isLeptonicB', 'isLeptonicB_C', 'isC', 'isGCC', 'isCC', 'isUD', 'isS', 'isG', 'isUndefined', 'genDecay', 'isPhysB', 'isPhysGBB', 'isPhysBB', 'isPhysLeptonicB', 'isPhysLeptonicB_C', 'isPhysC', 'isPhysGCC', 'isPhysCC', 'isPhysUD', 'isPhysS', 'isPhysG', 'isPhysUndefined', 'jet_pt', 'jet_corr_pt', 'jet_eta', 'jet_phi', 'jet_mass', 'jet_energy', 'jet_looseId', 'jet_qgl', 'QG_ptD', 'QG_axis2', 'QG_mult', 'y_multiplicity', 'y_charged_multiplicity', 'y_neutral_multiplicity', 'y_ptD', 'y_axis1', 'y_axis2', 'y_pt_dr_log', 'muons_number', 'electrons_number', 'muons_isLooseMuon', 'muons_isTightMuon', 'muons_isSoftMuon', 'muons_isHighPtMuon', 'muons_pt', 'muons_relEta', 'muons_relPhi', 'muons_energy', 'electrons_pt', 'electrons_relEta', 'electrons_relPhi', 'electrons_energy', 'gen_pt_Recluster', 'gen_pt_WithNu', 'Delta_gen_pt_Recluster', 'Delta_gen_pt_WithNu', 'pfCombinedInclusiveSecondaryVertexV2BJetTags', 'pfCombinedMVAV2BJetTags', 'pfDeepCSVJetTags_probb', 'pfDeepCSVJetTags_probbb', 'pfDeepCSVJetTags_probc', 'pfDeepCSVJetTags_probudsg', 'pfJetBProbabilityBJetTags', 'pfJetProbabilityBJetTags', 'softPFElectronBJetTags', 'softPFMuonBJetTags', 'n_Cpfcand', 'nCpfcand', 'Cpfcan_pt', 'Cpfcan_eta', 'Cpfcan_phi', 'Cpfcan_ptrel', 'Cpfcan_erel', 'Cpfcan_phirel', 'Cpfcan_etarel', 'Cpfcan_deltaR', 'Cpfcan_puppiw', 'Cpfcan_dxy', 'Cpfcan_dxyerrinv', 'Cpfcan_dxysig', 'Cpfcan_dz', 'Cpfcan_VTX_ass', 'Cpfcan_fromPV', 'Cpfcan_drminsv', 'Cpfcan_vertex_rho', 'Cpfcan_vertex_phirel', 'Cpfcan_vertex_etarel', 'Cpfcan_BtagPf_trackMomentum', 'Cpfcan_BtagPf_trackEta', 'Cpfcan_BtagPf_trackEtaRel', 'Cpfcan_BtagPf_trackPtRel', 'Cpfcan_BtagPf_trackPPar', 'Cpfcan_BtagPf_trackDeltaR', 'Cpfcan_BtagPf_trackPtRatio', 'Cpfcan_BtagPf_trackPParRatio', 'Cpfcan_BtagPf_trackSip3dVal', 'Cpfcan_BtagPf_trackSip3dSig', 'Cpfcan_BtagPf_trackSip2dVal', 'Cpfcan_BtagPf_trackSip2dSig', 'Cpfcan_BtagPf_trackDecayLen', 'Cpfcan_BtagPf_trackJetDistVal', 'Cpfcan_BtagPf_trackJetDistSig', 'Cpfcan_isMu', 'Cpfcan_isEl', 'Cpfcan_lostInnerHits', 'Cpfcan_numberOfPixelHits', 'Cpfcan_chi2', 'Cpfcan_quality', 'n_Npfcand', 'nNpfcand', 'Npfcan_pt', 'Npfcan_eta', 'Npfcan_phi', 'Npfcan_ptrel', 'Npfcan_erel', 'Npfcan_puppiw', 'Npfcan_phirel', 'Npfcan_etarel', 'Npfcan_deltaR', 'Npfcan_isGamma', 'Npfcan_HadFrac', 'Npfcan_drminsv', 'trackJetPt', 'jetNTracks', 'TagVarCSV_jetNSecondaryVertices', 'TagVarCSV_trackSumJetEtRatio', 'TagVarCSV_trackSumJetDeltaR', 'TagVarCSV_vertexCategory', 'TagVarCSV_trackSip2dValAboveCharm', 'TagVarCSV_trackSip2dSigAboveCharm', 'TagVarCSV_trackSip3dValAboveCharm', 'TagVarCSV_trackSip3dSigAboveCharm', 'n_TagVarCSV_jetNSelectedTracks', 'TagVarCSV_jetNSelectedTracks', 'TagVarCSVTrk_trackPtRel', 'TagVarCSVTrk_trackDeltaR', 'TagVarCSVTrk_trackPtRatio', 'TagVarCSVTrk_trackSip3dSig', 'TagVarCSVTrk_trackSip2dSig', 'TagVarCSVTrk_trackDecayLenVal', 'TagVarCSVTrk_trackJetDistVal', 'n_TagVarCSV_jetNTracksEtaRel', 'TagVarCSV_jetNTracksEtaRel', 'TagVarCSV_trackEtaRel', 'trackPParRatio', 'trackSip2dVal', 'trackSip3dVal', 'trackMomentum', 'trackEta', 'trackPPar', 'n_StoredVertices', 'NStoredVertices', 'TagVarCSV_vertexMass', 'TagVarCSV_vertexNTracks', 'TagVarCSV_vertexEnergyRatio', 'TagVarCSV_vertexJetDeltaR', 'TagVarCSV_flightDistance2dVal', 'TagVarCSV_flightDistance2dSig', 'TagVarCSV_flightDistance3dVal', 'TagVarCSV_flightDistance3dSig']

Pt_Range = [30.0,200.0,400.0,600.0,800.0,1000.0,1400.0,1800.0,2200.0,2600.0,3000.0,3500.0,4000.0,5000.0]

def FindMax(lily):
    MAX = {}
    for i in lily:
        MAX[i] = -100000
        for ind in range(100):
            if i.GetBinContent(ind)>MAX[i]:
                MAX[i] = i.GetBinContent(ind)

    Max = max(MAX.values())
    for i in lily:
        if MAX[i] == Max:
            i.DrawNormalized()
    for i in lily:
        if MAX[i] != Max:
            i.DrawNormalized('same')



if __name__=='__main__':

  fin = TFile('out.root')
  os.system('mkdir plotpack')
  for i in [600.0,2600.0,4000.0]:
      os.system('mkdir plotpack/%d'%int(i))
      os.system('mkdir plotpack/%d/ratio'%int(i))
      os.system('mkdir plotpack/overall')

  for i in VariableList:
      for pT in [600.0,2600.0,4000.0]:
          c = TCanvas()
          leg  = TLegend(0.7,0.7,0.9,0.9)
          plotB = fin.Get('pT'+str(int(pT))+'B_'+i)
          plotB.SetLineColor(kRed)
          plotUDSG = fin.Get('pT'+str(int(pT))+'_'+i)
          plotUDSG.SetLineColor(kBlue)
          leg.AddEntry(plotB,'b jet','L')
          leg.AddEntry(plotUDSG,'udsg jet','L')
          lily = [plotB,plotUDSG]
          FindMax(lily)
          leg.Draw('same')
          c.Print('plotpack/'+str(int(pT))+'/%s.pdf'%i)

for i in VariableList:
    x = array.array('d',[])
    y = {}
    gr = {}
    for pT in [600.0,2600.0,4000.0]:
        y[pT] = array.array('d',[])
    for pT in [600.0,2600.0,4000.0]:
        plotB = fin.Get('pT'+str(int(pT))+'B_'+i)
        plotUDSG = fin.Get('pT'+str(int(pT))+'_'+i)
        #plotB.Rebin(10)
        #plotUDSG.Rebin(10)
        for ind in range(100):
            if pT == 600.0:
                x.append(plotB.GetXaxis().GetBinCenter(ind))
            if plotUDSG.GetBinContent(ind) == 0:
                y[pT].append(0)
	    elif plotB.GetEntries() == 0:
	        y[pT].append(0)
            else:
                y[pT].append((plotB.GetBinContent(ind)/plotB.GetEntries())/(plotUDSG.GetBinContent(ind)/plotUDSG.GetEntries()))
        gr[pT] = TGraph(len(x),x,y[pT])
        gr[pT].SetTitle('%s when pT %d-%d'%(i,int(pT),Pt_Range[Pt_Range.index(pT)+1]))
        c = TCanvas()
        gr[pT].Draw('APL')
        c.Print('plotpack/%d/ratio/%s_RatioBoverUDSG.pdf'%(pT,i))

    color = 0
    c = TCanvas()
    leg  = TLegend(0.7,0.7,0.9,0.9)
    for pT in [600.0,2600.0,4000.0]:
        color +=1
        gr[pT].SetLineColor(color)
        if pT ==600.0:
            gr[pT].Draw('APL')
        else:
            gr[pT].Draw('PL,sames')
        leg.AddEntry(gr[pT],'pT %d-%d'%(int(pT),int(Pt_Range[Pt_Range.index(pT)+1])),'L')
    leg.Draw('same')
    c.Print('plotpack/overall/%s.pdf'%i)
