#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassAll/

eval `scramv1 runtime -sh`

python GetMass.py -i filelist_27.txt -o /tmp/output_27.root

mv /tmp/output_27.root .

