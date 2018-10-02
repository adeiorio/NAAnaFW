import os, commands

repo_0 = "/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/WToLNu_0J_13TeV-amcatnloFXFX-pythia8/80xV2_WToLNu_0J_13TeV-amcatnloFXFX-pythia8/180404_163149/0000/"
repo_1 = "/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/WToLNu_1J_13TeV-amcatnloFXFX-pythia8/80xV2_WToLNu_1J_13TeV-amcatnloFXFX-pythia8/180404_163202/0000/"
repo_2 = "/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/WToLNu_2J_13TeV-amcatnloFXFX-pythia8/80xV2_WToLNu_2J_13TeV-amcatnloFXFX-pythia8/180404_163216/0000/"
#root://cms-xrd-global.cern.ch/

dest_path = "."
#xrdcp root://xrootd-cms.infn.it//
for var in range(1,130):
    os.system("xrdcp root://cms-xrd-global.cern.ch/"+repo_0+"/treesTTJets_"+var+".root "+dest_path)
    print "xrdcp root://cms-xrd-global.cern.ch/"+repo_0+"/treesTTJets_"+var+" "+dest_path
for var in range(1,123):
    os.system("xrdcp root://cms-xrd-global.cern.ch/"+repo_1+"/treesTTJets_"+var+".root "+dest_path)
    print "xrdcp root://cms-xrd-global.cern.ch/"+repo_1+"/treesTTJets_"+var+" "+dest_path
for var in range(1,139):
    os.system("xrdcp root://cms-xrd-global.cern.ch/"+repo_2+"/treesTTJets_"+var+".root "+dest_path)
    print "xrdcp root://cms-xrd-global.cern.ch/"+repo_2+"/treesTTJets_"+var+" "+dest_path

