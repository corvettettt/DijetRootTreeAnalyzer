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
#    flist = open(Input)

    L = [1200,1600,2000,2400,2800,3200,3600,4000,4400,4800,5200,5600,6000]

    csv_list =  [0.1,0.15,0.2219,0.3,0.35,0.4,0.45,0.5, 0.5426,0.6, 0.6324,0.7,0.75,0.8, 0.8484, 0.8958, 0.9535]

    h_mjj = TH1F('total','total',len(L)-1,1246,8152)

    tchain = TChain('rootTupleTree/tree')
    for i,j in sampleNames_qg.iteritems():
        tchain.Add(j.replace('\n','').replace('\t',''))
    nEntries = tchain.GetEntries()

    N_all={}
    N_pass_CSV={}
    N_pass_DCSV={}
    ratio_CSV = {}
    ratio_DCSV = {}
    for i in range(len(L)-1):
      N_all[i] = {}
      N_pass_CSV[i] = {}
      N_pass_DCSV[i] = {}
      ratio_CSV[i] = {}
      ratio_DCSV[i] = {}
      for j in ['1','2','0','le1']:
        N_all[i][j]  = {}
        N_pass_CSV[i][j] = {}
        N_pass_DCSV[i][j] = {}
        ratio_CSV[i][j] = {}
        ratio_DCSV[i][j] = {}
        for k in csv_list:
           N_all[i][j][k] = 0
           N_pass_CSV[i][j][k] = 0
           N_pass_DCSV[i][j][k] = 0
           ratio_CSV[i][j][k] = 0
           ratio_DCSV[i][j][k] = 0 
    #for t in range(nEntries):
    for t in progressbar(range(nEntries), 'Progress: ', 40):
#    for t in range(2000):
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

  
         for j in range(len(L)-1):
    	  if L[j]<tchain.mjj<L[j+1]:
	    N_all[j]['0'][i]+=1
	    if N_csv == 0:
	      N_pass_CSV[j]['0'][i]+=1
            if N_csv > 0:
              N_pass_CSV[j]['le1'][i]+=1
            if N_csv == 1:
              N_pass_CSV[j]['1'][i]+=1
            if N_csv == 2:
              N_pass_CSV[j]['2'][i]+=1

	    if N_dcsv == 0:
	      N_pass_DCSV[j]['0'][i]=+1
            if N_dcsv > 0:
              N_pass_DCSV[j]['le1'][i]=+1
            if N_dcsv == 1:
              N_pass_DCSV[j]['1'][i]=+1
            if N_dcsv == 2:
              N_pass_DCSV[j]['2'][i]=+1

	

    for i in range(len(L)-1): 
      for j in ['1','2','0','le1']:
        for k in csv_list:
	  if N_all[i]['0'][k] == 0:
	    ratio_CSV[i][j][k] = 0
	    ratio_DCSV[i][j][k] = 0
	    continue
	  ratio_CSV[i][j][k] = float(N_pass_CSV[i][j][k])/float(N_all[i]['0'][k])
	  ratio_DCSV[i][j][k] = float(N_pass_DCSV[i][j][k])/float(N_all[i]['0'][k])
    Ls = []
    Fout = TFile('Rate.root','recreate')
    ListCSV = array.array('d',csv_list)
    for i in range(len(L)-1):
      for j in ['1','2','0','le1']:
	Ls=[]
        for k in csv_list:    
           Ls.append(ratio_CSV[i][j][k])
	Ls_a = array.array('d',Ls) 
        gr = TGraph(len(csv_list),ListCSV,Ls_a)
        gr.SetTitle('rate of '+j+' CSVv2 bin mass range '+str(L[i])+'-'+str(L[i+1]) )
        gr.GetXaxis().SetTitle('CSVv2')
        gr.GetYaxis().SetTitle('Efficiency')
        gr.SetName('CSVv2RateOf'+j+'Mass'+str(L[i])+'-'+str(L[i+1]))
	gr.Write()

        Ls=[]
        for k in csv_list:
           Ls.append(ratio_DCSV[i][j][k])
        Ls_a = array.array('d',Ls)
        gr1 = TGraph(len(csv_list),ListCSV,Ls_a)
        gr1.SetTitle('rate of '+j+' DeepCSV bin mass range '+str(L[i])+'-'+str(L[i+1]) )
        gr1.GetXaxis().SetTitle('DeepCSV')
        gr1.GetYaxis().SetTitle('Efficiency')
        gr1.SetName('DeepCSVRateOf'+j+'Mass'+str(L[i])+'-'+str(L[i+1]))
        gr1.Write()
    Fout.Close()
#    for i in csv_list:
#      Fin = TFile('signalHistos_bg_'+str(int(i*1000)))
#      rate_0=Fin.Get('g_0btag_rate')
#      rate_le1=Fin.Get('g_le1btag_rate')
#      rate_1=Fin.Get('g_1btag_rate')
#      rate_2=Fin.Get('g_2btag_rate')


      
