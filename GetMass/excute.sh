#!/bin/bash

python GetMass.py -i FileList_QCD500.txt -o QCD500.root
python GetMass.py -i FileList_QCD700.txt -o QCD700.root
python GetMass.py -i FileList_QCD1000.txt -o QCD1000.root
python GetMass.py -i FileList_QCD1500.txt -o QCD1500.root
python GetMass.py -i FileList_QCD2000.txt -o QCD2000.root
