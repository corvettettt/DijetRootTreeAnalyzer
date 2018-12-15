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

if '__main__'==__name__:
    parser = OptionParser()
    parser.add_option('-i','--Input',dest="Input",type="string",default="none",
                      help="Name of the signal flavour")
    parser.add_option('-o','--Output',dest="Output",type="string",default="non",
                      help="Name of the signal model")
    (options,args) = parser.parse_args()
    Input = options.Input
    Output  = options.Output
    flist = open(Input)
   

    tchain = TChain('rootTupleTree/tree')
    for i in flist.readlines():
        tchain.Add(i.replace('\n','').replace('\t',''))

    nEntries = tchain.GetEntries()

    content = ''

    #for i in progressbar(range(nEntries), 'Progress: ', 40):
    for i in range(nEntries):#in progressbar(range(nEntries), 'Progress: ', 40):
        tchain.GetEntry(i)

        if not (abs(tchain.deltaETAjj)<1.3       and
                abs(tchain.etaWJ_j1)<2.5         and
                abs(tchain.etaWJ_j2)<2.5         and

                tchain.pTWJ_j1>60                and
                tchain.pTWJ_j2>30                and
                tchain.PassJSON):
            continue


        if tchain.mjj > 7000:
            content += 'Run  '+str(tchain.run)+'\tEvent  '+str(tchain.event)+'\tmass  '+str(tchain.mjj)+'\n'


    Fout = open(Output,'w+')
    Fout.write(content)
    Fout.close()
