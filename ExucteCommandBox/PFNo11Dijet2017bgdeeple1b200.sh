#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Dec_For2017Scan_deep_le1b/ResonanceShapes_qg_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo11Dijet2017bgdeeple1b200 -d fits_2018_10/PFNo11Dijet2017bgdeeple1b200Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo11Dijet2017bgdeeple1b200_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo11Dijet2017bgdeeple1b200Scan/DijetFitResults_PFNo11Dijet2017bgdeeple1b200.root -b PFNo11Dijet2017bgdeeple1b200 --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo11Dijet2017bgdeeple1b200_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo11Dijet2017bgdeeple1b200 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo11Dijet2017bgdeeple1b200_scan_ns/ -m qg -b PFNo11Dijet2017bgdeeple1b200 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2
