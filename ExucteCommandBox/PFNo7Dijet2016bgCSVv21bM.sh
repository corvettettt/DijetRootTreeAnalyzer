#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 36000 -m qg -s signalHistos_bg_Oct_For2016Scan_CSVv2_central_1b/ResonanceShapes_qg_bg_13TeV_Spring16_M_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b PFNo7Dijet2016bgCSVv21bM -d fits_2018_09/PFNo7Dijet2016bgCSVv21bMScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo7Dijet2016bgCSVv21bM_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_09/PFNo7Dijet2016bgCSVv21bMScan/DijetFitResults_PFNo7Dijet2016bgCSVv21bM.root -b PFNo7Dijet2016bgCSVv21bM --rMax 20 --xsec 1e-3 -l 36.000

python python/GetCombine.py -d cards_PFNo7Dijet2016bgCSVv21bM_scan/ -m qg --mass range\(1600,7000,100\) -b PFNo7Dijet2016bgCSVv21bM --xsec 1e-3 -l 36.000

python python/Plot1DLimit.py -o exp -d cards_PFNo7Dijet2016bgCSVv21bM_scan/ -m qg -b PFNo7Dijet2016bgCSVv21bM -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2
