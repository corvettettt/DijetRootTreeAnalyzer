#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassMagda/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_16.txt -o /tmp/output_16.root

mv /tmp/output_16.root .

