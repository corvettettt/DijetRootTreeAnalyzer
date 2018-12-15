#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 41800 -m qg -s signalHistos_bg_Aug_For2016Scan_deep_le1b//ResonanceShapes_qg_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root inputs/JetHT_run2016_red_cert_scan.root -b PFDijet2016bgdeeple1b400 -d fits_2018_08/PFDijet2016bgdeeple1b400Scan --fit-spectrum

python python/RunCombine_I_btag.py -m qg -d cards_PFDijet2016bgdeeple1b400_scan_ns --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_08/PFDijet2016bgdeeple1b400Scan/DijetFitResults_PFDijet2016bgdeeple1b400.root -b PFDijet2016bgdeeple1b400 --rMax 20 --xsec 1e-3 -l 41.800 --no-signal-syspython python/GetCombine.py -d cards_PFDijet2016bgdeeple1b400_scan_ns/ -m qg --mass range\(1600,7000,100\) -b PFDijet2016bgdeeple1b400 --xsec 1e-3 -l 41.800python python/Plot1DLimit.py -o exp -d cards_PFDijet2016bgdeeple1b400_scan_ns/ -m qg -b PFDijet2016bgdeeple1b400 -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2