#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Mar_For2017Scan_DeepJet_1b/ResonanceShapes_qg_bg_13TeV_Spring16_303_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo30Dijet2017bgDeepJet1b303 -d fits_2019_02/PFNo30Dijet2017bgDeepJet1b303Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo30Dijet2017bgDeepJet1b303_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2019_02/PFNo30Dijet2017bgDeepJet1b303Scan/DijetFitResults_PFNo30Dijet2017bgDeepJet1b303.root -b PFNo30Dijet2017bgDeepJet1b303 --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo30Dijet2017bgDeepJet1b303_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo30Dijet2017bgDeepJet1b303 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo30Dijet2017bgDeepJet1b303_scan_ns/ -m qg -b PFNo30Dijet2017bgDeepJet1b303 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

