#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetNumber/Mine

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_8.txt -o output_8.root

