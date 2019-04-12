import os

#for i in [0.1,0.15,0.2,0.3,0.35,0.45,0.5,0.5803,0.65,0.75,0.8,0.8838,0.9,0.9693]:
#  cut = str(int(i*1000))
#  os.system('python python/Plot1DLimit.py -d cards_PF0bDijet2017Scan'+cut+'_scan_ns/ -m qq -b PF0bDijet2017Scan'+cut+' -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2 -o exp')

for i in ['M','L','T']:
  for j in ['1b','le1b']: 
    tag = 'PFNo1dDijet2017bgDeepJet'+j+i 
    print '\n\t'+tag
    os.system('python python/Plot1DLimit.py -d cards_'+tag+'_scan/ -m qg -b '+tag+' -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2 -o obs')
