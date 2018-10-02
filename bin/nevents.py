import os, commands
import optparse
import math
from ROOT import *

usage = 'python nevents.py'
parser = optparse.OptionParser(usage)
parser.add_option('--pathin', dest='pathin', type='string', default='Plot', help='')
parser.add_option('--pathout', dest='pathout', type='string', default='syst/', help='')
#parser.add_option('-L', '--lep', dest='lep', type='string', default='muon', help='Default checks integrals of muon systematics')
(opt, args) = parser.parse_args()

pathin = opt.pathin
if opt.pathin != "Plot":
     pathin == opt.pathin

pathout = opt.pathout
if opt.pathout != "syst/":
     pathout == opt.pathout

gStyle.SetPalette(1)
gStyle.SetOptStat(0)
gROOT.SetBatch()        # don't pop up canvases

leptons = {
     "muon":["h1D_2j1t_cr","h1D_2j1t_sr","h1D_3j1t_cr","h1D_3j1t_sr","h_3j2t_BDT_ST_vs_TT_3j2t"],
     "electron":["h1D_2j1t_cr","h1D_2j1t_sr","h1D_3j1t_cr","h1D_3j1t_sr","h_3j2t_BDT_ST_vs_TT_3j2t"]
#     "muon":["h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","h_2j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","h_3j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","h_3j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","h_3j2t_topMassLeading"],
#     "electron":["h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","h_2j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","h_3j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","h_3j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","h_3j2t_topMassLeading"]
#     "muon":["h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5", "h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5", "h_3j1t_BDT_ST_vs_VJ_mtweta_3j1t_mtw_G_50_AND_etajprime_L_2p5", "h_3j1t_BDT_STsd_vs_ST_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5", "h_3j2t_BDT_ST_vs_TT_3j2t"],
#     "electron":["h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5", "h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5", "h_3j1t_BDT_ST_vs_VJ_mtweta_3j1t_mtw_G_50_AND_etajprime_L_2p5", "h_3j1t_BDT_STsd_vs_ST_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5", "h_3j2t_BDT_ST_vs_TT_3j2t"]
     }

integrals = []
errors = []

samples = {
     "VV":"dibosons",
     "DYJets":"Z+Jets",
     "WJets_ext":"\\wjets",
#     "TT_sd":"t$\\bar{\\text{t}}_{\\text{sd}}$ decay",
     "TT":"\\ttbar",
     "ST_sch":"\\sch",
     "ST_tW":"tW assoc.prod.",
     "DDQCD":"QCD",
     "ST_tch_p_sd":"$t$-channel$_{\\text{sd}}$ production",
     "ST_tch_sd":"$t$-channel$_{\\text{sd}}$ decay",
     "ST_tch":"\\tch"
     }

def getSumError(_list):
     return math.sqrt(reduce(lambda x, y: x + y, list(map(lambda x: x**2, _list))))

def getSumSquared(_list):
     return reduce(lambda x, y: x + y, list(map(lambda x: x**2, _list)))

def getSignificance(_list):
     sign = []
     total = getSumSquared(_list)
     for el in _list:
          sign.append(100*(el**2/total))
#          print el, total 
     return sign

tex =  False #True #
signif =  True #False #
e = 0
for lep in leptons.keys():
     p=""
     for hist in leptons[lep]:
#          '''
          if lep == "muon" and hist == "h1D_2j1t_cr": 
               region = "muon_2j1t_central"
          elif lep == "muon" and hist == "h1D_2j1t_sr": 
               region = "muon_2j1t_forward"
          elif lep == "muon" and hist == "h1D_3j1t_cr": 
               region = "muon_3j1t_central"
          elif lep == "muon" and hist == "h1D_3j1t_sr": 
               region = "muon_3j1t_forward"
          elif lep == "muon" and hist == "h_3j2t_BDT_ST_vs_TT_3j2t":
               region = "muon_3j2t"
          elif lep == "electron" and hist == "h1D_2j1t_cr": 
               region = "electron_2j1t_central"
          elif lep == "electron" and hist == "h1D_2j1t_sr": 
               region = "electron_2j1t_forward"
          elif lep == "electron" and hist == "h1D_3j1t_cr": 
               region = "electron_3j1t_central"
          elif lep == "electron" and hist == "h1D_3j1t_sr": 
               region = "electron_3j1t_forward"
          elif lep == "electron" and hist == "h_3j2t_BDT_ST_vs_TT_3j2t":
               region = "electron_3j2t"
          '''

          if lep == "muon" and hist == "h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5":
               region = "muon_2j1t_central"
          elif lep == "muon" and hist == "h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5":
               region = "muon_2j1t_forward"
          elif lep == "muon" and hist == "h_3j1t_BDT_ST_vs_VJ_mtweta_3j1t_mtw_G_50_AND_etajprime_L_2p5":
               region = "muon_3j1t_central"
          elif lep == "muon" and hist == "h_3j1t_BDT_STsd_vs_ST_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5":
               region = "muon_3j1t_forward"
          elif lep == "muon" and hist == "h_3j2t_BDT_ST_vs_TT_3j2t":
               region = "muon_3j2t"
          elif lep == "electron" and hist == "h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5":
               region = "electron_2j1t_central"
          elif lep == "electron" and hist == "h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5":
               region = "electron_2j1t_forward"
          elif lep == "electron" and hist == "h_3j1t_BDT_ST_vs_VJ_mtweta_3j1t_mtw_G_50_AND_etajprime_L_2p5":
               region = "electron_3j1t_central"
          elif lep == "electron" and hist == "h_3j1t_BDT_STsd_vs_ST_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5":
               region = "electron_3j1t_forward"
          elif lep == "electron" and hist == "h_3j2t_BDT_ST_vs_TT_3j2t":
               region = "electron_3j2t"
               
          if(signif):
               infile = TFile.Open(pathin+"/"+lep+"/Data_"+lep+".root")
               tmp = (TH1F)(infile.Get(hist))
               for i in range(1,tmp.GetNbinsX()+1):
                    errors_bin = []
                    for s, sname in samples.iteritems():
                         error = Double(0)
                         infile = TFile.Open(pathin+"/"+lep+"/"+s+"_"+lep+".root")
                         tmp = (TH1F)(infile.Get(hist))
                         errors_bin.append(tmp.GetBinError(i))
                    print "Relative significance %-20s %-8s, bin %-2i" %(hist, lep, i)
                    for s, b in zip(samples.keys(), getSignificance(errors_bin)):
                         if(b>1.0):
                              e+=1
                              print "%-10s %-3f" %(s, b)
               print e
               '''
          if(signif):
               infile = TFile.Open(pathin+"/Data_"+lep+".root")
               tmp = (TH1F)(infile.Get(hist))
               for i in range(1,tmp.GetNbinsX()+1):
                    errors_bin = []
                    total_bin = 0
                    st_bin = 0
                    for s, sname in samples.iteritems():
                         error = Double(0)
                         infile = TFile.Open(pathin+"/"+s+"_"+lep+".root")
                         tmp = (TH1F)(infile.Get(hist))
                         errors_bin.append(tmp.GetBinError(i))
                         total_bin += tmp.GetBinContent(i)
                         if s == "ST_tch":
                              st_bin = tmp.GetBinContent(i)
#                    print "Relative uncertainty %-20s %-8s, bin %-2i" %(hist, lep, i)
                    b = 100*st_bin/total_bin
                    if(b>20): 
                         p += " mcstat_"+region+"_ST_tch_bin"+str(i)
                    for s, el in zip(samples.keys(), errors_bin):
                         sign = 100*el/total_bin
                         if(sign>4): # and s!="DDQCD" and s!="ST_sch" and s!="VV" and s=="WJets"
                              e+=1
#                              print "%-10s %-0.2f " %(s, sign)
                              p += " mcstat_"+region+"_"+s+"_bin"+str(i)
#               print e
          '''
          if(tex):
               print "**********************************************"
               print "\\begin{table}[]"
               print "\\begin{center}"
               print "\\caption{\label{tab:%s_%s} }" %(hist,lep)
               print "\\begin{tabular}{l|c}"
               print "Process  & Integral $\pm$  Uncertainty \\\\ " 
               print "\\hline"
               for s, sname in samples.iteritems():
                    error = Double(0)
                    infile = TFile.Open(pathin+"/"+lep+"/"+s+"_"+lep+".root")
                    tmp = (TH1F)(infile.Get(hist))
                    integrals.append(tmp.IntegralAndError(1,tmp.GetNbinsX()+1, error))
                    errors.append(error)
                    if(tex):
                    print "%-10s  & %-6i $\pm$  %-3i \\\\ " %(sname,integrals[-1],errors[-1])
               tmp.Reset("ICES")
          if(tex):
               print "\\hline"
               print "Total MC  & %-6i $\pm$  %-3i \\\\ " %(sum(integrals),getSumError(errors))
               print "\\hline"
          integrals = []
          errors = []
          filedata=TFile.Open(pathin+"/"+lep+"/Data_"+lep+".root")
          tmp = (TH1F)(filedata.Get(hist))
          integral = tmp.Integral()
          error = tmp.Integral()**0.5
          if(tex):
               print "Data  & %-6i $\pm$  %-3i \\\\ " %(integral,error)
               print "\\end{tabular}"
               print "\\end{center}"
               print "\\end{table}"
               '''
     if(signif):
          print p
