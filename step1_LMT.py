import sys
 
command = '' 
for n in ['CSVv2','deep']:
 for m in ['2017','2016']:
  for i in ['qq','qg']:
    if i == 'qq': 
     flavor = 'bb'
    if i == 'qg': 
     flavor = 'bg'
    for j in ['central','up','down']:
     command += 'python python/bTag_signalStudies_scan_'+n+'_'+m+'_LMT.py -f %s -m %s -s %s'%(flavor,i,j)+'\n'
     if j=='central':
      if i =='qq':
        cate = ['le1b','2b','Non']
      elif i =='qg':
        cate = ['le1b','1b','Non']
      for k in cate:
#        command  += 'cp -r signalHistos_%s_Dec_ForScan_'%flavor+n+'_central signalHistos_%s_Dec_ForScan_'%flavor+n+'_central_'+k+'\n'
	pass
print command
 
