import os, commands
import optparse
from ROOT import *

usage = 'python checksyst.py'
parser = optparse.OptionParser(usage)
parser.add_option('--pathin', dest='pathin', type='string', default='res', help='')
parser.add_option('--pathout', dest='pathout', type='string', default='sd', help='')
parser.add_option('-L', '--lep', dest='lep', type='string', default='muon', help='Default checks integrals of muon systematics')
parser.add_option('--norm', dest='norm', default = False, action='store_true', help='')
(opt, args) = parser.parse_args()

filenames = []
#filenames.append("ST_tch_p_sd_reshaped")
#filenames.append("ST_tch_sd_reshaped")
#filenames.append("ST_T_tch_sd_reshaped_improv")
#filenames.append("ST_tch_p_sd")
#filenames.append("ST_T_tch_sd")
filenames.append("TT")
filenames.append("ST_tch")
filenames.append("ST_sch")
filenames.append("ST_tW")
filenames.append("DYJets")
filenames.append("WJets")
#filenames.append("")

histos = []
'''
histos.append("h_nJets")
#histos.append("h_nJets_cr")
#histos.append("h_nJets_sr")
histos.append("h_nJets_0b")
#histos.append("h_nJets_0b_cr")
#histos.append("h_nJets_0b_sr")
histos.append("h_nJets_1b")
#histos.append("h_nJets_1b_cr")
#histos.append("h_nJets_1b_sr")
histos.append("h_nJets_2b")
#histos.append("h_nJets_2b_cr")
#histos.append("h_nJets_2b_sr")
histos.append("h_nbJets")
#histos.append("h_nbJets_cr")
#histos.append("h_nbJets_sr")
#2j1t
histos.append("h_2j1t_mtw")
#histos.append("h_2j1t_MET")
histos.append("h_2j1t_etajprime")
histos.append("h_2j1t_topMass")
histos.append("h_2j1t_bjetpt")
#histos.append("h_2j1t_costhetael")
#histos.append("h_2j1t_costhetapol")
#histos.append("h_2j1t_mlb")
#histos.append("h_2j1t_mljprime")
#histos.append("h_2j1t_topMassExtra")
#histos.append("h_2j1t_topPtExtra")
#histos.append("h_2j1t_costhetaelExtra")
#histos.append("h_2j1t_costhetapolExtra")
#histos.append("h_2j1t_nextrajets")

#3j1t
histos.append("h_3j1t_mtw")
histos.append("h_3j1t_mtwcut_topMass")
histos.append("h_3j1t_mtwcut_sr_topMass")
histos.append("h_3j1t_bjetpt")
#histos.append("h_3j1t_MET")
#histos.append("h_3j1t_etajprime")
#histos.append("h_3j1t_topMass")
#histos.append("h_3j1t_costhetael")
#histos.append("h_3j1t_costhetapol")
#histos.append("h_3j1t_mlb")
#histos.append("h_3j1t_mljprime")
#histos.append("h_3j1t_topMassExtra")
#histos.append("h_3j1t_topPtExtra")
#histos.append("h_3j1t_costhetaelExtra")
#histos.append("h_3j1t_costhetapolExtra")
#histos.append("h_3j1t_nextrajets")

#3j2t
histos.append("h_3j2t_etajprime")
histos.append("h_3j2t_bjetpt")
histos.append("h_3j2t_bjeteta")
histos.append("h_3j2t_ljetpt")
histos.append("h_3j2t_ljeteta")
histos.append("h_3j2t_mtw")
histos.append("h_3j2t_met")
histos.append("h_3j2t_nextrajets")
histos.append("h_2j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5")
histos.append("h_2j1t_BDT_STsd_vs_All_sr_mtw_G_50_AND_etajprime_G_2p5")
#histos.append("h_2j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_G_2p4")
#histos.append("h_3j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_L_2p5")
#histos.append("h_3j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_G_2p4")
histos.append("h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_mlb_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_nextrajets_mtw_G_50_AND_etajprime_L_2p5")
'''

histos.append("h_2j1t_mtw_mtw_G_50_AND_etajprime_L_2p5")
#histos.append("h_2j1t_mtw_mtw_G_50_AND_etajprime_G_2p5")

pathin = opt.pathin
if opt.pathin != "res":
     pathin == opt.pathin

pathout = opt.pathout
if opt.pathout != "sd":
     pathout == opt.pathout

leptons=[]
if opt.lep != "muon":
     for lep in (opt.lep).split(","):
          leptons.append(lep)
else:
     leptons.append("muon")

infile = []
gStyle.SetPalette(1)
gStyle.SetOptStat(0)
gROOT.SetBatch()        # don't pop up canvases

scale = opt.norm
rebin = False #True

for lep in leptons:
     for fil in filenames:
#          infile.append(TFile.Open(pathin+"/"+lep+"/"+fil+"_"+lep+".root"))
#          print pathin+"/"+lep+"/"+fil+"_"+lep+".root"
          infile.append(TFile.Open("Plot/fit/"+fil+"_"+lep+".root"))
          infile.append(TFile.Open("Plot/"+lep+"/"+fil+"_"+lep+".root"))
     for hist in histos:
          h1 = TH1F()
          h2 = TH1F()
          c1 = TCanvas(str(hist),"c1",50,50,700,600)
          leg = TLegend(0.7,0.7,0.9,0.9)
          for inf in infile:
               inf.cd()
               tmp = (TH1F)(inf.Get(hist))
#               norm = (TH1F)(inf.Get("h_cutFlow"))
#               if scale:
#                    print "norm",norm.GetBinContent(0)
               filename = (str)(inf.GetName())
     #          print "filename" , filename
               if("reshaped" in filename):
                    h1 = tmp.Clone() 
#                    h1.Scale(1./norm.GetBinContent(0))
                    if scale:
                         h1.Scale(1./h1.Integral())
                    if rebin:
                         h1.Rebin(4)
                    h1.SetTitle(str(hist+"_"+lep))
#               h1.SetName(str(hist))
               else:
                    h2 = tmp.Clone()
#                    h2.Scale(1./norm.GetBinContent(0))
                    if scale:
                         h2.Scale(1./h2.Integral())
                    if rebin:
                         h2.Rebin(4)
#                    h2.SetTitle("nominal")
               tmp.Reset("ICES")
          c1.cd()
          maximum = max(h1.GetMaximum(),h2.GetMaximum())
          minimum = min(h1.GetMinimum(),h2.GetMinimum())
          h1.SetMaximum(maximum*1.5)
          h1.SetMinimum(0.0)
          h1.Draw("E")
          print "integral reshaped",h1.Integral()
          h1.SetLineColor(kRed)
          h2.Draw("ESAME")
          h2.SetLineColor(kGreen)
          print "integral true",h2.Integral()
          leg.AddEntry(h1, "reshaped", "l")
          leg.AddEntry(h2, "true", "l")
          #     gPad.BuildLegend()
          #     c1.SetTitle(str(hist))
          leg.Draw("SAME")
          c1.Update()
          c1.Print(pathout+"/"+lep+"/"+hist+".pdf")
          c1.Print(pathout+"/"+lep+"/"+hist+".png")
          c1.Print(pathout+"/"+lep+"/"+hist+".root")
          c1.Close()
