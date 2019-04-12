#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 36000 -m qg -s signalHistos_bg_Jan_For2016Scan_deep_central_le1b/ResonanceShapes_qg_bg_13TeV_Spring16_L_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b PFNo13Dijet2016bgdeeple1bL -d fits_2018_10/PFNo13Dijet2016bgdeeple1bLScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo13Dijet2016bgdeeple1bL_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo13Dijet2016bgdeeple1bLScan/DijetFitResults_PFNo13Dijet2016bgdeeple1bL.root -b PFNo13Dijet2016bgdeeple1bL --rMax 20 --xsec 1e-3 -l 36.000

python python/GetCombine.py -d cards_PFNo13Dijet2016bgdeeple1bL_scan/ -m qg --mass range\(1600,7000,100\) -b PFNo13Dijet2016bgdeeple1bL --xsec 1e-3 -l 36.000

python python/Plot1DLimit.py -o exp -d cards_PFNo13Dijet2016bgdeeple1bL_scan/ -m qg -b PFNo13Dijet2016bgdeeple1bL -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

