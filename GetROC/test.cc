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
#include <TGraphAsymmErrors.h>
#include <string>
#include "TTree.h"
#include "TFile.h"
#include "TF1.h"
#include "TMath.h"
#include "math.h"
using namespace std;

int main(){
  float x[10],y[10];
  for(int i=0;i<100;i++){
    x[i]=1;
    y[i]=3;
  }
 
  std::map<int, TGraph*> Graph1D;

  TGraphAsymmErrors* gr[100];
  for (int i=0;i<100;i++){
     for(int j =0;j<10;j++){
	cout<<"start"<<endl;
        Graph1D[i]= new TGraph(10,x,y);
     }
   
  }

}
