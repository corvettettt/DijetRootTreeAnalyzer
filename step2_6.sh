#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepCSV_le1b -c le1b
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepCSV_le1b
python python/ReScaleInterpolation_2017.py  -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepCSV_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Mar_For2017Scan_CSVv2_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_CSVv2_le1b
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Mar_For2017Scan_CSVv2_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_le1b
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_le1b -c le1b
