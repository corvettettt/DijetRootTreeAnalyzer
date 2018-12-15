import os

for i in [0.1,0.15,0.2,0.3,0.35,0.45,0.5,0.5803,0.65,0.75,0.8,0.8838,0.9,0.9693]:
  cut = str(int(i*1000))
  box = 'PF2bDijet2017Scan'+cut
  os.system('python python/Plot1DLimit.py -d cards_'+box+'_scan_ns/ -m qq -b '+box+' -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2 -o exp')
