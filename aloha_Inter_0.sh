#!/bin/bash

python python/bTag_ForScan_Inter.py -f signalHistos_bb_MarInter_For2017Scan_DeepJet_central_Non -t PFNo35Dijet2017bbDeepJet -m qq -c Non

python python/bTag_ForScan_Inter.py -f signalHistos_bb_MarInter_For2017Scan_DeepJet_central_le1b -t PFNo35Dijet2017bbDeepJet -m qq -c le1b

python python/bTag_ForScan_Inter.py -f signalHistos_bb_MarInter_For2017Scan_DeepJet_central_2b -t PFNo35Dijet2017bbDeepJet -m qq -c 2b

python python/bTag_ForScan_Inter.py -f signalHistos_bg_MarInter_For2017Scan_DeepJet_central_Non -t PFNo35Dijet2017bgDeepJet -m qg -c Non

python python/bTag_ForScan_Inter.py -f signalHistos_bg_MarInter_For2017Scan_DeepJet_central_1b -t PFNo35Dijet2017bgDeepJet -m qg -c 1b

python python/bTag_ForScan_Inter.py -f signalHistos_bg_MarInter_For2017Scan_DeepJet_central_le1b -t PFNo35Dijet2017bgDeepJet -m qg -c le1b

