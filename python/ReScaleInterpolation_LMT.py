from ROOT import *
import sys
from optparse import OptionParser
import array

if __name__=='__main__':

  parser = OptionParser()
  parser.add_option('-m','--model',dest='model',type='string',default='none',help='model') 
  parser.add_option('-F','--Folder',dest= 'Folder',type='string',default='none',help='Name of Folder')
  parser.add_option('-c','--cate',dest="cate",type="string",default="le1b",help="category 0b/1b/2b/le1b")
  (options,args) = parser.parse_args()
  model = options.model
  folder = options.Folder
  cate = options.cate
  if model =='qq':
    model2 = 'qq'
    flavor = 'bb'
  if model =='qg':
    flavor = 'bg'
    model2 = 'qg'

#  CSV_Value =  [0.05,0.1,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9693]
  CSV_Value = ['L','M','T']

  mass = [1,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
  Fvalue = [1,1,1,1,1,1,1,1,1,1,1,1]
  m_a = array.array('d',mass)
  Fv_a = array.array('d',Fvalue)
  gr1 = TGraph(len(mass),m_a,Fv_a)

  if cate == 'mtb':
    eff = TFile(folder+'/signalHistos_'+flavor+'_L.root')
    eff_rate=eff.Get('g_'+cate+'tag_rate')

    histo={}
    for j in ['JER','JESUP','JESDOWN','Nominal']:
      rootFile = TFile(folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_MT_'+j+'_Interpolation.root')
      Hlist = rootFile.GetListOfKeys()
      names = [i.GetName() for i in Hlist]

      for i in names:
        histo[i]=rootFile.Get(i)

      for i in names:
        mass = int(i.split('_')[2])
        eff_rate_mass = eff_rate.Eval(mass)
        histo[i].Scale(eff_rate_mass)
 
      output=TFile(folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_MT_'+j+'_Interpolation_rescale.root','recreate')
      for i in names:
        histo[i].Write(i.replace(model2,model))
      output.Close

  else:
   for k in CSV_Value:

    eff = TFile(folder+'/signalHistos_'+flavor+'_'+k+'.root')
    if cate == 'Non':
      eff_rate = eff.Get("g_an_acc") 
    else:
      eff_rate=eff.Get('g_'+cate+'tag_rate')

    histo={}
    for j in ['JER','JESUP','JESDOWN','Nominal']:
      rootFile = TFile(folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+k+'_'+j+'_Interpolation.root')
      Hlist = rootFile.GetListOfKeys()
      names = [i.GetName() for i in Hlist]

      for i in names:
        histo[i]=rootFile.Get(i)

      for i in names:
        mass = int(i.split('_')[2])
        eff_rate_mass = eff_rate.Eval(mass)
        histo[i].Scale(eff_rate_mass)
 
      output=TFile(folder+'/ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+k+'_'+j+'_Interpolation_rescale.root','recreate')
      for i in names:
        histo[i].Write(i.replace(model2,model))
      output.Close
