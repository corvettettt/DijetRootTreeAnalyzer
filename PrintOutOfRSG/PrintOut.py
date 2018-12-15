from ROOT import *
import sys
from optparse import OptionParser
import array

def progressbar(it, prefix="", size=60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()

if __name__=='__main__':
    parser = OptionParser()
    parser.add_option('-i','--Input',dest="Input",type="string",default="none",
                      help="Name of the signal flavour")
    (options,args) = parser.parse_args()
    Input = options.Input
    flist = open(Input)
    
    tchain = TChain('rootTupleTree/tree')
    for i in flist.readlines():
        tchain.Add(i.replace('\n','').replace('\t',''))

    nEntries = tchain.GetEntries()

    n1=0
    n2=0
    Can = {}

    for i in progressbar(range(nEntries), 'Progress: ', 40):
      tchain.GetEntry(i)
      if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.PassJSON):
            continue
      if abs(tchain.jetpflavour_j1) ==  5 or abs(tchain.jetpflavour_j2) ==  5 :
        n1+=1
	continue
  
      #if abs(tchain.jetpflavour_j1) ==  5 and abs(tchain.jetpflavour_j2) ==  5 :
      #  n2+=1
   
      Now = [abs(int(tchain.jetpflavour_j1)),abs(int(tchain.jetpflavour_j2))]
      if 0 in Now:
        continue
      Now.sort()

      if not str(Now) in Can.keys():
        Can[str(Now)] = 1
      else  :
        Can[str(Now)] +=1
    print 'Total: '+str(nEntries)+'\nOne b: '+str(n1)+'\nTwo b: '+str(n2)
    print 'Else:'
    for i,j in Can.items():
      print i,' : ',j,'  ',float(j)/float(nEntries)*100,'%'
