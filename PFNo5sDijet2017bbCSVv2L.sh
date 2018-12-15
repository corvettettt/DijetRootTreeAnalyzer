#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_Oct_ForScan_CSVv2_central_2b/ResonanceShapes_qq_bb_13TeV_Spring16_L_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo5sDijet2017bbCSVv2L -d fits_2018_10/PFNo5sDijet2017bbCSVv2LScan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFNo5sDijet2017bbCSVv2L_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo5sDijet2017bbCSVv2LScan/DijetFitResults_PFNo5sDijet2017bbCSVv2L.root -b PFNo5sDijet2017bbCSVv2L --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFNo5sDijet2017bbCSVv2L_scan_ns/ -m qq --mass range\(1600,7000,100\) -b PFNo5sDijet2017bbCSVv2L --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo5sDijet2017bbCSVv2L_scan_ns/ -m qq -b PFNo5sDijet2017bbCSVv2L -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2
