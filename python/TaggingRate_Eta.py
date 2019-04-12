from ROOT import *
import sys,os
from optparse import OptionParser

sampleName = {}

sampleName['qg'] = {
500: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_500GeV_reduced_skim.root',
1000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_1000GeV_reduced_skim.root',
2000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_2000GeV_reduced_skim.root',
3000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_3000GeV_reduced_skim.root',
4000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_4000GeV_reduced_skim.root',
5000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_5000GeV_reduced_skim.root',
6000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_6000GeV_reduced_skim.root',
7000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_7000GeV_reduced_skim.root',
8000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_8000GeV_reduced_skim.root',
9000:'/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/bstar2bg_Jan_central/bstar_9000GeV_reduced_skim.root',
                  }

#CHANGE FILE NAME AS SOON AS THE NTUPLES ARE READY
sampleName['qq'] = {
1000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG1000GeV_reduced_skim.root',
2000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG2000GeV_reduced_skim.root',
3000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG3000GeV_reduced_skim.root',
4000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG4000GeV_reduced_skim.root',
5000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG5000GeV_reduced_skim.root',
6000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG6000GeV_reduced_skim.root',
7000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG7000GeV_reduced_skim.root',
8000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG8000GeV_reduced_skim.root',
9000: '/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/RSGraviton2qq_Jan_central/RSG9000GeV_reduced_skim.root',
                  }

ETA = [float(i)/10.0 for i in range(-25,30,5)]

MASS = [1000,2000,3000,4000,5000,6000,7000,8000,9000]

CSV_Value={}
CSV_Value['DeepCSV'] = {
   'L':0.1522,
   'M':0.4941,
   'T':0.8001
}

CSV_Value['CSV'] = {
   'L':0.5803,
   'M':0.8838,
   'T':0.9693
}

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



if __name__=='__main__':

  parser = OptionParser()
  parser.add_option('-m','--model',dest="model",type="string",default="qq",help="Name of the signal model")
  (options,args) = parser.parse_args()
  model   = options.model

  Ratio = {}
  histo = {}
  for i in MASS:
    for j in ['DeepCSV','CSV']:
      for k in ['M','T','L']:
        histo['Passed_%s_%s_Mass'%(k,j)+str(i)]=TH1D('Passed_%s_%s_Mass'%(k,j)+str(i),'Passed_%s_%s_Mass'%(k,j)+str(i),10,-2.5,2.5)
	histo['2D_Passed_%s_%s_Mass'%(k,j)+str(i)] = TH2D('2D_Passed_%s_%s_Mass'%(k,j)+str(i),'2D_Passed_%s_%s_Mass'%(k,j)+str(i),15,0,5000,10,-2.5,2.5)
	Ratio['2D_%s_%s_Mass'%(k,j)+str(i)] = TH2D('Ratio_%s_%s_Mass'%(k,j)+str(i),'Ratio__%s_%s_Mass'%(k,j)+str(i),15,0,5000,10,-2.5,2.5)
	Ratio['2D_Re_%s_%s_Mass'%(k,j)+str(i)] = TH2D('Ratio_Rescale_%s_%s_Mass'%(k,j)+str(i),'Ratio_Rescale_%s_%s_Mass'%(k,j)+str(i),15,0,5000,10,-2.5,2.5)
    histo['All_Mass'+str(i)]=TH1D('All_Mass'+str(i),'All_Mass'+str(i),10,-2.5,2.5)
    histo['2D_All_Mass'+str(i)] = TH2D('2DAll_Mass'+str(i),'2D_All_Mass'+str(i),15,0,5000,10,-2.5,2.5)
    histo['pt_Mass'+str(i)] = TH1D('pt_Mass'+str(i),'pt_Mass'+str(i),15,0,5000)  

  for j in ['DeepCSV','CSV']:
    for k in ['M','T','L']:
      histo['Passed_%s_%s'%(k,j)] = TH1D('Passed_%s_%s'%(k,j),'Passed_%s_%s'%(k,j),10,-2.5,2.5)
      histo['2D_Passed_%s_%s'%(k,j)] = TH2D('2D_Passed_%s_%s'%(k,j),'2D_Passed_%s_%s'%(k,j),15,0,5000,10,-2.5,2.5)
      Ratio['2D_%s_%s'%(k,j)] = TH2D('Ratio_%s_%s'%(k,j),'Ratio_%s_%s'%(k,j),15,0,5000,10,-2.5,2.5)
      Ratio['2D_Re_%s_%s'%(k,j)] = TH2D('Ratio_Rescale_%s_%s'%(k,j),'Ratio_Rescale_%s_%s'%(k,j),15,0,5000,10,-2.5,2.5)
  histo['All'] = TH1D('All','All',10,-2.5,2.5)
  histo['2D_All'] = TH2D('2D_All','2D_All',15,0,5000,10,-2.5,2.5)

  TreeName = 'rootTupleTree/tree'
  
  for i in MASS:
    tchain = TChain(TreeName)
    tchain.Add(sampleName[model][i])
    for j in progressbar(range(tchain.GetEntries()), str(i)+" : ", 40):

      tchain.GetEntry(j)


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

      for m in ['j1','j2']:
	 if abs(getattr(tchain,'jetpflavour_'+m)) != 5:
	   continue
	 histo['All'].Fill(getattr(tchain,'etaWJ_'+m))
	 histo['All_Mass'+str(i)].Fill(getattr(tchain,'etaWJ_'+m))
	 histo['2D_All'].Fill(getattr(tchain,'pTWJ_'+m),getattr(tchain,'etaWJ_'+m))
	 histo['2D_All_Mass'+str(i)].Fill(getattr(tchain,'pTWJ_'+m),getattr(tchain,'etaWJ_'+m))
	 histo['pt_Mass'+str(i)].Fill(getattr(tchain,'pTWJ_'+m))

         for k in ['DeepCSV','CSV']:
           for l in ['M','T','L']:
             if getattr(tchain,'jet%sAK4_%s'%(k,m)) > CSV_Value[k][l]:
	       histo['Passed_%s_%s'%(l,k)].Fill(getattr(tchain,'etaWJ_'+m))
               histo['Passed_%s_%s_Mass'%(l,k)+str(i)].Fill(getattr(tchain,'etaWJ_'+m))
	       histo['2D_Passed_%s_%s'%(l,k)].Fill(getattr(tchain,'pTWJ_'+m),getattr(tchain,'etaWJ_'+m))
               histo['2D_Passed_%s_%s_Mass'%(l,k)+str(i)].Fill(getattr(tchain,'pTWJ_'+m),getattr(tchain,'etaWJ_'+m))

  for j in ['DeepCSV','CSV']:
    for k in ['M','T','L']:
      Ratio['%s_%s'%(k,j)]  = TGraphAsymmErrors()
      for l in MASS:
        Ratio['%s_%s_Mass%d'%(k,j,l)] = TGraphAsymmErrors()

  for i in range(10):
    for j in ['DeepCSV','CSV']:
      for k in ['M','T','L']:
        for l in MASS:
	  a = histo['Passed_%s_%s_Mass'%(k,j)+str(l)].GetBinContent(i+1)
          b = histo['All_Mass'+str(l)].GetBinContent(i+1)
	  if b ==0:
	    R = 0
	  else:
            R = a/b
	  Ratio['%s_%s_Mass%d'%(k,j,l)].SetPoint(i,(ETA[i]+ETA[i+1])/2,R)
        a = histo['Passed_%s_%s'%(k,j)].GetBinContent(i+1)
	b = histo['All'].GetBinContent(i+1)
	if b ==0:
	  R = 0
	else:
	  R = a/b
	Ratio['%s_%s'%(k,j)].SetPoint(i,(ETA[i]+ETA[i+1])/2,R)

    for j in range(10):
     for k in ['DeepCSV','CSV']:
       for l in ['M','T','L']:
	 for m in  MASS:
	   a = histo['2D_Passed_%s_%s_Mass'%(l,k)+str(m)].GetBinContent(i+1,j+1)
	   b = histo['2D_All_Mass'+str(m)].GetBinContent(i+1,j+1)
	   if b == 0:
	     R = 0
	   else: 
	     R = a/b
	   Ratio['2D_%s_%s_Mass%d'%(l,k,m)].SetBinContent(i+1,j+1,R)
           Ratio['2D_Re_%s_%s_Mass%d'%(l,k,m)].SetBinContent(i+1,j+1,R/histo['2D_All_Mass'+str(m)].GetEntries()*10000)
	 a =  histo['2D_Passed_%s_%s'%(l,k)].GetBinContent(i+1,j+1)
         b = histo['2D_All'].GetBinContent(i+1,j+1)
         if b == 0 :
	   R = 0
	 else:
	   R = a/b
	 Ratio['2D_%s_%s'%(l,k)].SetBinContent(i+1,j+1,R)
	 Ratio['2D_Re_%s_%s'%(l,k)].SetBinContent(i+1,j+1,R/histo['2D_All'].GetEntries()*10000)

  for i in ['DeepCSV','CSV']:
    for j in ['M','T','L']:
      continue
      c1 = TCanvas()
      leg = TLegend(0.8,0.7,0.95,0.95)
      for k1,k2 in enumerate(MASS):
	Ratio['%s_%s_Mass%d'%(j,i,k2)].SetLineColor(k1+1)
	if k1 ==0 :
	  Ratio['%s_%s_Mass%d'%(j,i,k2)].SetTitle( '%s bTagging efficiency on %s WP;Eta;bTaging efficiency'%(i,j))
	  Ratio['%s_%s_Mass%d'%(j,i,k2)].Draw()
	  Ratio['%s_%s_Mass%d'%(j,i,k2)].GetYaxis().SetRangeUser(0,1)
	else:
	  if not (k2 ==3000 or k2 ==5000 or k2 ==9000):
	    continue
	  Ratio['%s_%s_Mass%d'%(j,i,k2)].Draw('same')
	if not (k1 ==0 or k2 ==3000 or k2 ==5000 or k2 ==9000):
            continue
        leg.AddEntry(Ratio['%s_%s_Mass%d'%(j,i,k2)],str(k2),'L')
      Ratio['%s_%s'%(j,i)].SetLineColor(30)	
      Ratio['%s_%s'%(j,i)].Draw('same')
      leg.AddEntry(Ratio['%s_%s'%(j,i)],'All','L')
      leg.Draw('same')
      c1.Print(j+'_'+i+'.pdf')
  Fout = TFile('output.root','recreate')
 
  for j in ['DeepCSV','CSV']:
    for k in ['M','T','L']:
      for i in MASS:
	Ratio['2D_%s_%s_Mass%d'%(k,j,i)].SetTitle('%s bTagging Efficiency on %s WP at %d GeV ;pT(GeV);Eta;Tagging Efficiency'%(j,k,i))
	Ratio['2D_%s_%s_Mass%d'%(k,j,i)].Write()
      Ratio['2D_%s_%s'%(k,j)].SetTitle('%s bTagging Efficiency on %s WP ;pT(GeV);Eta;Tagging Efficiency'%(j,k))
      Ratio['2D_%s_%s'%(k,j)].Write()

  for j in ['DeepCSV','CSV']:
    for k in ['M','T','L']:
      for i in MASS:
	Ratio['2D_Re_%s_%s_Mass%d'%(k,j,i)].SetTitle('ReScaled %s bTagging Efficiency on %s WP at %d GeV ;pT(GeV);Eta;Tagging Efficiency'%(j,k,i))
        Ratio['2D_Re_%s_%s_Mass%d'%(k,j,i)].Write()
      Ratio['2D_Re_%s_%s'%(k,j)].SetTitle('ReScaled %s bTagging Efficiency on %s WP ;pT(GeV);Eta;Tagging Efficiency'%(j,k))
      Ratio['2D_Re_%s_%s'%(k,j)].Write()

  for i in MASS:
    histo['pt_Mass'+str(i)].SetTitle('pT Distribution;pT(GeV);# of Events')
    histo['pt_Mass'+str(i)].Write()

  tmp = {}
  for i in MASS:
    tmp['pt_Mass'+str(i)] = histo['pt_Mass'+str(i)].Clone('pt_Rescale_Mass'+str(i))
    tmp['pt_Mass'+str(i)].Scale(1/histo['pt_Mass'+str(i)].Integral())
    tmp['pt_Mass'+str(i)].SetTitle('Normalized pT Distribution;pT(GeV);# of Events')
    tmp['pt_Mass'+str(i)].Write()

  Fout.Close()

     
