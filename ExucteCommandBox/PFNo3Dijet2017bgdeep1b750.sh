#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Aug_ForScan_deep_1b//ResonanceShapes_qg_bg_13TeV_Spring16_750_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo3Dijet2017bgdeep1b750 -d fits_2018_09/PFNo3Dijet2017bgdeep1b750Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo3Dijet2017bgdeep1b750_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_09/PFNo3Dijet2017bgdeep1b750Scan/DijetFitResults_PFNo3Dijet2017bgdeep1b750.root -b PFNo3Dijet2017bgdeep1b750 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFNo3Dijet2017bgdeep1b750_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo3Dijet2017bgdeep1b750 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo3Dijet2017bgdeep1b750_scan_ns/ -m qg -b PFNo3Dijet2017bgdeep1b750 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

