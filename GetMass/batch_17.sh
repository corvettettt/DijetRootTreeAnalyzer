#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_17.txt -o output_17.root
