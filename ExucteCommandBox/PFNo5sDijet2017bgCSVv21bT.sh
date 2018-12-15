#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Oct_ForScan_CSVv2_central_1b/ResonanceShapes_qg_bg_13TeV_Spring16_T_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo5sDijet2017bgCSVv21bT -d fits_2018_10/PFNo5sDijet2017bgCSVv21bTScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo5sDijet2017bgCSVv21bT_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo5sDijet2017bgCSVv21bTScan/DijetFitResults_PFNo5sDijet2017bgCSVv21bT.root -b PFNo5sDijet2017bgCSVv21bT --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFNo5sDijet2017bgCSVv21bT_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo5sDijet2017bgCSVv21bT --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo5sDijet2017bgCSVv21bT_scan_ns/ -m qg -b PFNo5sDijet2017bgCSVv21bT -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

