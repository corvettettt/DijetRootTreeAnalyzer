#!/bin/bash

python python/BinnedFit.py -c config/dijet.config -l 36000 -m  -s  inputs/JetHT_run2016_red_cert_scan.root -b ./ -d fits_2018_09/ --fit-spectrum

python python/RunCombine_I_btag.py -m  -d  --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_09//DijetFitResults_./.root -b ./ --rMax 20 --xsec 1e-3 -l 36.000 --no-signal-sys

python python/GetCombine.py -d / -m  --mass range\(1600,7000,100\) -b ./ --xsec 1e-3 -l 36.000

python python/Plot1DLimit.py -o  -d / -m  -b ./ -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2

