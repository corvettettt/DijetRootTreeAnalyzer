#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Aug_ForScan_deep_1b/ResonanceShapes_qg_bg_13TeV_Spring16_700_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFDijet2017bgdeep1b700 -d fits_2018_08/PFDijet2017bgdeep1b700Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFDijet2017bgdeep1b700_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_08/PFDijet2017bgdeep1b700Scan/DijetFitResults_PFDijet2017bgdeep1b700.root -b PFDijet2017bgdeep1b700 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFDijet2017bgdeep1b700_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFDijet2017bgdeep1b700 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFDijet2017bgdeep1b700_scan_ns/ -m qg -b PFDijet2017bgdeep1b700 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

