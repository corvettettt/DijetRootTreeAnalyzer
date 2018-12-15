import os
import ROOT as rt
from rootTools import tdrstyle as setTDRStyle

class Drawer():
    """Class to draw overlayed histos for data and signals"""

    def __init__(self, hData, hSignal):
        print "Drawer::init"

        self._hData = hData
        self._hSignal = hSignal

        self._dataHistos = {}
        self._sigHistos = {}

        #get the histos
        for sample,opts in hData.items():
            self._dataHistos[sample] = self.loopfile(opts[0])
        for sample,opts in hSignal.items():
            self._sigHistos[sample] = self.loopfile(opts[0])


    def scalePlots(self, lumi):
        for sample,opts in self._hSignal.items():
            for histo in self._sigHistos[sample]:
                integral = histo.Integral()
                if integral > 0:
                    print opts[1]*lumi/integral
                    histo.Scale(opts[1]*lumi/integral)


    def loopfile(self, infile):
        print "Drawer::loopfile",infile
        hlist = []
        rootFile = rt.TFile(infile)
        hnames = [k.GetName() for k in rootFile.GetListOfKeys()]
        for name in hnames:
            myTh1 = rootFile.Get(name)
            myTh1.SetDirectory(0)
            hlist.append(myTh1)
            
        return hlist
    
    def setStyle(self):
        print "Drawer::setStyle"
        setTDRStyle.setTDRStyle()

        
        

    def addRatioBox(self, histo):
        print "Drawer::addRatioBox"


    def printPlots(self, outPath):
        print "Drawer::printCanvas"
        self.setStyle()

        for it,dataplot in enumerate(self._dataHistos["data"]):
            corrCanvas = rt.TCanvas()

            dataplot.Draw()

            for mcsample,hlist in self._sigHistos.items():
                hlist[it].Draw("sames")
                
            
            corrCanvas.Print(outPath+'/'+dataplot.GetName()+'.pdf')

        #self.addRatioBox()



    #def drawSignificance
