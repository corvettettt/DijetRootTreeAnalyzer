import sys
 
command = '' 
for n in ['CSVv2','deep']:
 for m in ['2017','2016']:
  for i in ['qq','qg']:
    if i == 'qq': 
     flavor = 'bb'
    if i == 'qg': 
     flavor = 'bg'
    command += 'python python/bTag_signalStudies_scan_'+n+'_'+m+'.py -f %s -m %s'%(flavor,i)+'\n'
#    if i =='qq':
#        cate = ['le1b','2b','Non']
#    elif i =='qg':
#        cate = ['le1b','1b','Non']
#    for k in cate:
#        command  += 'cp -r signalHistos_%s_Dec_ForScan_'%flavor+n+' signalHistos_%s_Dec_ForScan_'%flavor+n+'_'+k+'\n'

print command
 
