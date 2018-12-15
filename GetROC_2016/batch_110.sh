#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetROC_2016/

eval `scramv1 runtime -sh`

python GetROC.py -i filelist_110.txt -o /tmp/ROC_2016_output_110.root

mv /tmp/ROC_2016_output_110.root .

