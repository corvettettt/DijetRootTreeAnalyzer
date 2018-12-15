import os

for i in os.listdir('.'):
  print i
  if not '_Dec_' in i:
    continue
  if 'bg' in i :
    os.system('cp '+i+' '+i+'_1b -r ')
    os.system('cp '+i+' '+i+'_le1b -r ')
  if 'bb' in i :
    os.system('cp '+i+' '+i+'_2b -r ')
    os.system('cp '+i+' '+i+'_le1b -r ')
