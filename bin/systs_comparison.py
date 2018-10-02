import os, commands
import optparse
from ROOT import *

usage = 'python systs_comparison.py'
parser = optparse.OptionParser(usage)
parser.add_option('--pathin', dest='pathin', type='string', default='Plot/fit/', help='')
parser.add_option('--pathout', dest='pathout', type='string', default='syst/', help='')
#parser.add_option('-L', '--lep', dest='lep', type='string', default='muon', help='Default checks integrals of muon systematics')
(opt, args) = parser.parse_args()

histos = []
#histos.append("h_2j1t_topMass_mtw_G_50")
histos.append("h1D_2j1t_cr")
histos.append("h1D_2j1t_sr")
histos.append("h1D_3j1t_cr")
histos.append("h1D_3j1t_sr")
histos.append("h_3j2t_BDT_ST_vs_TT_3j2t")
#histos.append("h_3j2t_BDT_ST_vs_TT_3j2t_E")

pathin = opt.pathin
if opt.pathin != "Plot/fit/":
     pathin == opt.pathin

pathout = opt.pathout
if opt.pathout != "syst/":
     pathout == opt.pathout
infile = []

gStyle.SetPalette(1)
gStyle.SetOptStat(0)
gROOT.SetBatch()        # don't pop up canvases

leptons = [
"muon"
"electron"
]
samples = [
"ST_tch",
"ST_tch_sd",
"ST_tch_p_sd",
"ST_sch",
"ST_tW",
"TT","TT_sd",
"WJets","VV","DYJets","DDQCD"]
scale = False
rebin = False

systematics = {
     "ST_tch":["btag","mistag", "jes", "jer", "pu" , "lepMu","lepE", "pdf_total", "hdampST_tch", "q2ST_tch", "psq2ST_tch", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],# 
#     "ST_tch":["btag","mistag", "jes", "jer", "pu", "lep", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],# 
     "ST_tch_sd":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch_sd", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "ST_tch_p_sd":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "ST_sch":["btag", "mistag", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],# "jes",
     "ST_tW":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "TT":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "hdampTT", "q2TT", "psq2TT","psq2ST_tch", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "TT_sd":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "WJets":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2WJets", "q2ST_tch","psq2ST_tch","psq2TT", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "VV":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "q2VV", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "DYJets":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "q2DYJets", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "DDQCD":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"]
     }

for lep in leptons:
     for s in samples:
          if not os.path.exists(pathout+lep+"/"+s):
               os.system("mkdir -p "+pathout+lep+"/"+s)
          for syst in systematics.get(s):#dictionary
               infile.append(TFile.Open(pathin+s+"_"+lep+".root"))
               infile.append(TFile.Open(pathin+s+"_"+lep+"_"+syst+"Up.root"))
               infile.append(TFile.Open(pathin+s+"_"+lep+"_"+syst+"Down.root"))
               for hist in histos:
                    print pathout+lep+"/"+s+"/"+hist+"_"+syst
                    h1 = TH1F()
                    h2 = TH1F()
                    h3 = TH1F()
                    c1 = TCanvas(str(hist),"c1",50,50,700,600)
                    leg = TLegend(0.7,0.7,0.9,0.9)
                    for inf in infile:
                         inf.cd()
                         tmp = (TH1F)(inf.Get(hist))
                         filename = (str)(inf.GetName())
          #          print "filename" , filename
                         if("Up" in filename):
                              h1 = tmp.Clone("nominal") 
                              if rebin:
                                   h1.Rebin(4)
                              h1.SetTitle(str(hist))
#               h1.SetName(str(hist))
                         elif("Down" in filename):
                              h2 = tmp.Clone("nominal") 
                              if rebin:
                                   h2.Rebin(4)
                              h2.SetTitle("down")
                         else:
                              h3 = tmp.Clone("nominal")
               #               print "i0ntegral ", h3.Integral()
                              if scale:
                                   h3.Scale(1./norm.GetBinContent(0))
               #               h3.SetName("nominal")
                              if rebin:
                                   h3.Rebin(4)
                              h3.SetTitle("nominal")
                         tmp.Reset("ICES")
                    c1.cd()
                    maximum = max(h1.GetMaximum(),h2.GetMaximum(),h3.GetMaximum())
                    minimum = min(h1.GetMinimum(),h2.GetMinimum(),h3.GetMinimum())
                    h1.SetMaximum(maximum*1.5)
                    h1.SetMinimum(0.0)
                    h1.Draw("E")
                    h1.SetTitle("")
                    h1.GetYaxis().SetTitle("Events/bin")
                    h1.GetXaxis().SetTitle("")
                    print "int h1 up",h1.Integral()
                    h1.SetLineColor(kRed)
                    h2.Draw("ESAME")
                    h2.SetLineColor(kGreen)
                    print "int h2 down",h2.Integral()
                    h3.Draw("HIST SAME")
                    h3.SetLineColor(kBlue)
                    print "int h3 nominal",h3.Integral()
                    leg.AddEntry(h1, "up", "l")
                    leg.AddEntry(h3, "nominal", "l")
                    leg.AddEntry(h2, "down", "l")
                    leg.Draw("SAME")
                    c1.cd()
                    TGaxis.SetMaxDigits(3)
                    c1.RedrawAxis()
                    c1.Update()
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".pdf")
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".png")
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".root")
                    c1.Close()

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
histos.append("h_2j1t_topMass")
histos.append("h_2j1t_mtwcut_topMass")
histos.append("h_2j1t_mtwcut_sr_topMass")
histos.append("h_2j1t_etajprime")
histos.append("h_2j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5")
histos.append("h_2j1t_BDT_STsd_vs_All_sr_mtw_G_50_AND_etajprime_G_2p5")
#histos.append("h_2j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_G_2p4")
#histos.append("h_3j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_L_2p5")
#histos.append("h_3j1t_BDT_ST_vs_TT_mtweta_mtw_G_50_AND_etajprime_G_2p4")
histos.append("h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_mtw_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_mlb_mtw_G_50_AND_etajprime_L_2p5")
histos.append("h_2j1t_nextrajets_mtw_G_50_AND_etajprime_L_2p5")
'''
