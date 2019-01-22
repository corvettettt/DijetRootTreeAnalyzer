import os

tag = 'PFNo12DijetYearflavorAlgo'

L= ['signalHistos_bg_Jan_For2017Scan_deep','signalHistos_bb_Jan_For2017Scan_deep','signalHistos_bb_Jan_For2017Scan_CSVv2','signalHistos_bg_Jan_For2017Scan_CSVv2']
L += ['signalHistos_bg_Jan_For2016Scan_deep','signalHistos_bb_Jan_For2016Scan_deep','signalHistos_bb_Jan_For2016Scan_CSVv2','signalHistos_bg_Jan_For2016Scan_CSVv2']
#L = ['signalHistos_bg_Dec_For2017Scan_deep','signalHistos_bg_Dec_For2016Scan_deep','signalHistos_bg_Dec_For2016Scan_CSVv2','signalHistos_bb_Dec_For2016Scan_deep','signalHistos_bb_Dec_For2017Scan_deep','signalHistos_bb_Dec_For2016Scan_CSVv2','signalHistos_bg_Dec_For2017Scan_CSVv2','signalHistos_bb_Dec_For2017Scan_CSVv2']

ns = ''#'ns'
nobtag= ''#'nobtag'

cata=[]
Com_list=[]
Comi=''
index = 0
Total=''

for i in L:
  if 'bg' in i:
    flavor = 'bg'
    model = 'qg'
    cata = ['Non','1b','le1b']
  if 'bb' in i:
    model = 'qq'
    flavor='bb'
    cata = ['Non','le1b','2b']

  if 'CSVv2' in i:
    Algo = 'CSVv2'
  if 'deep' in i:
    Algo = 'deep'

  if '2016' in i:
    Year = '2016'
  else:
    Year = '2017'
  
  for j in cata:
    NewTag = tag.replace('flavor',flavor).replace('model',model).replace('Algo',Algo).replace('Year',Year)
    comm1 = 'python python/bTag_ForScan'+nobtag+'.py -f '+i+'_'+j+' -t '+NewTag+' -m '+model+' -c '+j
    if Year == '2017':
      comm2 = 'python python/excute2_2017'+ns+'.py -t '+NewTag+j+' -m '+model+' -p exp -F '+i+'_'+j 
    if Year == '2016':
      comm2 = 'python python/excute2_2016'+ns+'.py -t '+NewTag+j+' -m '+model+' -p exp -F '+i+'_'+j 
    Total+=comm1+'\n\n'
    Comi += comm2+'\n\n'
    if index%6 ==0:
       Com_list.append(Comi)
       Comi = ''
    index = index +1 
index = 0
for i in Com_list:
   index+=1
   a = open('aloha_'+nobtag+ns+str(index)+'.sh','w+')
   a.write('#!/bin/bash\n\n'+i)
   a.close()
   os.system('chmod 751 aloha_'+nobtag+ns+str(index)+'.sh')
a= open('aloha_'+nobtag+ns+'0.sh','w+')
a.write('#!/bin/bash\n\n'+Total)
a.close()
os.system('chmod 751 aloha_'+nobtag+ns+'0.sh')
