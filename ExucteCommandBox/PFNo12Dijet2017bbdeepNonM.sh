#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_Jan_For2017Scan_deep_central_Non/ResonanceShapes_qq_bb_13TeV_Spring16_M_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo12Dijet2017bbdeepNonM -d fits_2018_10/PFNo12Dijet2017bbdeepNonMScan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFNo12Dijet2017bbdeepNonM_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo12Dijet2017bbdeepNonMScan/DijetFitResults_PFNo12Dijet2017bbdeepNonM.root -b PFNo12Dijet2017bbdeepNonM --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo12Dijet2017bbdeepNonM_scan/ -m qq --mass range\(1600,7000,100\) -b PFNo12Dijet2017bbdeepNonM --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo12Dijet2017bbdeepNonM_scan/ -m qq -b PFNo12Dijet2017bbdeepNonM -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

