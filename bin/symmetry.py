import ROOT 

def symmetry(s, lep, syst, hists):
    pathin = "Plot/fit/"
    filenom = ROOT.TFile.Open(pathin+s+"_"+lep+".root")
    hnom = ROOT.TH1F()
    fileup = ROOT.TFile.Open(pathin+s+"_"+lep+"_"+syst+"Up.root", "UPDATE")
    hup = ROOT.TH1F()
    filedown = ROOT.TFile.Open(pathin+s+"_"+lep+"_"+syst+"Down.root", "UPDATE")
    hdown = ROOT.TH1F()
    for h in hists:
        filedown.cd()
        hdown = (ROOT.TH1F)(filedown.Get(h))
        filenom.cd()
        hnom = (ROOT.TH1F)(filenom.Get(h))
        fileup.cd()
        hup = (ROOT.TH1F)(fileup.Get(h))
        hup.Scale((hnom.Integral()+(hup.Integral()-hdown.Integral())/2)/hup.Integral())
        hdown.Scale((hnom.Integral()-(hup.Integral()-hdown.Integral())/2)/hdown.Integral())
        print s, " ", lep, " " , syst,
        print hdown.GetName(), " ", hdown.Integral()
        print hup.GetName(), " ", hup.Integral()
        fileup.cd()
        hup.Write()
        filedown.cd()
        hdown.Write()
    filenom.Close()
    fileup.Close()
    filedown.Close()


histos = []
histos.append("h_2j1t_BDT_ST_vs_All_mtw_G_50")
histos.append("h_3j1t_BDT_STsd_vs_All_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5")
histos.append("h_3j2t_BDT_ST_vs_TT_3j2t")
histos.append("h_2j1t_BDT_ST_vs_All_2_mtw_G_50")
histos.append("h_3j1t_BDT_STsd_vs_All_sr_3j1t_2_mtw_G_50_AND_etajprime_G_2p5")
histos.append("h_3j2t_BDT_ST_vs_TT_3j2t_2")

symmetry("ST_tch", "muon", "psq2ST_tch", histos)
symmetry("TT", "muon", "psq2TT", histos)
symmetry("TT", "muon", "hdampTT", histos)
symmetry("ST_tch", "electron", "psq2ST_tch", histos)
symmetry("TT", "electron", "hdampTT", histos)
symmetry("TT", "electron", "psq2TT", histos)
