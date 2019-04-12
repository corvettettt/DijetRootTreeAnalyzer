from rootTools import tdrstyle as setTDRStyle 
from ROOT import *
from array import array

x = [0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.8838,0.9,0.9693]

x_bg_1b = array('d',[0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.9,0.9693])
x_bg_le1b = array('d',[0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.9,0.9693]) 
x_bb_2b = array('d',[0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35]) 
x_bb_le1b = array('d',[0.0521,0.1,0.1522,0.2,0.25,0.3033,0.35,0.4,0.45,0.4941,0.55,0.5803,0.6,0.65,0.7,0.7489,0.8001,0.85,0.9])

 
y_bg_1b = array('d',[0.442,0.406,0.402,0.426,0.454,0.498,0.5585,0.63,0.698,0.754,0.868,0.924,0.98,1.14,1.364,1.672,2.152,2.824,3.816,10.472])
y_bg_le1b = array('d',[0.379,0.365,0.377,0.402,0.442,0.486,0.546,0.618,0.69,0.746,0.858,0.916,0.972,1.124,1.348,1.658,2.12,2.824,3.816,10.362])
y_bb_2b= array('d',[3892.25,3566.75,3335.75,3110.75,2929.25,2738.25,2624.75 ])
y_bb_le1b= array('d',[4059.75,3923.75,3769.75,3609.75,3423.25,3261.25,3151.25,3031.25,2875.25,2798.25,2752.25,2710.25,2637.75,2512.75,2379.75,2159.75,1963.75,1836.25 ])
x_bg_1b_non = array('d',[])
x_bg_le1b_non = array('d',[]) 
x_bb_2b_non = array('d',[]) 
x_bb_le1b_non = array('d',[]) 
for i in x_bg_1b:
  x_bg_1b_non.append(0.395)
for i in x_bg_le1b: 
  x_bg_le1b_non.append(0.395) 
for i in y_bb_2b:
  x_bb_2b_non.append(4021.75)
for i in y_bb_le1b: 
  x_bb_le1b_non.append(4021.75)


gr_bg_1b_non = TGraph(len(x_bg_1b),x_bg_1b,x_bg_1b_non)
gr_bg_le1b_non = TGraph(len(x_bg_le1b),x_bg_le1b,x_bg_le1b_non) 
gr_bb_2b_non = TGraph(len(x_bb_2b),x_bb_2b,x_bb_2b_non) 
gr_bb_le1b_non = TGraph(len(x_bb_le1b),x_bb_le1b,x_bb_le1b_non) 


gr_bg_1b = TGraph(len(x_bg_1b),x_bg_1b,y_bg_1b)
gr_bg_le1b = TGraph(len(x_bg_le1b),x_bg_le1b,y_bg_le1b)
gr_bb_2b = TGraph(len(x_bb_2b),x_bb_2b,y_bb_2b)
gr_bb_le1b = TGraph(len(x_bb_le1b),x_bb_le1b,y_bb_le1b)
c = TCanvas()
c.SetLogy()
gr_bg_1b.SetLineColor(kRed)
gr_bg_le1b.SetLineColor(kBlue)
gr_bg_le1b_non.SetLineColor(17)
gr_bg_le1b_non.SetLineStyle(2)
leg = TLegend(0.75,0.8,0.9,0.9)
leg.AddEntry(gr_bg_1b,'1b','L')
leg.AddEntry(gr_bg_le1b,'le1b','L')
leg.AddEntry(gr_bg_le1b_non,'Non','L')
gr_bg_1b.SetTitle('Xsec of expected @ 2TeV;discriminator;\sigma * B * A[pb]')
gr_bg_1b.Draw()
gr_bg_le1b.Draw('same')
gr_bg_le1b_non.Draw('same')
leg.Draw('same') 
c.Print('bg.pdf')

c = TCanvas() 
gr_bb_2b.SetLineColor(kRed) 
gr_bb_le1b.SetLineColor(kBlue)
gr_bb_le1b_non.SetLineColor(17)
gr_bb_le1b_non.SetLineStyle(2)
gr_bb_le1b.SetTitle('Expected Limit Scan;Discriminator;Expected Limit(GeV)')
leg = TLegend(0.75,0.8,0.9,0.9) 
leg.AddEntry(gr_bb_2b,'2b','L') 
leg.AddEntry(gr_bb_le1b,'le1b','L') 
leg.AddEntry(gr_bb_le1b_non,'non','L') 
gr_bb_le1b.Draw() 
gr_bb_2b.Draw('same') 
gr_bb_le1b_non.Draw('same')
leg.Draw('same')  
c.Print('bb.pdf') 
