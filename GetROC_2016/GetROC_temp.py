from ROOT import *
import sys
from optparse import OptionParser
import array

def progressbar(it, prefix="", size=60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()

sampleNames_qg = {
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_1000_20180701_054551_0_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_2000_20180701_054603_0_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_3000_20180701_054616_0_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_4000_20180701_054628_0_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_5000_20180701_054641_0_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_6000_20180701_054653_0_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_7000_20180701_054706_0_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_8000_20180701_054718_0_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2016JetHT_reduced/Bstar2GQ/rootfile_list_Bstar2GQ_9000_20180701_054731_0_reduced_skim.root',
}
if '__main__'==__name__:
    parser = OptionParser()
    parser.add_option('-i','--Input',dest="Input",type="string",default="none",
                      help="Name of the signal flavour")
    parser.add_option('-o','--Output',dest="Output",type="string",default="non",
                      help="Name of the signal model")
    (options,args) = parser.parse_args()
    Input = options.Input
    Output  = options.Output
    flist = open(Input)

    L = [1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152]

    csv_list = [0.05,0.1,0.15,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5,0.55,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9,0.95,0.9693]

    h_mjj = TH1F('total','total',len(L)-1,1246,8152)

    tchain = TChain('rootTupleTree/tree')
    for i in flist.readlines():
        tchain.Add(i.replace('\n','').replace('\t',''))
    nEntries = tchain.GetEntries()

    N_all={}
    N_pass={}
    ratio = {}
    for i in range(len(L)-3):
      N_all[i] = {}
      N_pass[i] = {}
      ratio[i] = {}
      for j in ['1','2','0','le1']:
        N_all[i][j]  = {}
        N_pass[i][j] = {}
        ratio[i][j] = {}
        for k in csv_list:
           N_all[i][j][k] = 0
	   N_pass[i][j][k] = 0
	   ratio[i][j][k] = 0 
    for t in range(2000):#nEntries):#in progressbar(range(nEntries), 'Progress: ', 40):
#    for t in range(200):
      tchain.GetEntry(t)   

      if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                #tchain.pTWJ_j1<6500              and
                tchain.pTWJ_j2>30                and
                #tchain.pTWJ_j2<6500              and

                #tchain.mjj > 1246                and
                #tchain.mjj < 14000               and

                tchain.PassJSON):
            continue

      for i in csv_list:
         N_csv = 0
         N_dcsv = 0
         if tchain.jetCSVAK4_j1 > i:
	   N_csv +=1
         if tchain.jetCSVAK4_j2 > i:
           N_csv +=1
         if tchain.jetDeepCSVAK4_j1 > i:
           N_dcsv +=1
         if tchain.jetDeepCSVAK4_j2 > i:
           N_dcsv +=1

         for j in range(len(L)-3):
    	  if L[j]<tchain.mjj<L[j+3]:
	    N_all[j]['0'][i]+=1
	    if N_csv == 0:
	      N_pass[j]['0'][i]+=1
            if N_csv > 0:
              N_pass[j]['le1'][i]+=1
            if N_csv == 1:
              N_pass[j]['1'][i]+=1
            if N_csv == 2:
              N_pass[j]['2'][i]+=1

    for i in range(len(L)-3): 
      for j in ['1','2','0','le1']:
        for k in csv_list:
	  if N_all[i][j][k] == 0:
	    ratio[i][j][k] = 0
	    continue
	  ratio[i][j][k] = N_pass[i][j][k]/N_all[i][j][k]
    Ls = []
    Ls = []
    Fout = TFile(Output,'recreate')
    for i in range(len(L)-3):
      for j in ['1','2','0','le1']:
	Ls=[]
        for k in csv_list:    
           Ls.append(ratio[i][j][k])
	Ls_a = array.array('d',Ls) 
	ListCSV = array.array('d',csv_list)
        gr = TGraph(len(csv_list),ListCSV,Ls_a)
        gr.SetTitle('rate of '+j+'bin mass range '+str(L[i])+'-'+str(L[i+3]) )
        gr.GetXaxis().SetTitle('CSV')
        gr.GetYaxis().SetTitle('Efficiency')
        gr.SetName('RateOf'+j+'Mass'+str(L[i])+'-'+str(L[i+3]))
	gr.Write()
    Fout.Close()
#    for i in csv_list:
#      Fin = TFile('signalHistos_bg_'+str(int(i*1000)))
#      rate_0=Fin.Get('g_0btag_rate')
#      rate_le1=Fin.Get('g_le1btag_rate')
#      rate_1=Fin.Get('g_1btag_rate')
#      rate_2=Fin.Get('g_2btag_rate')


      
