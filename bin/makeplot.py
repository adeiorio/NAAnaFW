import os, commands
import optparse
from ROOT import * 
from variabile import variabile 
from Analysis.NAAnaFW.MakePlot.samples.VJets import *
from Analysis.NAAnaFW.MakePlot.samples.SingleTop import *
from Analysis.NAAnaFW.MakePlot.samples.TT import *
from Analysis.NAAnaFW.MakePlot.samples.VV import *
from Analysis.NAAnaFW.MakePlot.tdrstyle import *
from Analysis.NAAnaFW.MakePlot.samples.toPlot import samples as samplesDictionary
from Analysis.NAAnaFW.MakePlot.CMS_lumi import CMS_lumi

#definizioni funzioni 
def makelumi(macro, channel, lumi, sigma, lep):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\","+str(lumi)+","+str(sigma)+",\""+str(lep)+"\")\'")

def mergetree(sample, lep):
    if len(sample.components)!=1:
        add = "hadd -f trees_lumi/"+str(lep).strip('[]')+"/trees_"+sample.label+"_"+str(lep).strip('[]')+".root"
        for comp in sample.components:
            add+= " trees_lumi/"+str(lep).strip('[]')+"/trees_"+comp.label+"_"+str(lep).strip('[]')+".root"
        print add
        os.system(str(add))
    else:
         if not os.path.exists("trees_lumi/"+str(lep).strip('[]')+"/trees_"+sample.label+"_"+str(lep).strip('[]')+".root"):
              comp=sample.components
              os.system("cp trees_lumi/"+str(lep).strip('[]')+"/trees_"+comp[0].label+"_"+str(lep).strip('[]')+".root trees_lumi/"+str(lep).strip('[]')+"/trees_"+sample.label+"_"+str(lep).strip('[]')+".root")

def makeplot(macro, channel, variable, njmt, syst, cut_tag, lep):
    os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\","+str(variable)+",\""+str(njmt)+"\",\""+str(syst)+"\",\""+str(cut_tag)+"\",\""+str(lep)+"\")\'")

def cutToTag(cut):
    newstring = cut.replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

def makeTree(macro, channel):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\")\'")

def makeBDT(macro, channel, njmt, training_name, syst, lep):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\",\""+str(njmt)+"\",\""+str(training_name)+"\", \""+str(syst)+"\",\""+str(lep)+"\")\'")

def makehisto2D(macro, channel, njmt, syst, region, BDT1, BDT2, lep):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\",\""+str(njmt)+"\",\""+str(syst)+"\",\""+str(region)+"\",\""+str(BDT1)+"\",\""+str(BDT2)+"\",\""+str(lep)+"\")\'")

def makehisto1D(macro, channel, njmt, syst, region,  cut1x, cut2x, cut1y, cut2y, lep):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\",\""+str(njmt)+"\",\""+str(syst)+"\",\""+str(region)+"\","+str(cut1x)+","+str(cut2x)+","+str(cut1y)+","+str(cut2y)+",\""+str(lep)+"\")\'")

def rmfile(pathfile):
    os.system("rm "+str(pathfile))

def rmdir(pathdir):
    os.system("rm -rf"+str(pathdir))

def DDQCD(inpath_, outpath_, histoname, syst_, samples_, cut_tag_, code_tag_, region,  lep_):
    ROOT.TH1.SetDefaultSumw2()
#    index = samples_.index(samplesDictionary["TT_sd"])
#    samples_[index:index+1]=[]
    histo = []
    tmp = ROOT.TH1F()
    h = ROOT.TH1F()
    hsig =  TH1F()
    if cut_tag_!="":
        histoname += "_"+cut_tag_
    if code_tag!="":
#        histoname += "_"+code_tag_
         print histoname
    infileanti_nom = []
    infileanti = []
    infileiso = []
    for s in samples_:
         if not s.leglabel=="QCD":
              infileanti_nom.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
              if(syst_==""):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              elif((s.leglabel=="tW") and (syst=="pdf_totalUp" or syst=="pdf_totalDown")):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              elif((s.leglabel=="t, t-ch" or s.leglabel=="t, t-ch_sd") and (syst=="pdf_totalUp" or syst=="pdf_totalDown" or syst=="q2Up" or syst=="q2Down" or syst=="jerUp" or syst=="jerDown")):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              else:
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso_"+syst_+".root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))

    #Adding data file
    fdataanti = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/Data_"+str(lep_).strip('[]')+"antiiso.root")
    print inpath_+"/"+str(lep_).strip('[]')+"antiiso/Data_"+str(lep_).strip('[]')+"antiiso.root"
    hdataanti = (TH1F)(fdataanti.Get(histoname))
#    hdataanti.Sumw2()
    print "Integral Data anti iso:", hdataanti.Integral()
    fdataiso = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/Data_"+str(lep_).strip('[]')+".root")
    hdataiso = (TH1F)(fdataiso.Get(histoname))
#    hdataiso.Sumw2()
    print "Integral Data iso:", hdataiso.Integral()
    #subtraction in anti-isolated region for the nominal
    hdataanti_nom = hdataanti.Clone()
    sumMCanti_nom = hdataanti.Clone()
    sumMCanti_nom.Reset("ICES")
    for inf in infileanti_nom: 
        inf.cd()
        print "opening file: ", inf.GetName()
        tmp = (TH1F)(inf.Get(histoname))
        tmp.SetOption("HIST SAME")
        sumMCanti_nom.Add(tmp)
        tmp.Reset("ICES")
    hdataanti_nom.Add(sumMCanti_nom, -1)
    #subtraction in anti-isolated region
    sumMCanti = hdataanti.Clone()
    sumMCanti.Reset("ICES")
    for inf in infileanti: 
        inf.cd()
#        print "opening file: ", inf.GetName()
        tmp = (TH1F)(inf.Get(histoname))
        tmp.SetOption("HIST SAME")
        sumMCanti.Add(tmp)
        print "sum non-QCD anti-iso: ", sumMCanti.Integral()
        tmp.Reset("ICES")
    hdataanti.Add(sumMCanti, -1)
    for inf in infileiso:
        inf.cd()
        print "opening file: ", inf.GetName()
        tmp = (TH1F)(inf.Get(histoname))
        tmp.SetOption("HIST SAME")
        hdataiso.Add(tmp, -1)
        print "Integral Dati-MC iso: ", hdataiso.Integral()
        tmp.Reset("ICES")
    if hdataiso.Integral()<0: norm=1.
    else: norm = hdataiso.Integral()
    syst_SF = hdataanti.Integral()/hdataanti_nom.Integral()
    print "syst/nominal SF ", syst_SF
    if lep_ == "electron":
         if("2j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_L_2p5" or region == "cr")):
              hdataanti.Scale(1.46*syst_SF*norm/hdataanti.Integral())
         elif("2j1t" in histoname and cut_tag =="mtw_G_50"):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("2j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_G_2p5" or region == "sr")):
              hdataanti.Scale(1.10*syst_SF*norm/hdataanti.Integral())
         elif("3j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_L_2p5" or region == "cr")):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("3j1t" in histoname and cut_tag =="mtw_G_50"):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("3j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_G_2p5" or region == "sr")):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("3j2t" in histoname):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         else:
              hdataanti.Scale(1.*syst_SF*norm/hdataanti.Integral())
    else:
         if("2j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_L_2p5" or region == "cr")):
              hdataanti.Scale(0.83*syst_SF*norm/hdataanti.Integral())
         elif("2j1t" in histoname and cut_tag =="mtw_G_50"):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("2j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_G_2p5" or region == "sr")):
              hdataanti.Scale(1.09*syst_SF*norm/hdataanti.Integral())
         elif("3j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_L_2p5" or region == "cr")):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("3j1t" in histoname and cut_tag =="mtw_G_50"):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("3j1t" in histoname and (cut_tag =="mtw_G_50_AND_etajprime_G_2p5" or region == "cr")):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         elif("3j2t" in histoname):
              hdataanti.Scale(syst_SF*norm/hdataanti.Integral())
         else:
              hdataanti.Scale(1.*syst_SF*norm/hdataanti.Integral())
    print "l'integrale di DDQCD: ", hdataanti.Integral()
    fout = TFile.Open(outfile, "UPDATE")
    hdataanti.Write()
    fdataanti.Close()
    fdataiso.Close()
    i=0

    for s in samples_:
         if not s.leglabel=="QCD":
              infileanti[i].Close()
              infileiso[i].Close()
              i+=1
#    samples_[index:index]=[samplesDictionary["TT_sd"]]

def systerr(err_up, err_down, h_nom, histoname, sample, lep_):
    allsysts = {
         "ST_tch":["btag", "mistag", "jes", "jer", "pu" , "lep", "pdf_total", "hdamp", "q2", "psq2"],
         "ST_tch_sd":["btag", "mistag", "jes", "pu", "lep", "pdf_total", "q2"],# "jer",       
         "ST_tch_p_sd":["btag", "mistag", "jes", "pu", "lep", "pdf_total"],# "jer",
         "ST_sch":["btag", "mistag", "jes", "jer", "pu", "lep", "pdf_total"],
         "ST_tW":["btag", "mistag", "jes", "jer", "pu", "lep", "pdf_total"],
         "TT":["btag", "mistag", "jes", "jer", "pu", "lep", "pdf_total", "hdamp", "q2", "psq2"],
#         "TT_sd":["btag", "mistag", "jes", "pu", "lep", "pdf_total", "q2"],# "jer",
         "WJets":["btag", "mistag", "jes", "jer", "pu", "lep", "pdf_total", "q2"],
         "VV":["btag", "mistag", "jes", "jer", "pu", "lep", "pdf_total", "q2"],
         "DYJets":["btag", "mistag", "jes", "jer", "pu", "lep", "pdf_total", "q2"],
         "DDQCD":["qcdUnc"]
         }
    for syst in allsysts[sample.label]:
         infileUp = TFile.Open("Plot/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+"_"+syst+"Up.root")
         temp = infileUp.Get(histoname)
         for n in range(1,tmp.GetNBins()):
              var_up = tmp.GetBinContent(n)-h_nom.GetBinContent(n)
              if (var_up > 0):
                   err_up[n].append(abs(var_up))
              else:
                   err_down[n].append(abs(var_up))
         temp.Reset("ICES")
         infileUp.Close()
         infileDown = TFile.Open("Plot/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+"_"+syst+"Down.root")
         temp = infileDown.Get(histoname)
         for n in range(1,tmp.GetNBins()):
              var_down = tmp.GetBinContent(n)-h_nom.GetBinContent(n)
              if (var_down < 0):
                   err_down[n].append(abs(var_down))
              else:
                   err_up[n].append(abs(var_down))
    return err_up, err_down

def getSumError(_list):
     return math.sqrt(reduce(lambda x, y: x + y, list(map(lambda x: x**2, _list))))

def getSumSquared(_list):
     return reduce(lambda x, y: x + y, list(map(lambda x: x**2, _list)))

def getSum(_list):
     return reduce(lambda x, y: x + y, _list)

def makestack(njmt_, variabile_, syst_, samples_, cut_tag_, lep_):
 #   samples_[samples_.index(samplesDictionary["QCDMu"]):samples_.index(samplesDictionary["QCDMu"])+1]=[samplesDictionary["DDQCD"]]
    histo = []
    tmp = ROOT.TH1F()
    h = ROOT.TH1F()
    h_err = ROOT.TH1F()
    h_bkg_err = ROOT.TH1F()
    err_up = []
    err_down =  []
#    hsig =  TH1F("","",variabile_._nbins,variabile_._xmin,variabile_._xmax)
#    hsig = TH1F()
#    hratio = TH1F("","",variabile_._nbins,variabile_._xmin,variabile_._xmax)
    print "Variabile:", variabile_._name
    ROOT.gROOT.Reset()
    ROOT.gROOT.SetStyle('Plain')
    ROOT.gStyle.SetPalette(1)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gROOT.SetBatch()        # don't pop up canvases
    ROOT.TH1.SetDefaultSumw2()
#    ROOT.TH1.AddDirectory(False)
    ROOT.TGaxis.SetMaxDigits(3)
#    gROOT.ForceStyle()
    setTDRStyle()

    if cut_tag_=="":
        histoname = "h_"+njmt_+"_"+variabile_._name
        stackname = "Stack_"+njmt_+"_"+variabile_._name
        canvasname = "Stack_"+njmt_+"_"+variabile_._name+"_"+lep_
    else:
        histoname = "h_"+njmt_+"_"+variabile_._name+"_"+cut_tag_
        stackname = "Stack_"+njmt_+"_"+variabile_._name+"_"+cut_tag_
        canvasname = "Stack_"+njmt_+"_"+variabile_._name+"_"+cut_tag_+"_"+lep_
    stack = ROOT.THStack(stackname, variabile_._name)
    leg_stack = ROOT.TLegend(0.7,0.7,0.9,0.9)
    signal=False
    infile =[]
    #Adding data file
    fdata = TFile.Open("Plot/"+str(lep_).strip('[]')+"/Data_"+str(lep_).strip('[]')+".root")
    hdata = (TH1F)(fdata.Get(histoname))
    hdata.SetLineColor(kBlack)
    hdata.SetMarkerStyle(20)
    hdata.SetMarkerSize(0.9)
#    setTDRStyle() 
    leg_stack.AddEntry(hdata, "Data", "lp")
    hsig = hdata.Clone("")
    hsig.Reset("ICES")
    hratio = hdata.Clone("")
    hratio.Reset("ICES")
    for s in samples_:
        if s.leglabel=="t, t-ch_sd": signal=True
        if(syst_==""):
            outfile="Stack_"+str(lep_).strip('[]')+".root"
            infile.append(TFile.Open("Plot/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
        else:
            outfile="Stack_"+syst_+"_"+str(lep_).strip('[]')+".root"
            infile.append(TFile.Open("Plot/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+"_"+syst_+".root"))
    i=0
    for s in samples_:
        infile[i].cd()
        print "opening file: ", infile[i].GetName()
        tmp = (TH1F)(infile[i].Get(histoname))
        tmp.SetOption("HIST SAME")
        tmp.SetLineColor(kBlack)
        tmp.SetTitle("")
        tmp.SetName(s.leglabel)
        tmp.SetFillColor(s.color)
        if(signal): 
             if (tmp.GetName())=="t, t-ch_sd" or (tmp.GetName())=="t, t-ch_p_sd": # or (tmp.GetName())=="t#bar{t}_{sd}"
                  print "parz", tmp.Integral()
                  hsig.Add(tmp.Clone(""))
#                  hsig.Add(tmp)
                  hsig.SetName("t_sd")
                  hsig.SetTitle("")
             else:
                  histo.append(tmp.Clone(""))
                  stack.Add(tmp.Clone(""))
                  hratio.Add(tmp) 
        else:
             histo.append(tmp.Clone(""))
             stack.Add(tmp.Clone(""))
             hratio.Add(tmp) 
        i+=1
#        err_up,err_down = systerr(err_up, err_down, tmp, histoname, s, lep_)
        tmp.Reset("ICES")
    print "segnale somma", hsig.Integral()
    if(signal):
        leg_stack.AddEntry(hsig, "|V_{td,s}|^{2} proc. (#times 100)", "l")
#        leg_stack.AddEntry(hsig, "t_sd(*100)", "l")
    for hist in reversed(histo):
        if (hist.GetName())!="t_sd":
            leg_stack.AddEntry(hist, hist.GetName(), "f")
    #style options
    leg_stack.SetNColumns(2)
    leg_stack.SetFillColor(0)
    leg_stack.SetFillStyle(0)
    leg_stack.SetTextFont(42)
    leg_stack.SetTextSize(20)
    leg_stack.SetBorderSize(0) 
    leg_stack.SetTextSize(0.055)
    c1 = ROOT.TCanvas(canvasname,"c1",50,50,700,600)
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
    
    pad1= ROOT.TPad("pad1", "pad1", 0, 0.31 , 1, 1)
    pad1.SetTopMargin(0.1)
    pad1.SetBottomMargin(0)
    pad1.SetLeftMargin(0.12)
    pad1.SetRightMargin(0.05)
    pad1.SetBorderMode(0)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.Draw()
    pad1.cd()
    
    leg_stack.SetX1(.46)
    leg_stack.SetY1(.56)
    leg_stack.SetX2(.95)
    leg_stack.SetY2(.88)
    
    maximum = max(stack.GetMaximum(),hdata.GetMaximum())
    minimum = min(stack.GetMinimum(),hdata.GetMinimum())
    stack.SetMaximum(maximum*1.55)
    stack.SetMinimum(0.01)
    stack.Draw("HIST") 
    stack.GetYaxis().SetTitle("Events / bin")
    stack.GetYaxis().SetTitleFont(42)
    stack.GetXaxis().SetLabelOffset(1.8)
    stack.GetYaxis().SetTitleOffset(0.8)
    stack.GetXaxis().SetLabelSize(0.15)
    stack.GetYaxis().SetLabelSize(0.07)
    stack.GetYaxis().SetTitleSize(0.07)
    stack.SetTitle("")

    if(signal): 
        hsig.SetLineStyle(9)
        hsig.SetLineColor(kBlue)
        hsig.SetLineWidth(3)
#        hsig.SetFillColor(0)
        hsig.SetMarkerSize(0.)
        hsig.SetMarkerColor(kBlue)
        hsig.Scale(100)
        hsig.Draw("same L")
    leg_stack.Draw("same")
    h_err = stack.GetStack().Last().Clone("h_err")
    h_err.SetLineWidth(100)
    h_err.SetFillStyle(3154)
    h_err.SetMarkerSize(0)
    h_err.SetFillColor(ROOT.kGray+2)
    h_err.Draw("e2same0")

    hdata.Draw("eSAMEpx0")
    
    '''
    for n in range(1,tmp.GetNBins()):
         h_err_up.SetBinContent(n,(math.sqrt(pow(getSumError(err_up[n]),2)+pow(hratio.GetBinError(n)/2,2))))
         h_err_down.SetBinContent(n,(math.sqrt(pow(getSumError(err_down[n]),2)+pow(hratio.GetBinError(n)/2,2))))
    h_err_up.SetLineWidth(100)
    h_err_up.SetFillStyle(3154)
    h_err_up.SetMarkerSize(0)
    h_err_up.SetFillColor(kGray+2)
    h_err_down.SetLineWidth(100)
    h_err_down.SetFillStyle(3154)
    h_err_down.SetMarkerSize(0)
    h_err_down.SetFillColor(kGray+2)
    h_err_up.Draw("e2same0")
    h_err_down.Draw("e2same0")
    '''
    
    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "Preliminary"
    if(njmt_=="2j1t"):
        nJmT="2j1t"
    elif(njmt_=="3j1t"):
        nJmT="3j1t"
    elif(njmt_=="3j2t"):
        nJmT="3j2t"
    if str(lep_).strip('[]') == "muon":
         lep_tag = "#mu+"
    elif str(lep_).strip('[]') == "electron":
         lep_tag = "e+"
    lumi_sqrtS = lep_tag + str(nJmT)+" 35.89 fb^{-1}  (13 TeV)"
#    print lumi_sqrtS
    iPeriod = 0
    iPos = 11
    # writing the lumi information and the CMS "logo"
    # Ratio Check HERE
    CMS_lumi(pad1, lumi_sqrtS, iPos)
    hratio=stack.GetStack().Last()

    c1.cd()
    pad2= ROOT.TPad("pad2", "pad2", 0, 0.01 , 1, 0.30)
    pad2.SetTopMargin(0.05)
    pad2.SetBottomMargin(0.45)
    pad2.SetLeftMargin(0.12)
    pad2.SetRightMargin(0.05)
    ROOT.gStyle.SetHatchesSpacing(2)
    ROOT.gStyle.SetHatchesLineWidth(2)
    c1.cd()
    pad2.Draw()
    pad2.cd()
    ratio = hdata.Clone("ratio")
    ratio.SetLineColor(kBlack)
    ratio.SetMaximum(1.5)
    ratio.SetMinimum(0.5)
    ratio.Sumw2()
    ratio.SetStats(0)
    #hratio.Sumw2()
    ratio.Divide(hratio)
    ratio.SetMarkerStyle(20)
    ratio.SetMarkerSize(0.9)
    ratio.Draw("epx0e0")
    ratio.SetTitle("")

    h_bkg_err = hratio.Clone("h_err")
    h_bkg_err.Reset()
    h_bkg_err.Sumw2()

    for i in range(1,hratio.GetNbinsX()+1):
        h_bkg_err.SetBinContent(i,1)
        if(hratio.GetBinContent(i)):
            h_bkg_err.SetBinError(i, (hratio.GetBinError(i)/hratio.GetBinContent(i)))
        else:
            h_bkg_err.SetBinError(i, 0)
    h_bkg_err.SetLineWidth(100)
#    h_bkg_err.SetFillStyle(3001)
    h_bkg_err.SetMarkerSize(0)
    h_bkg_err.SetFillColor(ROOT.kGray+1)
    h_bkg_err.Draw("e20same")

    f1 = ROOT.TLine(variabile_._xmin, 1., variabile_._xmax,1.)
    f1.SetLineColor(ROOT.kBlack)
    f1.SetLineStyle(ROOT.kDashed)
    f1.Draw("same")
    
#    ratio.Draw("esamepx0e0") #0epx0same
    #print "ciao 3"
    #ratio.Sumw2()
    ratio.GetYaxis().SetTitle("Data / Bkg")
    ratio.GetYaxis().SetNdivisions(503)
    ratio.GetXaxis().SetLabelFont(42)
    ratio.GetYaxis().SetLabelFont(42)
    ratio.GetXaxis().SetTitleFont(42)
    ratio.GetYaxis().SetTitleFont(42)
    ratio.GetXaxis().SetTitleOffset(1.1)
    ratio.GetYaxis().SetTitleOffset(0.35)
    ratio.GetXaxis().SetLabelSize(0.15)
    ratio.GetYaxis().SetLabelSize(0.15)
    ratio.GetXaxis().SetTitleSize(0.16)
    ratio.GetYaxis().SetTitleSize(0.16)
    ratio.GetYaxis().SetRangeUser(0.5,1.5)
    ratio.GetXaxis().SetTitle(variabile_._title)
    ratio.GetXaxis().SetLabelOffset(0.04)
    ratio.GetYaxis().SetLabelOffset(0.01)
    ratio.Draw("epx0e0same")

    c1.cd()
    ROOT.TGaxis.SetMaxDigits(3)
    c1.RedrawAxis()
    pad2.RedrawAxis()
    c1.Update()
#    fout_name = "prova/"+outfile
    c1.Print("Stack/"+canvasname+".pdf")
    c1.Print("Stack/"+canvasname+".png")
#    c1.Print(canvasname+".root")
    fdata.Close()
    i=0
    for s in samples_:
        infile[i].Close()
        i+=1
    del histo
    del tmp 
    del h
    del hsig 
    del hratio
    del c1
    del stack
    del pad1
    del pad2
#    samples_[samples_.index(samplesDictionary["DDQCD"]):samples_.index(samplesDictionary["DDQCD"])+1]=[samplesDictionary["QCDMu"]]
#    c1.SaveAs("prova/stack_png/"+canvasname+".C")
#    c1.Print("Stack/stack_root/"+canvasname+".root",".root")
#    fout = TFile.Open(fout_name, "UPDATE")
#    c1.Write()

#fine makestack

usage = 'python makeplot.py'
parser = optparse.OptionParser(usage)
parser.add_option('--h1D', dest='h1D', default = False, action='store_true', help='Default make no histo1D')
parser.add_option('--h2D', dest='h2D', default = False, action='store_true', help='Default make no histo2D')
parser.add_option('--lumi', dest='lumi', default = False, action='store_true', help='Default make no trees lumi')
parser.add_option('--mertree', dest='mertree', default = False, action='store_true', help='Default make no trees lumi')
parser.add_option('--mva', dest='mva', default = False, action='store_true', help='Default make no mva')
parser.add_option('--plot', dest='plot', default = False, action='store_true', help='Default make no plots')
parser.add_option('-r', '--rm', dest='rm', default = False, action='store_true', help='Default no remove')
parser.add_option('-s', '--stack', dest='stack', default = False, action='store_true', help='Default make no stacks')
parser.add_option('-L', '--lep', dest='lep', type='string', default = 'muon', help='Default make muon analysis') 
parser.add_option('-S', '--syst', dest='syst', type='string', default = 'all', help='Default all systematics added')
parser.add_option('-C', '--cut', dest='cut', type='string', default = 'etajprime>0', help='Default no cut')
parser.add_option('-T', '--topol', dest='topol', type='string', default = 'all', help='Default all njmt')
parser.add_option('-P', '--process', dest='process', type='string', default = 'all', help="samples to add, according to the convention in 'script_rename.py'. Options are: 'All','ST','VJ','VV','QCDMu','QCDEle', or '_'+specific process, e.g. _ST_T_tch to add only the _ST_T_tch. Accepts also multiple processes, separated by comma, e.g. -P ST,_TT,VJ will select the V+jets samples and single top sample sets, as well as the one sample named TT.")
(opt, args) = parser.parse_args()

leptons=[]
if opt.lep != "muon":
     for lep in (opt.lep).split(","):
          leptons.append(lep)
else:
     leptons.append("muon")
for lep in leptons:
     print lep

samplesnames = []
samples = []
if opt.process!="all":
    for sn in (opt.process).split(","): 
        samplesnames.append(sn)
else:
    samplesnames.append("ST_tch")
    samplesnames.append("ST_tch_sd")
    samplesnames.append("ST_tch_p_sd")
    samplesnames.append("VV")
    samplesnames.append("ST_sch")
    samplesnames.append("DYJets")
    samplesnames.append("ST_tW")
    samplesnames.append("WJets_ext")
#    samplesnames.append("WJets")
    samplesnames.append("TT")
#    samplesnames.append("TT_sd")
    if opt.syst!="noSyst":
         samplesnames.append("ST_tch_psq2Up")
         samplesnames.append("ST_tch_psq2Down")
         samplesnames.append("ST_tch_hdampDown")
         samplesnames.append("ST_tch_hdampUp")
         samplesnames.append("TT_psq2Up")
         samplesnames.append("TT_psq2Down")
         samplesnames.append("TT_hdampUp")
         samplesnames.append("TT_hdampDown")

for sn in samplesnames:
    samples.append(samplesDictionary[sn])

components = []
for s in samples:
    components.extend(s.components)

samplesnames_stack = []
samples_stack = []
if opt.process!="all":
    for sn in (opt.process).split(","): 
        samplesnames_stack.append(sn)
else:
    samplesnames_stack.append("ST_tch")
    samplesnames_stack.append("ST_tch_sd")
    samplesnames_stack.append("ST_tch_p_sd")
    samplesnames_stack.append("ST_sch")
    samplesnames_stack.append("DDQCD")
    samplesnames_stack.append("VV")
    samplesnames_stack.append("DYJets")
    samplesnames_stack.append("WJets_ext")
#    samplesnames_stack.append("WJets")
    samplesnames_stack.append("ST_tW")
    samplesnames_stack.append("TT")
#    samplesnames_stack.append("TT_sd")
for sn in samplesnames_stack:
    samples_stack.append(samplesDictionary[sn])

cut = opt.cut #default cut must be obvious, for example etajprime>0
if opt.cut=="etajprime>0":
    cut_tag=""
else:
    cut_tag=cutToTag(opt.cut)
#print "cut tag is", cut_tag

variabili_2j1t = [] 
#wzero = "((((((((leadingextrajetcsvweight_sd>0.0)*(leadingextrajetcsvweight_sd))/0.154)+(leadingextrajetcsvweight_sd==0))*(nextrajets>0)+(nextrajets==0))))*w)"
wzero = "w"
#variabili_2j1t.append(variabile("mtw","m_{T}^{W} [GeV/c^{2}]",wzero+"*("+cut+")", 10, 0, 250))
#variabili_2j1t.append(variabile("mtw","m_{T}^{W} [GeV/c^{2}]",wzero+"*("+cut+")", 20, 0, 250))
#variabili_2j1t.append(variabile("etajprime", "|#eta_{j^{,}}|",wzero+"*("+cut+")", 10, 0, 4.7))
#variabili_2j1t.append(variabile("jprimeflavour","j^{,} flavour",wzero+"*("+cut+")", 12, -6, 6))
#variabili_2j1t.append(variabile("bjetflavour","b-jet flavour",wzero+"*("+cut+")", 12, -6, 6))
#variabili_2j1t.append(variabile("bjeteta","#eta_{b-jet}",wzero+"*("+cut+")", 48, -6, 6))
#variabili_2j1t.append(variabile("bjetpt","b-jet pT [GeV/c]",wzero+"*("+cut+")", 20, 0, 300))
#variabili_2j1t.append(variabile("topMass","top mass [GeV/c^{2}]",wzero+"*("+cut+")", 15, 90, 400))
#variabili_2j1t.append(variabile("topMt","top Mt",wzero+"*("+cut+")", 50, 0, 600))
#variabili_2j1t.append(variabile("topPt","top pT [GeV/c]",wzero+"*("+cut+")", 18, 0, 350))
#variabili_2j1t.append(variabile("topY","top Y",wzero+"*("+cut+")", 80, -400, 400))
#variabili_2j1t.append(variabile("topEta","#eta_{top}",wzero+"*("+cut+")", 48, -6, 6))
#variabili_2j1t.append(variabile("costhetael","cos#theta*_{hel}",wzero+"*("+cut+")", 10, -1, 1))
#variabili_2j1t.append(variabile("costhetapol","cos#theta*_{pol}",wzero+"*("+cut+")", 10, -1, 1))
#variabili_2j1t.append(variabile("mlb","lep+b-jet mass [GeV/c^{2}]",wzero+"*("+cut+")", 19, 20, 400))
#variabili_2j1t.append(variabile("mljprime","lep+j^{,} mass [GeV/c^{2}]",wzero+"*("+cut+")", 25, 0, 600))
#variabili_2j1t.append(variabile("mljextra","lep+j_{extra} Mass",wzero+"*("+cut+")", 25, 0, 600))
#variabili_2j1t.append(variabile("mt2w","mt2w",wzero+"*(nextrajets>2 && "+cut+")", 50, 0, 600))
#variabili_2j1t.append(variabile("MET","MET",wzero+"*("+cut+")", 50, 0, 600))
#variabili_2j1t.append(variabile("mindeltaphi","mindeltaphi", wzero+"*("+cut+")",20,-5,5))
#variabili_2j1t.append(variabile("mindeltaphi20", "mindeltaphi20",wzero+"*("+cut+")",20,-5,5))
#variabili_2j1t.append(variabile("topMassExtra","top Mass Extra",wzero+"*("+cut+")", 50, 50, 600))
#variabili_2j1t.append(variabile("topMtExtra","top Mt Extra",wzero+"*("+cut+")", 50, 50, 600))
#variabili_2j1t.append(variabile("topPtExtra","top P_{#Mathrm{T}} Extra",wzero+"*("+cut+")", 50, 50, 600))
#variabili_2j1t.append(variabile("topEtaExtra","#eta_{top} Extra",wzero+"*("+cut+")", 48, -6, 6))
#variabili_2j1t.append(variabile("topYExtra","top Y Extra",wzero+"*("+cut+")", 80, -400, 400))
#variabili_2j1t.append(variabile("costhetaelExtra","cos#theta*_{hel} Extra",wzero+"*("+cut+")", 10, -1, 1))
#variabili_2j1t.append(variabile("costhetapolExtra","cos#theta*_{pol} Extra",wzero+"*("+cut+")", 10, -1, 1))
#variabili_2j1t.append(variabile("nextrajets","nextrajets",wzero+"*("+cut+")", 6, -0.5, 5.5))
variabili_2j1t.append(variabile("leadingextrajetflavour","leadingextrajetflavour",wzero+"*("+cut+")", 12, -6, 6))
#variabili_2j1t.append(variabile("leadingextrajetpt","leadingextrajetp_{#mathrm{T}}",wzero+"*("+cut+")", 25, 17, 42))
#variabili_2j1t.append(variabile("leadingextrajeteta","leadingextrajeteta",wzero+"*("+cut+")", 48, -6, 6))
#variabili_2j1t.append(variabile("leadingextrajetcsv","leadingextrajetCMVAv2",wzero+"*("+cut+")", 60, -5, 1))
#variabili_2j1t.append(variabile("BDT_All_vs_QCDMu","BDT All vs QCDMu",wzero+"*("+cut+")", 50, -1, 1))
#variabili_2j1t.append(variabile("BDT_ST_vs_TT_mtweta","Discriminator ST vs TT qcd-depl cr",wzero+"*("+cut+")", 25, -0.7, 0.5))
#variabili_2j1t.append(variabile("BDT_ST_vs_VJ_mtweta","Discriminator ST vs VJ qcd-depl cr",wzero+"*("+cut+")", 15, -0.45, 0.4))
#variabili_2j1t.append(variabile("BDT_ST_vs_TT_mtweta_E","Discriminator ST vs TT qcd-depl cr",wzero+"*("+cut+")", 25, -0.7, 0.5))
#variabili_2j1t.append(variabile("BDT_ST_vs_VJ_mtweta_E","Discriminator ST vs VJ qcd-depl cr",wzero+"*("+cut+")", 25, -0.45, 0.4))
#variabili_2j1t.append(variabile("BDT_STsd_vs_All_sr","Discriminator STsd+TTsd vs TTb+VJ sr",wzero+"*("+cut+")", 10, -0.4, 0.3))
#variabili_2j1t.append(variabile("BDT_STsd_vs_ST_sr","Discriminator STsd+TTsd vs STb sr",wzero+"*("+cut+")", 10, -0.4, 0.2))
#variabili_2j1t.append(variabile("BDT_STsd_vs_All_sr_E","Discriminator STsd+TTsd vs TTb+VJ sr",wzero+"*("+cut+")", 10, -0.4, 0.3))
#variabili_2j1t.append(variabile("BDT_STsd_vs_ST_sr_E","Discriminator STsd+TTsd vs STb sr",wzero+"*("+cut+")", 10, -0.45, 0.85))

variabili_3j1t = [] 
#wzero = "(((((leadingextrajetcsvweight_sd>0.0)*(leadingextrajetcsvweight_sd))/0.154)+(leadingextrajetcsvweight_sd==0))*w)"
wzero = "w"
#variabili_3j1t.append(variabile("mtw","m_{T}^{W} [GeV/c^{2}]",wzero+"*("+cut+")", 12, 50, 250))
#variabili_3j1t.append(variabile("mtw","m_{T}^{W} [GeV/c^{2}]",wzero+"*("+cut+")", 20, 0, 250))
#variabili_3j1t.append(variabile("MET","MET",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j1t.append(variabile("leadingextrajetcsv","leading extra jet CMVA",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j1t.append(variabile("etajprime","|#eta_{j^{,}}|",wzero+"*("+cut+")", 10, 0, 4.7))
#variabili_3j1t.append(variabile("leadingextrajeteta","leading extra jet #eta",wzero+"*("+cut+")", 10, -4.2, 4.2))
#variabili_3j1t.append(variabile("nextrajets","no. extra jets",wzero+"*("+cut+")", 6, -0.5, 5.5))
#variabili_3j1t.append(variabile("mt2w","mt2w",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j1t.append(variabile("jprimeflavour","j^{,} flavour",wzero+"*("+cut+")", 12, -6, 6))
#variabili_3j1t.append(variabile("mlb","lep+b-jet mass [GeV/c^{2}]",wzero+"*("+cut+")", 25, 0, 500))
#variabili_3j1t.append(variabile("mljprime","lep+j^{,} mass [GeV/c^{2}]",wzero+"*("+cut+")", 25, 0, 600))
#variabili_3j1t.append(variabile("mljextra","lep+j_{extra} Mass",wzero+"*("+cut+")", 25, 0, 600))
#variabili_3j1t.append(variabile("bjetflavour","b-jet flavour",wzero+"*("+cut+")", 12, -6, 6))
#variabili_3j1t.append(variabile("bjeteta","#eta_{b-jet}",wzero+"*("+cut+")", 48, -6, 6))
#variabili_3j1t.append(variabile("bjetpt","b-jet pT [GeV/c]",wzero+"*("+cut+")", 20, 0, 300))
#variabili_3j1t.append(variabile("topMass","top mass [GeV/c^{2}]",wzero+"*("+cut+")", 15, 90, 400))
#variabili_3j1t.append(variabile("topMt","top Mt",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j1t.append(variabile("topPt","top pT [GeV/c]",wzero+"*("+cut+")", 18, 0, 350))
#variabili_3j1t.append(variabile("topY","top Y",wzero+"*("+cut+")", 80, -400, 400))
#variabili_3j1t.append(variabile("topEta","#eta_{top}",wzero+"*("+cut+")", 48, -6, 6))
#variabili_3j1t.append(variabile("costhetael","cos #theta_{hel}",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j1t.append(variabile("costhetapol","cos #theta_{pol}",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j1t.append(variabile("topMassExtra","top Mass Extra",wzero+"*("+cut+")", 50, 50, 600))
#variabili_3j1t.append(variabile("topPtExtra","top P_{#Mathrm{T}} Extra",wzero+"*("+cut+")", 50, 50, 600))
#variabili_3j1t.append(variabile("costhetaelExtra","cos #theta_{hel} Extra",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j1t.append(variabile("costhetapolExtra","cos #theta_{pol} Extra",wzero+"*("+cut+")", 10, -1, 1))
'''
variabili_3j1t.append(variabile("topMtExtra","top Mt Extra",wzero+"*("+cut+")", 50, 0, 600))
variabili_3j1t.append(variabile("topYExtra","top Y Extra",wzero+"*("+cut+")", 80, -400, 400))
variabili_3j1t.append(variabile("topEtaExtra","#eta_{top} Extra",wzero+"*("+cut+")", 48, -6, 6))
variabili_3j1t.append(variabile("leadingextrajetflavour","leadingextrajetflavour",wzero+"*("+cut+")", 12, -6, 6))
variabili_3j1t.append(variabile("leadingextrajetpt","leadingextrajetp_{#mathrm{T}}",wzero+"*("+cut+")", 25, 17, 42))
variabili_3j1t.append(variabile("BDT_STsd_vs_TT_sr_3j1t","BDT STsd vs TT sr",wzero+"*("+cut+")", 50, -1, 1))
variabili_3j1t.append(variabile("BDT_All_vs_QCDMu_mtw_3j1t","BDT All vs QCDMu",wzero+"*("+cut+")", 50, -1, 1))
'''
#variabili_3j1t.append(variabile("BDT_ST_vs_TT_mtweta_3j1t","Discriminator ST vs TT qcd-depl cr",wzero+"*("+cut+")", 15, -0.55, 0.45))
#variabili_3j1t.append(variabile("BDT_ST_vs_VJ_mtweta_3j1t","Discriminator ST vs VJ qcd-depl cr",wzero+"*("+cut+")", 15, -0.4, 0.4))
#variabili_3j1t.append(variabile("BDT_STsd_vs_All_sr_3j1t","Discriminator STsd+TTsd vs TTb+VJ sr",wzero+"*("+cut+")", 10, -0.4, 0.3))
variabili_3j1t.append(variabile("BDT_STsd_vs_ST_sr_3j1t","Discriminator STsd+TTsd vs STb sr",wzero+"*("+cut+")", 10, -0.4, 0.2))
#variabili_3j1t.append(variabile("BDT_ST_vs_TT_mtweta_3j1t_E","Discriminator ST vs TT qcd-depl cr",wzero+"*("+cut+")", 15, -0.55, 0.45))
#variabili_3j1t.append(variabile("BDT_ST_vs_VJ_mtweta_3j1t_E","Discriminator ST vs VJ qcd-depl cr",wzero+"*("+cut+")", 15, -0.4, 0.4))
#variabili_3j1t.append(variabile("BDT_STsd_vs_All_sr_3j1t_E","Discriminator STsd+TTsd vs TTb+VJ sr",wzero+"*("+cut+")", 10, -0.4, 0.3))
#variabili_3j1t.append(variabile("BDT_STsd_vs_ST_sr_3j1t_E","Discriminator STsd+TTsd vs STb sr",wzero+"*("+cut+")", 10, -0.4, 0.5))

variabili_3j2t = [] 
wzero = "w"
#variabili_3j2t.append(variabile("mtw","m_{T}^{W} [GeV/c^{2}]",wzero+"*("+cut+")", 12, 0, 250))
#variabili_3j2t.append(variabile("etajprime","|#eta_{j^{,}}|",wzero+"*("+cut+")", 10, 0, 4.7))
#variabili_3j2t.append(variabile("MET","MET",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j2t.append(variabile("mt2w","mt2w",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j2t.append(variabile("deltaEtabb","#Delta#eta_{bb}",wzero+"*("+cut+")", 24, 0, 6))
#variabili_3j2t.append(variabile("mlbleading","lep+b-jet leading mass [GeV/c]^{2}",wzero+"*("+cut+")", 35, 0, 500))
#variabili_3j2t.append(variabile("mlbsecond","lep+b-jet second mass [GeV/c]^{2}",wzero+"*("+cut+")", 35, 0, 500))
#variabili_3j2t.append(variabile("mljprime","lep+j^{,} Mass",wzero+"*("+cut+")", 100, 0, 800))
#variabili_3j2t.append(variabile("topMassLeading","top mass leading [GeV/c]^{2}",wzero+"*("+cut+")", 15, 90, 400))
#variabili_3j2t.append(variabile("topMtLeading","top Mt leading",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j2t.append(variabile("topPtLeading","top pT leading [GeV/c]",wzero+"*("+cut+")", 40, 0, 600))
#variabili_3j2t.append(variabile("topYLeading","top Y leading",wzero+"*("+cut+")", 80, -400, 400))
#variabili_3j2t.append(variabile("topEtaLeading","#eta_{top} leading",wzero+"*("+cut+")", 48, -6, 6))
#variabili_3j2t.append(variabile("costhetaelLeading","cos #theta_{hel} leading",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j2t.append(variabile("costhetapolLeading","cos #theta_{pol} leading",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j2t.append(variabile("topMassSecond","top mass second [GeV/c]^{2}",wzero+"*("+cut+")", 20, 0, 400))
#variabili_3j2t.append(variabile("topMtSecond","top Mt second",wzero+"*("+cut+")", 50, 0, 600))
#variabili_3j2t.append(variabile("topPtSecond","top pT second [GeV/c]",wzero+"*("+cut+")", 20, 0, 400))
#variabili_3j2t.append(variabile("topYSecond","top Y second",wzero+"*("+cut+")", 80, -400, 400))
#variabili_3j2t.append(variabile("topEtaSecond","#eta_{top} second",wzero+"*("+cut+")", 48, -6, 6))
#variabili_3j2t.append(variabile("costhetaelSecond","cos #theta_{hel} leading",wzero+"*("+cut+")", 10, -1, 1))
#variabili_3j2t.append(variabile("costhetapolSecond","cos #theta_{pol} second",wzero+"*("+cut+")", 10, -1, 1))
variabili_3j2t.append(variabile("BDT_ST_vs_TT_3j2t","Discriminator ST vs TT",wzero+"*("+cut+")", 15, -0.4, 0.4))
#variabili_3j2t.append(variabile("BDT_ST_vs_TT_3j2t_E","Discriminator ST vs TT",wzero+"*("+cut+")", 20, -0.4, 0.4))


systematics = []
if opt.syst!="all" and opt.syst!="noSyst":
    systematics.append((opt.syst).split(","))
elif opt.syst!="all" and opt.syst=="noSyst":
    systematics.append("") #di default per syst="" alla variabile si applica il peso standard incluso nella macro macro_plot.C
else:
    systematics.append("") #di default per syst="" alla variabile si applica il peso standard incluso nella macro macro_plot.C
    systematics.append("btagUp")  
    systematics.append("btagDown")
    systematics.append("mistagUp")
    systematics.append("mistagDown")
    systematics.append("puUp")
    systematics.append("puDown")
    systematics.append("lepUp")
    systematics.append("lepDown")
    systematics.append("jesUp")
    systematics.append("jesDown")
    systematics.append("jerUp")
    systematics.append("jerDown")
    systematics.append("q2Up")
    systematics.append("q2Down")
    systematics.append("pdf_totalUp")
    systematics.append("pdf_totalDown")
    systematics.append("cmvacferr1Up")
    systematics.append("cmvacferr1Down")
    systematics.append("cmvahfstats1Up")
    systematics.append("cmvahfstats1Down")
    systematics.append("cmvahfstats2Up")
    systematics.append("cmvahfstats2Down")
    systematics.append("cmvalfstats1Up")
    systematics.append("cmvalfstats1Down")
    systematics.append("cmvalfstats2Up")
    systematics.append("cmvalfstats2Down")

topologies = []
if opt.topol!="all":
    topologies.append((opt.topol).split(","))
else:
    topologies.append("2j1t")
    topologies.append("3j1t")
    topologies.append("3j2t")


trainings_2j1t = []
trainings_2j1t.append("ST_vs_TT_mtweta")
trainings_2j1t.append("ST_vs_VJ_mtweta")
trainings_2j1t.append("STsd_vs_All_sr")
trainings_2j1t.append("STsd_vs_ST_sr")

trainings_3j1t = []
trainings_3j1t.append("ST_vs_TT_mtweta_3j1t")
trainings_3j1t.append("ST_vs_VJ_mtweta_3j1t")
trainings_3j1t.append("STsd_vs_All_sr_3j1t")
trainings_3j1t.append("STsd_vs_ST_sr_3j1t")

trainings_3j2t = []
trainings_3j2t.append("ST_vs_TT_3j2t")

trainings_2j1t_E = []
trainings_2j1t_E.append("ST_vs_TT_mtweta")
trainings_2j1t_E.append("ST_vs_VJ_mtweta")
trainings_2j1t_E.append("STsd_vs_All_sr")
trainings_2j1t_E.append("STsd_vs_ST_sr")

trainings_3j1t_E = []
trainings_3j1t_E.append("ST_vs_TT_mtweta_3j1t")
trainings_3j1t_E.append("ST_vs_VJ_mtweta_3j1t")
trainings_3j1t_E.append("STsd_vs_All_sr_3j1t")
trainings_3j1t_E.append("STsd_vs_ST_sr_3j1t")

trainings_3j2t_E = []
trainings_3j2t_E.append("ST_vs_TT_3j2t")

lumi=35.89

print "trees lumi option is ", opt.lumi
if opt.lumi:
    if not os.path.exists("trees_lumi"):
        os.system("mkdir trees_lumi")
    for lep in leptons:
         if not os.path.exists("trees_lumi/"+str(lep).strip('[]')):
              os.system("mkdir trees_lumi/"+str(lep).strip('[]'))
         for comp in components:
              makelumi("macro_lumi.C", comp.label, lumi, comp.sigma, str(lep).strip('[]'))

print "mergetrees option is ", opt.mertree
if opt.mertree:
     for lep in leptons:
          for sample in samples:
               mergetree(sample, lep)
               print "merging file:", sample.label
          print "merging Data"
          if str(lep).strip('[]')=='muon' or str(lep).strip('[]')=='muonantiiso': 
               os.system("hadd -f trees/"+str(lep).strip('[]')+"/trees_Data_"+str(lep).strip('[]')+".root trees/"+str(lep).strip('[]')+"/*SingleMuon*.root")
          else:
               os.system("hadd -f trees/"+str(lep).strip('[]')+"/trees_Data_"+str(lep).strip('[]')+".root trees/"+str(lep).strip('[]')+"/*SingleElectron*.root")
          print "copying Data in folder tree_lumi"
          os.system("cp trees/"+str(lep).strip('[]')+"/trees_Data_"+str(lep).strip('[]')+".root trees_lumi/"+str(lep).strip('[]')+"/trees_Data_"+str(lep).strip('[]')+".root")

print "mva option is ", opt.mva
if opt.mva:
     for lep in leptons:
          if ((opt.topol=="2j1t")or(opt.topol=="all")):
               njmt="2j1t"
               if lep=="muon" or lep=="muonantiiso":
                    for train in trainings_2j1t:
                         makeBDT("macro_BDT.C", "Data", njmt, train, "", str(lep).strip('[]')) 
                         for syst in systematics:
                              if((syst=="")or(syst=="jesUp")or(syst=="jesDown")or(syst=="jerUp")or(syst=="jerDown")):
                                   for sample in samples:
                                        makeBDT("macro_BDT.C", sample.label, njmt, train, syst, str(lep).strip('[]')) 
               else:
                    for train in trainings_2j1t_E:
                         makeBDT("macro_BDT.C", "Data", njmt, train, "", str(lep).strip('[]')) 
                         for syst in systematics:
                              if((syst=="")or(syst=="jesUp")or(syst=="jesDown")or(syst=="jerUp")or(syst=="jerDown")):
                                   for sample in samples:
                                        makeBDT("macro_BDT.C", sample.label, njmt, train, syst, str(lep).strip('[]')) 

          if ((opt.topol=="3j1t")or(opt.topol=="all")):
               njmt="3j1t"
               if lep=="muon" or lep=="muonantiiso":
                    for train in trainings_3j1t:
                         makeBDT("macro_BDT.C", "Data", njmt, train, "", str(lep).strip('[]')) 
                         for syst in systematics:
                              if((syst=="")or(syst=="jesUp")or(syst=="jesDown")or(syst=="jerUp")or(syst=="jerDown")):
                                  for sample in samples:
                                        makeBDT("macro_BDT.C", sample.label, njmt, train, syst, str(lep).strip('[]')) 
               else:
                    for train in trainings_3j1t_E:
                         makeBDT("macro_BDT.C", "Data", njmt, train, "", str(lep).strip('[]')) 
                         for syst in systematics:
                              if((syst=="")or(syst=="jesUp")or(syst=="jesDown")or(syst=="jerUp")or(syst=="jerDown")):
                                   for sample in samples:
                                        makeBDT("macro_BDT.C", sample.label, njmt, train, syst, str(lep).strip('[]')) 

          if ((opt.topol=="3j2t")or(opt.topol=="all")):
               njmt="3j2t"
               if lep=="muon" or lep=="muonantiiso":
                    for train in trainings_3j2t:
                         makeBDT("macro_BDT.C", "Data", njmt, train, "", str(lep).strip('[]')) 
                         for syst in systematics:
                              if((syst=="")or(syst=="jesUp")or(syst=="jesDown")or(syst=="jerUp")or(syst=="jerDown")):
                                   for sample in samples:
                                        makeBDT("macro_BDT.C", sample.label, njmt, train, syst, str(lep).strip('[]')) 
               else:
                    for train in trainings_3j2t_E:
                         makeBDT("macro_BDT.C", "Data", njmt, train, "", str(lep).strip('[]')) 
                         for syst in systematics:
                              if((syst=="")or(syst=="jesUp")or(syst=="jesDown")or(syst=="jerUp")or(syst=="jerDown")):
                                   for sample in samples:
                                        makeBDT("macro_BDT.C", sample.label, njmt, train, syst, str(lep).strip('[]')) 

print "plot option is ", opt.plot
if opt.plot:
     doplot = True
     if not os.path.exists("Plot"):
          os.system("mkdir Plot")
     for lep in leptons:
          if ((opt.topol=="2j1t")or(opt.topol=="all")):
               njmt="2j1t"
               for var in variabili_2j1t:
                    for syst in systematics:
                         for sample in samples:
                              namech=sample.label
                              namefile=namech+"_"+str(lep).strip('[]')+".root"
                              pathfile = "Plot/"+str(namefile)
                              if os.path.exists(pathfile):
                                   if opt.rm:
                                        rmfile(pathfile)
                              if(((lep=="muonantiiso" or lep=="electronantiiso") and  namech=="TT_sd") or (("hdamp" in namech) or ("psq2" in namech)) and ((lep=="muonantiiso" or lep=="electronantiiso") or (syst!=""))):doplot = False
                              if doplot:
                                   makeplot("macro_plot.C", namech, var, njmt, syst, cut_tag, lep)
                              doplot=True
                    makeplot("macro_plot.C", "Data", var, njmt, "", cut_tag, lep)
          if ((opt.topol=="3j1t")or(opt.topol=="all")):
               njmt="3j1t"
               for var in variabili_3j1t:
                    for syst in systematics:
                         for sample in samples:
                              namech=sample.label
                              namefile=namech+"_"+str(lep).strip('[]')+".root"
                              pathfile = "Plot/"+str(namefile)
                              if os.path.exists(pathfile):
                                   if opt.rm:
                                        rmfile(pathfile)
                              if(((lep=="muonantiiso" or lep=="electronantiiso") and  namech=="TT_sd") or (("hdamp" in namech) or ("psq2" in namech)) and ((lep=="muonantiiso" or lep=="electronantiiso") or (syst!=""))):doplot = False
                              if doplot:
                                   makeplot("macro_plot.C", namech, var, njmt, syst, cut_tag, lep)
                              doplot = True
                    makeplot("macro_plot.C", "Data", var, njmt, "", cut_tag, lep)
          if ((opt.topol=="3j2t")or(opt.topol=="all")):
               njmt="3j2t"
               for var in variabili_3j2t:
                    for syst in systematics:
                         for sample in samples:
                              namech=sample.label
                              namefile=namech+"_"+str(lep).strip('[]')+".root"
                              pathfile = "Plot/"+str(namefile)
                              if os.path.exists(pathfile):
                                   if opt.rm:
                                        rmfile(pathfile)
                              if(((lep=="muonantiiso" or lep=="electronantiiso") and  namech=="TT_sd") or (("hdamp" in namech) or ("psq2" in namech)) and ((lep=="muonantiiso" or lep=="electronantiiso") or (syst!=""))):doplot = False
                              if doplot:
                                   makeplot("macro_plot.C", namech, var, njmt, syst, cut_tag, lep)
                              doplot = True
                    makeplot("macro_plot.C", "Data", var, njmt, "", cut_tag, lep)

print "stack option is ", opt.stack
if opt.stack:
    code_tag = ""
    region = ""
    for lep in leptons:
        if(lep=="muon" or lep =="electron"):
            print lep
            sist="" #per ora gli stack senza sistematiche 
            if not os.path.exists("Stack"):
                os.system("mkdir Stack")
            pathfile = "Stack/Stack_"+str(lep).strip('[]')+".root"
            if os.path.exists(pathfile):
                if opt.rm:
                    rmfile(pathfile)
            if ((opt.topol=="2j1t")or(opt.topol=="all")):
                njmt="2j1t"
                for var in variabili_2j1t:
                    histoname = "h_"+njmt+"_"+var._name
                    for syst in systematics:
                        if lep=='muon':
                            DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  lep)
                        else:
                            DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  lep)
                    makestack(njmt, var, sist, samples_stack, cut_tag, lep)
            if ((opt.topol=="3j1t")or(opt.topol=="all")):
                njmt="3j1t"
                for var2 in variabili_3j1t:
                    histoname = "h_"+njmt+"_"+var2._name
                    for syst in systematics:
                        if lep=='muon':
                            DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  lep)
                        else:
                            DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  lep)
                    makestack(njmt, var2, sist, samples_stack, cut_tag, lep)
            if ((opt.topol=="3j2t")or(opt.topol=="all")):
                njmt="3j2t"
                for var3 in variabili_3j2t:
                    histoname = "h_"+njmt+"_"+var3._name
                    for syst in systematics:
                         DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  lep)
                    makestack(njmt, var3, sist, samples_stack, cut_tag, lep)
    
print "histo2D option is ", opt.h2D
if opt.h2D:
     for lep in leptons:
         if ((opt.topol=="2j1t")or(opt.topol=="all")):
             njmt="2j1t"
             if lep=="muon" or lep=="muonantiiso":
                 BDT_TT="ST_vs_TT_mtweta"
                 BDT_VJ="ST_vs_VJ_mtweta"
             else:
                 BDT_TT="ST_vs_TT_mtweta"
                 BDT_VJ="ST_vs_VJ_mtweta"
#                 BDT_TT="ST_vs_TT_mtweta_E"
#                 BDT_VJ="ST_vs_VJ_mtweta_E"
             region="cr"
             makehisto2D("macro_2Dhisto.C", "Data", njmt, "", region, BDT_TT, BDT_VJ, lep)  
             for syst in systematics:
                 for sample in samples:
                      if not((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!=""): 
                           makehisto2D("macro_2Dhisto.C", sample.label, njmt, syst, region, BDT_TT, BDT_VJ, lep)
             if lep=="muon" or lep=="muonantiiso":
                 BDT_TT="STsd_vs_All_sr"
                 BDT_VJ="STsd_vs_ST_sr"
             else:
                 BDT_TT="STsd_vs_All_sr"
                 BDT_VJ="STsd_vs_ST_sr"
#                 BDT_TT="STsd_vs_All_sr_E"
#                 BDT_VJ="STsd_vs_ST_sr_E"
             region="sr"
             makehisto2D("macro_2Dhisto.C", "Data", njmt, "", region, BDT_TT, BDT_VJ, lep)  
             for syst in systematics:
                 for sample in samples:
                      if not((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!=""): 
                           makehisto2D("macro_2Dhisto.C", sample.label, njmt, syst, region, BDT_TT, BDT_VJ, lep)
         if ((opt.topol=="3j1t")or(opt.topol=="all")):
             njmt="3j1t"
             if lep=="muon" or lep=="muonantiiso":
                 BDT_TT="ST_vs_TT_mtweta_3j1t"
                 BDT_VJ="ST_vs_VJ_mtweta_3j1t"
             else:
                 BDT_TT="ST_vs_TT_mtweta_3j1t"
                 BDT_VJ="ST_vs_VJ_mtweta_3j1t"
#                 BDT_TT="ST_vs_TT_mtweta_3j1t_E"
#                 BDT_VJ="ST_vs_VJ_mtweta_3j1t_E"
             region="cr"
             makehisto2D("macro_2Dhisto.C", "Data", njmt, "", region, BDT_TT, BDT_VJ, lep)  
             for syst in systematics:
                 for sample in samples:
                      if not((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!=""): 
                           makehisto2D("macro_2Dhisto.C", sample.label, njmt, syst, region, BDT_TT, BDT_VJ, lep)  
             if lep=="muon" or lep=="muonantiiso":
                 BDT_TT="STsd_vs_All_sr_3j1t"
                 BDT_VJ="STsd_vs_ST_sr_3j1t"
             else:
                 BDT_TT="STsd_vs_All_sr_3j1t"
                 BDT_VJ="STsd_vs_ST_sr_3j1t"
#                 BDT_TT="STsd_vs_All_sr_3j1t_E"
#                 BDT_VJ="STsd_vs_ST_sr_3j1t_E"
             region="sr"
             makehisto2D("macro_2Dhisto.C", "Data", njmt, "", region, BDT_TT, BDT_VJ, lep)  
             for syst in systematics:
                 for sample in samples:
                      if not((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!=""): 
                           makehisto2D("macro_2Dhisto.C", sample.label, njmt, syst, region, BDT_TT, BDT_VJ, lep)  

lista_tagli_2j1t_cr = []
lista_tagli_2j1t_cr.append([-0.6, 0.6, -0.6, 0.6])

def code(nbins, xmin, xmax, lista):
  bin1x = (1+lista[0])*nbins/(xmax-xmin)+1
  bin2x = (1+lista[1])*nbins/(xmax-xmin)
  bin1y = (1+lista[2])*nbins/(xmax-xmin)+1
  bin2y = (1+lista[3])*nbins/(xmax-xmin)
  code_ = str(int(bin1x))+str(int(bin2x))+str(int(bin1y))+str(int(bin2y))
  return code_

print "histo1D option is ", opt.h1D
if opt.h1D:
     nbins = 10
     xmin = -1
     xmax = 1
     for lep in leptons:
          if ((opt.topol=="2j1t")or(opt.topol=="all")):
               njmt="2j1t"
               for list_ in lista_tagli_2j1t_cr:
                    region = "cr"
                    makehisto1D("macro_2Dto1D.C", "Data", njmt, "", region, list_[0], list_[1], list_[2], list_[3], lep)
                    for syst in systematics:
                         for sample in samples:
                             if not ((syst=="q2" and sample=="ST_tW") or ((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!="")):  
                                  makehisto1D("macro_2Dto1D.C", sample.label, njmt, syst, region, list_[0], list_[1], list_[2], list_[3], lep)
#                                  print "ciao"
                         if lep=='muonantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             print histoname, code_tag
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "muon")
                         if lep=='electronantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "electron")
               for list_ in lista_tagli_2j1t_cr:
                    region = "sr"
                    makehisto1D("macro_2Dto1D.C", "Data", njmt, "", region, list_[0], list_[1], list_[2], list_[3], lep)
                    for syst in systematics:
                         for sample in samples:
                             if not ((syst=="q2" and sample=="ST_tW") or ((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!="")):  
                                  makehisto1D("macro_2Dto1D.C", sample.label, njmt, syst, region, list_[0], list_[1], list_[2], list_[3], lep)
#                                  print "ciao"
                         if lep=='muonantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             print histoname, code_tag
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "muon")
                         if lep=='electronantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "electron")
          if lep=="muon" or lep=="muonantiiso":        
               os.system("cp Plot/"+lep+"/ST_tW_"+lep+".root " "Plot/"+lep+"/ST_tW_"+lep+"_pdf_totalUp.root")
               os.system("cp Plot/"+lep+"/ST_tW_"+lep+".root " "Plot/"+lep+"/ST_tW_"+lep+"_pdf_totalDown.root")

          if ((opt.topol=="3j1t")or(opt.topol=="all")):
               njmt="3j1t"
               for list_ in lista_tagli_2j1t_cr:
                    region = "cr"
                    makehisto1D("macro_2Dto1D.C", "Data", njmt, "", region, list_[0], list_[1], list_[2], list_[3], lep)
                    for syst in systematics:
                         for sample in samples:
                             if not ((syst=="q2" and sample=="ST_tW") or ((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!="")):  
                                 makehisto1D("macro_2Dto1D.C", sample.label, njmt, syst, region, list_[0], list_[1], list_[2], list_[3], lep)
#                                  print "ciao"
                         if lep=='muonantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             print histoname, code_tag
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "muon")
                         if lep=='electronantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "electron")
               for list_ in lista_tagli_2j1t_cr:
                    region = "sr"
                    makehisto1D("macro_2Dto1D.C", "Data", njmt, "", region, list_[0], list_[1], list_[2], list_[3], lep)
                    for syst in systematics:
                         for sample in samples:
                             if not ((syst=="q2" and sample=="ST_tW") or ((("psq2" in sample.label) or("hdamp" in sample.label)) and syst!="")):  
                                 makehisto1D("macro_2Dto1D.C", sample.label, njmt, syst, region, list_[0], list_[1], list_[2], list_[3], lep)
#                                  print "ciao"
                         if lep=='muonantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             print histoname, code_tag
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region,  "muon")
                         if lep=='electronantiiso':
                             histoname = "h1D_"+njmt+"_"+region
                             code_tag = code(nbins, xmin, xmax, list_)
                             DDQCD("./Plot", "./Plot", histoname, syst, samples_stack, cut_tag, code_tag, region, "electron")
          if lep=="muon" or lep=="muonantiiso":        
               os.system("cp Plot/"+lep+"/ST_tW_"+lep+".root " "Plot/"+lep+"/ST_tW_"+lep+"_pdf_totalUp.root")
               os.system("cp Plot/"+lep+"/ST_tW_"+lep+".root " "Plot/"+lep+"/ST_tW_"+lep+"_pdf_totalDown.root")


def stack_h1D(njmt_, region_, syst_, samples_, code_tag_, lep_):
    histo = []
    tmp = ROOT.TH1F()
    hsig =  TH1F()
    h = ROOT.TH1F()
    print "Region: ", region_
    ROOT.gROOT.Reset()
    ROOT.gROOT.SetStyle('Plain')
    ROOT.gStyle.SetPalette(1)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gROOT.SetBatch()        # don't pop up canvases
    ROOT.TH1.SetDefaultSumw2()
#    ROOT.TH1.AddDirectory(False)
    ROOT.TGaxis.SetMaxDigits(3)
#    gROOT.ForceStyle()
    setTDRStyle()

    if code_tag_=="":
        histoname = "h1D_"+njmt_+"_"+region_
        canvasname = "Stack_"+njmt_+"_"+region_+"_"+lep_


    else:
        histoname = "h1D_"+njmt_+"_"+region_+"_"+code_tag_
        canvasname = "Stack_"+njmt_+"_"+region_+"_"+code_tag_+"_"+lep_+syst_
    stack = ROOT.THStack(region_, region_)
    leg_stack = ROOT.TLegend(0.7,0.7,0.9,0.9)
    signal=False
    infile =[]
    for s in samples_:
        if s.leglabel=="t, t-ch_sd": signal=True
        if(syst_==""):
            outfile="Stack_"+str(lep_).strip('[]')+".root"
            infile.append(TFile.Open("Plot/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
        else:
            outfile="Stack_"+syst_+"_"+str(lep_).strip('[]')+".root"
            infile.append(TFile.Open("Plot/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+"_"+syst_+".root"))
    i=0
    for s in samples_:
        infile[i].cd()
        print "opening file: ", infile[i].GetName()
        tmp = (TH1F)(infile[i].Get(histoname))
        tmp.SetOption("HIST SAME")
        tmp.SetLineColor(kBlack)
        tmp.SetTitle("")
        tmp.SetName(s.leglabel)
        if(signal): 
             if (tmp.GetName())=="t, t-ch_sd" or (tmp.GetName())=="t, t-ch_p_sd" or (tmp.GetName())=="t#bar{t}_{sd}":
                  print "parz", tmp.Integral()
                  hsig.Add(tmp.Clone(""))
                  hsig.SetName("t_sd")
                  hsig.SetTitle("")
             else:
                  tmp.SetFillColor(s.color)
                  histo.append(tmp.Clone(""))
                  stack.Add(tmp.Clone(""))
        else:
             tmp.SetFillColor(s.color)
             histo.append(tmp.Clone(""))
             stack.Add(tmp.Clone(""))
        i+=1
        tmp.Reset("ICES")
    #Adding data file
    fdata = TFile.Open("Plot/"+str(lep_).strip('[]')+"/Data_"+str(lep_).strip('[]')+".root")
    hdata = (TH1F)(fdata.Get(histoname))
    hdata.SetLineColor(kBlack)
    hdata.SetMarkerStyle(20)
    hdata.SetMarkerSize(0.9)
#    setTDRStyle() 
    leg_stack.AddEntry(hdata, "Data", "lp")
    if(signal):
        leg_stack.AddEntry(hsig, "|V_{td,s}|^{2} proc. (#times 100)", "l")
    for hist in reversed(histo):
         if not(tmp.GetName())=="t, t-ch_sd" or (tmp.GetName())=="t, t-ch_p_sd" or (tmp.GetName())=="t#bar{t}_{sd}":
              leg_stack.AddEntry(hist, hist.GetName(), "f")
    hratio = (stack.GetStack()).Last()
    #style options
    leg_stack.SetNColumns(2)
    leg_stack.SetFillColor(0)
    leg_stack.SetFillStyle(0)
    leg_stack.SetTextFont(42)
    leg_stack.SetTextSize(20)
    leg_stack.SetBorderSize(0) 
    leg_stack.SetTextSize(0.055)
    c1 = ROOT.TCanvas(canvasname,"c1",50,50,700,600)
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
    
    pad1= ROOT.TPad("pad1", "pad1", 0, 0.31 , 1, 1)
    pad1.SetTopMargin(0.1)
    pad1.SetBottomMargin(0)
    pad1.SetLeftMargin(0.12)
    pad1.SetRightMargin(0.05)
    pad1.SetBorderMode(0)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.Draw()
    pad1.cd()
    leg_stack.SetX1(.46)
    leg_stack.SetY1(.56)
    leg_stack.SetX2(.95)
    leg_stack.SetY2(.88)
    
    maximum = max(stack.GetMaximum(),hdata.GetMaximum())
    minimum = min(stack.GetMinimum(),hdata.GetMinimum())
    stack.SetMaximum(maximum*50000)
    stack.SetMinimum(0.01)
    stack.Draw("HIST") 
    stack.GetYaxis().SetTitle("Events / bin")
    stack.GetYaxis().SetTitleFont(40)
    stack.GetXaxis().SetLabelOffset(1.8)
    stack.GetYaxis().SetTitleOffset(0.8)
    stack.GetXaxis().SetLabelSize(0.15)
    stack.GetYaxis().SetLabelSize(0.07)
    stack.GetYaxis().SetTitleSize(0.07)
    stack.SetTitle("")

    if(signal): 
        hsig.SetLineStyle(2)
        hsig.SetLineColor(kBlue)
        hsig.SetLineWidth(3)
#        hsig.SetFillColor(0)
        hsig.SetMarkerSize(0.)
        hsig.SetMarkerColor(kBlue)
#        hsig.Scale(1)
        hsig.Draw("same HIST")
    gPad.SetLogy()
    leg_stack.Draw("same")
    hdata.Draw("eSAMEpx0")

    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "Preliminary"
    if(njmt_=="2j1t"):
        nJmT="2J1T"
    if(njmt_=="3j1t"):
        nJmT="3J1T"
    if(njmt_=="3j2t"):
        nJmT="3J2T"
    lumi_sqrtS = str(nJmT)+" 35.89 pb^{-1}  (13 TeV)"
#    print lumi_sqrtS
    iPeriod = 0
    iPos = 11
    # writing the lumi information and the CMS "logo"
    # Ratio Check HERE
    CMS_lumi(pad1, lumi_sqrtS, iPos)

    c1.cd()
    pad2= ROOT.TPad("pad2", "pad2", 0, 0.01 , 1, 0.30)
    pad2.SetTopMargin(0.05)
    pad2.SetBottomMargin(0.45)
    pad2.SetLeftMargin(0.12)
    pad2.SetRightMargin(0.05)
    ROOT.gStyle.SetHatchesSpacing(2)
    ROOT.gStyle.SetHatchesLineWidth(2)
    c1.cd()
    pad2.Draw()
    pad2.cd()
    ratio = hdata.Clone("ratio")
    ratio.SetLineColor(kBlack)
    ratio.SetMaximum(1.5)
    ratio.SetMinimum(0.5)
    ratio.Sumw2()
    ratio.SetStats(0)
    #hratio.Sumw2()
    ratio.Divide(hratio)
    ratio.SetMarkerStyle(20)
    ratio.SetMarkerSize(0.9)
    ratio.Draw("epx0e0")
    ratio.SetTitle("")
    xmin=hsig.GetXaxis().GetFirst()
    xmax=hsig.GetXaxis().GetLast()
    print xmin, "_", xmax
    f1 = ROOT.TLine(xmin, 1., xmax,1.)
    f1.SetLineColor(ROOT.kBlack)
    f1.SetLineStyle(ROOT.kDashed)
    f1.Draw("same")
    
#    ratio.Draw("esamepx0e0") #0epx0same
    #print "ciao 3"
    #ratio.Sumw2()
    ratio.GetYaxis().SetTitle("Data / Bkg")
    ratio.GetYaxis().SetNdivisions(503)
    ratio.GetXaxis().SetLabelFont(42)
    ratio.GetYaxis().SetLabelFont(42)
    ratio.GetXaxis().SetTitleFont(42)
    ratio.GetYaxis().SetTitleFont(42)
    ratio.GetXaxis().SetTitleOffset(1.1)
    ratio.GetYaxis().SetTitleOffset(0.35)
    ratio.GetXaxis().SetLabelSize(0.15)
    ratio.GetYaxis().SetLabelSize(0.15)
    ratio.GetXaxis().SetTitleSize(0.16)
    ratio.GetYaxis().SetTitleSize(0.16)
    ratio.GetYaxis().SetRangeUser(0.5,1.5)
    ratio.GetXaxis().SetTitle("BDT_"+region_)
    ratio.GetXaxis().SetLabelOffset(0.04)
    ratio.GetYaxis().SetLabelOffset(0.01)

    c1.cd()
    c1.Update()
    ROOT.TGaxis.SetMaxDigits(3)
    c1.RedrawAxis()
#    c1.GetFrame().Draw()
#    fout_name = "prova/"+outfile
    c1.SaveAs("Stack_h1D/"+canvasname+".pdf")
    c1.SaveAs("Stack_h1D/"+canvasname+".png")
    fdata.Close()
    i=0
    for s in samples_:
        infile[i].Close()
        i+=1
    del histo
    del tmp 
    del h
    del hsig 
    del hratio
    del c1


stack = False # True #
if(stack):
    for lep in leptons:
        njmt="2j1t"
        code_tag="3838"
        region="cr"
        for syst in systematics:
#            stack_h1D(njmt, region, syst, samples_stack, code_tag, lep)
            print "ok"
        njmt="3j1t"
        code_tag="3838"
        region="cr"
        for syst in systematics:
#            stack_h1D(njmt, region, syst, samples_stack, code_tag, lep)
            print "ok"
        njmt="3j2t"
        code_tag="3838"
        region="cr"
        for syst in systematics:
#            stack_h1D(njmt, region, syst, samples_stack, code_tag, lep)
            print "non ancora incluso", njmt
        njmt="2j1t"
        code_tag="3838"
        region="sr"
        for syst in systematics:
            stack_h1D(njmt, region, syst, samples_stack, code_tag, lep)
            print "ok"
        njmt="3j1t"
        code_tag="3838"
        region="sr"
        for syst in systematics:
#            stack_h1D(njmt, region, syst, samples_stack, code_tag, lep)
            print "ok"



'''
def DDQCDMu(inpath_, outpath_, histoname, syst_, samples_, cut_tag_, code_tag_, lep_):
    index = samples_.index(samplesDictionary["TT_sd"])
#    index1 = samples_.index(samplesDictionary["WJets"])
    samples_[index:index+1]=[]
 #   samples_[index1:index1+1]=[]
    histo = []
    tmp = ROOT.TH1F()
    h = ROOT.TH1F()
    hsig =  TH1F()
    if cut_tag_!="":
        histoname += "_"+cut_tag_
    if code_tag!="":
        histoname += "_"+code_tag_
    infile =[]
    for s in samples_:
         if not s.leglabel=="QCD":
              if(syst_==""):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+".root"
                   infile.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
              elif(s.leglabel=="tW" and (syst=="pdf_totalUp" or syst=="pdf_totalDown")):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infile.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              else:
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infile.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso_"+syst_+".root"))

    #Adding data file
    fdata = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/Data_"+str(lep_).strip('[]')+"antiiso.root")
    hdata = fdata.Get(histoname)
    i=0
    for inf in infile:
        inf.cd()
        print "opening file: ", inf.GetName()
        tmp = inf.Get(histoname)
        tmp.SetOption("HIST SAME")
        hdata.Add(tmp, -1)
        print "l'integrale di DDQCD: ", hdata.Integral()
        tmp.Reset("ICES")
        i+=1
    if(syst_==""):
         fmcqcd = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/QCDMuPt20toInf_"+str(lep_).strip('[]')+".root")
         print "file", fmcqcd.GetName()
    elif(syst=="pdf_totalUp" or syst=="pdf_totalDown"):
         fmcqcd = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/QCDMuPt20toInf_"+str(lep_).strip('[]')+".root")
    else:
         fmcqcd = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/QCDMuPt20toInf_"+str(lep_).strip('[]')+"_"+syst_+".root")
    h = fmcqcd.Get(histoname)
    if("2j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_L_2p5"):
         hdata.Scale(1.15*h.Integral()/hdata.Integral())
    elif("2j1t" in histoname and cut_tag =="mtw_G_50"):
         hdata.Scale(0.98*h.Integral()/hdata.Integral())
    elif("2j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_G_2p5"):
         hdata.Scale(0.53*h.Integral()/hdata.Integral())
    elif("3j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_L_2p5"):
         hdata.Scale(0.95*h.Integral()/hdata.Integral())
    elif("3j1t" in histoname and cut_tag =="mtw_G_50"):
         hdata.Scale(1.42*h.Integral()/hdata.Integral())
    elif("3j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_G_2p5"):
         hdata.Scale(0.70*h.Integral()/hdata.Integral())
    elif("3j2t" in histoname):
         hdata.Scale(h.Integral()/hdata.Integral())
    else:
         hdata.Scale(1.*h.Integral()/hdata.Integral())
    print "l'integrale di DDQCD: ", hdata.Integral()
    fout = TFile.Open(outfile, "UPDATE")
    hdata.Write()
    fdata.Close()
    i=0
    for inf in infile:
        inf.Close()
        i+=1
    fmcqcd.Close()
    samples_[index:index]=[samplesDictionary["TT_sd"]]
#    samples_[index1:index1]=[samplesDictionary["WJets"]]

def DDQCDEle(inpath_, outpath_, histoname, syst_, samples_, cut_tag_, code_tag_, lep_):
    index = samples_.index(samplesDictionary["TT_sd"])
    samples_[index:index+1]=[]
    histo = []
    tmp = ROOT.TH1F()
    h = ROOT.TH1F()
    hsig =  TH1F()
    if cut_tag_!="":
        histoname += "_"+cut_tag_
    if code_tag!="":
        histoname += "_"+code_tag_
    infileanti = []
    infileiso = []
    for s in samples_:
         if not s.leglabel=="QCD":
              if(syst_==""):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              elif((s.leglabel=="tW") and (syst=="pdf_totalUp" or syst=="pdf_totalDown")):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              elif((s.leglabel=="t, t-ch" or s.leglabel=="t, t-ch_sd") and (syst=="pdf_totalUp" or syst=="pdf_totalDown" or syst=="q2Up" or syst=="q2Down" or syst=="jerUp" or syst=="jerDown")):
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso.root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+".root"))
              else:
                   outfile=outpath_+"/"+str(lep_).strip('[]')+"/DDQCD_"+str(lep_).strip('[]')+"_"+syst_+".root"
                   infileanti.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/"+s.label+"_"+str(lep_).strip('[]')+"antiiso_"+syst_+".root"))
                   infileiso.append(TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/"+s.label+"_"+str(lep_).strip('[]')+"_"+syst_+".root"))

    #Adding data file
    fdataanti = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"antiiso/Data_"+str(lep_).strip('[]')+"antiiso.root")
    print inpath_+"/"+str(lep_).strip('[]')+"antiiso/Data_"+str(lep_).strip('[]')+"antiiso.root"
    hdataanti = (TH1F)(fdataanti.Get(histoname))
    sumMCanti = hdataanti.Clone()
    sumMCanti.Reset("ICES")
    print "Integrale Data anti iso:", hdataanti.Integral()
    fdataiso = TFile.Open(inpath_+"/"+str(lep_).strip('[]')+"/Data_"+str(lep_).strip('[]')+".root")
    hdataiso = (TH1F)(fdataiso.Get(histoname))
    print "Integrale Data iso:", hdataiso.Integral()
    for inf in infileanti: 
        inf.cd()
        print "opening file: ", inf.GetName()
        tmp = (TH1F)(inf.Get(histoname))
        tmp.SetOption("HIST SAME")
        sumMCanti.Add(tmp)
        print "l'integrale di sumMCantiiso: ", sumMCanti.Integral()
        print "Integrale MC(200,Inf):" , sumMCanti.Integral(hdataanti.FindBin(200),hdataanti.GetNbinsX()+1)
        tmp.Reset("ICES")
    scalefactor = 1.
    hdataanti.Add(sumMCanti, -scalefactor)
    for inf in infileiso:
        inf.cd()
        print "opening file: ", inf.GetName()
        tmp = (TH1F)(inf.Get(histoname))
        tmp.SetOption("HIST SAME")
        hdataiso.Add(tmp, -1)
        print "l'integrale di Dati-MC iso: ", hdataiso.Integral()
        tmp.Reset("ICES")
    if hdataiso.Integral()<0: norm=1.
    else: norm=hdataiso.Integral()
    if("2j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_L_2p5"):
         hdataanti.Scale(1.15*norm/hdataanti.Integral())
    elif("2j1t" in histoname and cut_tag =="mtw_G_50"):
         hdataanti.Scale(0.75*norm/hdataanti.Integral())
    elif("2j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_G_2p5"):
         hdataanti.Scale(2*norm/hdataanti.Integral())
    elif("3j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_L_2p5"):
         hdataanti.Scale(0.95*norm/hdataanti.Integral())
    elif("3j1t" in histoname and cut_tag =="mtw_G_50"):
         hdataanti.Scale(norm/hdataanti.Integral())
    elif("3j1t" in histoname and cut_tag =="mtw_G_50_AND_etajprime_G_2p5"):
         hdataanti.Scale(norm/hdataanti.Integral())
    elif("3j2t" in histoname):
         hdataanti.Scale(norm/hdataanti.Integral())
    else:
         hdataanti.Scale(0.85*norm/hdataanti.Integral())
    print "l'integrale di DDQCD: ", hdataanti.Integral()
    fout = TFile.Open(outfile, "UPDATE")
    hdataanti.Write()
    fdataanti.Close()
    fdataiso.Close()
    i=0
    for s in samples_:
         if not s.leglabel=="QCD":
              infileanti[i].Close()
              infileiso[i].Close()
         i+=1
    samples_[index:index]=[samplesDictionary["TT_sd"]]
'''
