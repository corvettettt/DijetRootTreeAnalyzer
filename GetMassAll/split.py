import ROOT
import sys
import os

f=open('FileList.txt')
n=-1
m=0
NumOfFile=3

c = {}
Index = 0
m = -1
for line in f.readlines():
  if Index%NumOfFile == 0:
    m+=1
    c[m]=''
  c[m]+=line
  Index+=1
for i in range(len(c)):
  f=open('filelist_%s.txt' % str(i),"w+")
  f.write(c[i])
  f.close()





FinishList=[]
for f in os.listdir('.'):
   if not 'output' in f:
     continue
   FinishList.append(int(f.replace('output_','').replace('.root','')))

for i in range(m):
  f = open('batch_%s.sh' % str(i),"w+")
  f.writelines("#!/bin/sh\n\n")
  f.writelines("cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMassAll/\n\n")
  f.writelines("eval `scramv1 runtime -sh`\n\n")
  f.writelines("python GetMass.py -i filelist_%s.txt -o /tmp/output_%s.root\n\n"%(str(i), str(i) ))
  f.writelines("mv /tmp/output_%s.root"%str(i)+" .\n\n")
  f.close()
  if i in FinishList:#+[48,51,58,60,64,67,68,74,91,93,94,97,98,116,117]:
     continue
  print i
  os.system("chmod 751 batch_%s.sh"%(str(i)))

#  print "bsub -q 1nd -J jobs%s < batch_%s.sh"%(str(i),str(i))
  os.system("bsub -q 2nd -J jobs%s < batch_%s.sh"%(str(i),str(i)))
#  print "bsub -q 1nh -J jobs%s < %s/batch_%s.sh"%(str(i),model,str(i))

#os.system("mv batch*.sh %s" % model)
#os.system("mv file*.txt %s" % model)
