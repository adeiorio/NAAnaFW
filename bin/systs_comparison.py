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
histos.append("h_2j1t_etajprime_mtw_G_50")
histos.append("h_3j1t_etajprime_mtw_G_50_AND_etajprime_G_2p5")
histos.append("h_2j1t_etajprime_mtw_G_50")
#histos.append("h_2j1t_mlb_mtw_G_50")
#histos.append("h_2j1t_mljprime_mtw_G_50")
#histos.append("h_2j1t_costhetael_mtw_G_50")
#histos.append("h_2j1t_costhetapol_mtw_G_50")
#histos.append("h_2j1t_topMass_mtw_G_50")
#histos.append("h_2j1t_BDT_ST_vs_All_mtw_G_50")
#histos.append("h_3j1t_BDT_STsd_vs_All_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5")
#histos.append("h_3j2t_BDT_ST_vs_TT_3j2t")


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
#,"electron"
]

samples = [
"ST_tch"]
''',
"ST_tch_sd",
"ST_tch_p_sd",
"ST_sch",
"ST_tW",
"TT",#"TT_sd",
"WJets_ext","VV","DYJets","DDQCD"]
'''
scale = False
rebin = False
normalize = False # True

systematics = {
     "ST_tch":["pdf_totalSIG, pdf_totalBKG"],
#     "ST_tch":["jes", "jer", "pu" , "lep", "pdf_total", "hdamp", "q2", "psq2", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
#     "":["btag","mistag", "jes", "jer", "pu", "lep", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],# 
     "ST_tch_sd":["jes", "jer", "pu", "lep", "q2", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "ST_tch_p_sd":["jes", "jer", "pu", "lep", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "ST_sch":["jer", "pu", "lep", "q2", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],# "jes",
     "ST_tW":["jes", "jer", "pu", "lep", "q2", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "TT":["jes", "jer", "pu", "lep", "pdf_total", "hdamp", "q2", "psq2", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
#     "TT_sd":["jes", "jer", "pu", "lep", "q2", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "WJets_ext":["jes", "jer", "pu", "lep", "pdf_total", "q2", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "VV":["jes", "jer", "pu", "lep", "pdf_total", "q2", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "DYJets":["jes", "jer", "pu", "lep", "pdf_total", "q2", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "DDQCD":["jes", "jer", "pu", "lep", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"]
     }

'''
systematics = {
     "ST_tch":["jes", "jer", "pu" , "lepMu","lepE", "pdf_total", "hdampST_tch", "q2ST_tch", "psq2ST_tch", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],# 
#     "ST_tch":["btag","mistag", "jes", "jer", "pu", "lep", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],# 
     "ST_tch_sd":["jes", "jer", "pu", "lepMu","lepE", "q2ST_tch_sd", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "ST_tch_p_sd":["jes", "jer", "pu", "lepMu","lepE", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "ST_sch":["jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],# "jes",
     "ST_tW":["jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "TT":["jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "hdampTT", "q2TT", "psq2TT","psq2ST_tch", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
#     "TT_sd":["jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "WJets_ext":["jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2WJets_ext", "q2ST_tch","psq2ST_tch","psq2TT", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "VV":["jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "q2VV", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "DYJets":["jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "q2DYJets", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"],
     "DDQCD":["jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvacferr2", "cmvahf", "cmvahfstats1", "cmvahfstats2", "cmvalf", "cmvalfstats1", "cmvalfstats2", "cmvajes"]
     }

systematics = {
     "ST_tch":["jes"],# 
#     "ST_tch":["btag","mistag", "jes", "jer", "pu", "lep", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],# 
     "ST_tch_sd":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch_sd", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "ST_tch_p_sd":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "ST_sch":["jes"],# ["btag", "mistag", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],# "jes",
     "ST_tW":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "TT":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "hdampTT", "q2TT", "psq2TT","psq2ST_tch", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
#     "TT_sd":["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "WJets_ext":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2WJets_ext", "q2ST_tch","psq2ST_tch","psq2TT", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "VV":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "q2VV", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "DYJets":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "pdf_total", "q2ST_tch", "q2DYJets", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"],
     "DDQCD":["jes"],# ["btag", "mistag", "jes", "jer", "pu", "lepMu","lepE", "q2ST_tch", "pdf_total", "cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"]
     }
'''
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
                    h1.SetLineColor(kRed)
                    h1.GetXaxis().SetTitle("")
                    if(normalize):
                         h1.GetYaxis().SetTitle("Fraction of Events/bin")
                         h1.DrawNormalized("E")
                    else:
                         h1.GetYaxis().SetTitle("Events/bin")
                         h1.Draw("E")
                    h1.SetTitle("")
                    print "int h1 up",h1.Integral()
                    h2.SetLineColor(kGreen)
                    if(normalize):
                         h2.DrawNormalized("ESAME")
                    else:
                         h2.Draw("ESAME")
                    print "int h2 down",h2.Integral()
                    h3.SetLineColor(kBlue)
                    if(normalize):
                         h3.DrawNormalized("ESAME")
                    else:
                         h3.Draw("HIST SAME")
                    print "int h3 nominal",h3.Integral()
                    leg.AddEntry(h1, "up", "l")
                    leg.AddEntry(h3, "nominal", "l")
                    leg.AddEntry(h2, "down", "l")
                    leg.Draw("SAME")
                    c1.cd()
                    TGaxis.SetMaxDigits(3)
                    c1.RedrawAxis()
                    c1.Update()
#                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".pdf")
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".png")
#                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".root")
                    c1.Close()
'''
for lep in leptons:
     for s in samples:
          if not os.path.exists(pathout+"/"+lep+"/"+s):
               os.system("mkdir -p "+pathout+"/"+lep+"/"+s)
          for syst in systematics.get(s):#dictionary
               infile.append(TFile.Open(pathin+s+"_"+lep+".root"))
               infile.append(TFile.Open(pathin+s+"_"+lep+"_"+syst+"Up.root"))
               infile.append(TFile.Open(pathin+s+"_"+lep+"_"+syst+"Down.root"))
               for hist in histos:
                    print pathout+lep+"/"+s+"/"+hist+"_"+syst
                    h1 = TH1F()
                    h2 = TH1F()
                    h3 = TH1F()
                    h1_ratio = TH1F()
                    h2_ratio = TH1F()
                    h3_ratio = TH1F()
                    c1 = TCanvas(str(s+"_"+hist),"c1",50,50,700,600)
                    leg = TLegend(0.7,0.7,0.9,0.9)
                    c1.SetFillColor(0)
                    c1.SetBorderMode(0)
                    c1.SetFrameFillStyle(0)
                    c1.SetFrameBorderMode(0)
                    c1.SetLeftMargin( 0.12 )
                    c1.SetRightMargin( 0.9 )
                    c1.SetTopMargin( 1 )
                    c1.SetBottomMargin(-1)
                    c1.SetTickx(1)
                    c1.SetTicky(1)
                    c1.cd()
                    pad1 = TPad("pad1", "pad1", 0, 0.31 , 1, 1)
                    pad1.SetTopMargin(0.1)
                    pad1.SetBottomMargin(0)
                    pad1.SetLeftMargin(0.12)
                    pad1.SetRightMargin(0.05)
                    pad1.SetBorderMode(0)
                    pad1.SetTickx(1)
                    pad1.SetTicky(1)
                    pad1.Draw()
                    pad1.cd()
                    
                    leg.SetX1(.46)
                    leg.SetY1(.56)
                    leg.SetX2(.95)
                    leg.SetY2(.88)                
                    for inf in infile:
                         inf.cd()
                         tmp = (TH1F)(inf.Get(hist))
                         filename = (str)(inf.GetName())
          #          print "filename" , filename
                         if("Up" in filename):
                              h1 = tmp.Clone("nominal")
                              if rebin:
                                   h1.Rebin(4)
                              h1.SetTitle(str(s+"_"+hist+"_"+syst))
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
                    h1.SetMaximum(maximum*1.75)
                    h1.SetMinimum(0.0)
                    pad1.cd()
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
                    pad2 = TPad("pad2", "pad2", 0, 0.01 , 1, 0.30)
                    pad2.SetTopMargin(0.05)
                    pad2.SetBottomMargin(0.45)
                    pad2.SetLeftMargin(0.12)
                    pad2.SetRightMargin(0.05)
                    gStyle.SetHatchesSpacing(2)
                    gStyle.SetHatchesLineWidth(2)
                    c1.cd()
                    pad2.Draw()
                    pad2.cd()
                    h1.SetStats(0)
                    h1_ratio = h1.Clone("")
                    h2_ratio = h2.Clone("")
                    h3_ratio = h3.Clone("")
                    h1_ratio.Add(h3_ratio,-1)
                    h1_ratio.Divide((h3_ratio))
                    h2_ratio.SetLineColor(kGreen)
                    h1_ratio.SetMarkerStyle(20)
                    h2_ratio.SetMarkerStyle(24)
                    h1_ratio.SetMarkerSize(1)
                    h2_ratio.SetMarkerSize(1)
                    h1_ratio.SetFillStyle(3003)
                    h1_ratio.GetYaxis().SetNdivisions(505)
                    h1_ratio.GetYaxis().SetTitle("#frac{shifted-nom}{nom}")
                    h1_ratio.GetYaxis().SetTitleOffset(0.4)
                    h1_ratio.GetYaxis().SetTitleSize(0.1)
                    h1_ratio.GetYaxis().SetLabelSize(0.08)
                    h1_ratio.GetXaxis().SetLabelSize(0.1)
                    h1_ratio.GetXaxis().SetTitleOffset(0.9)
                    h1_ratio.GetXaxis().SetTitleSize(0.15)
                    #if(strcmp(var,"met")==0) h1_ratio.GetXaxis().SetTitle("MET p_{T} [GeV]");
                    #if(strcmp(var,"MT")==0) h1_ratio.GetXaxis().SetTitle("M_{T} [GeV]");
                    h1_ratio.SetTitle("")
                    h1_ratio.Draw("ex0")

                    h2_ratio.SetStats(0)
                    h2_ratio.Add(h3_ratio,-1)
                    h2_ratio.Divide((h3_ratio))
                    h1_ratio.SetLineColor(kRed)
                    h2_ratio.SetFillStyle(3003)
                    h2_ratio.Draw("ex0 same")
                    
                    h1_ratio.SetMaximum(0.6)
                    h1_ratio.SetMinimum(-0.6)
                    f1 = TLine(h1_ratio.GetXaxis().GetXmin(), 0., h1_ratio.GetXaxis().GetXmax(),0.)
                    f1.SetLineColor(kBlack)
                    f1.SetLineStyle(kDashed)
                    f1.Draw("same")

                    TGaxis.SetMaxDigits(3)
                    c1.RedrawAxis()
                    c1.Update()
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".pdf")
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".png")
                    c1.Print(pathout+lep+"/"+s+"/"+hist+"_"+syst+".root")
                    c1.Close()
'''
