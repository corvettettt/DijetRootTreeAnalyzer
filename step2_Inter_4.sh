#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_Non
python python/ReScaleInterpolation_2017_Inter.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_CSVv2_up_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_CSVv2_up_Non
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_CSVv2_up_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_CSVv2_down_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_CSVv2_down_Non
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_CSVv2_down_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_DeepJet_central_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_DeepJet_central_Non
python python/ReScaleInterpolation_2017_Inter.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_DeepJet_central_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_Non
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_Non
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_CSVv2_central_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_CSVv2_central_Non
python python/ReScaleInterpolation_2017_Inter.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_CSVv2_central_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepJet_up_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepJet_up_Non
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepJet_up_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepJet_down_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepJet_down_Non
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepJet_down_Non -c Non

