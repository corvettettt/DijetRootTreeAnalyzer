import ROOT
import sys
import os

model='BGenFilter'
f=open('FileList.txt')
n=-1
m=0
NumOfFile=2
for line in f.readlines():
  n=n+1
  if n%NumOfFile==0:
    f = open('filelist_%s.txt' % str(m),"w+")
    m=m+1
  f.writelines(line)

f.close()


FinishList=[]
for f in os.listdir('.'):
   if not 'ROC_2016_output' in f:
     continue
   FinishList.append(int(f.replace('ROC_2016_output_','').replace('.root','')))

for i in range(m):
  f = open('batch_%s.sh' % str(i),"w+")
  f.writelines("#!/bin/sh\n\n")
  f.writelines("cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetROC_2016/\n\n")
  f.writelines("eval `scramv1 runtime -sh`\n\n")
  f.writelines("python GetROC.py -i filelist_%s.txt -o /tmp/ROC_2016_output_%s.root\n\n"%(str(i), str(i) ))
  f.writelines("mv /tmp/ROC_2016_output_%s.root"%str(i)+" .\n\n")
  f.close()
  if i in FinishList:#+[48,51,58,60,64,67,68,74,91,93,94,97,98,116,117]:    
     continue
  os.system("chmod 751 batch_%s.sh"%(str(i)))
  print i

#  print "bsub -q 1nd -J jobs%s < batch_%s.sh"%(str(i),str(i))
  os.system("bsub -q 8nh -J jobs%s < batch_%s.sh"%(str(i),str(i)))
#  print "bsub -q 1nh -J jobs%s < %s/batch_%s.sh"%(str(i),model,str(i))

#os.system("mv batch*.sh %s" % model)
#os.system("mv file*.txt %s" % model)