#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_MarInter_For2017Scan_DeepJet_central_2b/ResonanceShapes_qq_bb_13TeV_Spring16_250_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo34Dijet2017bbDeepJet2b250 -d fits_2019_02/PFNo34Dijet2017bbDeepJet2b250Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFNo34Dijet2017bbDeepJet2b250_scan --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2019_02/PFNo34Dijet2017bbDeepJet2b250Scan/DijetFitResults_PFNo34Dijet2017bbDeepJet2b250.root -b PFNo34Dijet2017bbDeepJet2b250 --rMax 20 --xsec 1e-3 -l 41.800

python python/GetCombine.py -d cards_PFNo34Dijet2017bbDeepJet2b250_scan/ -m qq --mass range\(1600,7000,100\) -b PFNo34Dijet2017bbDeepJet2b250 --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo34Dijet2017bbDeepJet2b250_scan/ -m qq -b PFNo34Dijet2017bbDeepJet2b250 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

