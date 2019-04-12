#!/bin/bash


cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass

eval `scramv1 runtime -sh`



python GetMass.py -i CondorSubmittion_20190213_180314/FileList_19.txt -o CondorSubmittion_20190213_180314/output_19.root