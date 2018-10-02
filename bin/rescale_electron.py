import os, commands
import optparse
from os import listdir
from os.path import isfile, join
from ROOT import *

usage = 'python rescale_electron.py --pathin Plot/electron/ --pathout Plot/fit/ --lep electron --resc 0.5 --shift -0.025'
parser = optparse.OptionParser(usage)
parser.add_option('--pathin', dest='pathin', type='string', default='Plot/electron/', help='')
parser.add_option('--pathout', dest='pathout', type='string', default='Plot/R_electron/', help='')
parser.add_option('--lep', dest='lep', type='string', default='electron', help='')
parser.add_option('--shift', dest='shift', default=0.0, help='')
parser.add_option('--resc', dest='resc', default=1.0, help='')
(opt, args) = parser.parse_args()

gStyle.SetPalette(1)
gStyle.SetOptStat(0)
gROOT.SetBatch()        # don't pop up canvases


def getall(d, basepath=""):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
        if key.IsFolder():
            # TODO: -> "yield from" in Py3
            for i in getall(d.Get(kname), basepath+"/"+kname+"/"):
                yield i
        else:
#            yield basepath+"/"+kname, d.Get(kname)
            yield kname, d.Get(kname)

pathin = opt.pathin
if opt.pathin != "Plot/electron/":
     pathin == opt.pathin

pathout = opt.pathout
if opt.pathout != "Plot/R_electron/":
     pathout == opt.pathout

tmp = TH1F()
prev_str = ""
shift = float(opt.shift)
rescalefact = float(opt.resc)
infiles = [f for f in listdir(pathin) if isfile(join(pathin,f))]
lep = opt.lep

if not shift == 0.0:
    for f in infiles:
        if("WJets" in f):
            print "scaled file: ", f
            fin = TFile(pathin+f)
            fout = TFile(pathout+f, "UPDATE")
            for k, o in getall(fin):
                #    print o.ClassName(), k
                if(prev_str != k):
                    fin.cd()
                    tmp = fin.Get(k)
                    if "_"+lep in f: tmp.Scale(1+shift)
                    fout.cd()
                    tmp.Write()
                    tmp.Reset("ICES")
                prev_str = k
            fout.Close()
            fin.Close()
        else:
            os.system("cp "+pathin+f+ " "+pathout+f)
            print "copied file: ", f

samples = [
"ST_tch",
"ST_tch_sd",
"ST_tch_p_sd",
"ST_sch",
"ST_tW","TT","TT_sd","WJets","VV","DYJets"]

#,"DDQCD"
prev_str = ""
syst = "lepE"
#if lep =="muon": syst = "lepMu"

infile = []
if not rescalefact == 1:
    for s in samples:
        infile.append(TFile.Open(pathout+s+"_"+lep+"_"+syst+"Up.root", "UPDATE"))
        infile.append(TFile.Open(pathout+s+"_"+lep+".root"))
        infile.append(TFile.Open(pathout+s+"_"+lep+"_"+syst+"Down.root", "UPDATE"))
        for k, o in getall(infile[0]):
            if(prev_str != k):
                hnom = TH1F()
                hdown = TH1F()
                hup = TH1F()
                for inf in infile:
                    inf.cd()
                    tmp = (TH1F)(inf.Get(k))
                    filename = inf.GetName()
                    if("Up" in filename):
                        hup = tmp.Clone()
                    elif("Down" in filename):
                        hdown = tmp.Clone()
                    else:
                        hnom = tmp.Clone()
                if(hup.Integral()>hnom.Integral()):
                    hup.Scale((hnom.Integral()+rescalefact*(hup.Integral()-hnom.Integral()))/hup.Integral())
                    hdown.Scale((hnom.Integral()-rescalefact*(hnom.Integral()-hdown.Integral()))/hdown.Integral())
                elif(hdown.Integral()>hnom.Integral()):
                    hdown.Scale((hnom.Integral()+rescalefact*(hdown.Integral()-hnom.Integral()))/hdown.Integral())
                    hup.Scale((hnom.Integral()-rescalefact*(hnom.Integral()-hup.Integral()))/hup.Integral())
                for inf in infile:
                    inf.cd()
                    filename = inf.GetName()
                    if("Up" in filename):
                        hup.Write()
                    elif("Down" in filename):
                        hdown.Write()
            prev_str = k
        infile = []
