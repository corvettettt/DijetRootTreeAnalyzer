import ROOT
import sys
import os

model='BGenFilter'
f=open('FileList_unfinished.txt')
n=-1
m=0
NumOfFile=1
for line in f.readlines():
  n=n+1
  if n%NumOfFile==0:
    f = open('filelist_%s.txt' % str(m),"w+")
    m=m+1
  f.writelines(line)

f.close()

FinishList = []

for f in os.listdir('.'):
   if not 'outputt' in f:
     continue
   FinishList.append(int(f.replace('outputt_','').replace('.root','')))

#print FinishList

for i in range(m):
  f = open('batch_%s.sh' % str(i),"w+")
  f.writelines("#!/bin/sh\n\n")
  f.writelines("cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass_2016/unfinished/\n\n")
  f.writelines("eval `scramv1 runtime -sh`\n\n")
  f.writelines("python GetMass.py -i filelist_%s.txt -o /tmp/outputt_%s.root\n\n"%(str(i), str(i) ))
  f.writelines("mv /tmp/outputt_%s.root"%(str(i) )+" /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass_2016/unfinished/\n\n")
  f.close()
  if i in FinishList:#+[48,51,58,60,64,67,68,74,91,93,94,97,98,116,117]:
     continue 
  print i
  os.system("chmod 751 batch_%s.sh"%(str(i)))
#  print "bsub -q 1nd -J jobs%s < batch_%s.sh"%(str(i),str(i))
#  os.system('mv filelist_%s.txt ..'str(i))
  os.system("bsub -q 8nh -J jobs%s < batch_%s.sh"%(str(i),str(i)))
##  print "bsub -q 1nh -J jobs%s < %s/batch_%s.sh"%(str(i),model,str(i))
#  print i
#  os.system("mv batch*.sh %s" % model)
#os.system("mv file*.txt %s" % model)
