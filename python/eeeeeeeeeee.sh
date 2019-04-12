#!/bin/bash

python bTag_signalStudies_scan_DeepJet_2017_WithoutInter.py -f bg -m qg
python bTag_signalStudies_scan_DeepCSV_2017_WithoutInter.py -f bg -m qg
python bTag_signalStudies_scan_CSVv2_2017_WithoutInter.py -f bg -m qg

python bTag_signalStudies_scan_DeepJet_2017_WithoutInter.py -f bb -m qq
python bTag_signalStudies_scan_DeepCSV_2017_WithoutInter.py -f bb -m qq
python bTag_signalStudies_scan_CSVv2_2017_WithoutInter.py -f bb -m qq
