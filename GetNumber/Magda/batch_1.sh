#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetNumber/Magda

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_1.txt -o output_1.root

