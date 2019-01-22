import os

FolderName = 'signalHistos_flavor_Jan_ForYearScan_Algo'
cata = []

TComm = []
for a in ['bb','bg']:
  for b in ['2016','2017']:
    for c in ['CSVv2','deep']:
       folder = FolderName.replace('flavor',a).replace('Year',b).replace('Algo',c)
       name=[]
       for i in ['']:
         if 'bg' in folder:
           cata = ['Non','1b','le1b']
         if 'bb' in folder:
           cata = ['Non','2b','le1b']
         for j in cata:
           print('cp -r '+folder+i+' '+folder+i+'_'+j)
           os.system('cp -r '+folder+i+' '+folder+i+'_'+j)
           name.append(folder+i+'_'+j)
       
       for i in name:
	 comm = ''
         if '2016' in i:
            py = 'python/bTag_extractShapes_Interpolater_scan_2016.py'
            py2 = 'python/ReScaleInterpolation_2016.py '
       
         else:
            py = 'python/bTag_extractShapes_Interpolater_scan_2017.py'
            py2 = 'python/ReScaleInterpolation_2017.py '
       
       #  for j in ['up','central','down']:
       #    if j in i:
       #      py = py.replace('CEN',j)
       
         if 'bb' in i:
           add1 = ' qq '
         if 'bg' in i:
           add1 = ' qg '
       
	 comm += 'python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1] + '\n'
         comm += 'python python/extract.py -m '+add1+' -i '+i + '\n'
         comm += 'python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1] + '\n\n'
	 TComm.append(comm)

         #print('python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1])
         #os.system('python '+py+' -m '+add1+'-e '+i+' -c '+i.split('_')[-1])
       
         #print('python python/extract.py -m '+add1+' -i '+i)
         #os.system('python python/extract.py -m '+add1+' -i '+i)
       
         #print('python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1])
         #os.system('python '+py2+' -m '+add1+' -F '+i+' -c '+i.split('_')[-1])

excution = 4 
command = {}
for i in range(excution):
  command[i] = '#!/bin/bash\n\n'
for i,j in enumerate(TComm):
  command[i%excution] += j

for i in range(excution):
  cc = open('step2_%d.sh'%(i+1),'w+')
  cc.write(command[i])
  cc.close()
  os.system('chmod 751 step2_%d.sh'%(i+1))
