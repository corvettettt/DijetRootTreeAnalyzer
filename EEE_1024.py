import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-F',type='string',default="none",dest='folder',help='folder')
(options,args) = parser.parse_args()
folder = options.folder
name = []
cata = []

for i in ['_up','_central','_down']:
  if 'bg' in folder:
    cata = ['Non','1b','le1b']
  if 'bb' in folder:
    cata = ['Non','2b','le1b']
  for j in cata:
    print('cp -r '+folder+i+' '+folder+i+'_'+j)
    os.system('cp -r '+folder+i+' '+folder+i+'_'+j)
    name.append(folder+i+'_'+j)

for i in name:
  if '2016' in i:
     py = 'python/bTag_extractShapes_Interpolater_scan_2016_LMT_CEN.py'   

  else:
     py = 'python/bTag_extractShapes_Interpolater_scan_2017_LMT_CEN.py' 

  for j in ['up','central','down']:
    if j in i:
      py = py.replace('CEN',j)
 
  if 'central' in i:
    py2 = 'python/ReScaleInterpolation_LMT.py'
  else:
    py2 = 'python/ReScaleInterpolation_LMT_UD.py'

  if 'bb' in i:
    add1 = ' qq '
  if 'bg' in i:
    add1 = ' qg '
  
  print('python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1])
  os.system('python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1])
 
  print('python python/extract.py -m '+add1+' -i '+i)
  os.system('python python/extract.py -m '+add1+' -i '+i)
  
  print('python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1])
  os.system('python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1])
