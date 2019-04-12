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
   
    L = [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430, 10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000]  
 
    csv_list = [0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.8838,0.9,0.9693]

    WorkingPoint = {}
    WorkingPoint['CSVv2']={
'L':0.5803,
'M':0.8838,
'T':0.9693,
}
    WorkingPoint['DeepCSV'] = {
'L':0.1522,
'M':0.4941,
'T':0.8001,
}
    WorkingPoint['DeepJet'] = {
'L':0.0521,
'M':0.3033,
'T':0.7489,
}

    content = 'run\tevent\tmjj' 
    h_DCSV_mjj0={}
    h_DCSV_mjjle1={}
    h_DCSV_mjj1={}
    h_DCSV_mjj2={}
    h_DCSV_mjjmt={}

    h_CSV_mjj0={}
    h_CSV_mjjle1={}
    h_CSV_mjj1={}
    h_CSV_mjj2={}
    h_CSV_mjjmt={}

    h_DJ_mjj0={}
    h_DJ_mjjle1={}
    h_DJ_mjj1={}
    h_DJ_mjj2={}
    h_DJ_mjjmt={}

    h_mjj2 = TH1F('Mjj','Mjj',len(L)-1, array.array('f',L))
    h_mjj = TH1F('total','total',10000,0,10000)
    for i in csv_list:
       h_DCSV_mjj0[i] = TH1F('pass_0DeepCSV'+str(i),'pass_0DeepCSV'+str(i),10000,0,10000)
       h_DCSV_mjj1[i] = TH1F('pass_1DeepCSV'+str(i),'pass_1DeepCSV'+str(i),10000,0,10000)
       h_DCSV_mjjle1[i]=TH1F('pass_le1DeepCSV'+str(i),'pass_le1DeepCSV'+str(i),10000,0,10000)
       h_DCSV_mjj2[i] = TH1F('pass_2DeepCSV'+str(i),'pass_2DeepCSV'+str(i),10000,0,10000)
#    h_mjj = TH1F('h_mjj_btag0_m','h_mjj_btag0_m',10000,0,10000)
#    h_eta = TH1F('eta','eta',50,-3.14,3.14)
#    h_phi = TH1F('phi','phi',50,-3.14,3.14) 
#    h_deltaeta = TH1F('DeltaEta','DeltaEta',50,0,1.3 )
#    h_deltaphi = TH1F('DeltaPhi','DeltaPhi',50,0,3.14)
       h_CSV_mjj0[i] = TH1F('pass_0CSV'+str(i),'pass_0CSV'+str(i),10000,0,10000)
       h_CSV_mjj1[i] = TH1F('pass_1CSV'+str(i),'pass_1CSV'+str(i),10000,0,10000)
       h_CSV_mjjle1[i]=TH1F('pass_le1CSV'+str(i),'pass_le1CSV'+str(i),10000,0,10000)
       h_CSV_mjj2[i] = TH1F('pass_2CSV'+str(i),'pass_2CSV'+str(i),10000,0,10000)

       h_DJ_mjj0[i] = TH1F('pass_0DJ'+str(i),'pass_0DJ'+str(i),10000,0,10000)
       h_DJ_mjj1[i] = TH1F('pass_1DJ'+str(i),'pass_1DJ'+str(i),10000,0,10000)
       h_DJ_mjjle1[i]=TH1F('pass_le1DJ'+str(i),'pass_le1DJ'+str(i),10000,0,10000)
       h_DJ_mjj2[i] = TH1F('pass_2DJ'+str(i),'pass_2DJ'+str(i),10000,0,10000)

    h_CSV_mjjmt  =TH1F('pass_mtCSV'+str(i),'pass_2CSV'+str(i),10000,0,10000)
    h_DCSV_mjjmt = TH1F('pass_mtDeepCSV'+str(i),'pass_2DeepCSV'+str(i),10000,0,10000)
    h_DJ_mjjmt   = TH1F('pass_mtDeepJet'+str(i),'pass_mtDeepJet'+str(i),10000,0,10000)

    tchain = TChain('rootTupleTree/tree')
    for i in flist.readlines():
        tchain.Add(i.replace('\n','').replace('\t',''))
#'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/juska/moriond17_red_cert_v2/moriond17_v2_37fb_1nd_s15_20170127_164251/'+i.replace('\n','').replace('\t',''))

    nEntries = tchain.GetEntries()


    for i in progressbar(range(nEntries), 'Progress: ', 40):
#    for i in range(nEntries):#in progressbar(range(nEntries), 'Progress: ', 40):
        tchain.GetEntry(i)

	#if i >2000:
	  #break

         #if (i>50): continue
        if not (abs(tchain.deltaETAjj)<1.1       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

#                tchain.pTWJ_j1>60                and
        #        tchain.pTWJ_j1<6500              and
 #               tchain.pTWJ_j2>30                and
         #       tchain.pTWJ_j2<6500              and

          #      tchain.mjj > 1246                and
           #     tchain.mjj < 8152               and

                tchain.PassJSON):
            continue

	#if tchain.mjj>6300:
	   #content += tchain.run+'\t'+tchain.event+'\t'+str(tchain.mjj)
	
	h_mjj.Fill(tchain.mjj)
        if tchain.mjj>1530:
          h_mjj2.Fill(tchain.mjj)

       
	if (tchain.jetCSVAK4_j1>WorkingPoint['CSVv2']['T'] and tchain.jetCSVAK4_j2>WorkingPoint['CSVv2']['M']) or (tchain.jetCSVAK4_j1>WorkingPoint['CSVv2']['M'] and tchain.jetCSVAK4_j2>WorkingPoint['CSVv2']['T']):
	  h_CSV_mjjmt.Fill(tchain.mjj)

        if (tchain.jetDeepJetAK4_j1>WorkingPoint['DeepJet']['T'] and tchain.jetDeepJetAK4_j2>WorkingPoint['DeepJet']['M']) or (tchain.jetDeepJetAK4_j1>WorkingPoint['DeepJet']['M'] and tchain.jetDeepJetAK4_j2>WorkingPoint['DeepJet']['T']):
          h_DJ_mjjmt.Fill(tchain.mjj)


        if (tchain.jetDeepCSVAK4_j1>WorkingPoint['DeepCSV']['T'] and tchain.jetDeepCSVAK4_j2>WorkingPoint['DeepCSV']['M']) or (tchain.jetDeepCSVAK4_j1>WorkingPoint['DeepCSV']['M'] and tchain.jetDeepCSVAK4_j2>WorkingPoint['DeepCSV']['T']):
          h_DCSV_mjjmt.Fill(tchain.mjj)


        for j in csv_list:
 	  NofB = 0
	  NofDB = 0
	  NofDJ = 0
#          if tchain.jetCSVAK4_j1 < j/1000 and tchain.jetCSVAK4_j2 < j/1000 :
#	    h_mjj0[j].Fill(mjj)
#          if tchain.jetCSVAK4_j1 > j/1000 and tchain.jetCSVAK4_j2 > j/1000 :
#            h_mjj2[j].Fill(mjj)
	  if tchain.jetCSVAK4_j1 > j:
	    NofB +=1
	  if tchain.jetCSVAK4_j2 > j:
	    NofB += 1
          if tchain.jetDeepCSVAK4_j1 > j:
	    NofDB +=1 
          if tchain.jetDeepCSVAK4_j2 >j:
	    NofDB +=1
          if tchain.jetDeepJetAK4_j1 >j:
            NofDJ +=1
          if tchain.jetDeepJetAK4_j2 >j:
            NofDJ +=1


	  if NofB ==0:
	    h_CSV_mjj0[j].Fill(tchain.mjj)
          if NofB >0:
            h_CSV_mjjle1[j].Fill(tchain.mjj)
          if NofB ==1:
            h_CSV_mjj1[j].Fill(tchain.mjj)
          if NofB ==2:
            h_CSV_mjj2[j].Fill(tchain.mjj)

          if NofDB ==0:
            h_DCSV_mjj0[j].Fill(tchain.mjj)
          if NofDB >0:
            h_DCSV_mjjle1[j].Fill(tchain.mjj)
          if NofDB ==1:
            h_DCSV_mjj1[j].Fill(tchain.mjj)
          if NofDB ==2:
            h_DCSV_mjj2[j].Fill(tchain.mjj)

          if NofDJ ==0:
            h_DJ_mjj0[j].Fill(tchain.mjj)
          if NofDJ >0:
            h_DJ_mjjle1[j].Fill(tchain.mjj)
          if NofDJ ==1:
            h_DJ_mjj1[j].Fill(tchain.mjj)
          if NofDJ ==2:
            h_DJ_mjj2[j].Fill(tchain.mjj)
#         h_mjj.Fill(tchain.mjj)
#         h_eta.Fill(tchain.etaWJ_j1)
#         h_phi.Fill(tchain.phiWJ_j1)
#         h_deltaeta.Fill(tchain.deltaETAjj)
#	 h_mjj2.Fill(tchain.mjj)
#         h_deltaphi.Fill(tchain.deltaPHIjj)

    fout = TFile(Output,'recreate')
#    oooo  = open(Output.replace('root','txt'),'w+')
#    oooo.write(content)
#    oooo.close()
    h_mjj2.Write()
    h_mjj.Write()
    for j in csv_list:
      h_CSV_mjj0[j].Write('h_mass_passed_0b_CSVv2_'+str(j*1000))
    for j in csv_list:
      h_CSV_mjjle1[j].Write('h_mass_passed_le1b_CSVv2_'+str(j*1000))
    for j in csv_list:
      h_CSV_mjj1[j].Write('h_mass_passed_1b_CSVv2_'+str(j*1000))
    for j in csv_list:
      h_CSV_mjj2[j].Write('h_mass_passed_2b_CSVv2_'+str(j*1000))

    for j in csv_list:
      h_DCSV_mjj0[j].Write('h_mass_passed_0b_DeepCSV_'+str(j*1000))
    for j in csv_list:
      h_DCSV_mjjle1[j].Write('h_mass_passed_le1b_DeepCSV_'+str(j*1000))
    for j in csv_list:
      h_DCSV_mjj1[j].Write('h_mass_passed_1b_DeepCSV_'+str(j*1000))
    for j in csv_list:
      h_DCSV_mjj2[j].Write('h_mass_passed_2b_DeepCSV_'+str(j*1000))

    for j in csv_list:
      h_DJ_mjj0[j].Write('h_mass_passed_0b_DeepJet_'+str(j*1000))
    for j in csv_list:
      h_DJ_mjjle1[j].Write('h_mass_passed_le1b_DeepJet_'+str(j*1000))
    for j in csv_list:
      h_DJ_mjj1[j].Write('h_mass_passed_1b_DeepJet_'+str(j*1000))
    for j in csv_list:
      h_DJ_mjj2[j].Write('h_mass_passed_2b_DeepJet_'+str(j*1000))

    h_CSV_mjjmt.Write('h_mass_passed_mt_CSVv2')
    h_DCSV_mjjmt.Write('h_mass_passed_mt_DeepCSV')
    h_DJ_mjjmt.Write('h_mass_passed_mt_DeepJet')

#    h_mjj.Write()
#    h_eta.Write()
#    h_phi.Write()
#    h_deltaeta.Write()
#    h_deltaphi.Write()
#    h_mjj2.Write()


    fout.Close()

