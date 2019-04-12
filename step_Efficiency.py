for i in ['bb','bg']:
  for j in ['CSVv2','deep']:
    for k in ['2017','2016']:
      for m in ['LMT','']:
        if i == 'bb':
	  print 'python python/bTag_signalStudies_scan_%s_%s_%sEfficiency.py -m qq -f bb'%(j,k,m)
	if i == 'bg':
	  print 'python python/bTag_signalStudies_scan_%s_%s_%sEfficiency.py -m qg -f bg'%(j,k,m)
