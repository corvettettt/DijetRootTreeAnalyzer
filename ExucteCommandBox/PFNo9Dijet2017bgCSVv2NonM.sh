#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Oct_ForScan_CSVv2_central_Non/ResonanceShapes_qg_bg_13TeV_Spring16_M_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo9Dijet2017bgCSVv2NonM -d fits_2018_10/PFNo9Dijet2017bgCSVv2NonMScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo9Dijet2017bgCSVv2NonM_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo9Dijet2017bgCSVv2NonMScan/DijetFitResults_PFNo9Dijet2017bgCSVv2NonM.root -b PFNo9Dijet2017bgCSVv2NonM --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFNo9Dijet2017bgCSVv2NonM_scan/ -m qg --mass range\(1600,7000,100\) -b PFNo9Dijet2017bgCSVv2NonM --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo9Dijet2017bgCSVv2NonM_scan/ -m qg -b PFNo9Dijet2017bgCSVv2NonM -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

