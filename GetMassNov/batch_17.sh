#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassNov/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_17.txt -o /tmp/output_17.root

mv /tmp/output_17.root .

