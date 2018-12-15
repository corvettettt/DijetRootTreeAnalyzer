import sys,os
from optparse import OptionParser
from ROOT import *

if __name__=='__main__':
  parser = OptionParser()

  parser.add_option('-b','--box',dest="box",default="./",type="string",help="box name")
  parser.add_option('-f','--fit_dir',dest="fit_dir", default="",type="string", help="Folder which stores Fit Result")
  parser.add_option('-m','--model',dest="model", default="",type="string", help="model")
  parser.add_option('-o','--out_dir',dest="out_dir", default="",type="string", help="Folder which stores limit")
  parser.add_option('-s','--signal',dest="signal", default="",type="string", help="Nominal root file place")
  parser.add_option('-p','--printout',dest="printout", default="",type="string", help="expected or observed")
  
  (options,args) = parser.parse_args()

  signal=options.signal
  model = options.model
  out_dir=options.out_dir+''
  fit_dir=options.fit_dir+''
  box=options.box
  Print = options.printout

  content = '#!/bin/bash\n\n'
 
  os.system('mkdir fits_2018_10')
  os.system('mkdir fits_2018_10/'+fit_dir)
  os.system('mkdir '+out_dir)

  content += 'python python/BinnedFit.py -c config/dijet.config -l 36000 -m '+model+' -s '+signal+' inputs/JetHT_run2016_red_cert_scan.root -b '+box+' -d fits_2018_10/'+fit_dir+' --fit-spectrum\n\n'
  content += 'python python/RunCombine_I_btag.py -m '+model+' -d '+out_dir+' --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/'+fit_dir+'/DijetFitResults_'+box+'.root -b '+box+' --rMax 20 --xsec 1e-3 -l 36.000 --no-signal-sys\n\n'
  content += 'python python/GetCombine.py -d '+out_dir+'/ -m '+model+' --mass range\(1600,7000,100\) -b '+box+' --xsec 1e-3 -l 36.000\n\n'
  content += 'python python/Plot1DLimit.py -o '+Print+' -d '+out_dir+'/ -m '+model+' -b '+box+' -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2\n\n'

  os.system('python python/BinnedFit.py -c config/dijet.config -l 36000 -m '+model+' -s '+signal+' inputs/JetHT_run2016_red_cert_scan.root -b '+box+' -d fits_2018_10/'+fit_dir+' --fit-spectrum')
  os.system('python python/RunCombine_I_btag.py -m '+model+' -d '+out_dir+' --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2018_10/'+fit_dir+'/DijetFitResults_'+box+'.root -b '+box+' --rMax 20 --xsec 1e-3 -l 36.000 --no-signal-sys')
  os.system('python python/GetCombine.py -d '+out_dir+'/ -m '+model+' --mass range\(1600,7000,100\) -b '+box+' --xsec 1e-3 -l 36.000') 
  os.system('python python/Plot1DLimit.py -o '+Print+' -d '+out_dir+'/ -m '+model+' -b '+box+' -l 36.000 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2')

  excute_out = open(box+'.sh','w+')
  excute_out.write(content)
  excute_out.close()

  os.system('chmod 751 '+box+'.sh')
  os.system('mv '+box+'.sh /afs/cern.ch/work/z/zhixing/private/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/ExucteCommandBox') 
