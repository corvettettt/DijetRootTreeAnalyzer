from ROOT import *
import os 

CSV_Value = [0.1,0.15,0.2219,0.3,0.35,0.4,0.45,0.5, 0.5426,0.6, 0.6324,0.7,0.75,0.8, 0.8484, 0.8958, 0.9535]

for i in CSV_Value: 
  os.system('python python/Plot1DLimit.py -o exp -d cards_PFDijet2017bbdeeple1b'+str(int(i*1000))+'_scan_ns/ -m qq -b PFDijet2017bbdeeple1b'+str(int(i*1000))+' -l 41.800 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2')
  
