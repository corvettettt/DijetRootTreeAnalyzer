import os

last = ''

for F in sorted(os.listdir('ExucteCommandBox')):
  if 'PFNo10Dijet2016bbdeep2b' in F:
    if last != F.replace('.sh',''):
      print '\n\n'+F.replace('.sh','')+'\n\n'
      last = F.replace('.sh','')
    with open('ExucteCommandBox/'+F) as f:
      for i in f.readlines():
        if 'Plot1D' in i:
	  os.system(i) 
	  #print(' ')
