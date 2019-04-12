import os

FolderName = 'signalHistos_flavor_Feb_ForYearScan_Algo'
cata = []

TComm = []
for a in ['bb']:
  for b in ['2017']:
    for c in ['CSVv2','DeepCSV','DeepJet']:
       folder = FolderName.replace('flavor',a).replace('Year',b).replace('Algo',c)
       name=[]
       for i in ['_up','_central','_down']:
         if 'bg' in folder:
           cata = ['Non','1b','le1b','mtb']
         if 'bb' in folder:
           cata = ['Non','2b','le1b','mtb']
         for j in cata:
           print('cp -r '+folder+i+' '+folder+i+'_'+j)
           os.system('cp -r '+folder+i+' '+folder+i+'_'+j)
           name.append(folder+i+'_'+j)
       print name       
       for i in sorted(name):
	 comm = ''
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
         

	 comm += 'python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1]+'\n'
	 comm += 'python python/extract.py -m '+add1+' -i '+i+'\n'
         comm += 'python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1]+'\n\n'
         TComm.append(comm)

       #  print('python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1])
       #  os.system('python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1])
       
       #  print('python python/extract.py -m '+add1+' -i '+i)
       #  os.system('python python/extract.py -m '+add1+' -i '+i)
       
       #  print('python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1])
       #  os.system('python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1])
excution = 6
command = {}
for i in range(excution):
  command[i] = '#!/bin/bash\n\n'
for i,j in enumerate(TComm):
  command[i%excution] += j

for i in range(excution):
  cc = open('step2_LMT_%d.sh'%(i+1),'w+')
  cc.write(command[i])
  cc.close()
  os.system('chmod 751 step2_LMT_%d.sh'%(i+1))

