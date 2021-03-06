#!/bin/bash

python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_deep_le1b/ -t PFNo3Dijet2017bbdeep -m qq -c le1b
python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_deep_2b/ -t PFNo3Dijet2017bbdeep -m qq -c 2b
python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_deep_Non/ -t PFNo3Dijet2017bbdeep -m qq -c Non
python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_CSVv2_le1b/ -t PFNo3Dijet2017bbCSVv2 -m qq -c le1b
python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_CSVv2_2b/ -t PFNo3Dijet2017bbCSVv2 -m qq -c 2b
python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_CSVv2_Non/ -t PFNo3Dijet2017bbCSVv2 -m qq -c Non
python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_deep_le1b/ -t PFNo3Dijet2017bgdeep -m qg -c le1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_deep_1b/ -t PFNo3Dijet2017bgdeep -m qg -c 1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_deep_Non/ -t PFNo3Dijet2017bgdeep -m qg -c Non
python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_CSVv2_le1b/ -t PFNo3Dijet2017bgCSVv2 -m qg -c le1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_CSVv2_1b/ -t PFNo3Dijet2017bgCSVv2 -m qg -c 1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_CSVv2_Non/ -t PFNo3Dijet2017bgCSVv2 -m qg -c Non
python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_deep_le1b/ -t PFNo3Dijet2016bgdeep -m qg -c le1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_deep_1b/ -t PFNo3Dijet2016bgdeep -m qg -c 1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_deep_Non/ -t PFNo3Dijet2016bgdeep -m qg -c Non
python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_CSVv2_le1b/ -t PFNo3Dijet2016bgCSVv2 -m qg -c le1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_CSVv2_1b/ -t PFNo3Dijet2016bgCSVv2 -m qg -c 1b
python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_CSVv2_Non/ -t PFNo3Dijet2016bgCSVv2 -m qg -c Non
