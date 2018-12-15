from ROOT import *
import array

gr = {}
Threshold =  {}
Limit     =  {}
for i in ['2017bg','2017bb','2016bg','2016bb']:
   Threshold[i]={}
   Limit[i]={}
   gr[i]={}
   for j in ['CSVv2','DeepCSV']:
     Threshold[i][j]={}
     Limit[i][j]={}
     gr[i][j]={}

Threshold['2017bg']['Non'] = []
Threshold['2017bb']['Non'] = []
Limit['2017bg']['Non'] = []
Limit['2017bb']['Non'] = []

Threshold['2016bg']['Non'] = []
Threshold['2016bb']['Non'] = []
Limit['2016bg']['Non'] = []
Limit['2016bb']['Non'] = []

for i in range(11):
  Threshold['2017bg']['Non'].append(0.1*i)
  Limit['2017bg']['Non'].append(1780.25)
  Threshold['2017bb']['Non'].append(0.1*i)
  Limit['2017bb']['Non'].append(4540.25)

  Threshold['2016bg']['Non'].append(0.1*i)
  Limit['2016bg']['Non'].append(1983.75)
  Threshold['2016bb']['Non'].append(0.1*i)
  Limit['2016bb']['Non'].append(4607.75)

Threshold['2017bg']['CSVv2']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800,883,969] 
Threshold['2017bg']['CSVv2']['1b'] = [350,400,494,580,600,650,700,750,800,883,969]
Threshold['2017bg']['DeepCSV']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]
Threshold['2017bg']['DeepCSV']['1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]

Threshold['2017bb']['CSVv2']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]
Threshold['2017bb']['CSVv2']['2b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]
Threshold['2017bb']['DeepCSV']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]
Threshold['2017bb']['DeepCSV']['2b'] = [100,152,200,250,300,350,400,494]

Threshold['2016bg']['CSVv2']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bg']['CSVv2']['1b'] = [350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bg']['DeepCSV']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848]
Threshold['2016bg']['DeepCSV']['1b'] = [150,221,300,350,400,450,500,542,600,632,700,750,800,848]

Threshold['2016bb']['CSVv2']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bb']['CSVv2']['2b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bb']['DeepCSV']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bb']['DeepCSV']['2b'] = [100,150,221,300,350,400,450]

Limit['2017bg']['CSVv2']['le1b'] = []
Limit['2017bg']['CSVv2']['1b'] = []
Limit['2017bg']['DeepCSV']['le1b'] = []
Limit['2017bg']['DeepCSV']['1b'] = []

Limit['2017bb']['CSVv2']['le1b'] = [4540.25,4545.75,4553.75,4564.25,4564.25,4559.25,4556.25,4528.25,4497.75,4489.75,4461.75,4432.75,4408.75,4368.75]
Limit['2017bb']['CSVv2']['2b'] = [4545.75,4548.75,4535,4497.75,4465.75,4416.75,4368.75,4274.25,4190.25,4170.25,4114.75,4028.75,4028.75,3839.75]
Limit['2017bb']['DeepCSV']['le1b'] = [4493.75,4379.25,4273.25,4180.75,4088.75,4008.25,3886.75,3671.75,3492.75,3461.25,3328.75,3220.75,3168.25,2990.25] 
[4493.75,4379.25,4273.25,4180.75,4088.75,4008.25,4008.25,3886.75,3671.75,3492.75,3461.25,3328.75,3220.75,3168.25,2990.25]
Limit['2017bb']['DeepCSV']['2b'] = [4224.75,4022.75,3836.25,3668.75,3445.75,3336.75,3427.25,3263.75]

Limit['2016bg']['CSVv2']['le1b'] = [1983.75,1983.75,1992.75,1993.25,1993.75,1993.75,1993.25,1993.75,1988.75,1985.25,1980.75,1972.25,1963.75,1942.25,1904.25,1830.25,1661.75] 
Limit['2016bg']['CSVv2']['1b'] = [1627.25, 1695.25,1783.75,1832.25,1843.75,1875.75,1887.75,1891.25,1899.75,1892.25,1866.25,1782.75,1649.25]
Limit['2016bg']['DeepCSV']['le1b'] = [1983.75,1983.75,1927.25,1888.75,1874.25,1856.75,1846.25,1834.75,1825.75,1813.75,1796.75,1768.25,1771.75,1746.25,1721.25]
Limit['2016bg']['DeepCSV']['1b'] = [1834.25,1876.25,1864.25,1858.25,1845.75,1836.25,1823.75,1818.25,1810.25,1793.25,1765.25,1770.75,1743.25,1718.25]

Limit['2016bb']['CSVv2']['le1b'] = [4613.75,4614.75,4620.25,4613.75,4600.75,4585.75,4570.75,4546.25,4528.25,4486.25,4463.25,4463.25,4365.75,4305.25,4228.25,4123.25,3901.25]
Limit['2016bb']['CSVv2']['2b'] = [4590.25,4590.75,4590.75,4474.75,4408.25,4362.25,4294.75,4227.25,4179.25,4087.25,4022.75,3884.25,3796.75,3679.25,3510.25,3355.75,3056.75]
Limit['2016bb']['DeepCSV']['le1b']  = [4595.75,4595.75,4502.25,4145.75,4102.25,4193.75,4079.25,4035.25,3941.25,3906.25,3955.25,3803.75,3682.25,3513.25,3364.75,3295.25,2942.25]
Limit['2016bb']['DeepCSV']['2b'] = [4461.25,4177.75,3988.75,3813.75,3800.25,3704.75,3542.75]


for i in ['2017bb','2016bg','2016bb']:
  for j in ['CSVv2','DeepCSV']:
    if i == '2016bg':
      cata = ['le1b','1b']
    else:
      cata = ['le1b','2b']
    for k in cata:
      if len(Threshold[i][j][k]) != len(Limit[i][j][k]):
	 print i+j+k+' length do not agree'
         continue
      gr[i][j][k]  = TGraph(len(Threshold[i][j][k]),array.array('d',[float(t)/1000.0 for t in Threshold[i][j][k]]),array.array('d',Limit[i][j][k]))

#gr['2017bg']['Non'] = TGraph(len(Threshold['2017bg']['Non']),array.array('d',Threshold['2017bg']['Non']),array.array('d',Limit['2017bg']['Non']))
#gr['2017bg']['Non'].SetLineStyle(2)
#gr['2017bg']['Non'].SetLineColor(kBlack)
gr['2017bb']['Non'] =  TGraph(len(Threshold['2017bb']['Non']),array.array('d',Threshold['2017bb']['Non']),array.array('d',Limit['2017bb']['Non']))
gr['2017bb']['Non'].SetLineStyle(2)
gr['2017bb']['Non'].SetLineColor(kBlack)

gr['2016bg']['Non'] = TGraph(len(Threshold['2016bg']['Non']),array.array('d',Threshold['2016bg']['Non']),array.array('d',Limit['2016bg']['Non']))
gr['2016bg']['Non'].SetLineStyle(2)
gr['2016bg']['Non'].SetLineColor(kBlack)
gr['2016bb']['Non'] =  TGraph(len(Threshold['2016bb']['Non']),array.array('d',Threshold['2016bb']['Non']),array.array('d',Limit['2016bb']['Non']))
gr['2016bb']['Non'].SetLineStyle(2)
gr['2016bb']['Non'].SetLineColor(kBlack)

for i in ['2016bb','2017bb','2016bg']:
  c1 = TCanvas() 
  leg = TLegend(0.7,0.8,.9,.95)
  c1.cd()
  for j in ['CSVv2','DeepCSV']:
    if i == '2017bb': 
      cata = ['le1b','2b']
    elif i == '2017bg':
      cata = ['le1b','1b']
    elif i == '2016bg':
       cata = ['le1b','1b']
    elif i == '2016bb':
       cata = ['le1b','2b']

    for k in cata:
      if k == 'le1b':
	gr[i][j][k].SetLineColor(kGreen)
      elif k == '2b':
        gr[i][j][k].SetLineColor(kBlue)
      else:
        gr[i][j][k].SetLineColor(kRed)
      if j == 'DeepCSV':
        gr[i][j][k].SetLineStyle(2)
      if k == 'le1b' and j =='CSVv2':
	gr[i][j][k].GetXaxis().SetTitle('Discriminator')
        gr[i][j][k].GetYaxis().SetTitle('Limit(GeV)')
	if '2016' in i:
           if 'bg' in i:
              gr[i][j][k].SetTitle('LimitScan for bstar in 2016 scenario')
           if 'bb' in i:
	       gr[i][j][k].SetTitle('LimitScan for Coloron in 2016 scenario')
        elif 'bb' in i:
	   gr[i][j][k].SetTitle('LimitScan for Coloron in 2017 scenario')
        elif 'bg' in i :
           gr[i][j][k].SetTitle('LimitScan for bstar in 2017 scenario')
        gr[i][j][k].Draw()

        gr[i]['Non'].Draw('same')
        leg.AddEntry(gr[i]['Non'],'NoTagApplied','l')
      else:
        gr[i][j][k].Draw('same')
      leg.AddEntry( gr[i][j][k],j+k,'l')
  leg.Draw('same')
  c1.Print('LimitScan'+i+'_sept13.pdf')

