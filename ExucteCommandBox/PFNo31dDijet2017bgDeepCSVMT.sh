#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Mar_For2017Scan_DeepCSV_central_mtb/ResonanceShapes_qg_bg_13TeV_Spring16_MT_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo31dDijet2017bgDeepCSVMT -d fits_2019_02/PFNo31dDijet2017bgDeepCSVMTScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo31dDijet2017bgDeepCSVMT_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2019_02/PFNo31dDijet2017bgDeepCSVMTScan/DijetFitResults_PFNo31dDijet2017bgDeepCSVMT.root -b PFNo31dDijet2017bgDeepCSVMT --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo31dDijet2017bgDeepCSVMT_scan/ -m qg --mass range\(1600,7000,100\) -b PFNo31dDijet2017bgDeepCSVMT --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo31dDijet2017bgDeepCSVMT_scan/ -m qg -b PFNo31dDijet2017bgDeepCSVMT -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

