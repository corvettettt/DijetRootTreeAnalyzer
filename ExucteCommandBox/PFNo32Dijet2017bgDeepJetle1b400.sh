#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_MarInter_For2017Scan_DeepJet_le1b/ResonanceShapes_qg_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo32Dijet2017bgDeepJetle1b400 -d fits_2019_02/PFNo32Dijet2017bgDeepJetle1b400Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo32Dijet2017bgDeepJetle1b400_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2019_02/PFNo32Dijet2017bgDeepJetle1b400Scan/DijetFitResults_PFNo32Dijet2017bgDeepJetle1b400.root -b PFNo32Dijet2017bgDeepJetle1b400 --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo32Dijet2017bgDeepJetle1b400_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo32Dijet2017bgDeepJetle1b400 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo32Dijet2017bgDeepJetle1b400_scan_ns/ -m qg -b PFNo32Dijet2017bgDeepJetle1b400 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

