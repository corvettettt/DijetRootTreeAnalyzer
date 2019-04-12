#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepCSV_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepCSV_Non
python python/ReScaleInterpolation_2017.py  -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepCSV_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Mar_For2017Scan_CSVv2_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_CSVv2_Non
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Mar_For2017Scan_CSVv2_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_Non
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_Non -c Non

