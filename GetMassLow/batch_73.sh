#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_73.txt -o /tmp/2017_output_73.root

mv /tmp/2017_output_73.root .

