#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Aug_ForScan_CSVv2_1b//ResonanceShapes_qg_bg_13TeV_Spring16_969_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFDijet2017bgCSVv21b969 -d fits_2018_08/PFDijet2017bgCSVv21b969Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFDijet2017bgCSVv21b969_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_08/PFDijet2017bgCSVv21b969Scan/DijetFitResults_PFDijet2017bgCSVv21b969.root -b PFDijet2017bgCSVv21b969 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFDijet2017bgCSVv21b969_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFDijet2017bgCSVv21b969 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFDijet2017bgCSVv21b969_scan_ns/ -m qg -b PFDijet2017bgCSVv21b969 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

