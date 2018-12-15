import os 

filelist = [f for f in os.listdir('.') if 'output' in f and 'txt' in f]

content=''
for i in filelist:
  a = open(i)
  for j in a.readlines():
    if 'ETA1' in j:
      continue
    content += j

fout = open('merged.txt','w')
fout.write(content)
fout.close()
