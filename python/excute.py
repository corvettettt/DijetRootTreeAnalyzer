
import os,sys
from optparse import OptionParser

if __name__=='__main__':

  CSV_Value = [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.935]
 
  parser = OptionParser()

  parser.add_option('-t','--tag',dest='tag',type='string',default='none',help='')
  parser.add_option('-m','--model',dest='model',type='string',default='none',help='')
  parser.add_option('-p','--point',dest='point',type='string',default='none',help='')
  parser.add_option('-F','--folder',dest='Folder',type='string',default='none',help='') 

  (options,args) = parser.parse_args()

  tag = options.tag
  model = options.model
  point = options.point 
  Folder = options.Folder
  
  if model == 'qq':
    flavor = 'bb'
  elif model == 'qg':
    flavor = 'bg'
  for i in CSV_Value:
    print('python python/Working.py -b '+tag+str(int(i*1000))+' -f '+tag+str(int(i*1000))+'Scan -o cards_'+tag+str(int(i*1000))+'_scan -s '+Folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_Nominal_Interpolation_rescale.root -m '+model+' -p ' + point)
    os.system('python python/Working.py -b '+tag+str(int(i*1000))+' -f '+tag+str(int(i*1000))+'Scan -o cards_'+tag+str(int(i*1000))+'_scan -s '+Folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_Nominal_Interpolation_rescale.root -m '+model+' -p ' + point)
