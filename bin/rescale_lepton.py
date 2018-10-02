### Decorrelate Q2 syst among the processes

import sys
import os, commands
import shutil
import ROOT
import copy
from samples.toPlot import samples
ROOT.TH1.SetDefaultSumw2()
ROOT.TH1.AddDirectory(False)
import optparse


usage = 'usage: %prog -d histosDir'
parser = optparse.OptionParser(usage)

parser.add_option('-d', '--dir', dest='path', type='string', default = './histos/', help='Histos folder')
parser.add_option('', '--debug', dest='debug', type='int', default = '1', help='Increment level of verbosity for debugging purposes')
parser.add_option('-s', '--sys', dest='sys', type='string', default = 'jes', help='Systematics to de-correlate')
parser.add_option('-n', '--nsmooth', dest='nsmooth', type='int', default = '1', help='Smoothing level')

(opt, args) = parser.parse_args()


channels = ["muon", "electron"]
shift = [0., -0.025]

syst = "q2"
vs = ["Up", "Down"]
nsmooth = opt.nsmooth

newsyst = ["q2TT", "q2SingleTop", "q2VV", "q2QCD", "q2DY", "q2WJets", "q2ZToNuNu", "q2otherBkg", "q2DMj", "q2DMtt", "q2ZJets"]

verbose = False

VariablesSl = ["metFinal","metFinal_2lep", "metFinal_met_0btag"]
VariablesFh = ["metFinal", "metFinal_SR_1lep", "metFinal_CR5", "metFinal_CR6nw", "metFinal_CR7nw"]




def raiseError(histo, var, filename): 
    if not isinstance(histo, ROOT.TH1):
        raise RuntimeError('Failed to load histogram  %s from file  %s' % ( var, filename))

                
def symmetrize(syst):
    for s in samples.itervalues():
        for ch in channels:
            print "+channel ", ch, " samples ", s.label
            nom = opt.path + s.label + "_" + ch + ".root"
            jesUp = opt.path + s.label + "_" + ch + "_"+syst+"Up.root"
            jesDown = opt.path + s.label + "_" + ch + "_"+syst+"Down.root"
            jesUpSym = opt.path + s.label + "_" + ch + "_sym"+syst+"Up.root"
            jesDownSym = opt.path + s.label + "_" + ch + "_sym"+syst+"Down.root"
         
            f_nom = ROOT.TFile(nom)
            f_jup = ROOT.TFile(jesUp)
            f_jdown = ROOT.TFile(jesDown)

            vars = VariablesFh
            if (ch=="semileptonic"): vars = VariablesSl
            histos_up = []
            histos_down = []
            for v in vars:
                h_nom = f_nom.Get(v)
                h_jup = f_jup.Get(v)
                h_jdown = f_jdown.Get(v)
                raiseError(h_nom, v, f_nom)
                raiseError(h_jup, v, f_jup)
                raiseError(h_jdown, v, f_jdown)

                ## nh_nom = copy.deepcopy(h_nom)
                ## nh_up = copy.deepcopy(h_jup)
                ## nh_down = copy.deepcopy(h_jdown)

             
                ## #nh_nom.Scale(2)
                ## nh_up.Add(nh_down, -1)
                ## nh_up.Scale(0.5)
                ## #print "+ Nom Integral: ", nh_up.Integral()
                ## nh_up.Smooth()
                ## #print "++ Nom Integral after smoothing: ", nh_up.Integral()

                ## sym_jup = copy.deepcopy(h_nom)
                ## sym_jup.Add(nh_up)
                ## sym_jdown = copy.deepcopy(h_nom)
                ## sym_jdown.Add(nh_up,-1)
                #if(opt.debug and s.label.startswith("TT") and ch=="semileptonic"):
                if(opt.debug ):
                    print "Variable: ",v
                    print "+ JesUp: ", h_jup.Integral()
                    print "+ Nom: ", h_nom.Integral()
                    print "+ JesDown: ", h_jdown.Integral()
                    ## print "++ New jesUp: ", sym_jup.Integral()
                    ## print "++ Nom:       ", h_nom.Integral()       
                    ## print "++ New jesDown: ", sym_jdown.Integral()       
                    ## print "-"*30  

                    sym_new_jup = copy.deepcopy(h_nom)
                    sym_new_jdown = copy.deepcopy(h_nom)
                    k_smooth = copy.deepcopy(h_nom)

                    print " --> Symmetrization "
                    for b in xrange(h_nom.GetNbinsX()):
                        print "bin ", b + 1
                        up =  h_jup.GetBinContent(b+1)
                        nom = h_nom.GetBinContent(b+1)
                        down = h_jdown.GetBinContent(b+1)
                        #print "up ", up, " down ", down
                        #k =  ROOT.TMath.Abs(up-down)/2
                        k =  max(ROOT.TMath.Abs(up-nom),ROOT.TMath.Abs(nom-down))
                        print " k_smooth ", nom-k, " for bin ", b
                        k_smooth.SetBinContent(b+1, k)

                    #k_smooth.Smooth(nsmooth)     
                    
                    print " --> Smoothing "
                    for b in xrange(k_smooth.GetNbinsX()):
                        print "k_smooth post bin  ", b+1, " value= ", k_smooth.GetBinContent(b+1)

                    sym_new_jup.Add(k_smooth)
                    sym_new_jdown.Add(k_smooth, -1)

                    for b in xrange(sym_new_jdown.GetNbinsX()):
                        if(sym_new_jdown.GetBinContent(b+1)<0):
                            nom = h_nom.GetBinContent(b+1)
                            sym_new_jdown.SetBinContent(b+1, (ROOT.TMath.Power(10,-6)*nom))
                            print " --> CHECK nom = ", nom, "  down ", sym_new_jdown.GetBinContent(b+1)   


                    histos_up.append( sym_new_jup)
                    histos_down.append( sym_new_jdown)

                    print "++ New-2 jesUp: ", sym_new_jup.Integral()
                    print "++ Nom:       ", h_nom.Integral()       
                    print "++ New-2 jesDown: ", sym_new_jdown.Integral()
                    print "-"*30  

            f_symjup = ROOT.TFile(jesUpSym,"RECREATE")
            f_symjup.cd()
            [h.Write() for h in histos_up]
            f_symjup .Close()
            f_symjdown = ROOT.TFile(jesDownSym, "RECREATE")
            f_symjdown.cd()
            [h.Write() for h in histos_down]
            f_symjdown .Close()
            


symmetrize(opt.sys)

