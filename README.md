Set up
============

```
cmsrel CMSSW_7_4_14

cd CMSSW_7_4_14/src/

cmsenv

git clone https://github.com/corvettettt/DijetRootTreeAnalyzer.git

git clone -b dijetpdf_74X https://github.com/RazorCMS/HiggsAnalysis-CombinedLimit HiggsAnalysis/CombinedLimit

scram b -j 4

cd DijetRootTreeAnalyzer
```


Update
============
Just use step1.py step2.py step3.py for no-weight-appliy limit
and use step1_LMT.py step2_LMT.py step3_LMT.py for weight-appliy limit

Coresponding parameters should be modified in the python file in python/.

For Scan
============

```
1. python python/bTag_signalStudies_scan.py -m qq -f bg  #(or qq/bb ) 
2. python python/bTag_extractShapes_Interpolater_scan.py -m qq -e #(Folder name produced in last step)
3. python python/extract.py -m qq -i #(Folder name produced in last step)
4. python python/ReScaleInterpolation.py -m qq -F #(Folder name produced in last step)
```

For Normal 
============

```
1. python python/bTag_extractShapes_Interpolater_le1.py  -m qg -f bg  #(or qq/bb )
2. python python/bTag_signalStudies_le1.py -m qg -e #(Folder name produced in last step)
```


Then
============
```
After these two step, you will have a large amount of JESUP, JESDOWN and JER in the folder. 
You can use TIP2 to do the following steps:
1. add a new box in the config/dijet.config
2. change the histoName of this box
3. modifiy the python/RunCombine_I_btag.py, add the JESUP, JESDOWN and JER to the right position. 
4. modifiy the python/RunCombine_I_btag.py, add the Nominal. 
6. modifiy the python/RunCombine_I_btag.py, add the background of this box



Then all the preparation is ready. You can use the following command to excute everything:

python python/Working.py -b PFDijetbb2016Scan100 -f PFDijetbb2016Scan100Scan -o cards_qq_freq_100_scan -s signalHistos_bb_FinalScan/ResonanceShapes_qq_bg_13TeV_Spring16_100_Nominal_Interpolation_rescale.root -m qq -p exp

# option:( -b : box name / -f Folder which stores Fit Result / -o Folder which stores limit / -s Nominal root file place / -m model / -p expected or observed)

#  this will excute the following command:
#  1. python python/BinnedFit.py -c config/dijet.config -l 35900 -m qq -s signalHistos_bg/ResonanceShapes_qg_bb_13TeV_Spring16.root xinputs/JetHT_run2016_moriond17_red_cert_v2.root -b PFDijetbg20161tt -d fits_2017_04/PFDijetbg20161tt/ --fit-spectrum
#  2. python python/RunCombine_I.py -m qq -d cards_qq_freq_2tt_I/ --mass range\(1600,7000,100\) -c config/dijet.config -i fits_2017_06/PFDijetbb20162tt_I/DijetFitResults_PFDijetbb20162tt.root -b PFDijetbb20162tt --rMax 20 --xsec 1e-3 -l 35.900
#  3. python python/GetCombine.py -d cards_qg_freq_tt/ -m qg --mass range\(1600,7000,100\) -b PFDijetbg20161tt --xsec 1e-3 -l 35.900
#  4. python python/Plot1DLimit.py -d cards_qg_freq_tt_U/ -m qg -b PFDijetbg20161tt -l 35.900 --massMin 1000 --massMax 8000 --xsecMin 1e-4 --xsecMax 1e2


After that, there will be a print out to show the limit.

Or, for scan purpose, you can do:

python python/excute.py -p exp -m qq -F signalHistos_bb_Dec13_ForScan -t PFDijet2016Scan

# option:(-p expected or observed / -m model -F Folder in which all root files are / -t tag of boxes)


```

TIP1
============
```
inputs/JetHT_run2016_moriond17_red_cert_v2.root       --> original one
inputs/JetHT_run2016_moriond17_red_cert_v2_scan.root  --> use for scan, 0.1~0.95 with 0.5 step + 0.935
inputs/JetHT_run2016_moriond17_red_cert_v2_all.root   --> use for no-tag applied(no requirement)
inputs/JetHT_run2016_moriond17_red_cert_v2_le1.root   --> use for more than 0 btag.
```

TIP2
============
```
python python/bTag_ForScan.py  -f signalHistos_bb_Dec13_ForScan -t PFDijet2016Scan_ -m qq -c le1
#option (-f Folder contains all root files. / -t tag of the boxes / -m model / -c btag catagory)
--> add all scan jes, jer, norminal and so on


python python/bTag_Add.py -u test1 -d test2 -r test3 -n test4 -g test5 -b testbox -H test7
#option:(-u Jet energy scale up / -d Jet energy scale down / -r Jet energy resolution / -n nominal / -g background / -b box name / -H histo name in bg file)
-> just add one jes, jer, nominal and so on .


```
