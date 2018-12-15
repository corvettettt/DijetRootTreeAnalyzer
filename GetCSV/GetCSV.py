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

    CSV_D_j1 = {}
    CSV_D_j2 = {}
    DCSV_D_j1 = {}
    DCSV_D_j2 = {}
    for i in range(len(L)-1):	
      CSV_D_j1[i] = TH1F("CSV_J1_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),"CSV_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),100,0,1)
      DCSV_D_j1[i] = TH1F("DeepCSV_J1_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),"DeepCSV_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),100,0,1)

      CSV_D_j2[i] = TH1F("CSV_J2_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),"CSV_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),100,0,1)
      DCSV_D_j2[i] = TH1F("DeepCSV_J2_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),"DeepCSV_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),100,0,1)


    CSV2d  = TH2F("CSV_Pt_Distr","CSV_Pt_Distr",100,0,6000,100,0,1)
    DCSV2d = TH2F("DeepCSV_Pt_Distr","DeepCSV_Pt_Distr",100,0,6000,100,0,1)
    #CSV2d = TH2F("CSV_Pt_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),"CSV_PtEta_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),100,0,6000,100,3.14,3.14)
    #DCSV2d = TH2F("DCSV_Pt_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),"DCSV_PtEta_DistrIn"+str(int(L[i]))+"-"+str(int(L[i+1])),100,0,6000,100,3.14,3.14)

    h_mjj = TH1F('mjj','mjj',100,0,6000)

    tchain = TChain('rootTupleTree/tree')
    for i in flist.readlines():
        tchain.Add(i.replace('\n','').replace('\t',''))


    nEntries = tchain.GetEntries()
    for i in range(nEntries):#in progressbar(range(nEntries), 'Progress: ', 40):
        tchain.GetEntry(i)
	
        if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
        #        tchain.pTWJ_j1<6500              and
                tchain.pTWJ_j2>30                and
         #       tchain.pTWJ_j2<6500              and

          #      tchain.mjj > 1246                and
           #     tchain.mjj < 8152               and

                tchain.PassJSON):
            continue

        h_mjj.Fill(tchain.mjj)
 
	for  i in range(len(L)-1):
	  if L[i]<tchain.mjj<L[i+1]:
	    CSV_D_j1[i].Fill(tchain.jetCSVAK4_j1)
	    CSV_D_j2[i].Fill(tchain.jetCSVAK4_j2)

	    DCSV_D_j1[i].Fill(tchain.jetDeepCSVAK4_j1)
            DCSV_D_j2[i].Fill(tchain.jetDeepCSVAK4_j2)

	CSV2d.Fill(tchain.pTWJ_j1,tchain.jetCSVAK4_j1)
        CSV2d.Fill(tchain.pTWJ_j2,tchain.jetCSVAK4_j2)

        DCSV2d.Fill(tchain.pTWJ_j2,tchain.jetDeepCSVAK4_j2)
        DCSV2d.Fill(tchain.pTWJ_j1,tchain.jetDeepCSVAK4_j1)

    Fout = TFile(Output,'recreate')
    
    for  i in range(len(L)-1):
      CSV_D_j1[i].Write()
      CSV_D_j2[i].Write()

      DCSV_D_j1[i].Write()
      DCSV_D_j2[i].Write()
    DCSV2d.Write()
    CSV2d.Write()
