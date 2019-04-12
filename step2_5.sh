#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepCSV_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepCSV_2b
python python/ReScaleInterpolation_2017.py  -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepCSV_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Mar_For2017Scan_CSVv2_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_CSVv2_1b
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Mar_For2017Scan_CSVv2_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_1b
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_1b -c 1b

