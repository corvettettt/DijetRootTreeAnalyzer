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

hold['2016bg']['Non'] = []
Threshold['2016bb']['Non'] = []
Limit['2016bg']['Non'] = []
Limit['2016bb']['Non'] = []

for i in range(11):
  Threshold['2017bg']['Non'].append(0.1*i)
  Limit['2017bg']['Non'].append(1780.25)
  Threshold['2017bb']['Non'].append(0.1*i)
  Limit['2017bb']['Non'].append(4502.25)

  Threshold['2016bg']['Non'].append(0.1*i)
  Limit['2016bg']['Non'].append(1780.25)
  Threshold['2016bb']['Non'].append(0.1*i)
  Limit['2016bb']['Non'].append(4502.25)

Threshold['2017bg']['CSVv2']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800,883,969] 
Threshold['2017bg']['CSVv2']['1b'] = [350,400,494,580,600,650,700,750,800,883,969]
Threshold['2017bg']['DeepCSV']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]
Threshold['2017bg']['DeepCSV']['1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800]

Threshold['2017bb']['CSVv2']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800,883,969]
Threshold['2017bb']['CSVv2']['2b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800,883,969]
Threshold['2017bb']['DeepCSV']['le1b'] = [100,152,200,250,300,350,400,494,580,600,650,700,750,800,883]
Threshold['2017bb']['DeepCSV']['2b'] = [100,152,200,250,300,350,400,494,580,600]

Threshold['2016bg']['CSVv2']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bg']['CSVv2']['1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bg']['DeepCSV']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bg']['DeepCSV']['1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]

Threshold['2016bb']['CSVv2']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bb']['CSVv2']['2b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bb']['DeepCSV']['le1b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]
Threshold['2016bb']['DeepCSV']['2b'] = [100,150,221,300,350,400,450,500,542,600,632,700,750,800,848,895,953]

Limit['2017bg']['CSVv2']['le1b'] = 
Limit['2017bg']['CSVv2']['1b'] = 
Limit['2017bg']['DeepCSV']['le1b'] = 
Limit['2017bg']['DeepCSV']['1b'] = 

Limit['2017bb']['CSVv2']['le1b'] = 
Limit['2017bb']['CSVv2']['2b'] = 
Limit['2017bb']['DeepCSV']['le1b'] = 
Limit['2017bb']['DeepCSV']['2b'] = 

Limit['2016bg']['CSVv2']['le1b'] = 
Limit['2016bg']['CSVv2']['1b'] =
Limit['2016bg']['DeepCSV']['le1b'] =
Limit['2016bg']['DeepCSV']['1b'] =

Limit['2016bb']['CSVv2']['le1b'] =
Limit['2016bb']['CSVv2']['2b'] =
Limit['2016bb']['DeepCSV']['le1b'] =
Limit['2016bb']['DeepCSV']['2b'] =


for i in ['2017bg','2017bb','2016bg','2016bb']:
  for j in ['CSVv2','DeepCSV']:
    if i == '2017bb':
      cata = ['le1b','2b']
    else:
      cata = ['le1b','1b']
    for k in cata:
      if len(Threshold[i][j][k]) != len(Limit[i][j][k]):
	 print i+j+k+' length do not agree'
         continue
      gr[i][j][k]  = TGraph(len(Threshold[i][j][k]),array.array('d',[float(t)/1000.0 for t in Threshold[i][j][k]]),array.array('d',Limit[i][j][k]))

gr['2017bg']['Non'] = TGraph(len(Threshold['2017bg']['Non']),array.array('d',Threshold['2017bg']['Non']),array.array('d',Limit['2017bg']['Non']))
gr['2017bg']['Non'].SetLineStyle(2)
gr['2017bg']['Non'].SetLineColor(kBlack)
gr['2017bb']['Non'] =  TGraph(len(Threshold['2017bb']['Non']),array.array('d',Threshold['2017bb']['Non']),array.array('d',Limit['2017bb']['Non']))
gr['2017bb']['Non'].SetLineStyle(2)
gr['2017bb']['Non'].SetLineColor(kBlack)

gr['2016bg']['Non'] = TGraph(len(Threshold['2016bg']['Non']),array.array('d',Threshold['2016bg']['Non']),array.array('d',Limit['2016bg']['Non']))
gr['2016bg']['Non'].SetLineStyle(2)
gr['2016bg']['Non'].SetLineColor(kBlack)
gr['2016bb']['Non'] =  TGraph(len(Threshold['2016bb']['Non']),array.array('d',Threshold['2016bb']['Non']),array.array('d',Limit['2016bb']['Non']))
gr['2016bb']['Non'].SetLineStyle(2)
gr['2016bb']['Non'].SetLineColor(kBlack)

for i in ['2017bg','2017bb','2016bg']:
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

