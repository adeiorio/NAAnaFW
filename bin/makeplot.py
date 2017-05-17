import os, commands
from variabile import variabile 
#from taglio import taglio
from Analysis.NAAnaFW.MakePlot.samples.VJets import *
from Analysis.NAAnaFW.MakePlot.samples.SingleTop import *
from Analysis.NAAnaFW.MakePlot.samples.TT import *
from Analysis.NAAnaFW.MakePlot.samples.VV import *
from Analysis.NAAnaFW.MakePlot.samples.toPlot import samples as samplesDictionary
import optparse
from ROOT import * 
#definizioni funzioni 
def makeplot(canale, variabile, macro, sigma, lumi, njmt, syst):
    os.system("root -l -b -q \'"+str(macro)+"(\""+str(canale)+"\","+str(variabile)+","+str(sigma)+","+str(lumi)+",\""+str(njmt)+"\",\""+str(syst)+"\")\'")

#def makestack(macro, variabile, njmt, syst):
 #    os.system("root -l -b -q \'"+str(macro)+"("+str(variabile)+",\""+str(njmt)+"\",\""+str(syst)+"\")\'")

#def makecut(macro, variabile, njmt, taglio1, taglio2):
 #    os.system("root -l -b -q \'"+str(macro)+"("+str(variabile)+",\""+str(njmt)+"\",\""+str(taglio1)+"\",\""+str(taglio2)+"\")\'")

def makelumi(macro, channel, lumi, sigma):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\","+str(lumi)+","+str(sigma)+")\'")

def rmfile(pathfile):
    os.system("rm "+str(pathfile))

def rmdir(pathdir):
    os.system("rm -rf"+str(pathdir))
 
def makestack(njmt, variabile, syst, samples):
    histo = []
    components = []
    tmp = ROOT.TH1F()
    h = ROOT.TH1F()
    hsig =  TH1F()
    stack = ROOT.THStack("Stack_"+njmt+"_"+variabile._name, variabile._name)
    signal=False
    infile =[]
    for s in samples:
        if s.leglabel=="t, t-ch_sd": signal=True
        for comp in s.components:
            if(syst==""):
                outfile="Stack_muon.root"
                infile.append(TFile.Open("Plot/"+comp.label+"_muon.root"))
            else:
                outfile="Stack"+syst+"_muon.root"
                infile.append(TFile.Open("Plot/"+comp.label+syst+"_muon.root"))
    i=0
    for s in samples:
        for comp in s.components:
            print "component: ", comp.label
            infile[i].cd()
            print "opening file: ", infile[i].GetName()
            tmp = (TH1F)(infile[i].Get("h"+njmt+"_"+variabile._name))
            tmp.SetOption("HIST SAME")
            tmp.SetTitle(comp.label)
            tmp.SetFillColor(comp.color)
            tmp.SetLineColor(kBlack)
            if(i==0): 
                h=tmp.Clone("h")
            else: 
                h.Add(tmp)
            tmp.Reset("ICES")
            i+=1
        h.SetOption("HIST")

        h.SetLineColor(kBlack)
        h.SetTitle(s.leglabel)
        h.SetName(s.leglabel)
        h.SetFillColor(s.color)
        histo.append(h.Clone(s.leglabel))
        h.Reset("ICES")

    for hist in histo:
        print "hname ", hist.GetName()
        if(signal): 
            if (hist.GetName())=="t, t-ch_sd":
                hsig=hist.Clone("t, t-ch_sd")
                hsig.SetName("t, t-ch_sd")
                hsig.SetTitle("t, t-ch_sd")
            else:
                stack.Add(hist)
        else:
            stack.Add(hist)

    #Adding data file
    fdata = TFile.Open("trees/trees_Data_muon.root")
    treename = "events"+njmt
    histoname = "Data"
    hdata = TH1F(histoname, histoname, variabile._nbins, variabile._xmin, variabile._xmax)
    fdata.Get(treename).Project(histoname, variabile._name, variabile._taglio)
    hdata.SetLineColor(kBlack)
    hdata.SetMarkerStyle(20)
    hdata.SetMarkerSize(0.9)
    c1 = ROOT.TCanvas("Can_Stack"+njmt+"_"+variabile._name,"c1",50,50,700,600)
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
    stack.Draw()
    hdata.Draw("eSAMEpx0")
    if(signal): 
        hsig.SetLineStyle(9)
        hsig.SetLineColor(kBlue)
        hsig.SetLineWidth(3)
        hsig.SetFillColor(0)
        hsig.Scale(1000)
        hsig.Draw("SAME")
    gPad.BuildLegend(0.75,0.35,0.95,0.95,"")
    fout = TFile.Open("Stack/"+outfile, "UPDATE")
    c1.Write()
#fine makestack


usage = 'python makeplot.py'
parser = optparse.OptionParser(usage)
parser.add_option('-p', '--plot', dest='plot', default = False, action='store_true', help='Default dont make all the plots')
parser.add_option('-l', '--lumi', dest='lumi', default = False, action='store_true', help='Default dont make trees lumi')
parser.add_option('-s', '--stack', dest='stack', default = False, action='store_true', help='Default dont make all the stacks')
parser.add_option('-S', '--syst', dest='syst', type='string', default = 'nosyst', help='Default no systematics')
parser.add_option('-P', '--process', dest='process', type='string', default = 'all', help="samples to add, according to the convention in 'script_rename.py'. Options are: 'All','ST','VJ','VV','QCDMu','QCDEle', or '_'+specific process, e.g. _ST_T_tch to add only the _ST_T_tch. Accepts also multiple processes, separated by comma, e.g. -P ST,_TT,VJ will select the V+jets samples and single top sample sets, as well as the one sample named TT.")
(opt, args) = parser.parse_args()

samplesnames = []
samples = []
if opt.process!="all":
    for sn in (opt.process).split(","): 
        samplesnames.append(sn)
else:
    samplesnames.append("ST_tch")
    samplesnames.append("ST_tch_sd")
    samplesnames.append("ST_sch")
    samplesnames.append("ST_tW")
    samplesnames.append("WJets")
    samplesnames.append("VV")
    samplesnames.append("TT")
    samplesnames.append("DYJets")
    samplesnames.append("QCDMu")

for sn in samplesnames:
#    print "sn is: ",sn
    samples.append(samplesDictionary[sn])


component = []
for s in samples:
 #   print "sample: ", s
  #  print "leglabel: ", s.leglabel
    component.extend(s.components)

variabili_2j1t = [] 
wzero = "w"
variabili_2j1t.append(variabile("etajprime",wzero, 24, 0, 6))
variabili_2j1t.append(variabile("jprimeflavour",wzero, 12, -6, 6))
variabili_2j1t.append(variabile("bjetflavour",wzero, 12, -6, 6))
variabili_2j1t.append(variabile("bjeteta",wzero, 24, 0, 6))
variabili_2j1t.append(variabile("bjetpt",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topMass",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topMt",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topPt",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topY",wzero, 80, -400, 400))
variabili_2j1t.append(variabile("topEta",wzero, 48, -6, 6))
variabili_2j1t.append(variabile("costhetael",wzero, 10, -1, 1))
variabili_2j1t.append(variabile("costhetapol",wzero, 10, -1, 1))
variabili_2j1t.append(variabile("mlb",wzero, 50, 0, 700))
variabili_2j1t.append(variabile("mljprime",wzero, 100, 0, 800))
variabili_2j1t.append(variabile("mljextra",wzero, 100, 0, 800))
variabili_2j1t.append(variabile("mt2w",wzero+"*(nextrajets>2)", 50, 0, 600))
variabili_2j1t.append(variabile("mtw",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("MET",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("mindeltaphi", wzero+"*(nextrajets>0)",20,-5,5))
variabili_2j1t.append(variabile("mindeltaphi20", wzero+"*(nextrajets>0)",20,-5,5))
variabili_2j1t.append(variabile("topMassExtra",wzero+"*(nextrajets>0 && leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_2j1t.append(variabile("topMtExtra",wzero+"*(nextrajets>0 && leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_2j1t.append(variabile("topPtExtra",wzero+"*(nextrajets>0)", 50, 0, 600))
#variabili_2j1t.append(variabile("topEtaExtra",wzero+"*(nextrajets>0)", 48, -6, 6))  questa variabile manca!!!!
variabili_2j1t.append(variabile("topYExtra",wzero+"*(nextrajets>0)", 80, -400, 400))
variabili_2j1t.append(variabile("costhetaelExtra",wzero+"*(nextrajets>0)", 10, -1, 1))
variabili_2j1t.append(variabile("costhetapolExtra",wzero+"*(nextrajets>0)", 10, -1, 1))
variabili_2j1t.append(variabile("leadingextrajetflavour",wzero+"*(nextrajets>0)", 12, -6, 6))
variabili_2j1t.append(variabile("leadingextrajetpt",wzero+"*(nextrajets>0)", 50, 0, 600))
variabili_2j1t.append(variabile("leadingextrajeteta",wzero+"*(nextrajets>0)", 24, 0, 6))
variabili_2j1t.append(variabile("leadingextrajetcsv",wzero+"*(nextrajets>0)", 20, -1, 1))

variabili_3j1t = [] 
wzero = "w"
variabili_3j1t.append(variabile("mtw",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("mt2w",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("etajprime",wzero, 24, 0, 6))
variabili_3j1t.append(variabile("jprimeflavour",wzero, 12, -6, 6))
variabili_3j1t.append(variabile("mlb",wzero, 50, 0, 700))
variabili_3j1t.append(variabile("mljprime",wzero, 100, 0, 800))
variabili_3j1t.append(variabile("mljextra",wzero, 100, 0, 800))
variabili_3j1t.append(variabile("bjetflavour",wzero, 12, -6, 6))
variabili_3j1t.append(variabile("bjeteta",wzero, 24, 0, 6))
variabili_3j1t.append(variabile("bjetpt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topMass",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topMt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topPt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topY",wzero, 80, -400, 400))
variabili_3j1t.append(variabile("topEta",wzero, 48, -6, 6))
variabili_3j1t.append(variabile("costhetael",wzero, 10, -1, 1))
variabili_3j1t.append(variabile("costhetapol",wzero, 10, -1, 1))
variabili_3j1t.append(variabile("topMassExtra",wzero+"*(leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_3j1t.append(variabile("topMtExtra",wzero+"*(leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_3j1t.append(variabile("topPtExtra",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topYExtra",wzero, 80, -400, 400))
variabili_3j1t.append(variabile("topEtaExtra",wzero, 48, -6, 6))
variabili_3j1t.append(variabile("costhetaelExtra",wzero, 10, -1, 1))
variabili_3j1t.append(variabile("costhetapolExtra",wzero, 10, -1, 1))
variabili_3j1t.append(variabile("leadingextrajetflavour",wzero, 12, -6, 6))
variabili_3j1t.append(variabile("leadingextrajetpt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("leadingextrajeteta",wzero, 24, 0, 6))
variabili_3j1t.append(variabile("leadingextrajetcsv",wzero, 20, -1, 1))

variabili_3j2t = [] 
wzero = "w"
variabili_3j2t.append(variabile("mtw",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("mt2w",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("etajprime",wzero, 24, 0, 6))
variabili_3j2t.append(variabile("deltaEtabb",wzero, 24, 0, 6))
variabili_3j2t.append(variabile("mlbleading",wzero, 50, 0, 700))
variabili_3j2t.append(variabile("mlbsecond",wzero, 50, 0, 700))
variabili_3j2t.append(variabile("mljprime",wzero, 100, 0, 800))

variabili_3j2t.append(variabile("topMassLeading",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topMtLeading",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topPtLeading",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topYLeading",wzero, 80, -400, 400))
variabili_3j2t.append(variabile("topEtaLeading",wzero, 48, -6, 6))
variabili_3j2t.append(variabile("costhetaelLeading",wzero, 10, -1, 1))
variabili_3j2t.append(variabile("costhetapolLeading",wzero, 10, -1, 1))

variabili_3j2t.append(variabile("topMassSecond",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topMtSecond",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topPtSecond",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topYSecond",wzero, 80, -400, 400))
variabili_3j2t.append(variabile("topEtaSecond",wzero, 48, -6, 6))
variabili_3j2t.append(variabile("costhetaelSecond",wzero, 10, -1, 1))
variabili_3j2t.append(variabile("costhetapolSecond",wzero, 10, -1, 1))

systematics = []
systematics.append("") #di default per syst="" alla variabile si applica il peso w*w_nominal

if opt.syst!="nosyst":
    systematics.append((opt.systs).split(","))
#    systematics.append("btagUp")  
# systematics.append("btagDown")
 #   systematics.append("mistagUp")
  #  systematics.append("mistagDown")
   # systematics.append("puUp")
   # systematics.append("puDown")
#    systematics.append("lepUp")
 #   systematics.append("lepDown")
'''
#-----------------------------------------------------------
#tagli per la topologia 2 jet 1 tag
tagli1=[]
tagli1.append(taglio("topMt<225","Mt225"))
tagli1.append(taglio("mlb<155","mlb155"))
tagli1.append(taglio("topMt<225 && mlb<155","Mt225mlb155"))

tagli2=[]
tagli2.append(taglio("topMass>0","M0"))
#tagli2.append()
#-----------------------------------------------------------

#-----------------------------------------------------------
#tagli per la topologia 3 jet 2 tag
tagli3=[]
tagli3.append(taglio("topMassSecond<225","MS225"))
tagli3.append(taglio("mt2w<150","mt2w150"))
tagli3.append(taglio("mtw<150","mtw150"))
tagli3.append(taglio("topMassSecond<225 && mt2w<150 && mtw<150", "MS225mt2w150mtw150"))

tagli4=[]
tagli4.append(taglio("topMassLeading>0","M0"))
#tagli2.append()
#-----------------------------------------------------------
'''

lumi=35.8

print "plot option is ", opt.plot

if opt.plot:
    if not os.path.exists("Plot"):
        os.system("mkdir Plot")
    #ciclo sulle variabili
    for comp in component:
        sigma=comp.sigma
        namech=comp.label
        #makelumi("macro_lumi.C",namech, lumi, sigma) #applica la giusta normalizzazione ai treesSmall
        namefile=namech+"_muon.root"
        pathfile = "Plot/"+str(namefile)
        if os.path.exists(pathfile):
            rmfile(pathfile)
        for syst in systematics:
            namefile=namech+"_muon_"+syst+".root"
            pathfile = "Plot/"+str(namefile)
            if os.path.exists(pathfile):
                rmfile(pathfile)
            njmt="_2j1t"
            for var in variabili_2j1t:
                makeplot(namech, var, "macro_plot.C", sigma, lumi, njmt, syst)
            njmt="_3j1t"
            for var2 in variabili_3j1t:
                makeplot(namech, var2, "macro_plot.C", sigma, lumi, njmt, syst)
            njmt="_3j2t"
            for var3 in variabili_3j2t:
                makeplot(namech, var3, "macro_plot.C", sigma, lumi, njmt, syst)

if opt.stack:
    syst="" #per ora gli stack senza sistematiche 
    if not os.path.exists("Stack"):
        os.system("mkdir Stack")
    pathfile = "Stack/Stack_muon.root"
    if os.path.exists(pathfile):
        rmfile(pathfile)
    njmt="_2j1t"
    for var in variabili_2j1t:
        makestack(njmt, var, syst, samples)     
    njmt="_3j1t"
    for var2 in variabili_3j1t:
        makestack(njmt, var2, syst, samples)
    njmt="_3j2t"
    for var3 in variabili_3j2t:
        makestack(njmt, var3, syst, samples)
    
   
if opt.lumi:
    if not os.path.exists("trees_lumi"):
        os.system("mkdir trees_lumi")
    for comp in component:
        makelumi("macro_lumi.C", comp.label, lumi, comp.sigma)

'''     
for var in variabili:
    for taglio1 in tagli1:
        for taglio2 in tagli2:
            njmt="_2j1t_mtwcut"
            makecut("macro_cut.C",var,njmt,taglio1,taglio2)

for var3 in variabili_3j2t:
    for taglio3 in tagli3:
        for taglio4 in tagli4:
            njmt="_3j2t"
            makecut("macro_cut.C",var3,njmt,taglio3,taglio4)   
'''
