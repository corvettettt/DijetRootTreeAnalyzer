#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 36000 -m qg -s signalHistos_bg_Oct_For2016Scan_CSVv2_central_Non/ResonanceShapes_qg_bg_13TeV_Spring16_M_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b PFNo5sDijet2016bgCSVv2NonM -d fits_2018_09/PFNo5sDijet2016bgCSVv2NonMScan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFNo5sDijet2016bgCSVv2NonM_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_09/PFNo5sDijet2016bgCSVv2NonMScan/DijetFitResults_PFNo5sDijet2016bgCSVv2NonM.root -b PFNo5sDijet2016bgCSVv2NonM --rMax 20 --xsec 1e-3 -l 36.000 --no-signal-sys

python python/GetCombine.py -d cards_PFNo5sDijet2016bgCSVv2NonM_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFNo5sDijet2016bgCSVv2NonM --xsec 1e-3 -l 36.000

python python/Plot1DLimit.py -o exp -d cards_PFNo5sDijet2016bgCSVv2NonM_scan_ns/ -m qg -b PFNo5sDijet2016bgCSVv2NonM -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2
