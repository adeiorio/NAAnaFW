import os,commands

def split(macro, channel, lep, ph):
     os.system("root -l -b -q \'"+str(macro)+"(\""+str(channel)+"\",\""+str(lep)+"\",\""+str(ph)+"\")\'")

lepton = ["muon"] #,"electron"
#channel = ["ST_tch"]
channel = ["ST_tch","ST_tch_p_sd","ST_tch_sd","TT"]
phase = ["train","test"]

for lep in lepton:
    for ch in channel:
         os.system("mv trees_lumi/"+lep+"/trees_"+ch+"_"+lep+".root trees_lumi/trees_"+ch+"_"+lep+".root")
         print "mv trees_lumi/"+lep+"/trees_"+ch+"_"+lep+".root trees_lumi/trees_"+ch+"_"+lep+".root"
         for ph in phase:
              split("trees_splitter.C", ch, lep, ph)

os.system("cp trees_lumi/muon/trees_WJets_muon.root trees_lumi/train/trees_WJets_muon_train.root")
