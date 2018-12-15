from optparse import OptionParser
import os
from ROOT import *
from array import *
from rootTools import CMS_lumi, tdrstyle
from array import array

######## global variables and style settings ########
gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
TGaxis.SetMaxDigits(3)
gROOT.ForceStyle()
gROOT.Reset()
tdrstyle.setTDRStyle()
gROOT.SetStyle('tdrStyle')
gROOT.ForceStyle()

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

H_ref = 800; 
W_ref = 800; 
W = W_ref
H  = H_ref

iPeriod = 0

# references for T, B, L, R
T = 0.08*H_ref
B = 0.12*H_ref 
L = 0.12*W_ref
R = 0.04*W_ref

lineStyle={
    "qq":1,
    "qg":3,
    "gg":2 }

lineColor={
    "qq":kBlue,
    "qg":kRed,
    "gg":kBlack }
   
label={
    "qq":"quark-quark",
    "qg":"quark-gluon",
    "gg":"gluon-gluon" }



###### functions ########
def massIterable(massList):    
  if len(massList.split(','))==1:
    massIterableList = [massList]
  else:
    massIterableList = list(eval(massList))
    return massIterableList



def DrawSignals(hist_dict):
  count = 0;
  canvas = TCanvas("c","c",50,50,W,H)
  canvas.SetFillColor(0)
  canvas.SetBorderMode(0)
  canvas.SetFrameFillStyle(0)
  canvas.SetFrameBorderMode(0)
  canvas.SetLeftMargin(0.05+ L/W )
  canvas.SetRightMargin( R/W )
  canvas.SetTopMargin( T/H )
  canvas.SetBottomMargin( B/H )
  canvas.SetTickx()
  canvas.SetTicky()
  canvas.cd()
  leg = TLegend(0.6,0.45,0.9,0.6)
  leg.SetBorderSize(0)
  leg.SetLineColor(0)
  leg.SetFillColor(0)
  leg.SetFillStyle(0)
  leg.SetLineWidth(0)
  leg.SetTextFont(42)
  leg.SetTextAlign(23) 

  #Pave text
  pave_fit = TPaveText(0.56,0.65,0.95,0.75,"NDC")

  pave_fit.AddText("Wide Jets")
  pave_fit.AddText("|#eta| < 2.5, |#Delta#eta_{jj}| < 1.3")
  pave_fit.SetFillColor(0)
  pave_fit.SetLineColor(0)
  pave_fit.SetFillStyle(0)
  pave_fit.SetBorderSize(0)
  pave_fit.SetTextFont(42)
  pave_fit.SetTextSize(0.038)
  pave_fit.SetTextAlign(23) 

  i=0
  for key in ("qq","qg","gg"):
    j=0
    for hist in hist_dict[key]:
      hist.Scale(1000.)
      hist.SetLineColor(lineColor[key])
      hist.SetLineStyle(lineStyle[key])
      hist.SetLineWidth(2)
      hist.GetXaxis().SetRangeUser(0,9000)
      hist.GetXaxis().SetRangeUser(0,9000)
      hist.GetYaxis().SetRangeUser(0,3.5)
      hist.GetXaxis().SetLabelOffset(1000)
      hist.GetXaxis().SetTitle("Dijet mass [TeV]")
      hist.GetYaxis().SetTitle("Normalized yield / TeV")
      if j==0:
	leg.AddEntry(hist,label[key],"l")
      if i==0:
	hist.Draw("")
      else:
	hist.Draw("same")
      xLab = TLatex()
      xLab.SetTextAlign(22)
      xLab.SetTextSize(0.05)
      xLab.SetTextFont(42)
      xLab.SetTextSize(0.05)
      yOffset = -0.1 # for 1e-5 min
      for i in range(1,10):
        xLab.DrawLatex(i*1000, yOffset, "%g"%i)
      i+=1
      j+=1
  
  leg.Draw()
  pave_fit.Draw()
  #draw the lumi text on the canvas
  CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
  canvas.SaveAs("ResonanceShapes_PFReco.pdf")
   


def Binning():
  massBins = [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325,354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687,1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509,4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430,10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000]
  v_massbins = array('d',massBins)
  return v_massbins



################# main ##################



if __name__ == '__main__':

  parser = OptionParser()
#  parser.add_option('-i','--inputList',dest="inputList", default="list.txt",type="string",
#      help="list of signal sample to plot")
#  parser.add_option('-m','--model',dest="model", default="gg",type="string",
#      help="signal model name (or list with seprator ',')")
  parser.add_option('--mass',dest="mass", default='2000',type="string",
      help="mass of resonance (or list with separator ',')")
  parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
      help="Output directory to store cards")
  #parser.add_option('-k','--coupling',dest="coupling",default=0.54,type="string",
  #   help="number of toys per job(for bayesian expected limits)")

  
  (options,args) = parser.parse_args()

  hist_dict={}

  binning = Binning() 
  hist_mass_list_qq=[]
  hist_mass_list_qg=[]
  hist_mass_list_gg=[]
  res_file_qq = TFile("inputs/ResonanceShapes_qq_13TeV_Spring16.root","read")
  res_file_qg = TFile("inputs/ResonanceShapes_qg_13TeV_Spring16.root","read")
  res_file_gg = TFile("inputs/ResonanceShapes_gg_13TeV_Spring16.root","read")
  i=0
  for massPoint in massIterable(options.mass):
    res_file_qq.cd()
    hist_mass_list_qq.append( res_file_qq.Get("h_qq_%s"%massPoint))
    res_file_qg.cd()
    hist_mass_list_qg.append( res_file_qg.Get("h_qg_%s"%massPoint))
    res_file_gg.cd()
    hist_mass_list_gg.append( res_file_gg.Get("h_gg_%s"%massPoint))
  
  hist_dict["qq"]=hist_mass_list_qq
  hist_dict["qg"]=hist_mass_list_qg
  hist_dict["gg"]=hist_mass_list_gg

  DrawSignals(hist_dict)


