from ROOT import *
import sys
import os
import glob
from optparse import OptionParser

if __name__=='__main__': 
  parser = OptionParser()
  parser.add_option('-i','--inputs',dest='inputs',type='string',default='none',help='input file folder')
  parser.add_option('-m','--model',dest='model',type='string',default='none',help='model')
  (options,args) = parser.parse_args()
  folder = options.inputs
  model = options.model 

  cwd=os.getcwd()


  print cwd
  rootfilelist=glob.glob(cwd+'/'+folder+'/ResonanceShapes*.root')
  for i in rootfilelist:
     if 'tepolation' in i:
       continue
     print 'processing '+i
     o = i
     os.system('python python/extractShapes.py -i '+i+' -o '+o.replace('root','py'))

  pyfilelist=glob.glob(cwd+'/'+folder+'/*.py')
  for i in pyfilelist:
    if not ('ResonanceShapes' in i): 
      continue
    o = i
    if 'Interpolation' in i:
       continue
    print 'processs '+i
    os.system('python python/getResonanceShapes.py -i '+i+' -f '+model+' --fineBinning --massrange 1600 9000 100 -o '+o.replace('.py','_Interpolation.root'))

  os.system('rm '+cwd+'/'+folder+'/*.py') 
