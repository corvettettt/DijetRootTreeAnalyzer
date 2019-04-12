import os 
import datetime

now = datetime.datetime.now()
Dir = 'BTag'+str(now.year)+str(now.month)+str(now.day)

os.system('mkdir '+Dir)
os.chdir(Dir)

for i in os.listdir('..'):
#  if 'Efficiency' in i:
#    os.system('mkdir '+i)
#    os.system('cp ../'+i+'/*pdf '+ i)
#  continue
#  if 'GetMass' == i or 'GetMass_2016'==i:
#    os.system('mkdir '+i)
#    os.system('cp ../'+i+'/*pdf '+ i)
  if 'signalHistos' in i and 'Mar' in i:
    os.system('mkdir '+i)
    os.system('cp ../'+i+'/tag*pdf '+ i)
  if 'cards' in i and 'No33d' in i or 'No34D' in i and not ('CSVv2' in i or 'DeepCSV' in i):
    os.system('mkdir '+i)
    os.system('cp ../fits_2019_02/'+i.split('_')[1]+'Scan/fit*.pdf '+i+'/')
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
