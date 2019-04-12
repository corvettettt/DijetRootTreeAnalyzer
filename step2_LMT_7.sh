#!/bin/bash

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_central.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_central_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_central_Non
python python/ReScaleInterpolation_LMT.py -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_central_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_up.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_upNon -c Non
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_up_Non
python python/ReScaleInterpolation_LMT_UD.py -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_up_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_down.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepJet_down_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepJet_down_Non
python python/ReScaleInterpolation_LMT_UD.py -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepJet_down_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_down.py -m  qg -e signalHistos_bg_Mar_For2017Scan_DeepJet_down_Non -c Non
python python/extract.py -m  qg  -i signalHistos_bg_Mar_For2017Scan_DeepJet_down_Non
python python/ReScaleInterpolation_LMT_UD.py -m  qg  -F signalHistos_bg_Mar_For2017Scan_DeepJet_down_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_central.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepJet_central_Non -c Non
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepJet_central_Non
python python/ReScaleInterpolation_LMT.py -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepJet_central_Non -c Non

python python/bTag_extractShapes_Interpolater_scan_2017_LMT_up.py -m  qq -e signalHistos_bb_Mar_For2017Scan_DeepJet_upNon -c Non
python python/extract.py -m  qq  -i signalHistos_bb_Mar_For2017Scan_DeepJet_up_Non
python python/ReScaleInterpolation_LMT_UD.py -m  qq  -F signalHistos_bb_Mar_For2017Scan_DeepJet_up_Non -c Non

python python/excute2_2017_LMT.py -t PFNo33dDijet2017bbDeepJetNon -m qq -p exp -F signalHistos_bb_Mar_For2017Scan_DeepJet_central_Non
python python/excute2_2017_LMT.py -t PFNo33dDijet2017bgDeepJetNon -m qg -p exp -F signalHistos_bg_Mar_For2017Scan_DeepJet_central_Non
