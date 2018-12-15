#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow_2016/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_177.txt -o /tmp/outputt_177.root

mv /tmp/outputt_177.root /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow_2016/

