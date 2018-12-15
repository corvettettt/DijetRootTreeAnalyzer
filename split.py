import ROOT
import sys
import os

model='BGenFilter'
f=open('ROOTLIST.txt')
n=-1
m=0
NumOfFile=5
for line in f.readlines():
  n=n+1
  if n%NumOfFile==0:
    f = open('filelist_%s.txt' % str(m),"w+")
    m=m+1
  f.writelines(line)

f.close()

for i in range(m):
  f = open('batch_%s.sh' % str(i),"w+")
  f.writelines("#!/bin/sh\n\n")
  f.writelines("cd /afs/cern.ch/work/z/zhixing/public/CMSSW_7_4_14/src/DijetRootTreeAnalyzer/GetMass/\n\n")
  f.writelines("eval `scramv1 runtime -sh`\n\n")
  f.writelines("python GetMass.py -i filelist_%s.txt -o output_%s.root\n\n"%(str(i), str(i) ))
  f.close()
  os.system("chmod 751 batch_%s.sh"%(str(i)))
#  print "bsub -q 1nd -J jobs%s < batch_%s.sh"%(str(i),str(i))
  os.system("bsub -q 8nh -J jobs%s < batch_%s.sh"%(str(i),str(i)))
#  print "bsub -q 1nh -J jobs%s < %s/batch_%s.sh"%(str(i),model,str(i))

#os.system("mv batch*.sh %s" % model)
#os.system("mv file*.txt %s" % model)
