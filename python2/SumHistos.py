from optparse import OptionParser
import ROOT as rt
import rootTools
from array import *
import os
import sys

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-o','--output',dest="output",default="./",type="string",
                  help="Output ROOT file to store output histograms")
    parser.add_option('-l','--list',dest="list", default="lists/testlist.txt",type="string",
                  help="test list")

    (options,args) = parser.parse_args()
    
    f = open(options.list)
    histoList = {}
    for i, line in enumerate(f):
        if i == 0:
            print 'Creating list of histos from file',line.replace('\n','')
            rootFile = rt.TFile.Open(line.replace('\n',''))
            for k in rootFile.GetListOfKeys():
                obj = rootFile.Get(k.GetName())
                if obj.Class().InheritsFrom(rt.TH1.Class()):
                    histoList[k.GetName()] = obj
                    histoList[k.GetName()].SetDirectory(0)

            #print 'list of histograms',histoList
        else:
            print 'Summing',line.replace('\n','')
            rootFile = rt.TFile.Open(line.replace('\n',''))
            for n,h in histoList.iteritems():
                myh = rootFile.Get(n)
                h.Add(myh)



    output = rt.TFile(options.output,'recreate')
    output.cd()
    for n,h in histoList.iteritems():
        h.Write()
    output.Close()
