#!/bin/bash

python python/bTag_ForScan.py -f signalHistos_bb_MarInter_For2017Scan_DeepJet_Non -t PFNo32Dijet2017bbDeepJet -m qq -c Non

python python/bTag_ForScan.py -f signalHistos_bb_MarInter_For2017Scan_DeepJet_le1b -t PFNo32Dijet2017bbDeepJet -m qq -c le1b

python python/bTag_ForScan.py -f signalHistos_bb_MarInter_For2017Scan_DeepJet_2b -t PFNo32Dijet2017bbDeepJet -m qq -c 2b

python python/bTag_ForScan.py -f signalHistos_bg_MarInter_For2017Scan_DeepJet_Non -t PFNo32Dijet2017bgDeepJet -m qg -c Non

python python/bTag_ForScan.py -f signalHistos_bg_MarInter_For2017Scan_DeepJet_1b -t PFNo32Dijet2017bgDeepJet -m qg -c 1b

python python/bTag_ForScan.py -f signalHistos_bg_MarInter_For2017Scan_DeepJet_le1b -t PFNo32Dijet2017bgDeepJet -m qg -c le1b

