import os

for i in [0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.8838,0.9,0.9693]: 
  cut = str(int(i*1000))
  box = 'PFNo20Dijet2017bgDeepJetle1b'+cut
  os.system('python python/Plot1DLimit.py -d cards_'+box+'_scan_ns/ -m qg -b '+box+' -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2 -o exp')