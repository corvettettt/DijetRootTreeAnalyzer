from optparse import OptionParser
import ROOT as rt
import rootTools
from framework import Config
from array import *
from WriteDataCard import *
from BinnedFit import convertSideband
import os
import random
import sys
import math
#from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, FileTransferSpeed, FormatLabel, Percentage, ProgressBar, ReverseBar, RotatingMarker, SimpleProgress, Timer

def getErrorData(N,F):    
    alpha = 1-0.6827
    L = 0
    if N!=0:
        L = rt.Math.gamma_quantile(alpha/2,N,1.)
    U = rt.Math.gamma_quantile_c(alpha/2,N+1,1)
    
    err_tot_data = 0
    if (F >= N):
        err_tot_data = U-N
    else:
        err_tot_data = N-L
    
    return err_tot_data

def getTree(myTree,paramNames,nBins,box):
    
    rando = random.randint(1,999999)
    # first structure
    #stringMyStruct1 = "void tempMacro_%d(){struct MyStruct1{"%(rando)
    stringMyStruct1 = "struct MyStruct1{"
    stringMyStruct1 += "float toy_num; float nll_%s; float n2llr_%s; float chi2p_%s; float chi2_%s; float chi2non0_%s;"%(box,box,box,box,box)
    stringMyStruct1 += "int covQual_%s; int migrad_%s; int hesse_%s; int minos_%s;"%(box,box,box,box)
    for paramName in paramNames:
        stringMyStruct1 = stringMyStruct1+"float %s; float %s_error;" %(paramName,paramName)
        if paramName=='r':
            stringMyStruct1 = stringMyStruct1+"float r_errorlo; float r_errorhi;"           
    for iBinX in range(0,nBins):
        stringMyStruct1 = stringMyStruct1+"float b%i;" %(iBinX)
    tempMacro = open("tempMacro_%d.C"%rando,"w")
    tempMacro.write(stringMyStruct1+"};}")
    tempMacro.close()
    #rt.gROOT.Macro("tempMacro_%d.C"%rando)
    #rt.gROOT.ProcessLine(".x tempMacro_%d.C"%rando)
    rt.gROOT.ProcessLine(stringMyStruct1+"};")
    from ROOT import MyStruct1

    # fills the bins list and associate the bins to the corresponding variables in the structure
    s1 = MyStruct1()
    myTree.Branch('toy_num' , rt.AddressOf(s1,'toy_num'),'toy_num/F')
    myTree.Branch('nll_%s'%box , rt.AddressOf(s1,'nll_%s'%box),'nll_%s/F' %box)
    myTree.Branch('n2llr_%s'%box , rt.AddressOf(s1,'n2llr_%s'%box),'n2llr_%s/F' %box)
    myTree.Branch('chi2p_%s'%box , rt.AddressOf(s1,'chi2p_%s'%box),'chi2p_%s/F' %box)
    myTree.Branch('chi2_%s'%box , rt.AddressOf(s1,'chi2_%s'%box),'chi2_%s/F' %box)
    myTree.Branch('chi2non0_%s'%box , rt.AddressOf(s1,'chi2non0_%s'%box),'chi2non0_%s/F' %box)
    myTree.Branch('covQual_%s'%box , rt.AddressOf(s1,'covQual_%s'%box),'covQual_%s/I' %box)
    myTree.Branch('migrad_%s'%box , rt.AddressOf(s1,'migrad_%s'%box),'migrad_%s/I' %box)
    myTree.Branch('hesse_%s'%box , rt.AddressOf(s1,'hesse_%s'%box),'hesse_%s/I' %box)
    myTree.Branch('minos_%s'%box , rt.AddressOf(s1,'minos_%s'%box),'minos_%s/I' %box)
    for paramName in paramNames:
        myTree.Branch(paramName , rt.AddressOf(s1,paramName),'%s/F' %paramName)
        myTree.Branch('%s_error'%paramName , rt.AddressOf(s1,'%s_error'%paramName),'%s_error/F' %paramName)
        if paramName=='r':            
            myTree.Branch('r_errorlo' , rt.AddressOf(s1,'r_errorlo'),'r_errorlo/F')
            myTree.Branch('r_errorhi' , rt.AddressOf(s1,'r_errorhi'),'r_errorhi/F')
    for ix in range(0, nBins):
        myTree.Branch("b%i" %(ix) , rt.AddressOf(s1,"b%i" %(ix)),'b%i/F' %ix)

    os.system("rm tempMacro_%d.C"%rando)
    return s1


def runToys(w,options,cfg,seed):
    
    if seed>-1:
        rt.RooRandom.randomGenerator().SetSeed(seed)
    
    extDijetPdf = w.pdf('extDijetPdf')
    dataHist = w.data("data_obs")    
    if w.obj("fitresult_extDijetPdf_data_obs") != None:
        fr = w.obj("fitresult_extDijetPdf_data_obs")
    elif w.obj("nll_extDijetPdf_data_obs") != None:
        fr = w.obj("nll_extDijetPdf_data_obs")
    elif w.obj("fitresult_extDijetPdf_data_obs_with_constr") != None:
        fr = w.obj("fitresult_extDijetPdf_data_obs_with_constr")
    elif w.obj("nll_extDijetPdf_data_obs_with_constr") != None:
        fr = w.obj("nll_extDijetPdf_data_obs_with_constr")

    fr.Print("V")
    if options.r>-1:
        extSpBPdf = w.pdf('extSpBPdf')
    
    th1x = w.var("th1x")
    
    params = extDijetPdf.getParameters(dataHist)
    paramsToRemove = []
    for p in rootTools.RootIterator.RootIterator(params):
        if p.isConstant(): paramsToRemove.append(p)

    [params.remove(p) for p in paramsToRemove]
    paramNames = [p.GetName() for p in rootTools.RootIterator.RootIterator(params)]
    paramNames.sort()    
    if options.r>-1: paramNames.append('r')
    
    x = array('d', cfg.getBinning(options.box)[0]) # mjj binning
    nBins = (len(x)-1)
    
    th1x.setBins(nBins)
    
    fitband = convertSideband(options.fitRegion,w,x)

    unc = 'Bayes'
    if options.noStat: unc = "Bayes_noStat"
    elif options.noSys: unc = "Bayes_noSys"
    elif options.freq: unc = 'Freq'
        
    if options.r>-1:
        rString = str('%.3f'%options.r).replace(".","p")
        if seed>-1:
            output = rt.TFile.Open(options.outDir+'/toys_%s_r%s_s%i_%s.root'%(unc,rString,seedoptions.box),'recreate')
        else:
            output = rt.TFile.Open(options.outDir+'/toys_%s_r%s_%s.root'%(unc,rString,options.box),'recreate')
    else:
        if seed>-1:            
            output = rt.TFile.Open(options.outDir+'/toys_%s_s%i_%s.root'%(unc,seed,options.box),'recreate')
        else:
            output = rt.TFile.Open(options.outDir+'/toys_%s_%s.root'%(unc,options.box),'recreate')
        
    output.cd()
    myTree = rt.TTree("myTree", "myTree")
    
    s1 = getTree(myTree, paramNames, nBins, options.box)
    value =  setattr(s1, 'toy_num', -1) # set toy number to -1
    
    for p in rootTools.RootIterator.RootIterator(fr.floatParsFinal()):
        w.var(p.GetName()).setVal(p.getVal())
        w.var(p.GetName()).setError(p.getError())
        value = setattr(s1, p.GetName(), p.getVal())
        value = setattr(s1, p.GetName()+'_error', p.getError())
    if options.r>-1:
        value =  setattr(s1, 'r', 0)
        value =  setattr(s1, 'r_error', 0)
        value =  setattr(s1, 'r_errorlo', 0)
        value =  setattr(s1, 'r_errorhi', 0)
        
    asimov = extDijetPdf.generateBinned(rt.RooArgSet(th1x),rt.RooFit.Name('central'),rt.RooFit.Asimov())

    chi2p_data = 0
    chi2_data = 0
    chi2non0_data = 0
    n2llr_data = 0
    nll_data = 0
    bestFitByBin = []
    iBinX = -1    
    for i in range(1,len(x)):
                iBinX += 1
                th1x.setVal(iBinX+0.5)                
                inFitRange = any([th1x.inRange(fitname) for fitname in fitband.split(',')])     
                #expected = extDijetPdf.getValV(rt.RooArgSet(th1x)) * extDijetPdf.expectedEvents(rt.RooArgSet(th1x))
                if inFitRange:                    
                    expected = float(asimov.weight(rt.RooArgSet(th1x)))
                    bestFitByBin.append(expected)
                    observed = float(dataHist.weight(rt.RooArgSet(th1x)))
                    value = setattr(s1, 'b%i'%iBinX, expected)
                else:
                    expected = 0
                    bestFitByBin.append(0)
                    observed = 0
                    value = setattr(s1, 'b%i'%iBinX, 0)
                if expected>0 and inFitRange:
                    chi2p_data += ( observed - expected ) * ( observed - expected ) / ( expected )
                if inFitRange:                    
                    #print '%i: obs %.0f, exp %.2f, chi2 %.2f'%(iBinX, observed, expected, ( observed - expected ) * ( observed - expected ) / pow(getErrorData(observed,expected),2))
                    chi2_data += ( observed - expected ) * ( observed - expected ) / pow(getErrorData(observed,expected),2)
                    if observed>0:
                        chi2non0_data += ( observed - expected ) * ( observed - expected ) / pow(getErrorData(observed,expected),2)
                if expected>0 and inFitRange:            
                    nll_data -= observed*rt.TMath.Log(expected) - expected
                if observed>0 and expected>0 and inFitRange:
                    n2llr_data += 2 * ( observed*rt.TMath.Log(observed/expected) - observed )
                if expected>0 and inFitRange:                
                    n2llr_data += 2 * ( expected )
        
    value = setattr(s1, 'nll_%s'%options.box, nll_data)
    value = setattr(s1, 'n2llr_%s'%options.box, n2llr_data)
    value = setattr(s1, 'chi2p_%s'%options.box, chi2p_data)
    value = setattr(s1, 'chi2_%s'%options.box, chi2_data)
    value = setattr(s1, 'chi2non0_%s'%options.box, chi2non0_data)
    
    
        
    myTree.Fill()
        
    iToy = 0
    
    nBadPars = 0
    pBest = fr.floatParsFinal()
    pBestVal = {}
    pBestErr = {}
    for p in rootTools.RootIterator.RootIterator(pBest):
        pBestVal[p.GetName()] = p.getVal()
        pBestErr[p.GetName()] = p.getError()
                
    #widgets = ['Running %s toys '%unc, Percentage(), ' ', Bar(marker=RotatingMarker()),' ', ETA(), ' ', FileTransferSpeed()]
    #pbar = ProgressBar(widgets=widgets, max_value=options.nToys).start()
    iAttempt = -1
    while iToy < options.nToys:
        iAttempt+=1
        if options.freq:
            pSet = fr.floatParsFinal()
        else:
            if options.noSys:                
                pSet = fr.floatParsFinal()
            else:                
                pSet = fr.randomizePars()
        for p in rootTools.RootIterator.RootIterator(pSet):
            w.var(p.GetName()).setVal(p.getVal())
            w.var(p.GetName()).setError(p.getError())

        badPars = []
        if w.var('p0_%s'%options.box)!=None:                
            badPars.append(w.var('p0_%s'%options.box).getVal() <= 0)
        if any(badPars):
            nBadPars+=1
            #print "bad pars toy=%i"%iToy
            continue

        #print "good pars"                        
        errorCountBefore = rt.RooMsgService.instance().errorCount()

        badVal = False
        for iBinX in range(0,nBins):
            th1x.setVal(iBinX+0.5) # check number of events in each bin
            pdfValV = extDijetPdf.getValV(rt.RooArgSet(th1x)) * extDijetPdf.expectedEvents(rt.RooArgSet(th1x))
            pdfVal0 = extDijetPdf.getValV(0) * extDijetPdf.expectedEvents(rt.RooArgSet(th1x))
            if bestFitByBin[iBinX] > 0 and pdfValV/bestFitByBin[iBinX] <= 1e-12:
            #if bestFitByBin[iBinX] > 0 and pdfValV <= 0:
                #print "bin = %i"%iBinX
                #print "best fit = %e"%(bestFitByBin[iBinX])
                #print "pdf valv = %e"%(pdfValV)
                #print "pdf val0 = %e"%(pdfVal0)
                badVal = True                
        if badVal:
            #print "bad val"
            continue
        
        errorCountAfter = rt.RooMsgService.instance().errorCount()
        if errorCountAfter > errorCountBefore:            
            #print "can't evaulate pdf toy=%i"%iToy
            continue
        
        
        errorCountBefore = rt.RooMsgService.instance().errorCount()        
        #print "start generating toy=%i"%iToy
        if options.noStat:         
            if options.r>-1:
                w.var('r').setVal(options.r)            
                asimov = extSpBPdf.generateBinned(rt.RooArgSet(th1x),rt.RooFit.Name('toy'),rt.RooFit.Asimov())
            else:
                asimov = extDijetPdf.generateBinned(rt.RooArgSet(th1x),rt.RooFit.Name('toy'),rt.RooFit.Asimov())
        else:
            if options.r>-1:                
                w.var('r').setVal(options.r)                
                asimov = extSpBPdf.generateBinned(rt.RooArgSet(th1x),rt.RooFit.Name('toy'),rt.RooFit.Extended(True))
            else:
                asimov = extDijetPdf.generateBinned(rt.RooArgSet(th1x),rt.RooFit.Name('toy'),rt.RooFit.Extended(True))

        #print "toy entries = %.2f"%asimov.sumEntries()
        errorCountAfter = rt.RooMsgService.instance().errorCount()
        if errorCountAfter > errorCountBefore:
            #print "can't generate toy=%i"%iToy
            continue

        #print "SUCCESS: generated toy=%i"%iToy

        pSetSave = pSet
        migrad_status = -1
        hesse_status = -1
        minos_status = -1
        if options.freq:                      
            if options.r>-1:
                nll_func_toy = extSpBPdf.createNLL(asimov,rt.RooFit.Extended(True))
                m = rt.RooMinimizer(nll_func_toy)
                m.setStrategy(0)
                m.setPrintLevel(-1)
                m.setPrintEvalErrors(-1)
                rSet = rt.RooArgSet(w.var('r'))
                migrad_status = m.minimize('Minuit2','migrad')
                #hesse_status = m.minimize('Minuit2','hesse')
                #minos_status = m.minos(rSet)                
                fr_toy = m.save()
                value = setattr(s1,'migrad_%s'%options.box, migrad_status)   
                value = setattr(s1,'hesse_%s'%options.box, hesse_status)
                value = setattr(s1,'minos_%s'%options.box, minos_status)
            else:                
                nll_func_toy = extDijetPdf.createNLL(asimov,rt.RooFit.Extended(True),rt.RooFit.Range(fitband))               
                m = rt.RooMinimizer(nll_func_toy)
                m.setStrategy(0)
                m.setPrintLevel(-1)
                m.setPrintEvalErrors(-1)
                migrad_status = m.minimize('Minuit2','migrad')
                fr_toy = m.save()
            value = setattr(s1,'covQual_%s'%options.box, fr_toy.covQual())   
            value = setattr(s1,'migrad_%s'%options.box, migrad_status)   
            value = setattr(s1,'hesse_%s'%options.box, hesse_status)
            value = setattr(s1,'minos_%s'%options.box, minos_status)
            pSetSave = fr_toy.floatParsFinal()
            
                
        for p in rootTools.RootIterator.RootIterator(pSetSave):
            value = setattr(s1, p.GetName(), p.getVal())
            value = setattr(s1, p.GetName()+"_error", p.getError())
            if p.GetName()=='r':
                value = setattr(s1, "r_errorlo", p.getAsymErrorLo())
                value = setattr(s1, "r_errorhi", p.getAsymErrorHi())
                

        chi2p_toy = 0
        chi2_toy = 0
        chi2non0_toy = 0
        n2llr_toy = 0
        nll_toy = 0
        # restore best-fit to calculate expected values        
        for p in rootTools.RootIterator.RootIterator(pSetSave):
            w.var(p.GetName()).setVal(p.getVal())
            w.var(p.GetName()).setError(p.getError())

        iBinX = -1
        for i in range(1,len(x)):
                    iBinX += 1
                    th1x.setVal(iBinX+0.5)                 
                    inFitRange = any([th1x.inRange(fitname) for fitname in fitband.split(',')])
                    if inFitRange:
                        expected = extDijetPdf.getValV(rt.RooArgSet(th1x)) * extDijetPdf.expectedEvents(rt.RooArgSet(th1x))
                        toy = float(asimov.weight(rt.RooArgSet(th1x)))
                        observed = float(dataHist.weight(rt.RooArgSet(th1x)))  
                        value = setattr(s1, 'b%i'%iBinX, toy)
                    else:
                        expected = 0
                        toy = 0
                        observed = 0
                        value = setattr(s1, 'b%i'%iBinX, 0)                        
                    if expected>0 and inFitRange:
                        chi2p_toy += ( toy - expected ) * ( toy - expected ) / ( expected )
                    if inFitRange:
                        chi2_toy += ( toy - expected ) * ( toy - expected ) / pow(getErrorData(toy,expected),2)
                        if toy>0:
                            chi2non0_toy += ( toy - expected ) * ( toy - expected ) / pow(getErrorData(toy,expected),2)                            
                    if toy>0 and expected>0 and inFitRange:
                        n2llr_toy += 2 * ( toy*rt.TMath.Log(toy/expected) - toy )
                    if expected>0 and inFitRange:
                        n2llr_toy += 2 * ( expected )
                    if expected>0 and inFitRange:
                        nll_toy -= toy*rt.TMath.Log(expected) - expected

        # to check  nll, chi2 calculation
        #nll_func_toy = extDijetPdf.createNLL(asimov,rt.RooFit.Extended(True))
        #chi2_func_toy = extDijetPdf.createChi2(asimov,rt.RooFit.Extended(True),rt.RooFit.DataError(rt.RooAbsData.Expected))
        
        #print ''
        #print "chi2 func:   ", chi2_func_toy.getVal()
        #print "chi2 by hand  ", chi2_toy
        #print "nll func:    ", nll_func_toy.getVal()
        #print "nll by hand: ", nll_toy
            
        value = setattr(s1, 'nll_%s'%options.box, nll_toy)
        value = setattr(s1, 'n2llr_%s'%options.box, n2llr_toy)
        value = setattr(s1, 'chi2p_%s'%options.box, chi2p_toy)
        value = setattr(s1, 'chi2_%s'%options.box, chi2_toy)
        value = setattr(s1, 'chi2non0_%s'%options.box, chi2non0_toy)

        
        value =  setattr(s1, 'toy_num', iToy) # save toy number
        #pbar.update(iToy)
        myTree.Fill()
        iToy+=1        
    rt.RooMsgService.instance().reset()
    #pbar.finish()
    
    w.Print('v')
    output.cd()
    myTree.Write()
    w.Write()
    output.Close()
    return output.GetName()

        
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c','--config',dest="config",type="string",default="config/run2.config",
                  help="Name of the config file to use")
    parser.add_option('-d','--dir',dest="outDir",default="./",type="string",
                  help="Output directory to store cards")
    parser.add_option('-l','--lumi',dest="lumi", default=3000.,type="float",
                  help="integrated luminosity in pb^-1")
    parser.add_option('-b','--box',dest="box", default="MultiJet",type="string",
                  help="box name")
    parser.add_option('-t','--toys',dest="nToys", default=3000,type="int",
                  help="number of toys")
    parser.add_option('-s','--seed',dest="seed", default=-1,type="int",
                  help="random seed")
    parser.add_option('--no-stat',dest="noStat",default=False,action='store_true',
                  help="no statistical uncertainty, just systematic uncertainty, default is statstical + systematic uncertainty")
    parser.add_option('--no-sys',dest="noSys",default=False,action='store_true',
                  help="no systematic uncertainty, just statistical uncertainty, default is statstical + systematic uncertainty")
    parser.add_option('--freq',dest="freq",default=False,action='store_true',
                  help="refit each toy with only statistical fluctuations, as in frequentist approach; default is bayeseian")
    parser.add_option('-r','--signal-strength',dest="r", default=-1,type="float",
                  help="signal strength => do each fit the the SpB pdf")
    parser.add_option('-i','--input-fit-file',dest="inputFitFile", default=None,type="string",
                  help="input fit file")
    parser.add_option('--fit-region',dest="fitRegion",default="Full",type="string",
                  help="Fit region")
    parser.add_option('--sim',dest="doSimultaneousFit", default=False,action='store_true',
                  help="do simultaneous trigger fit")
    
    (options,args) = parser.parse_args()
    
    cfg = Config.Config(options.config)
    
    lumi = options.lumi

    inputFitFile = options.inputFitFile    
    
    lumi_in = 0.
    
    rt.RooMsgService.instance().setGlobalKillBelow(rt.RooFit.FATAL)

    if inputFitFile is not None:
        rootFile = rt.TFile.Open(inputFitFile,"r")
        w = rootFile.Get("w"+options.box)
        if w.obj("fitresult_extDijetPdf_data_obs") != None:
            fr = w.obj("fitresult_extDijetPdf_data_obs")
        elif w.obj("nll_extDijetPdf_data_obs") != None:
            fr = w.obj("nll_extDijetPdf_data_obs")
        elif w.obj("fitresult_extDijetPdf_data_obs_with_constr") != None:
            fr = w.obj("fitresult_extDijetPdf_data_obs_with_constr")
        elif w.obj("nll_extDijetPdf_data_obs_with_constr") != None:
            fr = w.obj("nll_extDijetPdf_data_obs_with_constr")
        
    outputName = runToys(w,options,cfg,options.seed)

    print "writing tree to %s"%(outputName)
