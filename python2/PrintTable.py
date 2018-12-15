import ROOT as rt
import os.path
import sys, glob, re
from array import *
from optparse import OptionParser

from Plot1DLimit import getHybridCLsArrays

if __name__ == '__main__':

    directory = {'gg':'Limits/gg/',
                 'qg':'Limits/qg/',
                 'qq':'Limits/qq/',
                 'gaus':'Limits/gaus/'}

    Box  = 'CaloDijet20152016'    
    #Box  = 'PFDijet2016'

    observed = {}
    expected = {}
    
    models = ['gg','qq','gaus']
    #models = ['gg','qg','qq']
    
    for model in models:
        gluinoMassArray, gluinoMassArray_er, observedLimit, observedLimit_er, expectedLimit, expectedLimit_minus1sigma, expectedLimit_plus1sigma, expectedLimit_minus2sigma, expectedLimit_plus2sigma = getHybridCLsArrays(directory[model], model, Box, False)
        observed[model] = observedLimit
        expected[model] = expectedLimit

    for i,mass in enumerate(gluinoMassArray):
        print '%i & %e & %e & %e & %e & %e & %e\\\\'%(mass, observed[models[0]][i], expected[models[0]][i], observed[models[1]][i], expected[models[1]][i], observed[models[2]][i], expected[models[2]][i])
        #print '%.1f & %e & %e & %e & %e & %e & %e\\\\'%(mass/1000., observed[models[0]][i], expected[models[0]][i], observed[models[1]][i], expected[models[1]][i], observed[models[2]][i], expected[models[2]][i])

        
