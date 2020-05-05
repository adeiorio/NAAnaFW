#!/bin/env python
########################################
###  Author: Annapaola de Cosa             
###  Code to produce pre e post fit plots  
###  from combine output (mlfit.root)
########################################
#Comment and uncomment the different folder to produce the plots for muons, electrons, and/or their combination

import optparse
from plots.plotUtils import *
usage = 'python plotPrePostFit.py -o fitfolder' #fit folder is the folder containing the FitDiagnostic.root file

'''
bkgs_m2j1tcr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets", "TT"] #, "ST_tch_sd"
bkgs_m2j1tsr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets", "TT"] #, "ST_tch_sd"
bkgs_m3j1tcr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets", "TT"] #, "ST_tch_sd"
bkgs_m3j1tsr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets", "TT"] #, "ST_tch_sd"
bkgs_m3j2t   = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets", "TT"] #, "ST_tch_sd"
# ["TT", "DDQCD", "ST_tch", "ST_tch_sd", "WJets","VV","DYJets","ST_tW","ST_sch"]

'''
bkgs_m2j1tcr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets_ext", "TT", "ST_tch_sd"]#
#bkgs_m2j1tsr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets_ext", "TT", "ST_tch_sd"]#
#bkgs_m3j1tcr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets_ext", "TT", "ST_tch_sd"]#
bkgs_m3j1tsr = ["ST_tch", "VV", "ST_sch", "DYJets", "DDQCD", "ST_tW", "WJets_ext", "TT", "ST_tch_sd"]#
bkgs_m3j2t   = ["ST_tch", "VV", "ST_sch", "DYJets", "ST_tW", "WJets_ext", "TT", "ST_tch_sd"]#

'''
regions_mu = {
    "m2j1tcr":("h1D_2j1t_cr_3838","muon_2j1t_central"),
    "m2j1tsr":("h1D_2j1t_sr_3838","muon_2j1t_forward"),
    "m3j1tcr":("h1D_3j1t_cr_3838","muon_3j1t_central"),
    "m3j1tsr":("h1D_3j1t_sr_3838","muon_3j1t_forward"),
    "m3j2t":("h_3j2t_BDT_ST_vs_TT_3j2t", "muon_3j2t"),
    }

regions_ele = {
    "e2j1tcr":("h1D_2j1t_cr_3838","electron_2j1t_central"),
    "e2j1tsr":("h1D_2j1t_sr_3838","electron_2j1t_forward"),
    "e3j1tcr":("h1D_3j1t_cr_3838","electron_3j1t_central"),
    "e3j1tsr":("h1D_3j1t_sr_3838","electron_3j1t_forward"),
    "e3j2t":("h_3j2t_BDT_ST_vs_TT_3j2t_E", "electron_3j2t"),
}
'''
regions_mu = {
    "m2j1tcr":("h_2j1t_BDT_ST_vs_All_mtw_G_50", "ch1", "muon_2j1t_cr"),
#    "m2j1tsr":("h1D_2j1t_sr","muon_2j1t_forward"),
#    "m3j1tcr":("h1D_3j1t_cr","muon_3j1t_central"),
    "m3j1tsr":("h_3j1t_BDT_STsd_vs_All_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5", "ch2", "muon_3j1t_sr"),
    "m3j2t":("h_3j2t_BDT_ST_vs_TT_3j2t", "ch3",  "muon_3j2t"),
    }
regions_ele = {
    "e2j1tcr":("h_2j1t_BDT_ST_vs_All_mtw_G_50", "ch4", "electron_2j1t_cr"),
#    "m2j1tsr":("h1D_2j1t_sr","muon_2j1t_forward"),
#    "m3j1tcr":("h1D_3j1t_cr","muon_3j1t_central"),
    "e3j1tsr":("h_3j1t_BDT_STsd_vs_All_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5", "ch5", "electron_3j1t_sr"),
    "e3j2t":("h_3j2t_BDT_ST_vs_TT_3j2t", "ch6", "electron_3j2t"),
    }

'''
regions_ele = {
    "e2j1tcr":("h1D_2j1t_cr","electron_2j1t_central"),
    "e2j1tsr":("h1D_2j1t_sr","electron_2j1t_forward"),
    "e3j1tcr":("h1D_3j1t_cr","electron_3j1t_central"),
    "e3j1tsr":("h1D_3j1t_sr","electron_3j1t_forward"),
    "e3j2t":("h_3j2t_BDT_ST_vs_TT_3j2t", "electron_3j2t"),
    }

regions_mu = {
    "m2j1tcr":("h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","muon_2j1t_central"),
    "m2j1tsr":("h_2j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","muon_2j1t_forward"),
    "m3j1tcr":("h_3j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","muon_3j1t_central"),
    "m3j1tsr":("h_3j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","muon_3j1t_forward"),
    "m3j2t":("h_3j2t_topMassLeading", "muon_3j2t"),
    }

regions_ele = {
    "e2j1tcr":("h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","electron_2j1t_central"),
    "e2j1tsr":("h_2j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","electron_2j1t_forward"),
    "e3j1tcr":("h_3j1t_topMass_mtw_G_50_AND_etajprime_L_2p5","electron_3j1t_central"),
    "e3j1tsr":("h_3j1t_topMass_mtw_G_50_AND_etajprime_G_2p5","electron_3j1t_forward"),
    "e3j2t":("h_3j2t_topMassLeading", "electron_3j2t"),
}
'''
lep = ""
#fitPhase = "prefit"
fitPhase = "fit_s"
#folder = "fit_17_01/ST_tch_mc_cb_na_fix/na/"
folder = "fit_18_07_19/ST_tch_mc_cb_na_fix/na/"
#lep = "muon"
if lep == "muon":    
    plot(folder, fitPhase, regions_mu["m2j1tcr"], bkgs_m2j1tcr)
#    plot(folder, fitPhase, regions_mu["m2j1tsr"], bkgs_m2j1tsr)
#    plot(folder, fitPhase, regions_mu["m3j1tcr"], bkgs_m3j1tcr)
    plot(folder, fitPhase, regions_mu["m3j1tsr"], bkgs_m3j1tsr)
    plot(folder, fitPhase, regions_mu["m3j2t"], bkgs_m3j2t)
#lep = "electron"
if lep == "electron":
    plot(folder, fitPhase, regions_ele["e2j1tcr"], bkgs_m2j1tcr)
#    plot(folder, fitPhase, regions_ele["e2j1tsr"], bkgs_m2j1tsr)
#    plot(folder, fitPhase, regions_ele["e3j1tcr"], bkgs_m3j1tcr)
    plot(folder, fitPhase, regions_ele["e3j1tsr"], bkgs_m3j1tsr)
    plot(folder, fitPhase, regions_ele["e3j2t"], bkgs_m3j2t)

lep = "muele"
if lep == "muele":    
    plot(folder, fitPhase, regions_mu["m2j1tcr"], bkgs_m2j1tcr)
#    plot(folder, fitPhase, regions_mu["m2j1tsr"], bkgs_m2j1tsr)
#    plot(folder, fitPhase, regions_mu["m3j1tcr"], bkgs_m3j1tcr)
    plot(folder, fitPhase, regions_mu["m3j1tsr"], bkgs_m3j1tsr)
    plot(folder, fitPhase, regions_mu["m3j2t"], bkgs_m3j2t)
    plot(folder, fitPhase, regions_ele["e2j1tcr"], bkgs_m2j1tcr)
#    plot(folder, fitPhase, regions_ele["e2j1tsr"], bkgs_m2j1tsr)
#    plot(folder, fitPhase, regions_ele["e3j1tcr"], bkgs_m3j1tcr)
    plot(folder, fitPhase, regions_ele["e3j1tsr"], bkgs_m3j1tsr)
    plot(folder, fitPhase, regions_ele["e3j2t"], bkgs_m3j2t)



