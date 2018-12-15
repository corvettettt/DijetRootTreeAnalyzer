#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow_2016/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_144.txt -o /tmp/outputt_144.root

mv /tmp/outputt_144.root /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassLow_2016/

