#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Aug_For2016Scan_CSVv2_1b/ResonanceShapes_qg_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b SeptDijet2016bgCSVv21b150 -d fits_2018_08/SeptDijet2016bgCSVv21b150Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_SeptDijet2016bgCSVv21b150_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_08/SeptDijet2016bgCSVv21b150Scan/DijetFitResults_SeptDijet2016bgCSVv21b150.root -b SeptDijet2016bgCSVv21b150 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_SeptDijet2016bgCSVv21b150_scan_ns/ -m qg --mass range\(1600,7000,100\) -b SeptDijet2016bgCSVv21b150 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_SeptDijet2016bgCSVv21b150_scan_ns/ -m qg -b SeptDijet2016bgCSVv21b150 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

