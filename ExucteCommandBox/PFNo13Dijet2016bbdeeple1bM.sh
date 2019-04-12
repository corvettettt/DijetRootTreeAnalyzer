#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 36000 -m qq -s signalHistos_bb_Jan_For2016Scan_deep_central_le1b/ResonanceShapes_qq_bb_13TeV_Spring16_M_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b PFNo13Dijet2016bbdeeple1bM -d fits_2018_10/PFNo13Dijet2016bbdeeple1bMScan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFNo13Dijet2016bbdeeple1bM_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo13Dijet2016bbdeeple1bMScan/DijetFitResults_PFNo13Dijet2016bbdeeple1bM.root -b PFNo13Dijet2016bbdeeple1bM --rMax 20 --xsec 1e-3 -l 36.000

python python/GetCombine.py -d cards_PFNo13Dijet2016bbdeeple1bM_scan/ -m qq --mass range\(1600,7000,100\) -b PFNo13Dijet2016bbdeeple1bM --xsec 1e-3 -l 36.000

python python/Plot1DLimit.py -o exp -d cards_PFNo13Dijet2016bbdeeple1bM_scan/ -m qq -b PFNo13Dijet2016bbdeeple1bM -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

