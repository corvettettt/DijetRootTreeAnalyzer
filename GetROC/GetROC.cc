//
//g++ `root-config --cflags` -o GetROC GetROC.cc `root-config --glibs`  
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <TH1.h>
#include <TH2.h>
#include <TGraph.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TChain.h>
#include <TStyle.h>
#include <TVectorF.h>
#include <TImage.h>
#include <TFile.h>
#include <TTree.h>
#include <TDirectory.h>
#include <vector>
#include <cmath>
#include <iomanip>
#include <map>
#include <string>
#include "TTree.h"
#include "TFile.h"
#include "TF1.h"
#include "TMath.h"
#include "math.h"
using namespace std;

int main(int argc, char** argv){

  std::map<std::string, TH1D*> histo1D;
  std::map<std::string, TH1D*>::iterator histo1Diter;
         
  std::map<std::string, TH2D*> histo2D;
  std::map<std::string, TH2D*>::iterator histo2Diter;

  std::ifstream infile(argv[1]);

//  TBranch *b_deltaETAjj;
//  TBranch *b_etaWJ_j1;
//  TBranch *b_etaWJ_j2;
//  TBranch *b_pTWJ_j1;
//  TBranch *b_pTWJ_j2;
//  TBranch *b_jetCSVAK4_j1;
//  TBranch *b_jetCSVAK4_j1;
//  TBranch *b_jetDeepCSVAK4_j1;
//  TBranch *b_jetDeepCSVAK4_j2;

  TChain* chain = new TChain("rootTupleTree/tree");
  std::string a;
  while (infile >> a){
     chain->Add(a.c_str());//"/eos/cms/store/GraphCSVoup/phys_exotica/dijet/Dijet13TeV/TylerW/2017JetHT_reduced/2017RunII_F/Run2017F_20180629_120646/rootfile_JetHT_2017F-17Nov2017-v1_Run2017F_20180629_120646_8_reduced_skim.root");
  cout<<a<<endl;
  } 

  cout<<"after"<<endl;

  float deltaETAjj,mjj,etaWJ_j1,etaWJ_j2,pTWJ_j1,pTWJ_j2,jetCSVAK4_j1,jetCSVAK4_j2,jetDeepCSVAK4_j1,jetDeepCSVAK4_j2;
  int PassJSON;
  float csv_list[]={0.05,0.1,0.15,0.1522,0.2,0.25,0.3,0.35,0.4,0.45,0.4941,0.5,0.55,0.5803,0.6,0.65,0.7,0.75,0.8,0.85,0.8838,0.9,0.95,0.9693};
  float MassRange[]={1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152};
  int N_all[sizeof(MassRange)][sizeof(csv_list)][4],N_pass_CSV[sizeof(MassRange)][sizeof(csv_list)][4],N_pass_DCSV[sizeof(MassRange)][sizeof(csv_list)][4];
  float ratio_CSV[sizeof(MassRange)][sizeof(csv_list)][4],ratio_DCSV[sizeof(MassRange)][sizeof(csv_list)][4];
  chain->SetBranchAddress("deltaETAjj",&deltaETAjj);
  chain->SetBranchAddress("etaWJ_j1",&etaWJ_j1);
  chain->SetBranchAddress("etaWJ_j2",&etaWJ_j2);
  chain->SetBranchAddress("pTWJ_j1",&pTWJ_j1);
  chain->SetBranchAddress("pTWJ_j2",&pTWJ_j2);
  chain->SetBranchAddress("jetCSVAK4_j1",&jetCSVAK4_j1);
  chain->SetBranchAddress("jetCSVAK4_j2",&jetCSVAK4_j2);
  chain->SetBranchAddress("jetDeepCSVAK4_j1",&jetDeepCSVAK4_j1);
  chain->SetBranchAddress("jetDeepCSVAK4_j2",&jetDeepCSVAK4_j2);
  chain->SetBranchAddress("PassJSON",&PassJSON);
  chain->SetBranchAddress("mjj",&mjj);

  int NEntries = chain->GetEntries();
  cout<<NEntries<<endl;
  for (int i=0;i<NEntries;i++){   
    chain->GetEntry(i);
//    cout<<deltaETAjj<<endl;

    if (!(abs(deltaETAjj)<1.3 &&
       abs(etaWJ_j1)<2.5 &&
       abs(etaWJ_j2)<2.5 &&

       pTWJ_j1>60 &&
       pTWJ_j2>30 && 

       PassJSON))
            continue;
    for(int j=0;j<sizeof(csv_list);j++){
      int N_csv = 0;
      int N_dcsv=0;

      if (jetCSVAK4_j1 > csv_list[j]) N_csv+=1;
      if (jetCSVAK4_j2 > csv_list[j]) N_csv+=1;
      if (jetDeepCSVAK4_j1 > csv_list[j]) N_dcsv+=1;
      if (jetDeepCSVAK4_j2 > csv_list[j]) N_dcsv+=1;
//cout<<jetDeepCSVAK4_j2<<endl;
      for (int k=0;k<(sizeof(MassRange)-3);k++)
	if (MassRange[k+3]>mjj && mjj>MassRange[k]){

	  N_all[i][j][k] +=1;
	  if (N_csv==0)  N_pass_CSV[k][j][0]+=1;
          if (N_csv==1)  N_pass_CSV[k][j][1]+=1;
          if (N_csv>0)   N_pass_CSV[k][j][2]+=1;
          if (N_csv==2)  N_pass_CSV[k][j][3]+=1;

	  if (N_dcsv==0) N_pass_DCSV[k][j][0]+=1;
          if (N_dcsv==1) N_pass_DCSV[k][j][1]+=1;
          if (N_dcsv>0)  N_pass_DCSV[k][j][2]+=1;
          if (N_dcsv==2) N_pass_DCSV[k][j][3]+=1;

        }
    }

  }

  string cata[4]={"0b","1b","le1b","2b"};
  for(int i=0;i<(sizeof(MassRange)-3);i++)
    for(int j=0;j<sizeof(csv_list);j++)
      for(int k=0;k<sizeof(cata);k++) {
	if (N_all[i][j][k]==0){
   	  ratio_CSV[i][j][k] =0;
	  ratio_CSV[i][j][k] =0;
	}
	ratio_CSV[i][j][k]  = float(N_pass_CSV[i][j][k] )/float(N_all[i][j][k]);
	ratio_DCSV[i][j][k]  = float(N_pass_DCSV[i][j][k] )/float(N_all[i][j][k]);
      }
  
  cout<<"afterratio"<<endl;
     
  char name[100]; 
  float Xaxis[sizeof(csv_list)]={},Yaxis[sizeof(csv_list)]={};
  TFile* Fout =new TFile(argv[2],"recreate"); 
  std::map<int,std::map<int, TGraph*>> GraphCSV;
  std::map<int,std::map<int, TGraph*>> GraphDCSV;
//  std::map<std::string,TGraph> TGraph1D;
  

  cout<<"startPlot"<<endl;
  for(int i=0;i<(sizeof(MassRange)-3);i++)
    for(int k=0;k<sizeof(cata);k++){
      for(int j=0;j<sizeof(csv_list);j++){
	Xaxis[j]=csv_list[j];
	Yaxis[j]=ratio_CSV[i][j][k];
      }
      GraphCSV[i][k]=new TGraph(sizeof(Xaxis),Xaxis,Yaxis);   
      sprintf(name,"rate of %s CSVv2 bin mass range %d-%d",cata[k].c_str(),MassRange[i],MassRange[i+3]);
      GraphCSV[i][k]->SetTitle(name);
      GraphCSV[i][k]->GetXaxis()->SetTitle("CSVv2");
      GraphCSV[i][k]->GetYaxis()->SetTitle("Efficiency");
      sprintf(name,"CSVv2RateOf%sMass%d-%d",cata[k].c_str(),MassRange[i],MassRange[i+3]);
      GraphCSV[i][k]->SetName(name);
      GraphCSV[i][k]->Write();
      cout<<"firstGraphCSVaph"<<endl;

      for(int j=0;j<sizeof(csv_list);j++){
	Yaxis[j]=ratio_DCSV[i][j][k];
      }
      GraphDCSV[i][k] =new TGraph(sizeof(Xaxis),Xaxis,Yaxis);
      sprintf(name,"rate of %s DeepCSV bin mass range %d-%d",cata[k].c_str(),MassRange[i],MassRange[i+3]);
      GraphDCSV[i][k]->SetTitle(name);
      GraphDCSV[i][k]->GetXaxis()->SetTitle("Deep CSV");
      GraphDCSV[i][k]->GetYaxis()->SetTitle("Efficiency");
      sprintf(name, "DeepCSVRateOf%sMass%d-%d",cata[k].c_str(),MassRange[i],MassRange[i+3]);
      GraphDCSV[i][k]->SetName(name);
      GraphDCSV[i][k]->Write();
      cout<<"scoundGraphCSVaph"<<endl;
    }  
  cout<<"End"<<endl;
  Fout->Close();
  
}
