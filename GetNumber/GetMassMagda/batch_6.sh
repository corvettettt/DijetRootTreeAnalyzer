#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetNumber/GetMassMagda

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_6.txt -o output_6.root

