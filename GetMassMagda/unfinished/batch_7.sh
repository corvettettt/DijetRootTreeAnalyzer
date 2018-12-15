#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass/unfinished/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_7.txt -o /tmp/output_7.root

mv /tmp/output_7.root /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass/unfinished/

