#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_Aug_ForScan_CSVv2_2b//ResonanceShapes_qq_bb_13TeV_Spring16_895_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFDijet2017bbCSVv22b895 -d fits_2018_08/PFDijet2017bbCSVv22b895Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFDijet2017bbCSVv22b895_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_08/PFDijet2017bbCSVv22b895Scan/DijetFitResults_PFDijet2017bbCSVv22b895.root -b PFDijet2017bbCSVv22b895 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFDijet2017bbCSVv22b895_scan_ns/ -m qq --mass range\(1600,7000,100\) -b PFDijet2017bbCSVv22b895 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFDijet2017bbCSVv22b895_scan_ns/ -m qq -b PFDijet2017bbCSVv22b895 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

