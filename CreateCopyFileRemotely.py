import os 
import datetime

content = 'import os\nimport datetime\n\n'
now = datetime.datetime.now()
Dir = 'BTag'+str(now.year)+str(now.month)+str(now.day)
content += 'os.system(\'mkdir '+Dir+'\')\n\n'
content += 'os.chdir(\'/Users/zhixingwang/Documents/'+Dir+'/\')\n\n'


for i in os.listdir('.'):

   if 'PFNo5sDijet' in i and 'card' in i : 
     content+= 'os.system(\'mkdir '+i+'\')\n\n'
     content+= 'os.system(\'scp zhixing@lxplus.cern.ch:/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/fits_2018_09/'+i.split('_')[1]+'Scan/fit*.pdf '+i+'\')\n\n'
     content+= 'os.system(\'scp zhixing@lxplus.cern.ch:/afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/'+i+'/*.pdf '+i+'\')\n\n'

f = open('CopyFileRemotely.py','w+')

f.write(content)

f.close()
