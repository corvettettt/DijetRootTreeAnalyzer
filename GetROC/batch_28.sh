#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetROC

eval `scramv1 runtime -sh`

python GetROC.py -i filelist_28.txt -o /tmp/ROC_2017_output_28.root

mv /tmp/ROC_2017_output_28.root .

