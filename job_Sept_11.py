import os

for j in ['deep','CSVv2']:
  for i in ['le1b','1b','Non']:
    print('python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_'+j+'_'+i+'/ -t PFNo2Dijet2017bg'+j+' -m qg -c '+i)
    print('python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_'+j+'_'+i+'/ -t PFNo2Dijet2016bg'+j+' -m qg -c '+i)
  for i in ['le1b','2b','Non']:
    print('python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_'+j+'_'+i+'/ -t PFNo2Dijet2017bb'+j+' -m qq -c '+i)

for j in ['deep','CSVv2']:
  continue

  for i in ['le1b','1b','Non']:
    if os.path.isdir('signalHistos_bg_Aug_ForScan_'+j+'_'+i+'/'):
       os.system('python python/bTag_ForScan.py -f signalHistos_bg_Aug_ForScan_'+j+'_'+i+'/ -t PFNo2Dijet2017bg'+j+' -m qg -c '+i)
    else:
       print('file signalHistos_bg_Aug_ForScan_'+j+'_'+i+' doesn\'t exist')

    if os.path.isdir('signalHistos_bg_Aug_For2016Scan_'+j+'_'+i+'/'):
       os.system('python python/bTag_ForScan.py -f signalHistos_bg_Aug_For2016Scan_'+j+'_'+i+'/ -t PFNo2Dijet2016bg'+j+' -m qg -c '+i)
    else:
       print('file signalHistos_bg_Aug_For2016Scan_'+j+'_'+i+' doesn\'t exist')

  for i in ['le1b','2b','Non']:
    if os.path.isdir('signalHistos_bb_Aug_ForScan_'+j+'_'+i+'/'):
      os.system('python python/bTag_ForScan.py -f signalHistos_bb_Aug_ForScan_'+j+'_'+i+'/ -t PFNo2Dijet2017bb'+j+' -m qq -c '+i)
    else:
       print('file signalHistos_bb_Aug_ForScan_'+j+'_'+i+' doesn\'t exist')
