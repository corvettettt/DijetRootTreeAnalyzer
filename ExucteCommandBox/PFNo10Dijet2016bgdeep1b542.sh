#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 36000 -m qg -s signalHistos_bg_Dec_For2016Scan_deep_1b/ResonanceShapes_qg_bg_13TeV_Spring16_542_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b PFNo10Dijet2016bgdeep1b542 -d fits_2018_10/PFNo10Dijet2016bgdeep1b542Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo10Dijet2016bgdeep1b542_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo10Dijet2016bgdeep1b542Scan/DijetFitResults_PFNo10Dijet2016bgdeep1b542.root -b PFNo10Dijet2016bgdeep1b542 --rMax 20 --xsec 1e-3 -l 36.000

python python/GetCombine.py -d cards_PFNo10Dijet2016bgdeep1b542_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo10Dijet2016bgdeep1b542 --xsec 1e-3 -l 36.000

python python/Plot1DLimit.py -o exp -d cards_PFNo10Dijet2016bgdeep1b542_scan_ns/ -m qg -b PFNo10Dijet2016bgdeep1b542 -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

