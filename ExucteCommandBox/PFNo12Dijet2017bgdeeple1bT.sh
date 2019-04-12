#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Jan_For2017Scan_deep_central_le1b/ResonanceShapes_qg_bg_13TeV_Spring16_T_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo12Dijet2017bgdeeple1bT -d fits_2018_10/PFNo12Dijet2017bgdeeple1bTScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo12Dijet2017bgdeeple1bT_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo12Dijet2017bgdeeple1bTScan/DijetFitResults_PFNo12Dijet2017bgdeeple1bT.root -b PFNo12Dijet2017bgdeeple1bT --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo12Dijet2017bgdeeple1bT_scan/ -m qg --mass range\(1600,7000,100\) -b PFNo12Dijet2017bgdeeple1bT --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo12Dijet2017bgdeeple1bT_scan/ -m qg -b PFNo12Dijet2017bgdeeple1bT -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

