from ROOT import *
from optparse import OptionParser
import bTag_Add
import os

if __name__=='__main__':
  parser = OptionParser()
  parser.add_option('-f','--folder',dest="folder",type="string",default="none",help="Folder contains all root files.")
  
  parser.add_option('-t','--tag',dest="tag",type="string",default="none",help="tag of the boxes")
  parser.add_option('-m','--model',dest="model",type="string",default="none",help="model")
  parser.add_option('-c','--catagory',dest="catagory",type="string",default="none",help="catagory")
  (options,args) = parser.parse_args()
  folder = options.folder
  tag = options.tag
  model = options.model
  catagory = options.catagory

  if 'CSVv2' in tag:
    tagger = 'CSVv2'
  elif 'DeepCSV' in tag:
    tagger = 'DeepCSV'
  elif 'DeepJet' in tag:
    tagger = 'DeepJet'

  if model == 'qq':
    flavor = 'bb'
  if model == 'qg':
    flavor = 'bg'
#  if '2017' in tag:
#     CSV_Value = {
#   'L':0.1522,
#   'M':0.4941,
#   'T':0.8001
#     }     
#  if '2016' in tag:
#    CSV_Value = {
#   'L':0.2219,
#   'M':0.6324,
#   'T':0.8958
#}
  if catagory =='Non':
    CSV_Value = [0.1]
  elif '2017' in tag: 
    CSV_Value = [0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.8838,0.9,0.9693] 
  elif '2016' in tag:
    CSV_Value = [0.1,0.15,0.2219,0.3,0.35,0.4,0.45,0.5, 0.5426,0.6, 0.6324,0.7,0.75,0.8, 0.8484, 0.8958, 0.9535]

  for i,j in enumerate(CSV_Value) :    
    if '2016' in tag:
         os.system('python python/bTag_Add_2016.py -u '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_JESUP_Interpolation_rescale.root -d '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_JESDOWN_Interpolation_rescale.root -r '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_JER_Interpolation_rescale.root -n '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_Nominal_Interpolation_rescale.root -g inputs/JetHT_run2016_red_cert_scan.root -b '+tag+catagory+str(int(j*1000))+' -H h_mass_passed_'+catagory+'_%s_'%tagger+str(format(j*1000,'.1f'))+' -i '+folder.replace('central','up')+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_Nominal_Interpolation_rescale.root -o '+folder.replace('central','down')+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_Nominal_Interpolation_rescale.root')


    if '2017' in tag:
      os.system('python python/bTag_Add_LMT_2017.py -u '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_JESUP_Interpolation_rescale.root -d '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_JESDOWN_Interpolation_rescale.root -r '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_JER_Interpolation_rescale.root -n '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_Nominal_Interpolation_rescale.root -g inputs/JetHT_run2017_red_cert_scan.root -b '+tag+catagory+str(int(j*1000))+' -H h_mass_passed_'+catagory+'_%s_'%tagger+str(format(j*1000,'.1f'))+' -i '+folder.replace('central','up')+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_Nominal_Interpolation_rescale.root -o '+folder.replace('central','down')+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(j*1000))+'_Nominal_Interpolation_rescale.root')
