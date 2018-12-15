
import ROOT as rt
from array import array

if __name__ == '__main__':
    tfile = rt.TFile.Open('inputs/data_CaloScoutingHT_Run2016BCDEFG_BiasCorrected_Mjj300_Golden27637pb_CaloDijet2016.root')
    myTH1 = tfile.Get('h_mjj_HLTpass_HT250_1GeVbin')
    
    x = array('d',[489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037])
    myTH1.Rebin(len(x)-1,'data_obs_rebin',x)
    myRebinnedTH1 = rt.gDirectory.Get('data_obs_rebin')
    myRebinnedTH1.SetDirectory(0)
    lumi = 27.6
    
    for i in range (1, len(x)):
        bincontent = myRebinnedTH1.GetBinContent(i)
        binwidth = myRebinnedTH1.GetBinWidth(i)
        binerror = myRebinnedTH1.GetBinError(i)
        myRebinnedTH1.SetBinContent(i,bincontent/(binwidth*lumi))  
        myRebinnedTH1.SetBinError(i,binerror/(binwidth*lumi))    

    func = rt.TF1('func','exp([1]*pow(x/[0],[2]) + [3]*pow(1.0-x/[0],[4])*(1+[5]*x/[0]))',x[0],x[-1])
    func.FixParameter(0,13000)
    func.SetParameter(1,1e4)
    func.SetParameter(2,0.1)
    func.SetParameter(3,0.1)
    func.SetParameter(4,0.1)
    func.FixParameter(5,0)


    myRebinnedTH1.Fit('func')

    c = rt.TCanvas('c','c',500,400)
    c.SetLogy()
    myRebinnedTH1.Draw()
    func.Draw('same')
    c.Print('simplefit.pdf')
