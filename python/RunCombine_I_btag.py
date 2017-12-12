from optparse import OptionParser
import os
import ROOT as rt
from array import *
from framework import Config
import sys
import glob
import rootTools
import time

NSIGMA = 10.0

def massIterable(massList):
    if len(massList.split(','))==1:
        massIterableList = [massList]
    else:
        massIterableList = list(eval(massList))
    return massIterableList

def exec_me(command,dryRun=True):
    print command
    if not dryRun: os.system(command)

def writeBashScript(options,massPoint,iJob=0):

    lumiFloat = [float(lumiStr) for lumiStr in options.lumi.split('_')]
    lumiTotal = sum(lumiFloat)

    submitDir = options.outDir
    massPoint = str(massPoint)


    signalSys = ''
    if options.noSignalSys:
        signalSys = '--no-signal-sys'
    elif options.noSys:
        signalSys = '--no-sys'

    penaltyString = ''
    if options.penalty:
        penaltyString = '--penalty'

    decoString = ''
    if options.deco:
        decoString  ='--deco'

    bayesString = ''
    if options.bayes:
        bayesString  ='--bayes'

    toyString = ''
    if options.toys>-1:
        toyString  ='--toys %i'%options.toys

    xsecString = '--xsec %f'%options.xsec

    signifString = ''
    if options.signif:
        signifString = '--signif'

    # prepare the script to run
    outputname = submitDir+"/submit_"+options.model+"_"+massPoint+"_lumi-%.3f_"%(lumiTotal)+options.box+"_%i"%(iJob)+".src"

    ffDir = submitDir+"/logs_"+options.model+"_"+massPoint+"_"+options.box+"_%i"%(iJob)
    user = os.environ['USER']
    pwd = os.environ['PWD']

    if options.noSys:
        combineDir = "/afs/cern.ch/work/%s/%s/DIJET/Limits/%s_nosys/"%(user[0],user,options.model) # directory where combine output files will be copied
    else:
        combineDir = "/afs/cern.ch/work/%s/%s/DIJET/Limits/%s/"%(user[0],user,options.model) # directory where combine output files will be copied
    cmsswBase = "/afs/cern.ch/work/%s/%s/DIJET/CMSSW_7_4_14"%(user[0],user) # directory where 'cmsenv' will be run (needs to have combine setup)

    script =  '#!/usr/bin/env bash -x\n'
    script += 'mkdir -p %s\n'%combineDir
    script += 'echo $SHELL\n'
    script += 'pwd\n'
    script += 'cd %s/src/CMSDIJET/DijetRootTreeAnalyzer \n'%(cmsswBase)
    script += 'pwd\n'
    script += "export SCRAM_ARCH=slc6_amd64_gcc491\n"
    script += "export CMSSW_BASE=%s\n"%(cmsswBase)
    script += 'eval `scramv1 runtime -sh`\n'
    script += 'cd - \n'
    script += "export TWD=${PWD}/%s_%s_lumi-%.3f_%s\n"%(options.model,massPoint,lumiTotal,options.box)
    script += "mkdir -p $TWD\n"
    script += "cd $TWD\n"
    script += 'pwd\n'
    script += 'git clone git@github.com:CMSDIJET/DijetRootTreeAnalyzer CMSDIJET/DijetRootTreeAnalyzer\n'
    script += 'cd CMSDIJET/DijetRootTreeAnalyzer\n'
    script += 'git checkout -b Limits %s\n'%(options.tag)
    script += 'mkdir -p %s\n'%submitDir
    if 'CaloDijet2015' in options.box.split('_') or options.box=='CaloDijet20152016':
        script += 'wget https://github.com/CMSDIJET/DijetShapeInterpolator/raw/master/ResonanceShapes_%s_13TeV_CaloScouting_Spring15.root -P inputs/\n'%(options.model)
        for sys in ['JERUP','JERDOWN','JESUP','JESDOWN']:
            script += 'wget https://github.com/CMSDIJET/DijetShapeInterpolator/raw/master/ResonanceShapes_%s_13TeV_CaloScouting_Spring15_%s.root -P inputs/\n'%(options.model,sys)
    if 'CaloDijet2016' in options.box.split('_'):
        script += 'wget https://github.com/CMSDIJET/DijetShapeInterpolator/raw/master/ResonanceShapes_%s_13TeV_CaloScouting_Spring16.root -P inputs/\n'%(options.model)
        for sys in ['JERUP','JERDOWN','JESUP','JESDOWN']:
            script += 'wget https://github.com/CMSDIJET/DijetShapeInterpolator/raw/master/ResonanceShapes_%s_13TeV_CaloScouting_Spring16_%s.root -P inputs/\n'%(options.model,sys)
    if 'PFDijet2016' in options.box.split('_'):
        script += 'wget https://github.com/CMSDIJET/DijetShapeInterpolator/raw/master/ResonanceShapes_%s_13TeV_Spring16.root -P inputs/\n'%(options.model)
        for sys in ['JERUP','JESUP','JESDOWN']:
            script += 'wget https://github.com/CMSDIJET/DijetShapeInterpolator/raw/master/ResonanceShapes_%s_13TeV_Spring16_%s.root -P inputs/\n'%(options.model,sys)
    script += 'python python/RunCombine.py -i %s -m %s --mass %s -c %s --lumi %s -d %s -b %s %s %s --min-tol %e --min-strat %i --rMax %f %s %s %s %s %s\n'%(options.inputFitFile,
                                                                                                                                                         options.model,
                                                                                                                                                         massPoint,
                                                                                                                                                         options.config,
                                                                                                                                                         options.lumi,
                                                                                                                                                         submitDir,
                                                                                                                                                         options.box,
                                                                                                                                                         penaltyString,
                                                                                                                                                         signalSys,
                                                                                                                                                         options.min_tol,
                                                                                                                                                         options.min_strat,
                                                                                                                                                         options.rMax,
                                                                                                                                                         decoString,
                                                                                                                                                         bayesString,
                                                                                                                                                         toyString,
                                                                                                                                                         xsecString,
                                                                                                                                                         signifString)
    script += 'cp %s/higgsCombine* %s/\n'%(submitDir,combineDir)
    script += 'cd ../..\n'
    script += 'rm -rf $TWD\n'

    outputfile = open(outputname,'w')
    outputfile.write(script)
    outputfile.close

    return outputname,ffDir

def submit_jobs(options,args):

    for massPoint in massIterable(options.mass):

        for iJob in range(0,options.jobs):
            outputname,ffDir = writeBashScript(options,massPoint,iJob)

            pwd = os.environ['PWD']
            os.system("mkdir -p "+pwd+"/"+ffDir)
            os.system("echo bsub -q "+options.queue+" -o "+pwd+"/"+ffDir+"/log.log source "+pwd+"/"+outputname)
            if not options.dryRun:
                time.sleep(3)
                os.system("bsub -q "+options.queue+" -o "+pwd+"/"+ffDir+"/log.log source "+pwd+"/"+outputname)

def main(options,args):

    boxes = options.box.split('_')

    signif = options.signif

    model = options.model

    lumiFloat = [float(lumiStr) for lumiStr in options.lumi.split('_')]

    rRangeStringList = []
    sysStringList = []

    pdfIndexMap = {'modexp': 0,
                   'fiveparam': 1,
                   'atlas': 2,
                   }

    for box,lumi in zip(boxes,lumiFloat):

        paramDict = {}
        if options.inputFitFile is not None and options.bayes:
            inputRootFile = rt.TFile.Open(options.inputFitFile,"r")
            wIn = inputRootFile.Get("w"+box).Clone("wIn"+box)
            if wIn.obj("fitresult_extDijetPdf_data_obs") != None:
                frIn = wIn.obj("fitresult_extDijetPdf_data_obs")
            elif wIn.obj("nll_extDijetPdf_data_obs") != None:
                frIn = wIn.obj("nll_extDijetPdf_data_obs")
            elif wIn.obj("fitresult_extDijetPdf_data_obs_with_constr") != None:
                fr = wIn.obj("fitresult_extDijetPdf_data_obs_with_constr")
            elif wIn.obj("nll_extDijetPdf_data_obs_with_constr") != None:
                frIn = wIn.obj("nll_extDijetPdf_data_obs_with_constr")
            elif wIn.obj("simNll") != None:
                frIn = wIn.obj("simNll")
            paramDict = {}
            for p in rootTools.RootIterator.RootIterator(frIn.floatParsFinal()):
                paramDict[p.GetName()] = [p.getVal(), p.getError()]
            print "grabbing parameter ranges +-%gsigma for bayesian"%NSIGMA


        signalSys = ''
        if options.noSignalSys or options.noSys:
            signalSys = '--no-signal-sys'
        else:
            if box=='CaloDijet2015' or box=='CaloDijet20152016':
                signalSys  =   '--jesUp inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring15_JESUP.root --jesDown inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring15_JESDOWN.root'%(model,model)
                signalSys += ' --jerUp inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring15_JERUP.root --jerDown inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring15_JERDOWN.root'%(model,model)
            elif box=='CaloDijet2016':
                signalSys  =   '--jesUp inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring16_JESUP.root --jesDown inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring16_JESDOWN.root'%(model,model)
                signalSys += ' --jerUp inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring16_JERUP.root --jerDown inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring16_JERDOWN.root'%(model,model)
            elif box=='PFDijet2016':
                signalSys  =   '--jesUp inputs/ResonanceShapes_%s_13TeV_Spring16_JESUP.root --jesDown inputs/ResonanceShapes_%s_13TeV_Spring16_JESDOWN.root'%(model,model)
                signalSys += ' --jerUp inputs/ResonanceShapes_%s_13TeV_Spring16_JERUP.root'%(model)
            elif box=='PFDijetbg20161tt':
                signalSys  = '--jesUp inputs/Inter_U/ResonanceShapes_qg_bg_13TeV_Spring16_Interpolation_JESUP_rescale.root --jesDown  inputs/Inter_U/ResonanceShapes_qg_bg_13TeV_Spring16_Interpolation_JESDOWN_rescale.root'
                signalSys += ' --jerUp inputs/Inter_U/ResonanceShapes_qg_bg_13TeV_Spring16_Interpolation_JER_rescale.root'
	    elif box=='PFDijetbb20162tt':	
	         signalSys = '--jesUp inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_med_Interpolation_JESUP_rescale.root --jesDown inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_med_Interpolation_JESDOWN_rescale.root'
	         signalSys += ' --jerUp inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_med_Interpolation_JER_rescale.root'
            elif box=='PFDijetbb20162mm2':
                signalSys = '--jesUp inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation.root --jesDown inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation.root'
                signalSys += ' --jerUp inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation.root'
            elif box=='PFDijetbb20162mm':
                signalSys = '--jesUp inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
	        signalSys += ' --jerUp inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
	    elif box=='PFDijetbg20161MyBTag050':
	        signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
	    	signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag060':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag070':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag080':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag090':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag085':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag095':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag091':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_910_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_910_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_910_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag093':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_930_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_930_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_930_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag097':
                signalSys = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_970_JESUP_Interpolation_rescale.root  --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_970_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_970_JER_Interpolation_rescale.root'
	    elif box=='PFDijetbg20161ttwithW':
	        signalSys = '--jesUp inputs/Weight_yn/ResonanceShapes_qg_bg_13TeV_Spring16_JESUP_withW_Interpolation_rescale.root --jesDown inputs/Weight_yn/ResonanceShapes_qg_bg_13TeV_Spring16_JESDOWN_withW_Interpolation_rescale.root'
	        signalSys += ' --jerUp inputs/Weight_yn/ResonanceShapes_qg_bg_13TeV_Spring16_JER_withW_Interpolation_rescale.root'
	    elif box=='PFDijetbg20161ttwithoutW':
		        signalSys = '--jesUp inputs/Weight_yn/ResonanceShapes_qg_bg_13TeV_Spring16_JESUP_Interpolation_rescale.root --jesDown inputs/Weight_yn/ResonanceShapes_qg_bg_13TeV_Spring16_JESDOWN_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/Weight_yn/ResonanceShapes_qg_bg_13TeV_Spring16_JER_Interpolation_rescale.root'
	    elif box=='PFDijetbg20161MyBTag081':
		        signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_810_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_810_JESDOWN_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_810_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag082':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_820_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_820_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_820_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag083':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_830_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_830_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_830_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag084':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_840_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_840_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_840_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag086':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_860_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_860_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_860_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag087':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_870_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_870_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_870_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag088':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_880_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_880_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_880_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag089':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_890_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_890_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_890_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag092':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_920_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_920_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_920_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20161MyBTag094':
                signalSys  = '--jesUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_940_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_940_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation/ResonanceShapes_qg_bg_13TeV_Spring16_940_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag050':
		        signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag060':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag070':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag080':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag081':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_810_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_810_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_810_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag082':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_820_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_820_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_820_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag083':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_830_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_830_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_830_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag084':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_840_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_840_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_840_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag085':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag086':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_860_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_860_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_860_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag087':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_870_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_870_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_870_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag088':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_880_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_880_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_880_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag089':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_890_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_890_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_890_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag090':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag091':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_910_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_910_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_910_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag092':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_920_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_920_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_920_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag093':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_930_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_930_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_930_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb20162MyBTag094':
                signalSys  = '--jesUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_940_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_940_JESDOWN_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Scan_Interpolation_bb/ResonanceShapes_qq_bg_13TeV_Spring16_940_JER_Interpolation_rescale.root'
	    elif box=='PFDijetbb20162ttQI':
		        signalSys  = '--jesUp inputs/Newbb/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/Newbb/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/Newbb/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
	    elif box=='PFDijetbb20162mmD':
		        signalSys  = '--jesUp inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_DOWN_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_DOWN_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_DOWN_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbb20162mmU':
                signalSys  = '--jesUp inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_UP_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_UP_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_UP_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbb20162mmC':
                signalSys  = '--jesUp inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_central_JESUP_Inter_Interpolation_rescale.root --jesDown  inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_central_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_central_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbb20162mm9':
                signalSys  = '--jesUp inputs/Inter_09/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/Inter_09/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/Inter_09/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbg20161ttC':
		        signalSys  = '--jesUp inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_central_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_central_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_central_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbg20161ttU':
                signalSys  = '--jesUp inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_UP_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_UP_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_UP_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbg20161ttD':
                signalSys  = '--jesUp inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_DOWN_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_DOWN_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys += ' --jerUp inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_DOWN_JER_Inter_Interpolation_rescale.root'
	    elif box=='PFDijetbg20161ttG':
                signalSys  = '--jesUp inputs/Gaus/ResonanceShapes_gaus10_13TeV_Spring16_JESUP_rescale.root --jesDown inputs/Gaus/ResonanceShapes_gaus10_13TeV_Spring16_JESDOWN_rescale.root'
                signalSys += ' --jerUp inputs/Gaus/ResonanceShapes_gaus10_13TeV_Spring16_JERUP_rescale.root'
	    elif box == 'PFDijetbb20161mm1btag':
		        signalSys  = '--jesUp inputs/1btag_mm_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/1btag_mm_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys += ' --jerUp inputs/1btag_mm_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
	    elif box == 'PFDijetbb20161tt1btag':
                signalSys = '--jesUp inputs/1btag_tt_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/1btag_tt_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp  inputs/1btag_tt_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'

	    elif box == 'PFDijetbb20161mmle1':
		        signalSys = '--jesUp inputs/1btag_mm_coloron_Uncertainty_le1/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/1btag_mm_coloron_Uncertainty_le1/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys +=' --jerUp inputs/1btag_mm_coloron_Uncertainty_le1/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
	    elif box == 'PFDijetbb20161tt':
		        signalSys = '--jesUp inputs/1ttColoron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/1ttColoron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root '
		        signalSys +=' --jerUp inputs/1ttColoron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
 	    elif box == 'PFDijetbb20161mmMyBTag050':
	        	signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
		        signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag060':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag070':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag080':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag090':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag091':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_910_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_910_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag092':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_920_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_920_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag093':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_930_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_930_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag094':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_940_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_940_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag095':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag096':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_960_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_960_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag082':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_820_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_820_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag084':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_840_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_840_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag086':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_860_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_860_JER_Interpolation_rescale.root'
            elif box == 'PFDijetbb20161mmMyBTag088':
                signalSys = '--jesUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_880_JESUP_Interpolation_rescale.root --jesDown inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_880_JER_Interpolation_rescale.root'
	    elif box == 'PFDijetbb20161mm1btag2':
		        signalSys = '--jesUp inputs/Coloron_bb_tight_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown inputs/Coloron_bb_tight_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys +=' --jerUp inputs/Coloron_bb_tight_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif  box == 'PFDijetbb2016le1mm':
                signalSys = '--jesUp signalHistos_bb_shape2_medium/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bb_shape2_medium/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_shape2_medium/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif  box == 'PFDijetbb2016le1tt':
                signalSys = '--jesUp signalHistos_bb_shape2_tight/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root  --jesDown  signalHistos_bb_shape2_tight/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_shape2_tight/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif  box == 'PFDijetbg2016le1mmN':
		        signalSys = '--jesUp   signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root  '
		        signalSys +=' --jerUp signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif  box == 'PFDijetbb2016le1mmN':
                signalSys = '--jesUp signalHistos_bb_New_K_medium/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bb_New_K_medium/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_New_K_medium/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif  box == 'PFDijetbg2016le1ttN':
	        	signalSys +=' --jesUp  signalHistos_bg_New_K_tight/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bg_New_K_tight/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root '
	        	signalSys +=' --jerUp  signalHistos_bg_New_K_tight/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root '
            elif  box == 'PFDijetbb2016le1ttN':
                signalSys +=' --jesUp  signalHistos_bb_New_K_tight/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root  --jesDown signalHistos_bb_New_K_tight/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root '
                signalSys +=' --jerUp  signalHistos_bb_New_K_tight/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root '
            elif  box == 'PFDijetbg2016le1mmO':
                signalSys +=' --jesUp signalHistos_bg_shape_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bg_shape_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_shape_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
	    elif  box == 'PFDijetbg2016woCSV':
		        signalSys +=' --jesUp signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation.root --jesDown signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation.root'
		        signalSys +=' --jerUp signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation.root'
            elif  box == 'PFDijetbg2016Gtt':
	        	signalSys +=' --jesUp signalHistos_bg_gaussian_tight/ResonanceShapes_gaus10_13TeV_Spring16_JESUP_rescale.root --jesDown signalHistos_bg_gaussian_tight/ResonanceShapes_gaus10_13TeV_Spring16_JESDOWN_rescale.root'
		        signalSys +=' --jerUp signalHistos_bg_gaussian_tight/ResonanceShapes_gaus10_13TeV_Spring16_JERUP_rescale.root'
            elif  box == 'PFDijetbg2016Gmm':
                signalSys +=' --jesUp signalHistos_bg_gaussian_medium/ResonanceShapes_gaus10_13TeV_Spring16_JESUP_rescale.root --jesDown signalHistos_bg_gaussian_medium/ResonanceShapes_gaus10_13TeV_Spring16_JESDOWN_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_gaussian_medium/ResonanceShapes_gaus10_13TeV_Spring16_JERUP_rescale.root'
	    elif box=='PFDijetbg2016le1llN':
		        signalSys +=' --jesUp signalHistos_bg_New_K_loose/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bg_New_K_loose/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
		        signalSys +=' --jerUp signalHistos_bg_New_K_loose/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbb2016le1llN':
                signalSys +=' --jesUp signalHistos_bb_New_K_loose/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bb_New_K_loose/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_New_K_loose/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan100':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan150':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan200':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan250':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan300':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_300_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_300_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_300_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan350':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_350_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_350_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_350_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan400':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_400_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_400_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_400_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan450':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_450_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_450_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_450_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan500':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan550':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_550_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_550_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_550_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan600':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan650':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_650_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_650_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_650_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan700':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan750':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_750_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_750_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_750_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan800':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan850':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan900':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan950':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_950_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan460':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_460_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_460_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_460_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan935':
                signalSys +=' --jesUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_935_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_935_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_935_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan100':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan150':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan200':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan250':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan300':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_300_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_300_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_300_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan350':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_350_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_350_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_350_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan400':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_400_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_400_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_400_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan450':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_450_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_450_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_450_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan500':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan550':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_550_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_550_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_550_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan600':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan650':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_650_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_650_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_650_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan700':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan750':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_750_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_750_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_750_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan800':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan850':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan900':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan950':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan460':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_460_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_460_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_460_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan935':
                signalSys +=' --jesUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_935_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_935_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_935_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg20160llN':
		signalSys +=' --jesUp signalHistos_bg_New_K_loose_0/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bg_New_K_loose_0/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_New_K_loose_0/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root '
            elif box=='PFDijetbb20160llN':
                signalSys +=' --jesUp signalHistos_bb_New_K_loose_0/ResonanceShapes_qq_bb_13TeV_Spring16_JESUP_Inter_Interpolation_rescale.root --jesDown signalHistos_bb_New_K_loose_0/ResonanceShapes_qq_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation_rescale.root'
                signalSys +=' --jerUp  signalHistos_bb_New_K_loose_0/ResonanceShapes_qq_bb_13TeV_Spring16_JER_Inter_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan1002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan1502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan2002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan2502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan3002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_300_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_300_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_300_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan3502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_350_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_350_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_350_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan4002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_400_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_400_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_400_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan4502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_450_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_450_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_450_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan5002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan5502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_550_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_550_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_550_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan6002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan6502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_650_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_650_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_650_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan7002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan7502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_750_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_750_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_750_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan8002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan8502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan9002b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan9502b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_950_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan4602b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_460_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_460_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_460_JER_Interpolation_rescale.root'
            elif box=='PFDijetbb2016Scan9352b':
                signalSys +=' --jesUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_935_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_935_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_935_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan1001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan1501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan2001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan2501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan3001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan3501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan4001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan4501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan5001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan5501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan6001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan6501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan7001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan7501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan8001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan8501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan9001b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan9501b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan4601b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_460_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_460_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_460_JER_Interpolation_rescale.root'
            elif box=='PFDijetbg2016Scan9351b':
                signalSys +=' --jesUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan100Dec0':
		        signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
		        signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan150Dec0':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan200Dec0':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan250Dec0':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan100Dec0':
		        signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                	signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan150Dec0':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan200Dec0':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan250Dec0':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan100Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan150Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan200Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan250Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan100Dec':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan150Dec':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan200Dec':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_JER_Interpolation_rescale.root'
            elif box=='PFDijetbbScan250Dec':
                signalSys +=' --jesUp  signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESUP_Interpolation_rescale.root --jesDown signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan300Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan350Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan400Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan450Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan500Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan550Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan600Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan650Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan700Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan750Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan800Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan850Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan900Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan950Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_JER_Interpolation_rescale.root'
            elif box=='PFDijetbgScan935Dec':
                signalSys +=' --jesUp  signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_JESUP_Interpolation_rescale.root --jesDown signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_JESDOWN_Interpolation_rescale.root'
                signalSys +=' --jerUp signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_JER_Interpolation_rescale.root'
	    elif box=='PFDijetbg2016all':
		signalSys +=' --jesUp signalHistos_bg_Dec12_ForAll/ResonanceShapes_qg_bb_13TeV_Spring16_JESUP_Inter_Interpolation.root --jesDown signalHistos_bg_Dec12_ForAll/ResonanceShapes_qg_bb_13TeV_Spring16_JESDOWN_Inter_Interpolation.root'
		signalSys +=' --jerUp signalHistos_bg_Dec12_ForAll/ResonanceShapes_qg_bb_13TeV_Spring16_JER_Inter_Interpolation.root'



        penaltyString = ''
        if options.penalty:
            penaltyString = '--penalty'
        elif options.noSys:
            penaltyString = '--fixed'

        xsecString = '--xsec %f'%(options.xsec)


        if box=='CaloDijet2015' or box=='CaloDijet20152016':
            signalDsName = 'inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring15.root'%model
        elif box=='CaloDijet2016':
            signalDsName = 'inputs/ResonanceShapes_%s_13TeV_CaloScouting_Spring16.root'%model
        elif box=='PFDijet2016':
            signalDsName = 'inputs/ResonanceShapes_%s_13TeV_Spring16.root'%model
	elif 'PFDijetbg20161tt' == box:
	    	signalDsName = 'inputs/Inter_U/ResonanceShapes_qg_bg_13TeV_Spring16_Interpolation_Norminal_rescale.root'
	elif 'PFDijetbb20162ttQI' == box:
	    	signalDsName = 'inputs/Newbb/ResonanceShapes_qq_bb_13TeV_Spring16_Inter_Interpolation_rescale.root'
	elif 'PFDijetbb20162tt' == box:
	    	signalDsName = 'signalHistos_bb_t/ResonanceShapes_qq_bb_13TeV_Spring16_tight_Interpolation_rescale.root'
        elif 'PFDijetbb20162mm2' == box:
            signalDsName = 'inputs/Med_Inter_U/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation.root'
        elif 'PFDijetbb20162mm' == box:
            signalDsName = 'inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_central_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbb20162mmU'==box:
            signalDsName = 'inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_UP_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbb20162mmD'==box:
            signalDsName = 'inputs/bTag_uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_DOWN_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbb20162mm9'==box:
            signalDsName = 'inputs/Inter_09/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif 'PFDijetbg20161ttC'==box:
	    	signalDsName = 'inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_central_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbg20161ttU'==box:
            signalDsName = 'inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_UP_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbg20161ttD'==box:
            signalDsName = 'inputs/bTag_uncertainty_bg/ResonanceShapes_qg_bb_13TeV_Spring16_DOWN_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbg20161ttG'==box:
            signalDsName = 'inputs/Gaus/ResonanceShapes_gaus10_13TeV_Spring16_rescale.root'
	elif 'PFDijetbb20161mm1btag'==box:
		    signalDsName = 'inputs/1btag_mm_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbb20161tt1btag'==box:
		    signalDsName = 'inputs/1btag_tt_coloron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif 'PFDijetbb20161mm1btag2'==box:
	   	 	signalDsName = 'inputs/Coloron_bb_tight_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif 'PFDijetbb20161mmle1'==box:
	  	  signalDsName = 'inputs/1btag_mm_coloron_Uncertainty_le1/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif 'PFDijetbb20161tt'==box:
	 	   signalDsName = 'inputs/1ttColoron_Uncertainty/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif 'PFDijetbb20161mmMyBTag050'==box:
	        signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag060'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag070'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag080'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag090'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag091'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag092'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag093'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag094'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag096'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag095'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag082'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag084'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag086'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb20161mmMyBTag088'==box:
            signalDsName = 'inputs/Scan_1mmle1_Uncertainty/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif box=='PFDijetbb2016le1tt':
            signalDsName = 'signalHistos_bb_shape2_tight/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif box=='PFDijetbb2016le1mm':
            signalDsName = 'signalHistos_bb_shape2_medium/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif box=='PFDijetbb2016le1ttN':
	        signalDsName = 'signalHistos_bb_New_K_tight/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif box=='PFDijetbg2016le1ttN':
            signalDsName = 'signalHistos_bg_New_K_tight/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif box=='PFDijetbb2016le1mmN':
            signalDsName = 'signalHistos_bb_New_K_medium/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif box=='PFDijetbg2016le1mmN':
            signalDsName = 'signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif box=='PFDijetbg2016le1mmO':
	 	   signalDsName = 'signalHistos_bg_shape_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
	elif box=='PFDijetbg2016woCSV':
	    	signalDsName = 'signalHistos_bg_New_K_medium/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation.root'
	elif box=='PFDijetbg2016Gtt':
		    signalDsName = 'signalHistos_bg_gaussian_tight/ResonanceShapes_gaus10_13TeV_Spring16_rescale.root'
        elif box=='PFDijetbg2016Gmm':
	        signalDsName = 'signalHistos_bg_gaussian_medium/ResonanceShapes_gaus10_13TeV_Spring16_rescale.root'
        elif box=='PFDijetbg2016le1llN':
	        signalDsName = 'signalHistos_bg_New_K_loose/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif box=='PFDijetbb2016le1llN':
            signalDsName = 'signalHistos_bb_New_K_loose/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan100'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan150'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan200'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan250'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan300'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_300_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan350'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_350_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan400'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan450'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_450_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan500'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan550'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_550_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan600'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_600_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan650'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_650_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan700'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_700_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan750'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_750_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan800'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_800_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan850'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_850_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan900'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_900_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan950'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_950_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan935'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_935_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan460'==box:
            signalDsName = 'signalHistos_bg_FinalScan/ResonanceShapes_qg_bg_13TeV_Spring16_460_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan100'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan150'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan200'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan250'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan300'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_300_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan350'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_350_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan400'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan450'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_450_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan500'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan550'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_550_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan600'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_600_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan650'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_650_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan700'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_700_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan750'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_750_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan800'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_800_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan850'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_850_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan900'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_900_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan950'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_950_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan935'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_935_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan460'==box:
            signalDsName = 'signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_460_Nominal_Interpolation_rescale.root'
	elif 'PFDijetbb20160llN'==box:
	        signalDsName = 'signalHistos_bb_New_K_loose_0/ResonanceShapes_qq_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbg20160llN'==box:
            signalDsName = 'signalHistos_bg_New_K_loose_0/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan1001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan1501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan2001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan2501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan3001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan3501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan4001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan4501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan5001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan5501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan6001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan6501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan7001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan7501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan8001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan8501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan9001b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan9501b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan9351b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbg2016Scan4601b'==box:
            signalDsName = 'signalHistos_bg_FinalScan_1btag/ResonanceShapes_qg_bg_13TeV_Spring16_460_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan1002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan1502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan2002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan2502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan3002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_300_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan3502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_350_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan4002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan4502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_450_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan5002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan5502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_550_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan6002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_600_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan6502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_650_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan7002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_700_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan7502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_750_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan8002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_800_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan8502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_850_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan9002b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_900_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan9502b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_950_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan9352b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_935_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbb2016Scan4602b'==box:
            signalDsName = 'signalHistos_bb_FinalScan_2btag/ResonanceShapes_qq_bg_13TeV_Spring16_460_Nominal_Interpolation_rescale.root'
	elif 'PFDijetbbScan100Dec0'==box:
	  	    signalDsName = 'signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan150Dec0'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan200Dec0'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan250Dec0'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/0btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan100Dec0'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan150Dec0'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan200Dec0'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan250Dec0'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/0btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan100Dec'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan150Dec'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan200Dec'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbbScan250Dec'==box:
            signalDsName = 'signalHistos_bb_Scan_Dec8/le1btag/ResonanceShapes_qq_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan100Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan150Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_150_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan200Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_200_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan250Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_250_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan300Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_300_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan350Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_350_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan400Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_400_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan450Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_450_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan500Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_500_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan550Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_550_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan600Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_600_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan650Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_650_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan700Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_700_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan750Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_750_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan800Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_800_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan850Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_850_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan900Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_900_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan935Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_935_Nominal_Interpolation_rescale.root'
        elif 'PFDijetbgScan950Dec'==box:
            signalDsName = 'signalHistos_bg_Scan_Dec8/le1btag/ResonanceShapes_qg_bg_13TeV_Spring16_950_Nominal_Interpolation_rescale.root'
	elif 'PFDijetbg2016all'==box:
	    signalDsName = 'signalHistos_bg_Dec12_ForAll/ResonanceShapes_qg_bb_13TeV_Spring16_Norminal_Inter_Interpolation.root'


        backgroundDsName = {'CaloDijet2015':'inputs/data_CaloScoutingHT_Run2015D_BiasCorrected_CaloDijet2015.root',
                            #'CaloDijet2016':'inputs/data_CaloScoutingHT_Run2016BCD_NewBiasCorrectedFlat_Golden12910pb_CaloDijet2016.root',
                            'CaloDijet2016':'inputs/data_CaloScoutingHT_Run2016BCDEFG_BiasCorrected_Mjj300_Golden27637pb_CaloDijet2016.root',
                            #'PFDijet2016':'inputs/data_PFRECOHT_Run2016BCD_Golden12910pb_PFDijet2016.root',
                            'CaloDijet20152016':'inputs/data_CaloScoutingHT_Run2015D2016B_CaloDijet20152016.root',
                            'PFDijet2016':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20160mt':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20161mt':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20162mt':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20160mm':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20161mm':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20162mm':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbb20162mm2':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbg20161tt':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbg20161ttwithW':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbg20161ttwithoutW':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbb20162tt':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbb20162ttQI':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbg20161ttD':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbg20161ttG':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbb20162mmC':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20162mmU':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20162mmD':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
                            'PFDijetbb20162mm9':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbb20161mm1btag':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbb20161mm1btag2':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbb20161tt1btag':'inputs/JetHT_run2016_moriond17_red_cert_v2.root',
			    'PFDijetbb20161mmle1':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbb20161tt':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbb2016le1tt':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbb2016le1mm':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbg2016le1mmN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbg2016le1ttN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbb2016le1mmN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbb2016le1ttN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbg2016le1mmO':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbg2016woCSV':'inputs/JetHT_run2016_moriond17_red_cert_v2_withoutCSV.root',
			    'PFDijetbg2016Gtt':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbg2016Gmm':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbg2016le1llN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
			    'PFDijetbb2016le1llN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbg2016Scan100':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan200':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan300':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan400':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan500':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan600':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan700':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan800':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan900':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan150':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan250':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan350':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan450':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan550':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan650':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan750':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan850':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan950':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan460':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan935':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan100':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan200':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan300':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan400':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan500':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan600':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan700':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan800':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan900':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan150':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan250':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan350':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan450':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan550':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan650':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan750':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan850':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan950':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan460':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan935':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan1001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan2001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan3001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan4001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan5001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan6001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan7001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan8001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan9001b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan1501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan2501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan3501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan4501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan5501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan6501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan7501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan8501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan9501b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan4601b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbg2016Scan9351b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan1002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan2002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan3002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan4002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan5002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan6002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan7002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan8002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan9002b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan1502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan2502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan3502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan4502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan5502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan6502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan7502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan8502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan9502b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan4602b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbb2016Scan9352b':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
	                    'PFDijetbb20160llN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbg20160llN':'inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root',
                            'PFDijetbgScan100Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan150Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan200Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan250Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbbScan100Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbbScan150Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbbScan200Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbbScan250Dec0':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan100Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan150Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan200Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan250Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan300Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan350Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan400Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan450Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan500Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan550Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan600Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan650Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan700Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan750Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan800Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan850Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan900Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan935Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
                            'PFDijetbgScan950Dec':'inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root',
			    'PFDijetbg2016all':'inputs/JetHT_run2016_moriond17_red_cert_v2_all.root',
                            }





        blindString = ''
        if options.blind:
            blindString = '--noFitAsimov --run expected'

        sysString = ''
        if options.noSys and options.deco:
            sysString = '-S 0 --freezeNuisances=shapeBkg_%s_bkg_deco_%s__norm,deco_%s_eig1,deco_%s_eig2,deco_%s_eig3,jes,jer,lumi'%(box,box,box,box,box)
        elif options.noSys:
            sysString = '-S 0 --freezeNuisances=shapeBkg_%s_bkg_%s__norm,p1_%s,p2_%s,p3_%s,jes,jer,lumi'%(box,box,box,box,box)
        elif options.multi and options.fitPdf!='all':
            sysString = '--setPhysicsModelParameters pdf_index=%i --freezeNuisances pdf_index'%(pdfIndexMap[options.fitPdf])
            if options.fitPdf != 'fiveparam':
                sysString += ',p51_CaloDijet2016,p52_CaloDijet2016,p53_CaloDijet2016,p54_CaloDijet2016'
            if options.fitPdf != 'modexp':
                sysString += ',pm1_CaloDijet2016,pm2_CaloDijet2016,pm3_CaloDijet2016,pm4_CaloDijet2016'
            if options.fitPdf != 'atlas':
                sysString += ',pa1_CaloDijet2016,pa2_CaloDijet2016,pa3_CaloDijet2016,pa4_CaloDijet2016'

        sysStringList.append(sysString)

        decoString = ''
        if options.deco:
            decoString  ='--deco'

        multiString = ''
        if options.multi:
            decoString  ='--multi'

        for massPoint in massIterable(options.mass):
            exec_me('python python/WriteDataCard_btag_2.py -m %s --mass %s -i %s -l %f -c %s -b %s -d %s %s %s %s %s %s %s %s'%(model, massPoint, options.inputFitFile,1000*lumi,options.config,box,options.outDir,signalDsName,backgroundDsName[box],penaltyString,signalSys,xsecString,decoString,multiString),options.dryRun)
            if options.bayes:
                rRangeString =  '--setPhysicsModelParameterRanges '
                if options.deco:
                    rRangeString += 'shapeBkg_%s_bkg_deco_%s__norm=%f,%f'%(box,box,1-NSIGMA*paramDict['Ntot_bkg_%s'%box][1]/paramDict['Ntot_bkg_%s'%box][0],1+NSIGMA*paramDict['Ntot_bkg_%s'%box][1]/paramDict['Ntot_bkg_%s'%box][0])
                    rRangeString += ':deco_%s_eig1=%f,%f'%(box,-1.0*NSIGMA,NSIGMA)
                    rRangeString += ':deco_%s_eig2=%f,%f'%(box,-1.0*NSIGMA,NSIGMA)
                    rRangeString += ':deco_%s_eig3=%f,%f'%(box,-1.0*NSIGMA,NSIGMA)
                else:
                    rRangeString += 'shapeBkg_%s_bkg_%s__norm=%f,%f'%(box,box,1-NSIGMA*paramDict['Ntot_bkg_%s'%box][1]/paramDict['Ntot_bkg_%s'%box][0],1+NSIGMA*paramDict['Ntot_bkg_%s'%box][1]/paramDict['Ntot_bkg_%s'%box][0])
                    rRangeString += ':p1_%s=%f,%f'%(box,paramDict['p1_%s'%box][0]-NSIGMA*paramDict['p1_%s'%box][1],paramDict['p1_%s'%box][0]+NSIGMA*paramDict['p1_%s'%box][1])
                    rRangeString += ':p2_%s=%f,%f'%(box,paramDict['p2_%s'%box][0]-NSIGMA*paramDict['p2_%s'%box][1],paramDict['p2_%s'%box][0]+NSIGMA*paramDict['p2_%s'%box][1])
                    rRangeString += ':p3_%s=%f,%f'%(box,paramDict['p3_%s'%box][0]-NSIGMA*paramDict['p3_%s'%box][1],paramDict['p3_%s'%box][0]+NSIGMA*paramDict['p3_%s'%box][1])
                if options.rMax>-1:
                    rRangeString += ':r=0,%f'%(options.rMax)
                rRangeStringList.append(rRangeString)
                toyString = ''
                if options.toys>-1:
                    toyString = '-t %i -s -1'%options.toys
                if len(boxes)==1:
                    exec_me('combine -M MarkovChainMC -H Asymptotic %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt -n %s_%s_lumi-%.3f_%s --tries 20 --proposal ortho --burnInSteps 200 --iteration 30000 --propHelperWidthRangeDivisor 10 %s %s %s %s'%(options.outDir,model,massPoint,lumi,box,model,massPoint,lumi,box,rRangeString,blindString,sysString,toyString),options.dryRun)
                    exec_me('mv higgsCombine%s_%s_lumi-%.3f_%s.MarkovChainMC.mH120*root %s/'%(model,massPoint,lumi,box,options.outDir),options.dryRun)
            else:
                if signif:
                    rRangeString = ''
                    if options.rMax>-1:
                        rRangeString = '--setPhysicsModelParameterRanges r=0,%f'%(options.rMax)
                        rRangeStringList.append(rRangeString)
                    if len(boxes)==1:
                        exec_me('combine -M ProfileLikelihood --signif %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt -n %s_%s_lumi-%.3f_%s %s %s'%(options.outDir,model,massPoint,lumi,box,model,massPoint,lumi,box,rRangeString,sysString),options.dryRun)
                        exec_me('mv higgsCombine%s_%s_lumi-%.3f_%s.ProfileLikelihood.mH120.root %s/'%(model,massPoint,lumi,box,options.outDir),options.dryRun)
                else:
                    rRangeString = ''
                    if options.rMax>-1:
                        rRangeString =  '--setPhysicsModelParameterRanges r=0,%f'%(options.rMax)
                        rRangeStringList.append(rRangeString)
                    if len(boxes)==1:
                        exec_me('combine -M Asymptotic -H ProfileLikelihood %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt -n %s_%s_lumi-%.3f_%s --minimizerTolerance %f --minimizerStrategy %i %s --saveWorkspace %s %s'%(options.outDir,model,massPoint,lumi,box,model,massPoint,lumi,box,options.min_tol,options.min_strat,rRangeString,blindString,sysString),options.dryRun)
                        exec_me('mv higgsCombine%s_%s_lumi-%.3f_%s.Asymptotic.mH120.root %s/'%(model,massPoint,lumi,box,options.outDir),options.dryRun)
    if len(boxes)>1:
        lumiTotal = sum(lumiFloat)
        for box,lumi in zip(boxes,lumiFloat): exec_me('cp %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt .'%(options.outDir,model,massPoint,lumi,box),options.dryRun)
        cmds = ['%s=dijet_combine_%s_%s_lumi-%.3f_%s.txt'%(box,model,massPoint,lumi,box) for box,lumi in zip(boxes,lumiFloat)]
        exec_me('combineCards.py %s > %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt'%(' '.join(cmds),options.outDir,model,massPoint,lumiTotal,options.box),options.dryRun)
        exec_me('cat %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt'%(options.outDir,model,massPoint,lumiTotal,options.box),options.dryRun)
        if options.bayes:
            rRangeStringListMod = [rRangeString.replace('--setPhysicsModelParameterRanges ','') for rRangeString in rRangeStringList ]
            paramRangeList = []
            for listMod in rRangeStringListMod:
                paramRangeList.extend(listMod.split(':'))
            paramRangeList = list(set(paramRangeList))
            rRangeStringTotal = ''
            if options.deco or rMax>=-1:
                rRangeStringTotal = '--setPhysicsModelParameterRanges ' + ','.join(paramRangeList)

            sysStringListMod = [sysString.replace('-S 0 --freezeNuisances=','') for sysString in sysStringList ]
            paramFreezeList = []
            for listMod in sysStringListMod:
                paramFreezeList.extend(listMod.split(','))
            paramFreezeList = list(set(paramFreezeList))
            sysStringTotal = ''
            if options.noSys:
                sysStringTotal = '-S 0 --freezeNuisances=' + ','.join(paramFreezeList)
            exec_me('combine -M MarkovChainMC -H Asymptotic %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt -n %s_%s_lumi-%.3f_%s --tries 30 --proposal ortho --burnInSteps 1000 --iteration 40000 --propHelperWidthRangeDivisor 10 %s %s %s %s'%(options.outDir,model,massPoint,lumiTotal,options.box,model,massPoint,lumiTotal,options.box,rRangeStringTotal,blindString,sysStringTotal,toyString),options.dryRun)
            exec_me('mv higgsCombine%s_%s_lumi-%.3f_%s.MarkovChainMC.mH120*root %s/'%(model,massPoint,lumiTotal,options.box,options.outDir),options.dryRun)
        else:
            if signif:
                rRangeString = ''
                if options.rMax>-1:
                    rRangeString = '--setPhysicsModelParameterRanges r=0,%f'%(options.rMax)
                exec_me('combine -M ProfileLikelihood --signif %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt -n %s_%s_lumi-%.3f_%s %s %s'%(options.outDir,model,massPoint,lumiTotal,options.box,model,massPoint,lumiTotal,options.box,rRangeString,sysString),options.dryRun)
                exec_me('mv higgsCombine%s_%s_lumi-%.3f_%s.ProfileLikelihood.mH120.root %s/'%(model,massPoint,lumiTotal,options.box,options.outDir),options.dryRun)
            else:
                rRangeString = ''
                if options.rMax>-1:
                    rRangeString =  '--setPhysicsModelParameterRanges r=0,%f'%(options.rMax)
                exec_me('combine -M Asymptotic -H ProfileLikelihood %s/dijet_combine_%s_%s_lumi-%.3f_%s.txt -n %s_%s_lumi-%.3f_%s --minimizerTolerance %f --minimizerStrategy %i %s --saveWorkspace %s %s'%(options.outDir,model,massPoint,lumiTotal,options.box,model,massPoint,lumiTotal,options.box,options.min_tol,options.min_strat,rRangeString,blindString,sysString),options.dryRun)
                exec_me('mv higgsCombine%s_%s_lumi-%.3f_%s.Asymptotic.mH120.root %s/'%(model,massPoint,lumiTotal,options.box,options.outDir),options.dryRun)
            for box,lumi in zip(boxes,lumiFloat): exec_me('rm dijet_combine_%s_%s_lumi-%.3f_%s.txt'%(model,massPoint,lumi,box),options.dryRun)

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('-c','--config',dest="config",type="string",default="config/run2.config",
                  help="Name of the config file to use")
    parser.add_option('-b','--box',dest="box", default="CaloDijet",type="string",
                  help="box name")
    parser.add_option('-m','--model',dest="model", default="gg",type="string",
                  help="signal model name")
    parser.add_option('--mass',dest="mass", default='750',type="string",
                  help="mass of resonance")
    parser.add_option('-l','--lumi',dest="lumi", default="1.918",type="string",
                  help="lumi in fb^-1, possibly for different channels e.g.: 1.918_2.590")
    parser.add_option('--signif',dest="signif",default=False,action='store_true',
                  help="calculate significance instead of limit")
    parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
                  help="Output directory to store cards")
    parser.add_option('--min-tol',dest="min_tol",default=0.001,type="float",
                  help="minimizer tolerance (default = 0.001)")
    parser.add_option('--min-strat',dest="min_strat",default=2,type="int",
                  help="minimizer strategy (default = 2)")
    parser.add_option('--dry-run',dest="dryRun",default=False,action='store_true',
                  help="Just print out commands to run")
    parser.add_option('--penalty',dest="penalty",default=False,action='store_true',
                  help="penalty terms on background parameters")
    parser.add_option('-i','--input-fit-file',dest="inputFitFile", default='FitResults/BinnedFitResults.root',type="string",
                  help="input fit file")
    parser.add_option('--no-signal-sys',dest="noSignalSys",default=False,action='store_true',
                  help="do not create signal shape systematic histograms / uncertainties")
    parser.add_option('--no-sys',dest="noSys",default=False,action='store_true',
                  help="no systematic uncertainties when running combine")
    parser.add_option('--blind',dest="blind",default=False,action='store_true',
                  help="run only blinded expected limits")
    parser.add_option('--rMax',dest="rMax",default=-1,type="float",
                  help="maximum r value (for better precision)")
    parser.add_option('--xsec',dest="xsec",default=1,type="float",
                  help="xsec for signal in pb (r = 1)")
    parser.add_option('-j','--jobs',dest="jobs",default=0,type="int",
                  help="number of jobs to submit when running toys for each mass point (just set to 1 for observed limits)")
    parser.add_option('--bayes',dest="bayes",default=False,action='store_true',
                  help="bayesian limits")
    parser.add_option('--deco',dest="deco",default=False,action='store_true',
                  help="decorrelate shape parameters")
    parser.add_option('--tag',dest="tag", default='master',type="string",
                  help="tag for repository")
    parser.add_option('-q','--queue',dest="queue",default="1nh",type="string",
                  help="queue: 1nh, 8nh, 1nd, etc.")
    parser.add_option('-t','--toys',dest="toys",default=-1,type="int",
                  help="number of toys per job(for bayesian expected limits)")
    parser.add_option('--multi',dest="multi",default=False,action='store_true',
                  help="using RooMultiPdf for total background")
    parser.add_option('--fit-pdf',dest="fitPdf", default="all", choices=['all','modexp','fiveparam','atlas'],
                  help="pdf for fitting")


    (options,args) = parser.parse_args()


    if options.jobs:
        submit_jobs(options,args)
    else:
        main(options,args)
