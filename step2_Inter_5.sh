#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_2b
python python/ReScaleInterpolation_2017_Inter.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_CSVv2_up_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_CSVv2_up_2b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_CSVv2_up_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_CSVv2_down_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_CSVv2_down_2b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_CSVv2_down_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_DeepJet_central_2b -c 2b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_DeepJet_central_2b
python python/ReScaleInterpolation_2017_Inter.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_DeepJet_central_2b -c 2b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_CSVv2_central_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_CSVv2_central_1b
python python/ReScaleInterpolation_2017_Inter.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_CSVv2_central_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepJet_up_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepJet_up_1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepJet_up_1b -c 1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepJet_down_1b -c 1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepJet_down_1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepJet_down_1b -c 1b

