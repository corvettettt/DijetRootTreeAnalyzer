#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetROC

eval `scramv1 runtime -sh`

python GetROC.py -i filelist_108.txt -o /tmp/ROC_2017_output_108.root

mv /tmp/ROC_2017_output_108.root .

