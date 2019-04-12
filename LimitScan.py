import ROOT as rt
from rootTools import tdrstyle as setTDRStyle
rt.gROOT.SetBatch()
setTDRStyle.setTDRStyle()


from ROOT import *

dis = {}
xsec = {}

dis['le1bbg'] = [0.2, 0.25, 0.3033, 0.35, 0.4, 0.45, 0.4941, 0.55, 0.5803, 0.6, 0.65, 0.7, 0.7498, 0.8001, 0.85]
dis['1bbg'] = [0.35, 0.4, 0.45, 0.4941, 0.55, 0.5803, 0.6, 0.65, 0.7, 0.7498, 0.8001, 0.85]
dis['le1bbb'] = [0.0521, 0.1, 0.1522, 0.2, 0.25, 0.3033, 0.35, 0.4, 0.45, 0.4941, 0.55, 0.5803, 0.6, 0.65, 0.7, 0.7498, 0.8001, 0.85, 0.9, 0.9793]
dis['2bbb'] = [0.0521, 0.1, 0.1522, 0.2, 0.25, 0.3033, 0.35, 0.4, 0.45, 0.4941, 0.55, 0.5803, 0.6, 0.65, 0.7, 0.7498, 0.8001, 0.85, 0.9]

xsec['le1bbg'] = [1829.25, 1831.25, 1856.75, 1862.25, 1866.25, 1871.75, 1874.75, 1877.75, 1877.75, 1877.75, 1871.25, 1861.75, 1855.25, 1845.75, 1831.25]
xsec['1bbg'] = [1806.25, 1824.75, 1834.25, 1844.25, 1848.25, 1850.75, 1850.75, 1845.75, 1835.75, 1832.75, 1819.75, 1814.25]
xsec['le1bbb'] = [4573.25, 4625.25, 4662.25, 4658.75, 4629.75, 4591.25, 4551.25, 4519.75, 4461.75, 4419.75, 4373.75, 4347.25, 4327.25, 4282.75, 4224.75, 4185.25, 4150.25, 4077.25, 3993.75, 3743.75]
xsec['2bbb'] = [4569.25, 4613.75, 4556.25, 4474.25, 4369.25, 4295.75, 4224.75, 4139.25, 4074.25, 4006.25, 3912.75, 3885.75, 3848.25, 3813.25, 3743.75, 3672.75, 3582.75, 3494.25, 3340.75]

gr = {}

for i in ['le1bbg','1bbg','le1bbb','2bbb']:
  gr[i] = TGraph(len(dis[i]),dis[i],xsec[i])

xsec['nobbb']
for i in dis['le1bbb']:
  xsec['nobbb'].append(4518.75)

gr['nobbb'] = TGraph(len(dis['le1bbb']),dis['le1bbb'],xsec['nobbb'])
gr['nobbb'].SetLineColor(kGrey)
gr['nobbb'].SetLineStyle(8)

c1 = TCanvas()
leg = TLegend(0.7,0.8,0.9,0.9)
gr['le1bbb'].SetLineColor(kRed)
gr['2bbb'].SetLineColor(kGreen)
leg.AddEntry(gr['le1bbb'],'le1b','L')
leg.AddEntry(gr['2bbb'],'2b','L')
leg.AddEntry(gr['nobbb'],'nob','L')
gr['le1bbb'].Draw()
gr['le1bbb']
gr['2bbb'].Draw('same')
gr['nobbb'].Draw('same')

