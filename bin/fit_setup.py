### Decorrelate Q2 syst among the processes
import sys
import os, commands
import shutil
#from samples.toPlot import samples
from Analysis.NAAnaFW.MakePlot.samples.toPlot import samples as samplesDictionary
import optparse
import ROOT
import copy

usage = 'usage: %prog -d histosDir'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dir', dest='path', type='string', default = './Plot', help='Histos folder')
(opt, args) = parser.parse_args()

samplesnames = []
samplesnames.append("ST_tch")
samplesnames.append("ST_tch_sd")
samplesnames.append("ST_tch_p_sd")
samplesnames.append("ST_sch")
samplesnames.append("ST_tW")
samplesnames.append("WJets_ext")
samplesnames.append("VV")
samplesnames.append("TT")
#samplesnames.append("TT_sd")
samplesnames.append("DYJets")
samplesnames.append("DDQCD")

samples = []
for sn in samplesnames:
    samples.append(samplesDictionary[sn])

channels = ["muon", "electron"]
systs = ["q2","psq2", "hdamp"]
vs = ["Up", "Down"]

newsysts = {"q2":["q2TT","q2ST_tch","q2ST_tch_sd", "q2WJets_ext", "q2DYJets", "q2VV"], "psq2":["psq2TT","psq2ST_tch"], "hdamp":["hdampST_tch","hdampTT"]}
systsamples  =  {"q2":["TT","ST_tch","ST_tch_sd", "WJets_ext", "DYJets", "VV"], "psq2":["TT","ST_tch"], "hdamp":["ST_tch","TT"]}
allsysts = ["", "btag", "mistag", "jes", "jer", "pu", "pdf_total"]
newlepSyst = {"lep":["lepMu","lepE"]}
for sy in systs:
    for s in newsysts[sy]:
        allsysts.append(s)
for s in newlepSyst["lep"]:
    allsysts.append(s)

def createSyst(versus, syst, newsyst, systsamp, verbose = True):
    for ch in channels:
        for s in samples:
            if ("QCDMu" in s.label)  and "electron" in ch : continue 
            pathch = opt.path+"/"+ch+"/"

            if s.label == "Data":continue
            src = s.label + "_" + ch + ".root"
            dst =  [s.label + "_" + ch + "_" + nSyst + versus + ".root" for nSyst in newsyst]
#            print dst

            if(verbose):
                for d in dst:
                    print "Copying " + pathch + src + " to "+ pathch + d
    
            [shutil.copyfile(pathch + src, pathch + d) for d in dst]

        for sysa in systsamp:
            s = samplesDictionary[sysa]
            srcSys = s.label + "_" + ch + "_" + syst + versus + ".root"  
            dstSys = s.label + "_" + ch + "_" + syst + s.label + versus + ".root" 
            
            if verbose: print "Copying " + pathch + srcSys + " to "+ pathch + dstSys
            shutil.copyfile(pathch + srcSys, pathch + dstSys)

def createLepSyst(versus, newlepsyst, verbose = True):
    for ch in channels:
        for s in samples:
            if ("QCDMu" in s.label)  and "electron" in ch : continue 
            pathch = opt.path+"/"+ch+"/"

            if s.label == "Data":continue
            src = s.label + "_" + ch + ".root"
            dst =  [s.label + "_" + ch + "_" + nlepSyst + versus + ".root" for nlepSyst in newlepsyst]
#            print dst

            if(verbose):
                for d in dst:
                    print "Copying " + pathch + src + " to "+ pathch + d
    
            [shutil.copyfile(pathch + src, pathch + d) for d in dst]

            if ch == "muon":
                srcSys = s.label + "_" + ch + "_lep" + versus + ".root"  
                dstSys = s.label + "_" + ch + "_lepMu" + versus + ".root" 
            else:
                srcSys = s.label + "_" + ch + "_lep" + versus + ".root"  
                dstSys = s.label + "_" + ch + "_lepE" + versus + ".root" 
            if verbose: print "Copying " + pathch + srcSys + " to "+ pathch + dstSys
            shutil.copyfile(pathch + srcSys, pathch + dstSys)

def invertname(samp_label, syst_, versus):
    for ch in channels:
        pathch = opt.path+"/"+ch+"/"
        srcSys = samp_label + "_" + syst_ + versus + "_" + ch + ".root"  
        dstSys = samp_label + "_" + ch + "_" + syst_ + versus + ".root" 
        shutil.copyfile(pathch + srcSys, pathch + dstSys)
        print "Renaming " + pathch + srcSys + " in " + pathch + dstSys

def rmdircont(namedir):
    os.system("rm " + opt.path + "/" + namedir + "/*.root")
    print "Deleting all previous files from " + opt.path + "/" + namedir + "/"

def copyall():
    for ch in channels:
        pathch = opt.path+"/"+ch+"/"
        pathout = opt.path+"/fit/"
        os.system("cp " + pathch + "*.root " + pathout)  
        print "Copying all root files from " + pathch + " to " + pathout
 
def merge(syst_, versus):
    for ch in channels:
        pathin = opt.path+"/"+ch+"/"
        pathout = opt.path+"/fit/"
        if syst_=="":
            srcST = "ST_tch_sd_" + ch + ".root"
            srcSTp = "ST_tch_p_sd_" + ch + ".root"
            srcTT = "TT_sd_" + ch + ".root"
        else:
            srcST = "ST_tch_sd_" + ch + "_" + syst_ + versus + ".root"
            srcSTp = "ST_tch_p_sd_" + ch + "_" + syst_ + versus + ".root"
            srcTT = "TT_sd_" + ch + "_" + syst_ + versus + ".root"
#        os.system("hadd -f " + pathout + srcST + " " + pathin + srcST + " " + pathin + srcTT + " " + pathin + srcSTp)
        os.system("hadd -f " + pathout + srcST + " " + pathin + srcST + " " + pathin + srcSTp)

def cureNaN(ch, sample, syst_, versus):
    pathin = opt.path+"/"+ch+"/"
    pathout = opt.path+"/fit/"
    os.system("cp " + pathin + sample + "_" + ch + ".root " + pathout + sample + "_" + ch + "_" + syst_ + versus + ".root")
    print "Copying "  + pathin + sample + "_" + ch + ".root" + " to " + pathout + sample + "_" + ch + "_"  + syst_ + versus + ".root"

def bfcopy(ch, sample, syst_, versus):
    path = opt.path+"/fit/"
    os.system("cp " + path + sample + "_" + ch + ".root " + path + sample + "_" + ch + "_" + syst_ + versus + ".root")
    print "Copying "  + path + sample + "_" + ch + ".root" + " to " + path + sample + "_" + ch + "_"  + syst_ + versus + ".root"



def shift(h, ib, shift, slabel, channel, v):
    corr = 1
    if(shift == "Down"): corr = -1
    oh = 0.
    eoh = 0.
   # nhName = ""
    oh = h.GetBinContent(ib)
    eoh = h.GetBinError(ib)
    oh += eoh * corr
    if(oh<0.): # per i WJets ci sono problemi di underflow... questo puo evitarlo
        oh=0
    #print "++ Bin 1: ", h.GetAt(ib)
    #print "++ W Bin 1: ", h.GetBinError(ib)
    nh = copy.deepcopy(h)
    nh.SetAt(oh, ib)
    #print "++ nh Bin 1: ", nh.GetBinContent(ib)
    #print "---- Old name: ",h.GetName()
    if ch == "electron": 
        nhName = h.GetName() + "_mcstat_" + varE[v] + "_" + slabel+"_bin"+str(ib)+"_"+shift
    elif ch == "muon": 
        nhName = h.GetName() + "_mcstat_" + var[v] + "_" + slabel+"_bin"+str(ib)+"_"+shift
    nh.SetName(nhName)
    print "---- New name: ",nh.GetName()
    #nh.GetSumw2().SetAt(X, ib)
    return nh


def makeBinHistos(v, ch):
    for s in samples:
        hfilename = opt.path + "/fit/%s_%s.root" % (s.label,ch)
        hfile = ROOT.TFile(hfilename, "UPDATE")
        print "file ", hfile
        hin = hfile.Get(v)
        if not isinstance(hin, ROOT.TH1):
            raise RuntimeError('Failed to load histogram %s from %s' % (hin, var))
        else:
            mcStat_down = [ shift(hin, ib, "Down", s.label, ch, v) for ib in xrange(1, hin.GetXaxis().GetNbins()+1) ]
            mcStat_up = [ shift(hin, ib, "Up", s.label, ch, v) for ib in xrange(1, hin.GetXaxis().GetNbins()+1) ]
            hfile.cd()
            [nh.Write() for nh in mcStat_down]
            [nh.Write() for nh in mcStat_up]
            hfile.Close()

def getall(d, basepath=""):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
        if key.IsFolder():
            for i in getall(d.Get(kname), basepath+"/"+kname+"/"):
                yield i
        else:
            yield kname, d.Get(kname)

def smoothing(filename,h):
    fin = ROOT.TFile(filename, "UPDATE")
    tmp = ROOT.TH1F()
    fin.cd()
    tmp = fin.Get(h)
    tmp.Smooth(4)
    tmp.Write()
    fin.Close()

def scale(f, shift):
    prev_str = ""
    fin = ROOT.TFile(f,"UPDATE")
    tmp = ROOT.TH1F()
    for k, o in getall(fin):
        #    print o.ClassName(), k
        if(prev_str != k):
            fin.cd()
            tmp = fin.Get(k)
            tmp.Scale(1+shift)
            tmp.Write()
            tmp.Reset("ICES")
        prev_str = k
    fin.Close()

samp = ["ST_tch", "TT"]
syst_name = ["hdamp","psq2"]
for v in vs:
    for sa in samp:
        for sy in syst_name:
            invertname(sa, sy, v)

for v in vs:
    for s in systs:
        createSyst(v, s, newsysts[s], systsamples[s])

for v in vs:
    createLepSyst(v, newlepSyst["lep"])

rmdircont("fit")
copyall()

poorstats = ["DYJets", "VV", "WJets_ext"]
systematics = []
systematics.append("btag")
systematics.append("mistag")
systematics.append("pu")
systematics.append("lepE")
systematics.append("lepMu")
systematics.append("jes")
systematics.append("jer")
systematics.append("q2WJets_ext")
systematics.append("q2ST_tch")
systematics.append("q2ST_tch_sd")
systematics.append("q2TT")
systematics.append("q2DYJets")
systematics.append("q2VV")
systematics.append("psq2TT")
systematics.append("psq2ST_tch")
systematics.append("hdampTT")
systematics.append("hdampST_tch")
systematics.append("pdf_total")
systematics.append("cmvacferr1")
systematics.append("cmvahfstats1")
systematics.append("cmvahfstats2")
systematics.append("cmvalfstats1")
systematics.append("cmvalfstats2")

for ps in poorstats:
    for ch in channels:
        if ch == "muon":
            smoothing(opt.path + "/fit/"+ps+"_"+ch+".root","h_3j2t_BDT_ST_vs_TT_3j2t")
            for v in vs:
                for s in systematics:
                    smoothing(opt.path + "/fit/"+ps+"_"+ch+"_"+s+v+".root","h_3j2t_BDT_ST_vs_TT_3j2t")
        else:
            smoothing(opt.path + "/fit/"+ps+"_"+ch+".root","h_3j2t_BDT_ST_vs_TT_3j2t")
            for v in vs:
                for s in systematics:
                    smoothing(opt.path + "/fit/"+ps+"_"+ch+"_"+s+v+".root","h_3j2t_BDT_ST_vs_TT_3j2t")

merger = False
if(merger):
    for sy in allsysts:
        for v in vs:
            merge(sy, v)

for v in vs:
    for ch in channels:   
        cureNaN(ch, "ST_tW", "pdf_total", v)
        cureNaN(ch, "ST_sch", "pdf_total", v)
    cureNaN("electron", "DDQCD", "pdf_total", v)

cmvasyst=["cmvacferr1", "cmvahfstats1", "cmvahfstats2", "cmvalfstats1", "cmvalfstats2"]
for v in vs:
    for ch in channels:
        for syst in cmvasyst:   
            bfcopy(ch, "ST_tch_sd", syst, v)
#Function to add statistical uncertainties to MC samples
#var = {"h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5":"muon_2j1t_central", "h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5":"muon_2j1t_forward", "h_3j1t_BDT_ST_vs_VJ_mtweta_3j1t_mtw_G_50_AND_etajprime_L_2p5":"muon_3j1t_central", "h_3j1t_BDT_STsd_vs_ST_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5":"muon_3j1t_forward", "h_3j2t_BDT_ST_vs_TT_3j2t":"muon_3j2t"}
#varE = {"h_2j1t_BDT_ST_vs_VJ_mtweta_mtw_G_50_AND_etajprime_L_2p5":"electron_2j1t_central", "h_2j1t_BDT_STsd_vs_ST_sr_mtw_G_50_AND_etajprime_G_2p5":"electron_2j1t_forward", "h_3j1t_BDT_ST_vs_VJ_mtweta_3j1t_mtw_G_50_AND_etajprime_L_2p5":"electron_3j1t_central", "h_3j1t_BDT_STsd_vs_ST_sr_3j1t_mtw_G_50_AND_etajprime_G_2p5":"electron_3j1t_forward", "h_3j2t_BDT_ST_vs_TT_3j2t":"electron_3j2t"}
var = {"h1D_2j1t_cr":"muon_2j1t_central", "h1D_2j1t_sr":"muon_2j1t_forward", "h1D_3j1t_cr":"muon_3j1t_central", "h1D_3j1t_sr":"muon_3j1t_forward", "h_3j2t_BDT_ST_vs_TT_3j2t":"muon_3j2t"}
varE = {"h1D_2j1t_cr":"electron_2j1t_central", "h1D_2j1t_sr":"electron_2j1t_forward", "h1D_3j1t_cr":"electron_3j1t_central", "h1D_3j1t_sr":"electron_3j1t_forward", "h_3j2t_BDT_ST_vs_TT_3j2t":"electron_3j2t"}
#var = {"h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5":"muon_2j1t_central", "h_2j1t_topMass_mtw_G_50_AND_etajprime_G_2p5":"muon_2j1t_forward", "h_3j1t_topMass_mtw_G_50_AND_etajprime_L_2p5":"muon_3j1t_central", "h_3j1t_topMass_mtw_G_50_AND_etajprime_G_2p5":"muon_3j1t_forward", "h_3j2t_topMassLeading":"muon_3j2t"}
#varE = {"h_2j1t_topMass_mtw_G_50_AND_etajprime_L_2p5":"electron_2j1t_central", "h_2j1t_topMass_mtw_G_50_AND_etajprime_G_2p5":"electron_2j1t_forward", "h_3j1t_topMass_mtw_G_50_AND_etajprime_L_2p5":"electron_3j1t_central", "h_3j1t_topMass_mtw_G_50_AND_etajprime_G_2p5":"electron_3j1t_forward", "h_3j2t_topMassLeading":"electron_3j2t"}
for ch in channels:
    if ch == "electron": 
        [makeBinHistos(v,ch) for v in varE.keys()]
    elif ch == "muon": 
        [makeBinHistos(v,ch) for v in var.keys()]

process_to_scale = []
process_to_scale.append("WJets_ext")
channel_to_scale = []
#channel_to_scale.append("muon")
channel_to_scale.append("electron")
for ch in channel_to_scale:
    for ps in process_to_scale:
        print "Scaling the histos of the %s sample" % ps 
        scale(opt.path + "/fit/"+ps+"_"+ch+".root", 0.1)
        for v in vs:
            for s in systematics:
                print "Scaling the histos of the %s%s%s " % (ps, s, v) 
                scale(opt.path + "/fit/"+ps+"_"+ch+"_"+s+v+".root", 0.1)

