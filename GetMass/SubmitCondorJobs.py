from ROOT import *
from optparse import OptionParser
import os,sys
import datetime


if __name__=='__main__':

  current_time = datetime.datetime.now()

  parser = OptionParser()
  parser.add_option('-o','--outputfile',dest='Ofile',type="string",default="none",help='')
  parser.add_option('-i','--inputfile',dest='Ifile',type='string',default='none')
  parser.add_option('-s','--split',dest='split',type='int',default=35)
  (options,args) = parser.parse_args()
 
  split     = options.split
  OutputFile= options.Ofile
  InputFile = options.Ifile

  FolderName = 'CondorSubmittion_%04d%02d%02d_%02d%02d%02d' % (current_time.year,current_time.month,current_time.day,current_time.hour,current_time.minute,current_time.second)

  os.system('mkdir %s'%FolderName)
  os.system('mkdir %s'%FolderName+'/error')
  os.system('mkdir %s'%FolderName+'/log')
  os.system('mkdir %s'%FolderName+'/output')
  txtfile = open(InputFile)
  content = {}
  contentFull = {}
  for i in range(split):
    content[i]= ''
    contentFull[i] = ''
  for index,line in enumerate(txtfile.readlines()):
    content[index%split] += line.split('/')[-1]
    contentFull[index%split] += line

  for i in range(split):
 
    tmp = open('%s/FileList_%d.txt'%(FolderName,i+1),'w+')
    tmp.write(contentFull[i])
    tmp.close()

    ExcuteFile=open('%s/CondorJob_%d.sh'%(FolderName,i+1),'w+')
    ExcuteFile.write('#!/bin/bash\n\n')

    ExcuteFile.write('''
cd /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/GetMass

eval `scramv1 runtime -sh`

'''+'\n\n')

    ExcuteFile.write('python GetMass.py -i %s -o %s'%('%s/FileList_%d.txt'%(FolderName,i+1),'%s/%s_%d.root'%(FolderName,OutputFile.replace('txt','root'),i+1)))

    #ExcuteFile.write('GetMass.py -i %s -o %s'('23','23'))
    
    ExcuteFile.close()

    os.system('chmod 751 %s/CondorJob_%d.sh'%(FolderName,i+1))

  for i in range(split):
    SubCont = '''+JobFlavour= "tomorrow"
executable = %s
output     = %s/output/$(ClusterId).$(ProcId).out
error      = %s/error/$(ClusterId).$(ProcId).err
log        = %s/log/$(ClusterId).$(ProcId).log

queue'''%('%s/CondorJob_%d.sh'%(FolderName,i+1),FolderName,FolderName,FolderName)

    submition = open('%s/Sub_%d.sub'%(FolderName,i+1),'w+')
    submition.write(SubCont)
    submition.close()

  for i in range(split):
    print 'condor_submit %s/Sub_%d.sub'%(FolderName,i+1)
    os.system('condor_submit %s/Sub_%d.sub'%(FolderName,i+1))
