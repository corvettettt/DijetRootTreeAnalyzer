
import os,sys
from optparse import OptionParser

if __name__=='__main__':

 
  parser = OptionParser()

  parser.add_option('-t','--tag',dest='tag',type='string',default='none',help='')
  parser.add_option('-m','--model',dest='model',type='string',default='none',help='')
  parser.add_option('-p','--point',dest='point',type='string',default='none',help='')
  parser.add_option('-F','--folder',dest='Folder',type='string',default='none',help='') 

  (options,args) = parser.parse_args()

  if 'Non' in options.tag :
    CSV_Value = [0.1]
  elif '2017' in options.tag:
    CSV_Value = [0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8001,0.8838,0.9693]
  elif '2016' in options.tag:
    CSV_Value = [0.1,0.15,0.2219,0.3,0.35,0.4,0.45,0.5, 0.5426,0.6, 0.6324,0.7,0.75,0.8, 0.8484, 0.8958, 0.9535]

  tag = options.tag
  model = options.model
  point = options.point 
  Folder = options.Folder
  
  if model == 'qq':
    flavor = 'bb'
  elif model == 'qg':
    flavor = 'bg'
  for i in CSV_Value:
#    print('python python/Working2_2016.py -b '+tag+str(int(i*1000))+' -f '+tag+str(int(i*1000))+'Scan -o cards_'+tag+str(int(i*1000))+'_scan_ns -s '+Folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_Nominal_Interpolation_rescale.root -m '+model+' -p ' + point)
    os.system('python python/Working2_2016.py -b '+tag+str(int(i*1000))+' -f '+tag+str(int(i*1000))+'Scan -o cards_'+tag+str(int(i*1000))+'_scan_ns -s '+Folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_Nominal_Interpolation_rescale.root -m '+model+' -p ' + point)