from ROOT import *


def Modify_JU(Folder):
  content = ''
  content += '            elif box==\'PFDijetbg20161MyBTag060\'\n'
  content += '                 signalSys += \'--jesUp '+Folder+'/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root  --jesDown '+Folder+'/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root\'\n'
  content += '                 signalSys += \' --jerUp '+Folder+'/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root\''
  return content

def Modify_Ds(Folder):
  content=''
  content += '        elif box==\'PFDijetbg20161MyBTag060\':\n'
  content += '                signalDsName = \''+Folder+'/ResonanceShapes_qg_bg_13TeV_Spring16_Interpolation_Norminal_rescale.root\''

  return content 
def Modify_bg(Folder):
  content = ''
  content += '                            \'PFDijetbg2016Scan750\':\'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root\','
  return content 

def Modify_box():
  content = ''
  base = '''[BOXBASE]
variables = ['mjj[1246.,1246.,7866.]','th1x[0,0,44]']

histoName = 'HISTONAME'

variables_range = ['mjj_Low[1246.,7866.]', 'mjj_Blind[1246.,7866.]', 'mjj_High[1246.,7866.]']

combine_parameters = ['Ntot_bkg_BOXBASE[1.e+04]', 'p0_BOXBASE[1]', 'p1_BOXBASE[-14]', 'p2_BOXBASE[13]','p3_BOXBASE[1.2]',
              'sqrts[13000]','BOXBASE_bkg_norm[1]',
              'meff_BOXBASE[-1]','seff_BOXBASE[-1]']

combine_pdfs = ['RooDijetBinPdf::BOXBASE_bkg(th1x,p1_BOXBASE,p2_BOXBASE,p3_BOXBASE,sqrts)',
                "EXPR::BOXBASE_bkg_unbin('p0_BOXBASE*(pow(1-mjj/sqrts,p1_BOXBASE)/pow(mjj/sqrts,p2_BOXBASE+p3_BOXBASE*log(mjj/sqrts)))',mjj,p0_BOXBASE,p1_BOXBASE,p2_BOXBASE,p3_BOXBASE,sqrts)",
                'SUM::extDijetPdf(Ntot_bkg_BOXBASE*BOXBASE_bkg)']

#signal and plotting binning
signal_mjj = [1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866]
signal_th1x = range(0,44+1)'''

  content.replace('BOXBASE',box)
  content.replace('HISTONAME','h_mjj_btagle1_mybtag_75.0')
  return content 

def Edit_RunCombine(file_name,tag,Folder):
  a = open(file_name).read()
  jeu = Modify_JU(Folder)
  si  = Modify_Ds(Folder)
  bg  = Modify_bg(Folder)
  a.replace('#EDITJEU', jeu+'\n\n#EDITJEU')
  a.replace('#EDITSI',  si +'\n\n#EDITSI')
  a.replace('#EDITDATA',bg +'\n\n#EDITBG')
  a.write(file_name)
#'python/RunCombine_I_btag+scan.py')

def Edit_Config(file_name,tag,Folder):
  a = open(file_name).read()
  boxes = Modify_box()
  a.replace('#EDITHERE', boxes+'\n\n#EDITHERE')
  a.write(file_name)

if __name__=='__main__':

    parser = OptionParser()
    parser.add_option('-f','--Folder',dest="folder",type="string",default="none",help="")
    parser.add_option('-b','--box',dest="box",type="string",default="qq",help="boxname")
    (options,args) = parser.parse_args()
    folder = options.folder
    box    = options.tag

    Edit_RunCombine('python/RunCombine_I_btag.py',)
    Edit_Config('config/dijet.config',)
