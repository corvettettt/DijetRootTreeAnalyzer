#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetCSV_2016/

eval `scramv1 runtime -sh`

python GetCSV.py -i filelist_8.txt -o /tmp/outputt_8.root

mv /tmp/outputt_8.root .

