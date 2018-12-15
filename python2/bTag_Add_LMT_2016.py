from ROOT import *
from optparse import OptionParser

def Modify_JU(box,jesu,jesd,btu,btd,jer):
  content = ''
  content += '            elif box==\''+box+'\':\n'
  content += '                 signalSys += \' --jesUp '+jesu+' --jesDown '+jesd+'\'\n'
  content += '                 signalSys += \' --btagUp '+btu+' --btagDown '+btd+'\'\n'
  content += '                 signalSys += \' --jerUp '+jer+'\''
  
  return content

def Modify_Ds(box,nor):
  content=''
  content += '        elif box==\''+box+'\':\n'
  content += '                signalDsName = \''+nor+'\''
  return content 

def Modify_bg(box,bg):
  content = ''
  content += '                            \''+box+'\':\''+bg+'\','
  return content 

def Modify_box(box,histoname):
  content = ''
  content += '''
[BOXNAME]
variables = ['mjj[1249.,1249.,7866.]','th1x[0,0,44]']

histoName = 'HISTONAME'

variables_range = ['mjj_Low[1249.,7866.]', 'mjj_Blind[1249.,7866.]', 'mjj_High[1249.,7866.]']

combine_parameters = ['Ntot_bkg_BOXNAME[1.e+04]', 'p0_BOXNAME[1]', 'p1_BOXNAME[-14]', 'p2_BOXNAME[13]','p3_BOXNAME[1.2]',
              'sqrts[13000]','BOXNAME_bkg_norm[1]',
              'meff_BOXNAME[-1]','seff_BOXNAME[-1]']
                
combine_pdfs = ['RooDijetBinPdf::BOXNAME_bkg(th1x,p1_BOXNAME,p2_BOXNAME,p3_BOXNAME,sqrts)',
                "EXPR::BOXNAME_bkg_unbin('p0_BOXNAME*(pow(1-mjj/sqrts,p1_BOXNAME)/pow(mjj/sqrts,p2_BOXNAME+p3_BOXNAME*log(mjj/sqrts)))',mjj,p0_BOXNAME,p1_BOXNAME,p2_BOXNAME,p3_BOXNAME,sqrts)",
                'SUM::extDijetPdf(Ntot_bkg_BOXNAME*BOXNAME_bkg)']

#signal and plotting binning 
signal_mjj = [1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866]
signal_th1x = range(0,44+1)
'''
  if 'Non' in box:
    content_r = content.replace('BOXNAME',box).replace('HISTONAME','total')
  else:
    content_r = content.replace('BOXNAME',box).replace('HISTONAME',histoname)
  return content_r 

def Edit_RunCombine(file_name,box,jesu,jesd,btu,btd,jer,nor,bg):
  a = open(file_name).read()
  jeu = Modify_JU(box,jesu,jesd,btu,btd,jer)
  si  = Modify_Ds(box,nor)
  BG  = Modify_bg(box,bg)

  b = a.replace('#EDITJEU',  jeu+'\n\n#EDITJEU').replace('#EDITSI' ,  si +'\n\n#EDITSI').replace('#EDITBG' ,  BG +'\n\n#EDITBG')
  #a.replace('#EDITSI' ,  si +'\n\n#EDITSI')
  #a.replace('#EDITBG' ,  BG +'\n\n#EDITBG')
  Out = open(file_name,'w+')
  Out.write(b)
  Out.close

def Edit_Config(file_name,box,histoname):
  a = open(file_name).read()
  boxes = Modify_box(box,histoname)
  b = a.replace('#EDITHERE', boxes+'\n\n#EDITHERE')
  Out = open(file_name,'w+')
  Out.write(b)
  Out.close

if __name__=='__main__':

    parser = OptionParser()
    parser.add_option('-u','--JesUP',dest="jesu",type="string",default="none",help="Jet energy scale up")
    parser.add_option('-d','--JesDOWN',dest="jesd",type="string",default="none",help="Jet energy scale down")
    parser.add_option('-i','--btagUP',dest="btu",type="string",default="none",help="btag scale up")
    parser.add_option('-o','--btagDOWN',dest="btd",type="string",default="none",help="btag scale down")
    parser.add_option('-r','--jer',dest="jer",type="string",default="none",help="Jet energy resolution")
    parser.add_option('-n','--Nor',dest="nor",type="string",default="none",help="nominal")
    parser.add_option('-g','--BG',dest="bg",type="string",default="none",help="background")
    parser.add_option('-H','--histonName',dest="histoN",type="string",default="none",help="histo name in bg")
    parser.add_option('-b','--box',dest="box",type="string",default="none",help="boxname")
    (options,args) = parser.parse_args()
    box    = options.box
    jesu   = options.jesu
    jesd   = options.jesd
    jer    = options.jer
    nor    = options.nor
    bg     = options.bg
    histoN = options.histoN


    Edit_RunCombine('python/RunCombine_I_btag.py',box,jesu,jesd,options.btu,options.btd,jer,nor,bg)
    Edit_Config('config/dijet.config',box,histoN)
