#!/bin/bash

python python/bTag_ForScan_LMT.py -f signalHistos_bg_Mar_For2017Scan_DeepJet_central_Non -t PFNo33dDijet2017bgDeepJet -m qg -c Non

python python/bTag_ForScan_LMT.py -f signalHistos_bg_Mar_For2017Scan_DeepJet_central_1b -t PFNo33dDijet2017bgDeepJet -m qg -c 1b

python python/bTag_ForScan_LMT.py -f signalHistos_bg_Mar_For2017Scan_DeepJet_central_le1b -t PFNo33dDijet2017bgDeepJet -m qg -c le1b

python python/bTag_ForScan_LMT.py -f signalHistos_bb_Mar_For2017Scan_DeepJet_central_Non -t PFNo33dDijet2017bbDeepJet -m qq -c Non

python python/bTag_ForScan_LMT.py -f signalHistos_bb_Mar_For2017Scan_DeepJet_central_le1b -t PFNo33dDijet2017bbDeepJet -m qq -c le1b

python python/bTag_ForScan_LMT.py -f signalHistos_bb_Mar_For2017Scan_DeepJet_central_2b -t PFNo33dDijet2017bbDeepJet -m qq -c 2b

