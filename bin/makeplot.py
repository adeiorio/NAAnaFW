import os, commands
from variabile import variabile 
#from taglio import taglio
#import sys
#sys.path.append('../python/MakePlot/samples')
from Analysis.NAAnaFW.MakePlot.samples.VJets import *
from Analysis.NAAnaFW.MakePlot.samples.SingleTop import *
from Analysis.NAAnaFW.MakePlot.samples.TT import *
from Analysis.NAAnaFW.MakePlot.samples.VV import *

#import utils
#print "wj sigma is: ", WJetsToLNu.sigma
#from SingleTop import *

'''
from NAAnaFW.python.MakePlot.samples.VJets import *
from NAAnaFW.python.MakePlot.samples.SingleTop import *
from NAAnaFW.python.MakePlot.samples.TT import *
from NAAnaFW.python.MakePlot.samples.VV import *
'''
#definizioni funzioni 
def makeplot(canale, variabile, macro, sigma, lumi, njmt, syst):
    os.system("root -l -b -q \'"+str(macro)+"(\""+str(canale)+"\","+str(variabile)+","+str(sigma)+","+str(lumi)+",\""+str(njmt)+"\",\""+str(syst)+"\")\'")

def makestack(macro, variabile, njmt, syst):
     os.system("root -l -b -q \'"+str(macro)+"("+str(variabile)+",\""+str(njmt)+"\",\""+str(syst)+"\")\'")

def makecut(macro, variabile, njmt, taglio1, taglio2):
     os.system("root -l -b -q \'"+str(macro)+"("+str(variabile)+",\""+str(njmt)+"\",\""+str(taglio1)+"\",\""+str(taglio2)+"\")\'")

def makelumi(macro, channel, lumi, sigma):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\","+str(lumi)+","+str(sigma)+")\'")

def rmfile(namefile):
    os.system("rm Plot/"+str(namefile))


#uso della funzione
canali=[ST_T_tch,ST_Tbar_tch,DYJetsToLL,TT,WToLNu0J,WToLNu1J,WToLNu2J,ST_T_sch,ST_T_tW,ST_Tbar_tW,WWTo1L1Nu2Q,WWTo2L2Nu,WZTo1L1Nu2Q,WZTo2L2Q,ZZTo2L2Q] #  ,ST_T_tch_sd,ST_Tbar_tch_sd
variabili_2j1t=[] 
wzero ="w"
variabili_2j1t.append(variabile("etajprime",wzero, 24, 0, 6))
variabili_2j1t.append(variabile("jprimeflavour",wzero, 12, -6, 6))
variabili_2j1t.append(variabile("bjetflavour",wzero, 12, -6, 6))
variabili_2j1t.append(variabile("topMass",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topMt",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topPt",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("topY",wzero, 80, -400, 400))
variabili_2j1t.append(variabile("topEta",wzero, 48, -6, 6))
variabili_2j1t.append(variabile("costhetael",wzero, 10, -1, 1))
variabili_2j1t.append(variabile("mlb",wzero, 50, 0, 700))
variabili_2j1t.append(variabile("mljprime",wzero, 100, 0, 1200))
variabili_2j1t.append(variabile("mt2w",wzero+"*(nextrajets>2)", 50, 0, 600))
variabili_2j1t.append(variabile("mtw",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("MET",wzero, 50, 0, 600))
variabili_2j1t.append(variabile("mindeltaphi", wzero+"*(nextrajets>0)",20,-5,5))
variabili_2j1t.append(variabile("mindeltaphi20", wzero+"*(nextrajets>0)",20,-5,5))
variabili_2j1t.append(variabile("topMassExtra",wzero+"*(nextrajets>0 && leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_2j1t.append(variabile("topMtExtra",wzero+"*(nextrajets>0 && leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_2j1t.append(variabile("topPtExtra",wzero+"*(nextrajets>0)", 50, 0, 600))
variabili_2j1t.append(variabile("topYExtra",wzero+"*(nextrajets>0)", 80, 0, 500))
variabili_2j1t.append(variabile("leadingextrajetflavour",wzero+"*(nextrajets>0)", 12, -6, 500))
variabili_2j1t.append(variabile("leadingextrajetpt",wzero+"*(nextrajets>0)", 50, 0, 600))
variabili_2j1t.append(variabile("leadingextrajeteta",wzero+"*(nextrajets>0)", 48, -6, 6))
variabili_2j1t.append(variabile("leadingextrajetcsv",wzero+"*(nextrajets>0)", 20, -1, 1))

variabili_3j1t=[] 
wzero ="w"
variabili_3j1t.append(variabile("mtw",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("mt2w",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("etajprime",wzero, 24, 0, 6))
variabili_3j1t.append(variabile("jprimeflavour",wzero, 12, -6, 6))
variabili_3j1t.append(variabile("mlb",wzero, 50, 0, 700))
variabili_3j1t.append(variabile("mljprime",wzero, 100, 0, 1200))
variabili_3j1t.append(variabile("mljextra",wzero, 100, 0, 1200))
variabili_3j1t.append(variabile("bjetflavour",wzero, 12, -6, 6))
variabili_3j1t.append(variabile("bjeteta",wzero, 48, -6, 6))
variabili_3j1t.append(variabile("bjetpt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topMass",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topMt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topPt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topY",wzero, 80, -400, 400))
variabili_3j1t.append(variabile("topEta",wzero, 48, -6, 6))
variabili_3j1t.append(variabile("costhetael",wzero, 10, -1, 1))
variabili_3j1t.append(variabile("topMassExtra",wzero+"*(leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_3j1t.append(variabile("topMtExtra",wzero+"*(leadingextrajetcsv>0.935)", 50, 0, 600))
variabili_3j1t.append(variabile("topPtExtra",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("topYExtra",wzero, 80, 0, 500))
variabili_3j1t.append(variabile("topEtaExtra",wzero, 48, -6, 6))
variabili_3j1t.append(variabile("costhetaelExtra",wzero, 10, -1, 1))
variabili_3j1t.append(variabile("leadingextrajetflavour",wzero, 12, -6, 500))
variabili_3j1t.append(variabile("leadingextrajetpt",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("leadingextrajeteta",wzero, 48, -6, 6))
variabili_3j1t.append(variabile("leadingextrajetcsv",wzero, 20, -1, 1))
'''
variabili_3j1t.append(variabile("MET",wzero, 50, 0, 600))
variabili_3j1t.append(variabile("mindeltaphi", wzero+"*(nextrajets>0)",20,-5,5))
variabili_3j1t.append(variabile("mindeltaphi20", wzero+"*(nextrajets>0)",20,-5,5))
'''

variabili_3j2t=[] 
wzero ="w"
variabili_3j2t.append(variabile("mtw",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("mt2w",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("etajprime",wzero, 24, 0, 6))
variabili_3j2t.append(variabile("deltaEtabb",wzero, 24, 0, 6))
variabili_3j2t.append(variabile("mlbleading",wzero, 50, 0, 700))
variabili_3j2t.append(variabile("mlbsecond",wzero, 50, 0, 700))
variabili_3j2t.append(variabile("mljprime",wzero, 100, 0, 1200))

variabili_3j2t.append(variabile("topMassLeading",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topMtLeading",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topPtLeading",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topYLeading",wzero, 80, -400, 400))
variabili_3j2t.append(variabile("topEtaLeading",wzero, 48, -6, 6))
variabili_3j2t.append(variabile("costhetaelLeading",wzero, 10, -1, 1))

variabili_3j2t.append(variabile("topMassSecond",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topMtSecond",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topPtSecond",wzero, 50, 0, 600))
variabili_3j2t.append(variabile("topYSecond",wzero, 80, -400, 400))
variabili_3j2t.append(variabile("topEtaSecond",wzero, 48, -6, 6))
variabili_3j2t.append(variabile("costhetaelSecond",wzero, 10, -1, 1))

sistematiche=[]
sistematiche.append("") #di default per syst="" alla variabile su applica il peso w*w_nominal
sistematiche.append("btagUp")
sistematiche.append("btagDown")
sistematiche.append("mistagUp")
sistematiche.append("mistagDown")
sistematiche.append("puUp")
sistematiche.append("puDown")
sistematiche.append("lepUp")
sistematiche.append("lepDown")
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

#ciclo sulle variabili
for ch in canali:
    sigma=ch.sigma
    namech=ch.label
    #makelumi("macro_lumi.C",namech, lumi, sigma) #applica la giusta normalizzazione ai treesSmall
    namefile=namech+"_muon.root"
    rmfile(namefile)
    for syst in sistematiche:
        namefile=namech+"_muon_"+syst+".root"
        rmfile(namefile)
        njmt="_2j1t"
        for var in variabili_2j1t:
            makeplot(namech, var, "macro_plot.C",sigma, lumi, njmt, syst)
        njmt="_3j1t"
        for var2 in variabili_3j1t:
            makeplot(namech, var2, "macro_plot.C",sigma, lumi, njmt, syst)
        njmt="_3j2t"
        for var3 in variabili_3j2t:
            makeplot(namech, var3, "macro_plot.C",sigma, lumi, njmt, syst)
'''     
namefile = "Stack.root"
rmfile(namefile) 
for syst in sistematiche:
    namefile="Stack_"+syst+".root"
    rmfile(namefile)
    njmt="_2j1t_mtwcut"
    for var in variabili:
        makestack("macro_stack.C",var, njmt, syst)
    njmt="_3j2t"
    for var3 in variabili_3j2t:
        makestack("macro_stack.C",var3, njmt, syst)

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
