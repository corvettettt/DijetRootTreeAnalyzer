from ROOT import *
import sys
from optparse import OptionParser

if __name__=='__main__':

  parser = OptionParser()
  parser.add_option('-m','--model',dest='model',type='string',default='none',help='model') 
  (options,args) = parser.parse_args()
  model = options.model
  if model =='qq':
    flavor = 'bb'
  if model =='qg':
    flavor = 'bg'

  CSV_Value=[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.46,0.5,0.55,0.60,0.65,0.70,0.75,0.8,0.85,0.9,0.935,0.95]

  for k in CSV_Value:
 
    eff = TFile('signalHistos_'+flavor+'_'+str(int(k*1000))+'.root')
    eff_rate=eff.Get('g_le1btag_rate')

    histo={}
    for j in ['JER','JESUP','JESDOWN','Nominal']:
      rootFile = TFile('ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(k*1000))+'_'+j+'_Interpolation.root')
      Hlist = rootFile.GetListOfKeys()
      names = [i.GetName() for i in Hlist]

      for i in names:
        histo[i]=rootFile.Get(i)

      for i in names:
        mass = int(i.split('_')[2])
        eff_rate_mass = eff_rate.Eval(mass)
        histo[i].Scale(eff_rate_mass)
 
      output=TFile('ResonanceShapes_'+model+'_'+flavor+'_13TeV_Spring16_'+str(int(k*1000))+'_'+j+'_Interpolation_rescale.root','recreate')
      for i in names:
        histo[i].Write()
      output.Close
