#!usr/bin/python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi
import optparse
from setTDRStyle import setTDRStyle


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()

gROOT.Reset()
setTDRStyle()
gROOT.ForceStyle()
gROOT.SetStyle('tdrStyle')


#######################################################

usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("--var",action="store",type="string",dest="var",default='ptHat')
parser.add_option("--xmin",action="store",type="float",dest="xmin",default=1)
parser.add_option("--xmax",action="store",type="float",dest="xmax",default=1)
parser.add_option("--xtitle",action="store",type="string",dest="xtitle",default='')
parser.add_option("--bins",action="store",type="int",dest="bins",default=11111111111)
parser.add_option("--rebin",action="store",type="int",dest="rebin",default=1)
parser.add_option("--logy",action="store_true",default=False,dest="logy")
parser.add_option("--outputDir",action="store",type="string",default="./",dest="outputDir")
parser.add_option("--inputList",action="store",type="string",default="list.txt",dest="inputList")
parser.add_option("--lumi",action="store",type="float",default="1000.",dest="lumi")

(options, args) = parser.parse_args()

var = options.var
xmin = options.xmin
xmax = options.xmax
bins = options.bins
xtitle = options.xtitle
rebin = options.rebin
logy = options.logy
outputDir = options.outputDir
inputList = options.inputList
lumi = options.lumi
#############################

CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = str(options.lumi)+" pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0
#######################
minX_mass = 119.
maxX_mass = 1607. 

massBins_list = [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430, 10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000]
    
massBins = array("d",massBins_list)


#############################
#fileNames = ['QCD_Pt-301to470','QCD_Pt-470to600','QCD_Pt-600to800', 'QCD_Pt-800to1000', 'QCD_Pt-1000to1400', 'QCD_Pt-1400to1800', 'QCD_Pt-1800to2400', 'QCD_Pt-2400to3200', 'QCD_Pt-3200']
#xsections = [7475 ,587., 167, 28.25, 8.195, 0.7346, 0.102, 0.00644, 0.000163]
#colorF    = [ROOT.kBlue-9, ROOT.kBlue-9, ROOT.kBlue-9, ROOT.kBlue-9, ROOT.kBlue-9, ROOT.kBlue-9, ROOT.kBlue-9, ROOT.kBlue-9,ROOT.kBlue-9]
#colorL    = [ROOT.kBlack, ROOT.kBlack, ROOT.kBlack, ROOT.kBlack, ROOT.kBlack, ROOT.kBlack, ROOT.kBlack, ROOT.kBlack,ROOT.kBlack]
hist_allCuts      = []

#LUMI      = lumi
#PATH      = inputDir

#---- read the list -----------------
lines = [line.strip() for line in open(inputList)]

#---- split sample name and xsec
fileNames = []
xsecs = []
ii = 0
for line in lines:
  parts = line.split()
  fileNames.append(parts[0])
  xsecs.append(parts[1])
  print ("dataset : %s    xsec : %s" % (fileNames[ii], xsecs[ii]))


  ii+=1

#---- open the files --------------------
var1 = ""
if var=="pTWJ_j1" : var1 = "pT_j1"
elif var=="pTWJ_j2" : var1 = "pT_j2"
elif var=="etaWJ_j1" : var1 = "eta_j2"
elif var=="etaWJ_j2" : var1 = "eta_j2"
elif var=="phiWJ_j1" : var1 = "phi_j1"
elif var=="phiWJ_j2" : var1 = "phi_j2"
else : var1 = var

i_f = 0
for f in fileNames:
  inf = TFile.Open(f)
  print inf.GetName()
  
  Nev = inf.Get('DijetFilter/EventCount/EventCounter').GetBinContent(1)
  print ('processed events: %s' % Nev)
  wt = 1.0
  #if i_f < 3:

  h_allCuts = TH1F("h_allCuts", "", bins, xmin, xmax)
  h_allCuts.Sumw2()
  tree = inf.Get('rootTupleTree/tree')
  tree.Project(h_allCuts.GetName(), var,'deltaETAjj < 1.3')
  Npassed = h_allCuts.GetEntries()
  eff = float(Npassed)/Nev
  print('eff : %f' % eff)
  print('(not using efficiency in the weight)')
  if not (i_f == 9):
    wt = options.lumi*float(xsecs[i_f])/Nev
  print('weight : %f' % wt)
  h_allCuts.Scale(wt)
  h_allCuts.SetDirectory(0)
  h_allCuts.SetFillColor(kBlue-9)
  h_allCuts.SetLineColor(kBlue-9)
  h_allCuts.SetMarkerColor(kBlue-9)
  hist_allCuts.append(h_allCuts)
  print "entries: %d" % h_allCuts.GetEntries()
  print "integral: %f" % h_allCuts.Integral()
   
  i_f += 1

h_dat = hist_allCuts[9].Clone()
h_dat.SetName("h_dat")
#h_dat.SetLineStyle(2)
#h_dat.SetLineWidth(2)
h_dat.SetMarkerColor(kBlack)
h_dat.SetLineColor(kBlack)

#kFactor = NDAT/NQCD
kFactor = 1.3
print ("kFactor = %f" % kFactor)

                                      
#for i in range(0,len(fileNames)) :
for i in range(0,9) :
  hist_allCuts[i].Scale(kFactor)
 
NQCD_allCuts = hist_allCuts[0].Integral()

#for i in range(0,len(fileNames)) :
for i in range(0,9) :
  NQCD_allCuts += hist_allCuts[i].Integral()
    
hist_allCutsQCD = hist_allCuts[0].Clone('hist_allCutsQCD')

#for i in range(1,len(fileNames)):
for i in range(1,9):
  hist_allCutsQCD.Add(hist_allCuts[i]) 
  print "hist_allCutsQCD entries: %f" % hist_allCutsQCD.Integral()

hsQCD_allCuts = THStack('QCD_allCuts','QCD_allCuts')

#for i in range(0,len(fileNames)) :
for i in range(0,9) :
  hsQCD_allCuts.Add(hist_allCuts[i])



print ("---- After scaling signal to bkg (if not plotting mjj) -----")
print ("bkg integral all cuts = %f" % NQCD_allCuts)


#----- Drawing  and save on file -----------------------

outFile = TFile(outputDir+"histo_data_"+var+"_fromTree.root", "recreate")
outFile.cd()
#scale to data
integral_data = h_dat.Integral()
integral_qcd = hist_allCutsQCD.Integral()
#if not integral_qcd==0:
#  hist_allCutsQCD.Scale(integral_data/integral_qcd)
#else:
#  hist_allCutsQCD.Scale(0)
#  print("QCD scaled to 0!")
#rebin only for plot
hist_allCutsQCD.Write()
h_dat.Write()

#Rebin only for the plots
#hist_allCutsQCD.Rebin(rebin)
#h_dat.Rebin(rebin)
if var=="mjj":
  hist_allCutsQCD_rebin = hist_allCutsQCD.Rebin(len(massBins_list)-1,var+"_rebin",massBins)
  h_dat_rebin = h_dat.Rebin(len(massBins_list)-1,var+"_data_rebin",massBins)
  hist_allCutsQCD_rebin.GetXaxis().SetRangeUser(minX_mass,maxX_mass)  
  h_dat_rebin.GetXaxis().SetRangeUser(minX_mass,maxX_mass)  
else :
  hist_allCutsQCD.Rebin(rebin)
  h_dat.Rebin(rebin)
  hist_allCutsQCD_rebin = hist_allCutsQCD.Clone(var+"_rebin")
  h_dat_rebin = h_dat.Clone(var+"_data_rebin")

can_allCuts = TCanvas('can_allCuts_'+var,'can_allCuts_'+var,600,600)

leg = TLegend(0.6, 0.7, 0.85, 0.85)
leg.SetLineColor(0)
leg.SetFillColor(0)
leg.AddEntry(hist_allCutsQCD_rebin, "QCD", "l")
leg.AddEntry(h_dat_rebin, "data", "p")

can_allCuts.cd()
max = hist_allCutsQCD_rebin.GetBinContent(hist_allCutsQCD_rebin.GetMaximumBin())

if logy:
  gPad.SetLogy()
  hist_allCutsQCD_rebin.SetMaximum(1000.*max)  

#hist_allCutsQCD.Reset()
hist_allCutsQCD_rebin.GetXaxis().SetTitle(xtitle)
h_dat_rebin.GetXaxis().SetTitle(xtitle)
#maximumBin = array('f',  [hist_allCutsQCD_rebin.GetBinContent(hist_allCutsQCD_rebin.GetMaximumBin()), h_dat_rebin.GetBinContent(h_dat_rebin.GetMaximumBin())])
#max = TMath.MaxElement(2, maximumBin)
#hist_allCutsQCD_rebin.SetMaximum(1.2*max)
hist_allCutsQCD_rebin.SetMinimum(0.0001)
h_dat_rebin.Draw("p")
hist_allCutsQCD_rebin.Draw("hist same")
h_dat_rebin.Draw("p same")
leg.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(can_allCuts, iPeriod, iPos)

gPad.RedrawAxis()


can_allCuts.Write()   
can_allCuts.SaveAs(outputDir+var+'_allCuts.png')
can_allCuts.SaveAs(outputDir+var+'_allCuts.svg')
can_allCuts.Close()

outFile.Close()

##----- keep the GUI alive ------------
#if __name__ == '__main__':
#  rep = ''
#  while not rep in ['q','Q']:
#    rep = raw_input('enter "q" to quit: ')
#    if 1 < len(rep):
#      rep = rep[0]