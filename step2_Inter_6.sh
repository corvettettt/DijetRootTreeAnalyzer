#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_le1b -c le1b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_le1b
python python/ReScaleInterpolation_2017_Inter.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_DeepCSV_central_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_CSVv2_up_le1b -c le1b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_CSVv2_up_le1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_CSVv2_up_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_CSVv2_down_le1b -c le1b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_CSVv2_down_le1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_CSVv2_down_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qq -e signalHistos_bb_MarInter_For2017Scan_DeepJet_central_le1b -c le1b
python python/extract.py -m  qq  -i signalHistos_bb_MarInter_For2017Scan_DeepJet_central_le1b
python python/ReScaleInterpolation_2017_Inter.py  -m  qq  -F signalHistos_bb_MarInter_For2017Scan_DeepJet_central_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_le1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepCSV_up_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_le1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepCSV_down_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_central.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_CSVv2_central_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_CSVv2_central_le1b
python python/ReScaleInterpolation_2017_Inter.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_CSVv2_central_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_up.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepJet_up_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepJet_up_le1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepJet_up_le1b -c le1b

python python/bTag_extractShapes_Interpolater_scan_2017_Inter_down.py -m  qg -e signalHistos_bg_MarInter_For2017Scan_DeepJet_down_le1b -c le1b
python python/extract.py -m  qg  -i signalHistos_bg_MarInter_For2017Scan_DeepJet_down_le1b
python python/ReScaleInterpolation_2017_Inter_UD.py  -m  qg  -F signalHistos_bg_MarInter_For2017Scan_DeepJet_down_le1b -c le1b

