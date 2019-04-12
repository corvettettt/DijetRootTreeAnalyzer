#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_down.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_down_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_down_1b
python python/ReScaleInterpolation_LMT_UD.py -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_down_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_central.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepJet_central_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepJet_central_2b
python python/ReScaleInterpolation_LMT.py -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepJet_central_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_up.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepJet_up_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepJet_up_2b
python python/ReScaleInterpolation_LMT_UD.py -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepJet_up_2b -c 2b

