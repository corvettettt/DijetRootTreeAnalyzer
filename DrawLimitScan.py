from ROOT import *
import array

gr = {}
Threshold =  {}
Limit     =  {}
for i in ['2017bg','2017bb','2016bg']:
   Threshold[i]={}
   Limit[i]={}
   gr[i]={}
   for j in ['CSVv2','DeepCSV']:
     Threshold[i][j]={}
     Limit[i][j]={}
     gr[i][j]={}


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

Limit['2017bg']['CSVv2']['le1b'] = [1782.25,1792.25,1825.75,1849.25,1877.25,1899.25,1922.25,1942.75,1966.25,1968.25,1977.75,1977.75,1978.75,1964.75,1919.25,1619.25]
Limit['2017bg']['CSVv2']['1b'] = [1639.75,1673.25,1745.25,1822.25,1841.25,1875.75,1890.25,1904.75,1899.75,1877.25,1610.75]
Limit['2017bg']['DeepCSV']['le1b'] = [1912.25,1957.25,1966.75,1961.75,1962.25,1955.25,1950.75,1911.25,1876.75,1870.25,1850.25,1803.75,1791.75,1708.75]
Limit['2017bg']['DeepCSV']['1b'] = [1659.25,1823.75,1895.75,1919.25,1931.25,1932.75,1933.75,1897.75,1869.75,1863.75,1843.25,1796.25,1783.25,1702.25]

Limit['2017bb']['CSVv2']['le1b'] = [4502.25,4513.25,4518.75,4529.75,4529.75,4524.25,4518.75,4489.75,4465.75,4460.25,4432.75,4394.25,4381.25,4340.75,4194.25,3892.25]
Limit['2017bb']['CSVv2']['2b'] = [4502.25,4502.25,4502.25,4477.75,4442.75,4394.25,4352.75,4260.75,4183.25,4156.25,4087.75,3997.25,3954.25,3850.75,3626.25,2677.75]
Limit['2017bb']['DeepCSV']['le1b'] = [4468.75,4370.75,4270.25,4194.25,4102.25,4015.75,3901.25,3687.75,3504.25,3468.25,3334.75,3227.75,3204.25,3075.75,3082.75]
Limit['2017bb']['DeepCSV']['2b'] = [4203.25,4002.75,3837.75,3688.25,3490.25,3425.25,3355.25,3258.25,3289.25,3309.25,3121.25]

Limit['2016bg']['CSVv2']['le1b'] = [2046.25,2047.25,2057.75,2067.75,2073.75,2074.75,2077.75,2077.75,2077.75,2075.75,2070.75,2066.25,2061.25,2041.75,2017.25,1918.25,1848.75]
Limit['2016bg']['CSVv2']['1b'] = [1698.25,1763.75,1817.75,1855.75,1869.25,1884.25,1891.75,1899.75,1935.75,1984.25,1995.75,2008.25,2013.25,2002.75,1971.75,1891.75,1840.75]
Limit['2016bg']['DeepCSV']['le1b'] = [2062.25,2061.25,2024.75,1986.25,1968.75,1959.75,1956.25,1953.25,1950.25,1946.75,1943.75,1936.75,1941.25,1932.25,1920.25,1915.25,1848.75]
Limit['2016bg']['DeepCSV']['1b'] = [1859.25,1899.75,1977.25,1963.75,1953.75,1948.25,1949.25,1947.75,1944.75,1943.75,1942.25,1935.25,1940.25,1931.25,1919.25,1913.75,1846.75]

for i in ['2017bg','2017bb','2016bg']:
  for j in ['CSVv2','DeepCSV']:
    if i == '2017bb':
      cata = ['le1b','2b']
    else:
      cata = ['le1b','1b']
    for k in cata:
      if len(Threshold[i][j][k]) != len(Limit[i][j][k]):
	 print i+j+k+' length do not agree'
         continue
      gr[i][j][k]  = TGraph(len(Threshold[i][j][k]),array.array('d',Threshold[i][j][k]),array.array('d',Limit[i][j][k]))

for i in ['2017bg','2017bb','2016bg']:
  c1 = TCanvas() 
  leg = TLegend(0.7,0.7,.9,.8)
  c1.cd()
  for j in ['CSVv2','DeepCSV']:
    if i == '2017bb': 
      cata = ['le1b','2b']
    else:
      cata = ['le1b','1b']
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
        gr[i][j][k].Draw()
      else:
        gr[i][j][k].Draw('same')
      leg.AddEntry( gr[i][j][k],j+k,'l')
  leg.Draw('same')
  c1.Print('LimitScan'+i+'.pdf')

