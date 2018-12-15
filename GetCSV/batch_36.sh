#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetCSV/

eval `scramv1 runtime -sh`

python GetCSV.py -i filelist_36.txt -o /tmp/output_36.root

mv /tmp/output_36.root .

