#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Mar_For2017Scan_DeepJet_central_Non/ResonanceShapes_qg_bg_13TeV_Spring16_M_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo33dDijet2017bgDeepJetNonM -d fits_2019_02/PFNo33dDijet2017bgDeepJetNonMScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo33dDijet2017bgDeepJetNonM_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2019_02/PFNo33dDijet2017bgDeepJetNonMScan/DijetFitResults_PFNo33dDijet2017bgDeepJetNonM.root -b PFNo33dDijet2017bgDeepJetNonM --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo33dDijet2017bgDeepJetNonM_scan/ -m qg --mass range\(1600,7000,100\) -b PFNo33dDijet2017bgDeepJetNonM --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo33dDijet2017bgDeepJetNonM_scan/ -m qg -b PFNo33dDijet2017bgDeepJetNonM -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

