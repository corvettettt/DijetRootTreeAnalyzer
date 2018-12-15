#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassNov/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_29.txt -o /tmp/output_29.root

mv /tmp/output_29.root .

