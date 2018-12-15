#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow_2016/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_29.txt -o /tmp/outputt_29.root

mv /tmp/outputt_29.root /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow_2016/

