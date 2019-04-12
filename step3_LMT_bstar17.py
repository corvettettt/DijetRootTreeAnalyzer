import os

tag = 'PFNo1dDijetYearflavorAlgo'

L = ['signalHistos_bg_Feb_For2017Scan_CSVv2','signalHistos_bg_Feb_For2017Scan_DeepCSV','signalHistos_bg_Feb_For2017Scan_DeepJet']
#L= ['signalHistos_bg_Dec_For2017Scan_deep','signalHistos_bb_Dec_For2017Scan_deep','signalHistos_bb_Dec_For2017Scan_CSVv2','signalHistos_bg_Dec_For2017Scan_CSVv2']
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
    cata = ['Non','1b','le1b','mtb']
  if 'bb' in i:
    model = 'qq'
    flavor='bb'
    cata = ['Non','le1b','2b','mtb']

  if 'CSVv2' in i:
    Algo = 'CSVv2'
  if 'DeepCSV' in i:
    Algo = 'DeepCSV'
  if 'DeepJet' in i:
    Algo = 'DeepJet'

  if '2016' in i:
    Year = '2016'
  else:
    Year = '2017'
  
  for j in cata:
    NewTag = tag.replace('flavor',flavor).replace('model',model).replace('Algo',Algo).replace('Year',Year)
    comm1 = 'python python/bTag_ForScan_LMT'+nobtag+'.py -f '+i+'_central_'+j+' -t '+NewTag+' -m '+model+' -c '+j
    if Year == '2017':
      comm2 = 'python python/excute2_2017_LMT'+ns+'.py -t '+NewTag+j+' -m '+model+' -p exp -F '+i+'_central_'+j 
    if Year == '2016':
      comm2 = 'python python/excute2_2016'+ns+'.py -t '+NewTag+j+' -m '+model+' -p exp -F '+i+'_central_'+j 
    Total+=comm1+'\n\n'
    Comi += comm2+'\n\n'
    if index%1 ==0:
       Com_list.append(Comi)
       Comi = ''
    index = index +1 
index = 0
for i in Com_list:
   if 'mtb' in i:
     continue
   index+=1
   a = open('aloha_'+nobtag+ns+str(index)+'.sh','w+')
   a.write('#!/bin/bash\n\n'+i)
   if 'Non' in i:
     a.write(i.replace('Non','mtb'))
   a.close()
   os.system('chmod 751 aloha_'+nobtag+ns+str(index)+'.sh')
a= open('aloha_'+nobtag+ns+'0.sh','w+')
a.write('#!/bin/bash\n\n'+Total)
a.close()
os.system('chmod 751 aloha_'+nobtag+ns+'0.sh')
