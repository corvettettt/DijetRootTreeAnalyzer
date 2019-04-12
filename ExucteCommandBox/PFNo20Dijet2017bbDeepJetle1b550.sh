#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_Feb_For2017Scan_DeepJet_le1b/ResonanceShapes_qq_bb_13TeV_Spring16_550_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo20Dijet2017bbDeepJetle1b550 -d fits_2019_02/PFNo20Dijet2017bbDeepJetle1b550Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFNo20Dijet2017bbDeepJetle1b550_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2019_02/PFNo20Dijet2017bbDeepJetle1b550Scan/DijetFitResults_PFNo20Dijet2017bbDeepJetle1b550.root -b PFNo20Dijet2017bbDeepJetle1b550 --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo20Dijet2017bbDeepJetle1b550_scan_ns/ -m qq --mass range\(1600,7000,100\) -b PFNo20Dijet2017bbDeepJetle1b550 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo20Dijet2017bbDeepJetle1b550_scan_ns/ -m qq -b PFNo20Dijet2017bbDeepJetle1b550 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

