import os 
import datetime

now = datetime.datetime.now()
Dir = 'BTag'+str(now.year)+str(now.month)+str(now.day)

os.system('mkdir '+Dir)
os.chdir(Dir)

for i in os.listdir('..'):
  if 'GetMass' == i or 'GetMass_2016'==i:
    os.system('mkdir '+i)
    os.system('cp ../'+i+'/*pdf '+ i)
  if 'signalHistos' in i and 'Dec' in i:
    os.system('mkdir '+i)
    os.system('cp ../'+i+'/*pdf '+ i)
  if 'PFNo11Dijet'in i or 'PFNo10Dijet' in i or 'PFNo7Dijet' in i or 'PFNo8Dijet' in i and 'card' in i :
    os.system('mkdir '+i)
    os.system('cp ../fits_2018_10/'+i.split('_')[1]+'Scan/fit*.pdf '+i+'/')
    os.system('cp ../'+i+'/*.pdf '+i)

os.chdir('..')

os.system('tar -zcvf '+Dir+'.tar.gz '+Dir)




#content = 'import os\nimport datetime\n\n'
#now = datetime.datetime.now()
#Dir = 'BTag'+str(now.year)+str(now.month)+str(now.day)
#content += 'os.system(\'mkdir '+Dir+'\')\n\n'
##content += 'os.chdir(\'/Users/zhixingwang/Documents/'+Dir+'/\')\n\n'


#for i in os.listdir('.'):

#   if 'PFNo2Dijet' in i and 'card' in i : 
#     content+= 'os.system(\'mkdir '+i+'\')\n\n'
#     content+= 'os.system(\'scp zhixing@lxplus.cern.ch:/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/fits_2018_08/'+i.split('_')[1]+'Scan/fit*.pdf '+i+'\')\n\n'
#     content+= 'os.system(\'scp zhixing@lxplus.cern.ch:/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/'+i+'/*.pdf '+i+'\')\n\n'

#f = open('CopyFileRemotely.py','w+')

#f.write(content)

#f.close()
