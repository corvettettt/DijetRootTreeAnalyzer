#!/bin/sh

cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetHighMassEvent/

eval `scramv1 runtime -sh`

python GetMassHighMassEvent.py -i filelist_25.txt -o /tmp/output_25.txt

mv /tmp/output_25.txt .

