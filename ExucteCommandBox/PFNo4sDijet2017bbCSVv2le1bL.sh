#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qq -s signalHistos_bb_Oct_ForScan_CSVv2_central_le1b//ResonanceShapes_qq_bb_13TeV_Spring16_L_Nominal_Interpolation_rescale.root inputs/JetHT_run2017_red_cert_scan.root -b PFNo4sDijet2017bbCSVv2le1bL -d fits_2018_10/PFNo4sDijet2017bbCSVv2le1bLScan --fit-spectrum

python python/RunCombine_I_btag.py -m qq -d cards_PFNo4sDijet2017bbCSVv2le1bL_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/PFNo4sDijet2017bbCSVv2le1bLScan/DijetFitResults_PFNo4sDijet2017bbCSVv2le1bL.root -b PFNo4sDijet2017bbCSVv2le1bL --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-sys

python python/GetCombine.py -d cards_PFNo4sDijet2017bbCSVv2le1bL_scan_ns/ -m qq --mass range\(1600,7000,100\) -b PFNo4sDijet2017bbCSVv2le1bL --xsec 1e-3 -l 41.800

python python/Plot1DLimit.py -o exp -d cards_PFNo4sDijet2017bbCSVv2le1bL_scan_ns/ -m qq -b PFNo4sDijet2017bbCSVv2le1bL -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

