from ROOT import *
from array import array

x_a= array('d',[0.1,0.15,0.2,0.3,0.35,0.45,0.5,0.5803,0.65,0.75,0.8,0.8838,0.9,0.9693])
CSV_0 = array('d',[0,0,0,3753.25,4029.25, 4369.25, 4497.25, 4625.25, 4713.75, 4828.75, 4878.75, 4961.25, 4975.25, 5034.75])
CSV_2 = array('d',[5071.75, 5032.75,4980.25,4904.75,4856.75,4766.25, 4688.75,4600.75,4528.75,4358.75, 4236.75,3997.25,3892.25,2729.25])
CSV_le1 = array('d',[5079.75, 5077.75, 5066.25, 5058.25, 5049.25, 5026.75, 4999.25, 4970.75, 4951.75, 4888.75, 4846.75, 4733.75, 4693.75, 4455.75])
#DCSV_0 = array('d',)
#DCSV_2 = array('d',[5071.75,5032.75, 4980.25, 4904.75, 4856.75, 4766.25, 4688.75, 4600.75, 4528.75, 4358.75, 4236.75, 3997.25, 3892.25, 2729.25])
#DCSV_le1 = array('d',)

gr0 = TGraph(len(x_a),x_a,CSV_0)
gr0.SetLineColor(kBlack)
grle1 = TGraph(len(x_a),x_a,CSV_le1)
grle1.SetLineColor(kGreen)
gr2 = TGraph(len(x_a),x_a,CSV_2)
gr2.SetLineColor(kBlue)

c1= TCanvas()
gr0.Draw("APL")
gr2.Draw("PLsame")
grle1.Draw("PLsame")

leg = TLegend(0.87, 0.80, 0.96, 0.89)
leg.AddEntry(gr0,'0-tag',"L")
leg.AddEntry(gr2,"2-tag","L")
leg.AddEntry(grle1,"le1-tag","L")
leg.Draw("same")

c1.Print("Scan.pdf")
