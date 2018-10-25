#! /usr/bin/env python
import ROOT as rt
import os.path
import sys, glob, re
from array import *
from optparse import OptionParser
from FindCrossPoint import *

def getThyXsecDict():    
    thyXsecDict = {}
    xsecFiles = ['data/all_lowmass_lhc13TeV.txt','data/rsg_gg_lhc13TeV.txt','data/S8_13TeV_narrow.txt','data/string_total_13TeV.txt','data/axi_lhc13TeV_NLO.txt','data/dm_xsec.txt','data/Zprimebb_xsec.txt','data/dmbb_xsec.txt','data/bstar.txt','data/colorons.txt']
    for xsecFile in xsecFiles:
        moreThyModels = []
	f = file(xsecFile)
        for i,line in enumerate(f.readlines()):
            if line[0]=='#': continue
            line = line.replace('\n','')
            line = line.replace('\t','')
            line = line.replace('\r','')
            lineList = [l for l in line.split(" ") if l!='']
            if lineList[0]=='Mass':
                for l in lineList:
                    if l=='Mass': continue
                    thyXsecDict[l] = {}
                    moreThyModels.append(l)
            else:
                for j, thyModel in enumerate(moreThyModels):
                    thyXsecDict[thyModel][int(float(lineList[0]))] = float(lineList[j+1])
        f.close()

        thyXsecDict['AxigluonkNLO'] = {}
    for (mass,thyXsec) in thyXsecDict['Axigluon'].iteritems():
        thyXsecDict['AxigluonkNLO'][mass] = 1.08 * thyXsec
    for (mass,thyXsec) in thyXsecDict['DM1GeV'].iteritems():
        thyXsecDict['DM1GeV'][mass] = (5./6.) * thyXsec
    for (mass,thyXsec) in thyXsecDict['DMbb1GeV'].iteritems():
        thyXsecDict['DMbb1GeV'][mass] = (5./6.) * thyXsec
    return thyXsecDict


def file_key(filename):
    massPoint = re.findall("[0-9]+.000000",filename)
    gluinoMass    = massPoint[0]
    LSPMass  = massPoint[1]
    return float(gluinoMass)
    
def getHybridCLsArrays(directory, model, Box, bayes):
    if bayes:
        tfile = rt.TFile.Open("%s/xsecUL_MarkovChainMC_%s_%s.root"%(directory,model,Box))
    else:
        tfile = rt.TFile.Open("%s/xsecUL_Asymptotic_%s_%s.root"%(directory,model,Box))
    xsecTree = tfile.Get("xsecTree")
    
    gluinoMassArray = array('d')
    gluinoMassArray_er = array('d')
    observedLimit = array('d')
    observedLimit_er = array('d')
    expectedLimit = array('d')
    expectedLimit_minus1sigma = array('d')
    expectedLimit_plus1sigma = array('d')
    expectedLimit_minus2sigma = array('d')
    expectedLimit_plus2sigma = array('d')

    
    xsecTree.Draw('>>elist','','entrylist')
    elist = rt.gDirectory.Get('elist')
    entry = -1
    while True:
        entry = elist.Next()
        if entry == -1: break
        xsecTree.GetEntry(entry)

        gluinoMassArray.append(xsecTree.mass)
        gluinoMassArray_er.append(0.0)
        
        exec 'xsecULObs = xsecTree.xsecULObs_%s'%Box
        exec 'xsecULExp = xsecTree.xsecULExp_%s'%Box
        exec 'xsecULExpPlus = xsecTree.xsecULExpPlus_%s'%Box
        exec 'xsecULExpMinus = xsecTree.xsecULExpMinus_%s'%Box
        exec 'xsecULExpPlus2 = xsecTree.xsecULExpPlus2_%s'%Box
        exec 'xsecULExpMinus2 = xsecTree.xsecULExpMinus2_%s'%Box

            
            
        xsecULObs = xsecULObs
        xsecULExp = xsecULExp
        observedLimit.append(xsecULObs)#*crossSections[i])
        observedLimit_er.append(0.0)#*crossSections[i])

        expectedLimit.append(xsecULExp)#*crossSections[i])
        
            

        xsecULExpPlus = max(xsecULExpPlus,xsecULExp)
        xsecULExpMinus = min(xsecULExpMinus,xsecULExp)
        xsecULExpPlus2 = max(xsecULExpPlus2,xsecULExpPlus)
        xsecULExpMinus2 = min(xsecULExpMinus2,xsecULExpMinus)

        expectedLimit_minus1sigma.append(xsecULExp - xsecULExpMinus)#*crossSections[i])
        expectedLimit_plus1sigma.append(xsecULExpPlus - xsecULExp)#*crossSections[i])
        expectedLimit_minus2sigma.append(xsecULExp - xsecULExpMinus2)#*crossSections[i])
        expectedLimit_plus2sigma.append(xsecULExpPlus2 - xsecULExp)#*crossSections[i])

    #return gluinoMassArray, gluinoMassArray_er, observedLimit, observedLimit_er, expectedLimit, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma
    
    # sort arrays first by gluino mass (in case tree entries are out of order)
    allTuples = zip(*sorted(zip(gluinoMassArray, gluinoMassArray_er, observedLimit, observedLimit_er, expectedLimit, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma)))
    allArrays = []
    for t in allTuples:
        allArrays.append(array('d',t))
    return tuple(allArrays)


def getSignificanceArrays(directory, model, Box):
    tfile = rt.TFile.Open("%s/xsecUL_ProfileLikelihood_%s_%s.root"%(directory,model,Box))
    xsecTree = tfile.Get("xsecTree")
    
    gluinoMassArray = array('d')
    gluinoMassArray_er = array('d')
    observedLimit = array('d')
    observedLimit_er = array('d')
    expectedLimit = array('d')
    expectedLimit_minus1sigma = array('d')
    expectedLimit_plus1sigma = array('d')
    expectedLimit_minus2sigma = array('d')
    expectedLimit_plus2sigma = array('d')

    
    xsecTree.Draw('>>elist','','entrylist')
    elist = rt.gDirectory.Get('elist')
    entry = -1
    while True:
        entry = elist.Next()
        if entry == -1: break
        xsecTree.GetEntry(entry)

        gluinoMassArray.append(xsecTree.mass)
        gluinoMassArray_er.append(0.0)
        
        exec 'xsecULObs = xsecTree.xsecULObs_%s'%Box
        exec 'xsecULExp = xsecTree.xsecULExp_%s'%Box
        exec 'xsecULExpPlus = xsecTree.xsecULExpPlus_%s'%Box
        exec 'xsecULExpMinus = xsecTree.xsecULExpMinus_%s'%Box
        exec 'xsecULExpPlus2 = xsecTree.xsecULExpPlus2_%s'%Box
        exec 'xsecULExpMinus2 = xsecTree.xsecULExpMinus2_%s'%Box

            
            
        xsecULObs = xsecULObs
        xsecULExp = xsecULExp
        observedLimit.append(xsecULObs)#*crossSections[i])
        observedLimit_er.append(0.0)#*crossSections[i])

        expectedLimit.append(xsecULExp)#*crossSections[i])
        
            

        xsecULExpPlus = max(xsecULExpPlus,xsecULExp)
        xsecULExpMinus = min(xsecULExpMinus,xsecULExp)
        xsecULExpPlus2 = max(xsecULExpPlus2,xsecULExpPlus)
        xsecULExpMinus2 = min(xsecULExpMinus2,xsecULExpMinus)

        expectedLimit_minus1sigma.append(xsecULExp - xsecULExpMinus)#*crossSections[i])
        expectedLimit_plus1sigma.append(xsecULExpPlus - xsecULExp)#*crossSections[i])
        expectedLimit_minus2sigma.append(xsecULExp - xsecULExpMinus2)#*crossSections[i])
        expectedLimit_plus2sigma.append(xsecULExpPlus2 - xsecULExp)#*crossSections[i])
    
    
    #return gluinoMassArray, gluinoMassArray_er, observedLimit, observedLimit_er, expectedLimit, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma    
    # sort arrays first by gluino mass (in case tree entries are out of order)
    allTuples = zip(*sorted(zip(gluinoMassArray, gluinoMassArray_er, observedLimit, observedLimit_er, expectedLimit, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma)))
    allArrays = []
    for t in allTuples:
        allArrays.append(array('d',t))
    return tuple(allArrays)
    
def setstyle():
    # For the canvas:
    rt.gStyle.SetCanvasBorderMode(0)
    rt.gStyle.SetCanvasColor(rt.kWhite)
    rt.gStyle.SetCanvasDefH(400) #Height of canvas
    rt.gStyle.SetCanvasDefW(600) #Width of canvas
    rt.gStyle.SetCanvasDefX(0)   #POsition on screen
    rt.gStyle.SetCanvasDefY(0)
    
    # For the Pad:
    rt.gStyle.SetPadBorderMode(0)
    # rt.gStyle.SetPadBorderSize(Width_t size = 1)
    rt.gStyle.SetPadColor(rt.kWhite)
    rt.gStyle.SetPadGridX(False)
    rt.gStyle.SetPadGridY(False)
    rt.gStyle.SetGridColor(0)
    rt.gStyle.SetGridStyle(3)
    rt.gStyle.SetGridWidth(1)
    
    # For the frame:
    rt.gStyle.SetFrameBorderMode(0)
    rt.gStyle.SetFrameBorderSize(1)
    rt.gStyle.SetFrameFillColor(0)
    rt.gStyle.SetFrameFillStyle(0)
    rt.gStyle.SetFrameLineColor(1)
    rt.gStyle.SetFrameLineStyle(1)
    rt.gStyle.SetFrameLineWidth(1)
    
    # set the paper & margin sizes
    rt.gStyle.SetPaperSize(20,26)
    rt.gStyle.SetPadTopMargin(0.09)
    rt.gStyle.SetPadRightMargin(0.065)
    rt.gStyle.SetPadBottomMargin(0.15)
    rt.gStyle.SetPadLeftMargin(0.17)
    
    # use large Times-Roman fonts
    rt.gStyle.SetTitleFont(42,"xyz")  # set the all 3 axes title font
    rt.gStyle.SetTitleFont(42," ")    # set the pad title font
    rt.gStyle.SetTitleSize(0.06,"xyz") # set the 3 axes title size
    rt.gStyle.SetTitleSize(0.06," ")   # set the pad title size
    rt.gStyle.SetTitleSize(0.052,"y")   # set the pad title size
    rt.gStyle.SetTitleOffset(1.2,"y")   # set the pad title size
    rt.gStyle.SetLabelFont(42,"xyz")
    rt.gStyle.SetLabelSize(0.05,"xyz")
    rt.gStyle.SetLabelColor(1,"xyz")
    rt.gStyle.SetTextFont(42)
    rt.gStyle.SetTextSize(0.08)
    rt.gStyle.SetStatFont(42)
    
    # use bold lines and markers
    rt.gStyle.SetMarkerStyle(8)
    rt.gStyle.SetLineStyleString(2,"[12 12]") # postscript dashes
    
    #..Get rid of X error bars
    rt.gStyle.SetErrorX(0.001)
    
    # do not display any of the standard histogram decorations
    rt.gStyle.SetOptTitle(0)
    rt.gStyle.SetOptStat(0)
    rt.gStyle.SetOptFit(11111111)
    
    # put tick marks on top and RHS of plots
    rt.gStyle.SetPadTickX(1)
    rt.gStyle.SetPadTickY(1)
    
    ncontours = 999
    
    stops = [ 0.00, 0.34, 0.61, 0.84, 1.00 ]
    red =   [ 1.0,   0.95,  0.95,  0.65,   0.15 ]
    green = [ 1.0,  0.85, 0.7, 0.5,  0.3 ]
    blue =  [ 0.95, 0.6 , 0.3,  0.45, 0.65 ]
    s = array('d', stops)
    r = array('d', red)
    g = array('d', green)
    b = array('d', blue)
        
    npoints = len(s)
    rt.TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
    rt.gStyle.SetNumberContours(ncontours)
   
    rt.gStyle.cd()
        

if __name__ == '__main__':
    
    rt.gROOT.SetBatch()
    parser = OptionParser()
    parser.add_option('-b','--box',dest="box", default="CaloDijet",type="string",
                  help="box name")
    parser.add_option('-m','--model',dest="model", default="gg",type="string",
                  help="signal model name")
    parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
                  help="Input/Output directory to store output")    
    parser.add_option('-l','--lumi',dest="lumi", default=1.,type="float",
                  help="integrated luminosity in fb^-1")
    parser.add_option('--massMin',dest="massMin", default=500.,type="float",
                  help="minimum mass")
    parser.add_option('--massMax',dest="massMax", default=8000.,type="float",
                  help="maximum mass")
    parser.add_option('--xsecMin',dest="xsecMin", default=1e-4,type="float",
                  help="minimum mass")
    parser.add_option('--xsecMax',dest="xsecMax", default=1e4,type="float",
                  help="maximum mass")
    parser.add_option('--signif',dest="doSignificance",default=False,action='store_true',
                  help="for significance instead of limit")
    parser.add_option('--bayes',dest="bayes",default=False,action='store_true',
                  help="for bayesian limits")
    parser.add_option('--no-sys',dest="noSys",default=False,action='store_true',
                  help="for no systematics limits")
    parser.add_option('-o',dest="output",default='exp',type='string',
                  help="expected or observed")   

 
    (options,args) = parser.parse_args()
    Boxes = options.box.split('_')
    models = options.model.split('_')
    model = models[0]
    directory      = options.outDir
    Box = Boxes[0]
    box = Box.lower()
    output = options.output 
    
    thyXsecDict = getThyXsecDict() 
    thyModels = thyXsecDict.keys()

    thyModelsToDraw = []
    
    if options.model=='gg':
        if 'PF' in options.box:
            thyModelsToDraw = ['S8']
        else:
            thyModelsToDraw = []
    elif options.model=='qq':        
#        if 'PF' in options.box:
#            thyModelsToDraw = ['AxigluonNLO','E6Diquark',"W'","Z'",'DM1GeV']            
        if 'Sept' in options.box or 'PF' in options.box :
            thyModelsToDraw = ['colorons'] 
    elif options.model=='qg':
	if 'PFDijetbg20161tt' == options.box:
	    thyModelsToDraw = ['b*']
	elif 'MyBTag' in options.box:
	    thyModelsToDraw = ['b*']
        elif 'PF' in options.box:
            thyModelsToDraw = ['b*']
         
        else:
            thyModelsToDraw = ['b*']        
    elif options.model=='gg_qq_gaus' or options.model=='gg_qq_gaus10':
        thyModelsToDraw = ['AxigluonkNLO','E6Diquark',"W'","Z'"]
    elif options.model=='gg_qg_qq':
        thyModelsToDraw = ['String','q*','AxigluonNLO','E6Diquark','S8',"W'","Z'",'DM1GeV','RSGraviton']
    elif options.model=='gg_qg_qq_gaus' or options.model=='gg_qg_qq_gaus10':
        thyModelsToDraw = ['q*','AxigluonkNLO','E6Diquark','RSGraviton',"W'","Z'","DM1GeV"]


    lineStyle = {'RSGravitonGG':4,
                 'RSGraviton':4,
                 'Axigluon':3,
                 'AxigluonkNLO':3,
                 'AxigluonNLO':3,
                 'E6Diquark':9,
		 'colorons':4,
                 'S8':1,
                 "W'":5,
                 "Z'":6,       
                 "Zprimebb":6,       
                 "String":7,     
                 "q*":10,
		 "b*":7,
                 "DM1GeV": 8,
                 "DMbb1GeV": 8,
                 'None':1               
                 }
        
    lineColor = {'RSGravitonGG':rt.kGray+1,
                 'RSGraviton':rt.kGray+2,
		 'colorons':rt.kGray+2,
                 'Axigluon':rt.kBlue+1,
                 'AxigluonkNLO':rt.kBlue+1,
                 'AxigluonNLO':rt.kBlue+1,
                 'E6Diquark':rt.kOrange+2,
                 'S8':rt.kMagenta,
                 "W'":rt.kRed+1,
                 "Z'":rt.kBlue-1,
                 "Zprimebb":rt.kBlue-1,
                 "DM1GeV":rt.kViolet,
                 "DMbb1GeV":rt.kViolet,
                 "String":rt.kAzure-3,
                 "q*":rt.kBlack,
		 "b*":rt.kAzure-3,
                 'None':1,
                 'gg':rt.kGreen+1,
                 'qq':rt.kRed,
                 'qg':rt.kBlue,
                 'gaus':rt.kCyan+1,
                 'gaus10':rt.kCyan+1
                 }
        
    markerStyle = {'gg':24,
                 'qq':20,
                 'qg':23,
                 'gaus':26,
                 'gaus10':26
                 }
        
    legendLabel = {'RSGravitonGG':'RS graviton (gg#rightarrowG#rightarrowgg)',
                   'RSGraviton':'RS graviton',
		   'colorons':'coloron',
                   'Axigluon':     'Axiguon/coloron      ',
                   'AxigluonkNLO': 'Axiguon/coloron      ',
                   'AxigluonNLO':  'Axiguon/coloron      ',
                   'E6Diquark':'Scalar diquark',
                   'S8':'Color-octet scalar (k_{s}^{2} = 1/2) ',
                   #'S8':'Color-octet scalar',
                   'None': '',
                   "W'": "W'",
                   "Z'": "Z'",
                   "Zprimebb": "Z' to bb",
                   "DM1GeV": "DM mediator",
                   "DMbb1GeV": "DM mediator to bb",
                    "String": "String",
                    "q*": "Excited quark",
		    "b*": "Excited b quark",
                   'gg':'gluon-gluon',
                   'qq':'quark-quark',
                   'qg':'quark-gluon',
                   'gaus':'Gaussian, 7% width',
                   'gaus10':'Gaussian, 10% width'
                   }
    
    mass_xsec = {}
    sig_xsec = {}
    N_g_xsec = {}
    xsec_gr_nom = {}
    for thyModel in thyModelsToDraw:        
        mass_xsec[thyModel] = array('d')
        sig_xsec[thyModel] = array('d')
        for mg in sorted(thyXsecDict[thyModel].keys()):
            mass_xsec[thyModel].append(mg)
            sig_xsec[thyModel].append(thyXsecDict[thyModel][mg])
            
        N_g_xsec[thyModel] = len(mass_xsec[thyModel])
        xsec_gr_nom[thyModel] = rt.TGraph(N_g_xsec[thyModel], mass_xsec[thyModel], sig_xsec[thyModel])
        xsec_gr_nom[thyModel].SetMarkerSize(0)
        xsec_gr_nom[thyModel].SetLineWidth(2)
        xsec_gr_nom[thyModel].SetLineStyle(lineStyle[thyModel])
        xsec_gr_nom[thyModel].SetLineColor(lineColor[thyModel])

    setstyle()
    rt.gStyle.SetOptStat(0)
    c = rt.TCanvas("c","c",800,800)
    if options.doSignificance:
        c.SetLogy(0)
    else:        
        c.SetLogy()

    h_limit = rt.TMultiGraph()
    gr_observedLimit = {}
    gr_expectedLimit = {}
    gr_expectedLimit2sigma = {}
    gr_expectedLimit1sigma = {}
    gluinoMassArray = {}
    gluinoMassArray_er = {}
    observedLimit = {}
    observedLimit_er = {}
    expectedLimit = {}
    expectedLimit_minus1sigma = {}
    expectedLimit_plus1sigma = {}
    expectedLimit_minus2sigma = {}
    expectedLimit_plus2sigma = {}
    
    if options.doSignificance:
        h_limit.SetTitle(" ;Resonance mass [GeV];Local significance n#sigma")
    else:
        h_limit.SetTitle(" ;Resonance mass [GeV]; #sigma #times #bf{#it{#Beta}} #times #bf{#it{#Alpha}} [pb]")

    for Box in Boxes:
        for model in models:
            if len(models)>1:
                #directory =  options.outDir+'/%s_IntermediateRange'%model
                directory =  options.outDir+'/%s'%model
            if options.doSignificance:
                gluinoMassArray[(Box,model)], gluinoMassArray_er[(Box,model)], observedLimit[(Box,model)], observedLimit_er[(Box,model)], expectedLimit[(Box,model)], expectedLimit_minus1sigma[(Box,model)], expectedLimit_plus1sigma[(Box,model)], expectedLimit_minus2sigma[(Box,model)], expectedLimit_plus2sigma[(Box,model)] = getSignificanceArrays(directory, model, Box)
            else:
                gluinoMassArray[(Box,model)], gluinoMassArray_er[(Box,model)], observedLimit[(Box,model)], observedLimit_er[(Box,model)], expectedLimit[(Box,model)], expectedLimit_minus1sigma[(Box,model)], expectedLimit_plus1sigma[(Box,model)], expectedLimit_minus2sigma[(Box,model)], expectedLimit_plus2sigma[(Box,model)] = getHybridCLsArrays(directory, model, Box, options.bayes)




	    for thyModel in thyModelsToDraw:
	      if output=='exp':
	         print thyModel
	         FindPoint(gluinoMassArray[(Box,model)], expectedLimit[(Box,model)], mass_xsec[thyModel], sig_xsec[thyModel])
	         print
              if output=='obs': 
                 print thyModel
                 FindPoint(gluinoMassArray[(Box,model)], observedLimit[(Box,model)], mass_xsec[thyModel], sig_xsec[thyModel])
                 print
            nPoints = len(observedLimit[(Box,model)])


            gr_observedLimit[(Box,model)] = rt.TGraph(nPoints, gluinoMassArray[(Box,model)], observedLimit[(Box,model)])
            gr_observedLimit[(Box,model)].SetMarkerColor(1)
            gr_observedLimit[(Box,model)].SetMarkerStyle(22)
            gr_observedLimit[(Box,model)].SetMarkerSize(1)
            gr_observedLimit[(Box,model)].SetLineWidth(3)
            gr_observedLimit[(Box,model)].SetLineColor(rt.kBlack)
            gr_observedLimit[(Box,model)].SetMarkerStyle(20)
            if len(models)>1:
                gr_observedLimit[(Box,model)].SetLineColor(lineColor[model])
                gr_observedLimit[(Box,model)].SetMarkerStyle(markerStyle[model])
                gr_observedLimit[(Box,model)].SetMarkerColor(lineColor[model])


            gr_expectedLimit[(Box,model)] = rt.TGraph(nPoints, gluinoMassArray[(Box,model)], expectedLimit[(Box,model)])
            gr_expectedLimit[(Box,model)].SetLineWidth(3)
            gr_expectedLimit[(Box,model)].SetLineStyle(2)
            if len(models)>1:
                gr_expectedLimit[(Box,model)].SetLineColor(lineColor[model])

            gr_expectedLimit2sigma[(Box,model)] = rt.TGraphAsymmErrors(nPoints, gluinoMassArray[(Box,model)], expectedLimit[(Box,model)], gluinoMassArray_er[(Box,model)], gluinoMassArray_er[(Box,model)], expectedLimit_minus2sigma[(Box,model)], expectedLimit_plus2sigma[(Box,model)])
            #gr_expectedLimit2sigma[(Box,model)].SetLineColor(5)
            #gr_expectedLimit2sigma[(Box,model)].SetFillColor(5)
            gr_expectedLimit2sigma[(Box,model)].SetLineColor(rt.kOrange)
            gr_expectedLimit2sigma[(Box,model)].SetFillColor(rt.kOrange)
            gr_expectedLimit2sigma[(Box,model)].SetFillStyle(1001)

            gr_expectedLimit1sigma[(Box,model)] = rt.TGraphAsymmErrors(nPoints, gluinoMassArray[(Box,model)], expectedLimit[(Box,model)], gluinoMassArray_er[(Box,model)], gluinoMassArray_er[(Box,model)], expectedLimit_minus1sigma[(Box,model)], expectedLimit_plus1sigma[(Box,model)])

            #gr_expectedLimit1sigma[(Box,model)].SetLineColor(rt.kGreen-7)
            #gr_expectedLimit1sigma[(Box,model)].SetFillColor(rt.kGreen-7)
            gr_expectedLimit1sigma[(Box,model)].SetLineColor(rt.kGreen+1)
            gr_expectedLimit1sigma[(Box,model)].SetFillColor(rt.kGreen+1)

            if len(models)==1:
                h_limit.Add(gr_expectedLimit2sigma[(Box,model)])
                h_limit.Add(gr_expectedLimit1sigma[(Box,model)])
            h_limit.Add(gr_observedLimit[(Box,model)])

        
    for thyModel in thyModelsToDraw:
        h_limit.Add(xsec_gr_nom[thyModel])
        
    h_limit.Draw("a3")
    if 'PF' in Box:
        h_limit.GetXaxis().SetLimits(options.massMin,options.massMax)
    else:
        h_limit.GetXaxis().SetLimits(options.massMin,options.massMax)
    if options.doSignificance:
        h_limit.SetMaximum(4)
        h_limit.SetMinimum(0)
    else:
        if 'PF' in Box:
            h_limit.SetMaximum(options.xsecMax)
            h_limit.SetMinimum(options.xsecMin)
        else:
            h_limit.SetMaximum(options.xsecMax)
            h_limit.SetMinimum(options.xsecMin)
            
    h_limit.Draw("a3")
    if options.doSignificance:
        h_limit.GetYaxis().SetNdivisions(405,True)

    for Box in Boxes:
        for model in models:    
            if options.doSignificance:
                gr_observedLimit[(Box,model)].SetMarkerStyle(21)
                gr_observedLimit[(Box,model)].SetMarkerSize(1)
                gr_observedLimit[(Box,model)].SetLineColor(rt.kRed)
                gr_observedLimit[(Box,model)].SetMarkerColor(rt.kBlue)
                gr_observedLimit[(Box,model)].Draw("lp SAME")
            else:
                if len(models)==1:
                    gr_expectedLimit[(Box,model)].Draw("c same")
                for thyModel in thyModelsToDraw:
                    xsec_gr_nom[thyModel].Draw("c same")
                gr_observedLimit[(Box,model)].Draw("lp SAME")

            gr_expectedLimit1sigma[(Box,model)].SetLineStyle(2)
            gr_expectedLimit1sigma[(Box,model)].SetLineWidth(3)
            gr_expectedLimit1sigma[(Box,model)].SetLineColor(rt.kBlack)
            gr_expectedLimit2sigma[(Box,model)].SetLineStyle(2)
            gr_expectedLimit2sigma[(Box,model)].SetLineWidth(3)
            gr_expectedLimit2sigma[(Box,model)].SetLineColor(rt.kBlack)
    
    l = rt.TLatex()
    l.SetTextAlign(11)
    l.SetTextSize(0.045)
    l.SetNDC()
    l.SetTextFont(62)
    #l.DrawLatex(0.17,0.92,"CMS")    
    if len(Boxes)>1 and len(models)>1:
        l.DrawLatex(0.3,0.92,"CMS Preliminary")
    elif len(Boxes)>1:
        l.DrawLatex(0.41,0.92,"CMS Preliminary")
    else:
        l.DrawLatex(0.2,0.92,"CMS Preliminary")
        
    l.SetTextFont(52)
    #l.DrawLatex(0.28,0.92,"Preliminary")
    l.SetTextFont(42)
    #l.DrawLatex(0.65,0.92,"%.0f pb^{-1} (13 TeV)"%(options.lumi*1000))
    l.DrawLatex(0.63,0.92,"%.1f fb^{-1} (13 TeV)"%(options.lumi))
    
    if options.model=="gg":
        if len(Boxes)>1:
            l.DrawLatex(0.3,0.77,"gluon-gluon")
        else:
            l.DrawLatex(0.3,0.77,"gluon-gluon")
    elif options.model=="qg":        
        if len(Boxes)>1:
            l.DrawLatex(0.3,0.77,"quark-gluon")
        else:
            l.DrawLatex(0.3,0.77,"quark-gluon")
    elif options.model=="qq":
        if len(Boxes)>1:
            l.DrawLatex(0.3,0.77,"quark-quark")
        else:
            l.DrawLatex(0.3,0.77,"quark-quark")
    elif options.model=="gaus":
        l.SetTextSize(0.04)
        if len(Boxes)>1:
            l.DrawLatex(0.24,0.79,"Gaussian, 7% width")
        else:
            l.DrawLatex(0.24,0.835,"Gaussian, 7% width")
        l.SetTextSize(0.045)
    elif options.model=="gaus10":
        l.SetTextSize(0.04)
        if len(Boxes)>1:
            l.DrawLatex(0.3,0.79,"#splitline{Gaussian}{10% width}")
        else:            
            l.DrawLatex(0.3,0.77,"#splitline{Gaussian}{10% width}")
        l.SetTextSize(0.045)

    #if options.bayes:
    #    if options.noSys:        
    #        l.DrawLatex(0.2,0.85,"Bayesian, no syst.")
    #    else:
    #        l.DrawLatex(0.2,0.85,"Bayesian, with syst.")
    #else:        
    #    if options.noSys:        
    #        l.DrawLatex(0.2,0.85,"Frequentist, no syst.")
    #    else:
    #        l.DrawLatex(0.2,0.85,"Frequentist, with syst.")

    if options.doSignificance:
        c.SetGridy()
        leg = rt.TLegend(0.55,0.79,0.92,0.87)      
    elif options.model =="gg_qg_qq" and options.box=="CaloDijet2016_PFDijet2016":
        leg = rt.TLegend(0.19,0.17,0.57,0.35)        
    else:        
        leg = rt.TLegend(0.55,0.68,0.92,0.87)
    
    leg.SetTextFont(42)
    leg.SetFillColorAlpha(0,0)
    leg.SetLineColor(0)
    if not options.doSignificance:
        leg.SetHeader("95% CL limits")
    if len(models)==1:
        if options.doSignificance:
            leg.AddEntry(gr_observedLimit[(Box,model)], "Observed","lp")
        else:
            #leg.AddEntry(None,"95% CL limits","")
            #leg.AddEntry(None,"90% CL limits","")
            leg.AddEntry(gr_observedLimit[(Box,model)], "Observed","lp")
        if not options.doSignificance:
            leg.AddEntry(gr_expectedLimit1sigma[(Box,model)], "Expected #pm 1 s.d.","lf")    
        if not options.doSignificance:
            leg.AddEntry(gr_expectedLimit2sigma[(Box,model)], "Expected #pm 2 s.d.","lf")
    else:
        #leg.AddEntry(None,"95% CL limits","")
        #leg.AddEntry(None,"90% CL limits","")
        for model in models:
            leg.AddEntry(gr_observedLimit[(Box,model)], legendLabel[model],"lp")
            
    leg.Draw("SAME")
        
    if len(thyModelsToDraw)>0 and not options.doSignificance:        
        if options.model =="gg_qg_qq" and options.box=="CaloDijet2016_PFDijet2016":
            #legThyModel = rt.TLegend(0.2,0.17,0.55,0.45)
            legThyModel = rt.TLegend(0.45,0.7,0.9,0.92)
            legThyModel2 = rt.TLegend(0.55,0.54,0.9,0.7)            
            legThyModel2.SetTextFont(42)
            legThyModel2.SetFillColor(rt.kWhite)
            legThyModel2.SetLineColor(rt.kWhite)
            legThyModel2.SetFillColorAlpha(0,0)
            legThyModel2.SetLineColorAlpha(0,0)
        elif options.model =="gg":
            #legThyModel = rt.TLegend(0.2,0.17,0.6,0.4)
            legThyModel = rt.TLegend(0.2,0.17,0.7,0.4)
        else:
            legThyModel = rt.TLegend(0.2,0.17,0.55,0.4)
        legThyModel.SetTextFont(42)
        legThyModel.SetFillColor(rt.kWhite)
        legThyModel.SetLineColor(rt.kWhite)
        legThyModel.SetFillColorAlpha(0,0)
        legThyModel.SetLineColorAlpha(0,0)
        
        if model=='qq':
            legThyModel.AddEntry(None,"","")
        elif model=='gg':            
            legThyModel.AddEntry(None,"","")
            
        for i, thyModel in enumerate(thyModelsToDraw):
            if i>4:
                try:
                    legThyModel2.AddEntry(xsec_gr_nom[thyModel], legendLabel[thyModel],'l')
                except:
                    pass
            else:
                legThyModel.AddEntry(xsec_gr_nom[thyModel], legendLabel[thyModel],'l')
        legThyModel.Draw("same")
        try:
            legThyModel2.Draw("same")
        except:
            pass
            

    for Box in Boxes:
        for model in models:    
            if options.doSignificance:
                gr_observedLimit[(Box,model)].Draw("lp SAME")
            else:
                if len(models)==1:
                    gr_expectedLimit[(Box,model)].Draw("c same")
                for thyModel in thyModelsToDraw:
                    xsec_gr_nom[thyModel].Draw("c same")
                gr_observedLimit[(Box,model)].Draw("lp SAME")


    if 'PF' in Box or options.massMax>1600:
        h_limit.GetXaxis().SetTitle('Resonance mass [TeV]')
        h_limit.GetXaxis().SetLabelOffset(1000)
        #h_fit_residual_vs_mass.GetXaxis().SetNoExponent()
        #h_fit_residual_vs_mass.GetXaxis().SetMoreLogLabels()    
        xLab = rt.TLatex()
        xLab.SetTextAlign(22)
        xLab.SetTextSize(0.05)
        xLab.SetTextFont(42)
        xLab.SetTextSize(0.05)
        if options.doSignificance:
            yOffset = -0.138
        else:
            #yOffset = 6.5e-5 # for 1e-4 min
            #yOffset = 5.25e-6 # for 1e-5 min
            yOffset = 5.25e-5 # for 1e-5 min
        for i in range(1,10):
            if i*1000>=options.massMin:
                xLab.DrawLatex(i*1000, yOffset, "%g"%i)

    else:
        h_limit.GetXaxis().SetNdivisions(408,True)

    if options.box=="CaloDijet2016_PFDijet2016":
        #line1 = rt.TLine(1600,1e4,1600,options.xsecMax)
        line1 = rt.TLine(1600,1e-1,1600,options.xsecMax)
        line1.SetLineStyle(2)
        line1.SetLineWidth(2)
        line1.SetLineColor(rt.kGray+1)
        line1.Draw()
        #line2 = rt.TLine(1600,1e-1,1600,2)
        #line2.SetLineStyle(2)
        #line2.SetLineWidth(2)
        #line2.SetLineColor(rt.kGray+1)
        #line2.Draw()
        
          
        lab = rt.TLatex()
        lab.SetTextSize(0.035)
        lab.SetTextFont(42)
        lab.SetTextColor(rt.kGray+1)
        lab.SetTextAlign(33)
        lab.DrawLatex(1600-10,6e4,"#leftarrow")
        lab.SetTextAlign(13)
        lab.DrawLatex(1600+10,6e4,"#rightarrow") 
        lab.SetTextAlign(23)
        lab.DrawLatex(1600-400,3.5e4,"Low")
        lab.DrawLatex(1600-400,1.2e4,"mass")
        lab.DrawLatex(1600+400,3.5e4,"High")
        lab.DrawLatex(1600+400,1.2e4,"mass")
        

    #c.SetLogx()    
    c.RedrawAxis() # request from David
    if options.doSignificance:
        c.SaveAs(options.outDir+"/signif_"+options.model+"_"+options.box.lower()+".pdf")
        c.SaveAs(options.outDir+"/signif_"+options.model+"_"+options.box.lower()+".C")
    else:
        if options.bayes:
            if options.noSys:
                c.SaveAs(options.outDir+"/limits_bayes_nosys_"+options.model+"_"+options.box.lower()+".pdf")
                c.SaveAs(options.outDir+"/limits_bayes_nosys_"+options.model+"_"+options.box.lower()+".C")
            else:
                c.SaveAs(options.outDir+"/limits_bayes_"+options.model+"_"+options.box.lower()+".pdf")
                c.SaveAs(options.outDir+"/limits_bayes_"+options.model+"_"+options.box.lower()+".C")
        else:
            if options.noSys:
                c.SaveAs(options.outDir+"/limits_freq_nosys_"+options.model+"_"+options.box.lower()+".pdf")
                c.SaveAs(options.outDir+"/limits_freq_nosys_"+options.model+"_"+options.box.lower()+".C")
            else:
                c.SaveAs(options.outDir+"/limits_freq_"+options.model+"_"+options.box.lower()+".pdf")
                c.SaveAs(options.outDir+"/limits_freq_"+options.model+"_"+options.box.lower()+".C")
                outFile = rt.TFile.Open(options.outDir+"/limits_freq_"+options.model+"_"+options.box.lower()+".root","recreate")
                outFile.cd()
                c.Write()
                graphDict = {}
                graphDict['obs'] = gr_observedLimit
                graphDict['exp'] = gr_expectedLimit
                graphDict['exp1sigma'] = gr_expectedLimit1sigma
                graphDict['exp2sigma'] = gr_expectedLimit2sigma
                for limitType, graphs in graphDict.iteritems(): 
                    for (Box,model), graph in graphs.iteritems():
                        graph.SetName('%s_%s_%s'%(limitType,model,Box.lower()))
                        graph.Write()

