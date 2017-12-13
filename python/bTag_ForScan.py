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

  if model == 'qq':
    flavor = 'bb'
  if model == 'qg':
    flavor = 'bg'
  CSV_Value = [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.935]
  for i in CSV_Value :
    os.system('python python/bTag_Add.py -u '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_JESUP.root -d '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_JESDOWN.root -r '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_JER.root -n '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_Nominal.root -g inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root -b '+tag+str(int(i*1000))+' -H  h_mjj_btag'+catagory+'_mybtag_'+str(format(i*100,'.1f')))
#    os.system('python python/bTag_Add.py -u '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_JESUP.root -d '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_JESDOWN.root -r '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_JER.root -n '+folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(i*1000))+'_Nominal.root -g inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root -b '+tag+str(int(i*1000))+' -H  h_mjj_btag'+catagory+'_mybtag_'+str(format(i*100,'.1f')))

   
