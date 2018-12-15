#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassAll/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_8.txt -o /tmp/output_8.root

mv /tmp/output_8.root .

