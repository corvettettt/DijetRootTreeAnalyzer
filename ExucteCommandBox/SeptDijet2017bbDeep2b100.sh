#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_Aug_ForScan_deep_2b//ResonanceShapes_qq_bb_13TeV_Spring16_100_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b SeptDijet2017bbDeep2b100 -d fits_2018_08/SeptDijet2017bbDeep2b100Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_SeptDijet2017bbDeep2b100_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_08/SeptDijet2017bbDeep2b100Scan/DijetFitResults_SeptDijet2017bbDeep2b100.root -b SeptDijet2017bbDeep2b100 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_SeptDijet2017bbDeep2b100_scan_ns/ -m qq --mass range\(1600,7000,100\) -b SeptDijet2017bbDeep2b100 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_SeptDijet2017bbDeep2b100_scan_ns/ -m qq -b SeptDijet2017bbDeep2b100 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

