#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2016.py -m  qq -e signalHistos_bb_Jan_For2016Scan_deep_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_Jan_For2016Scan_deep_Non
python python/ReScaleInterpolation_2016.py  -m  qq  -F signalHistos_bb_Jan_For2016Scan_deep_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qq -e signalHistos_bb_Jan_For2017Scan_CSVv2_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_Jan_For2017Scan_CSVv2_2b
python python/ReScaleInterpolation_2017.py  -m  qq  -F signalHistos_bb_Jan_For2017Scan_CSVv2_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qq -e signalHistos_bb_Jan_For2017Scan_deep_le1b -c le1b
python python/extract.py -m  qq  -i signalHistos_bb_Jan_For2017Scan_deep_le1b
python python/ReScaleInterpolation_2017.py  -m  qq  -F signalHistos_bb_Jan_For2017Scan_deep_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2016.py -m  qg -e signalHistos_bg_Jan_For2016Scan_deep_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_Jan_For2016Scan_deep_Non
python python/ReScaleInterpolation_2016.py  -m  qg  -F signalHistos_bg_Jan_For2016Scan_deep_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Jan_For2017Scan_CSVv2_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_Jan_For2017Scan_CSVv2_1b
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Jan_For2017Scan_CSVv2_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017.py -m  qg -e signalHistos_bg_Jan_For2017Scan_deep_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_Jan_For2017Scan_deep_le1b
python python/ReScaleInterpolation_2017.py  -m  qg  -F signalHistos_bg_Jan_For2017Scan_deep_le1b -c le1b

