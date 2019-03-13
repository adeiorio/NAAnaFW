nohup cmsRun topplusdmTrees_skim_cfg.py isData=False doSynch=False doPreselection=False changeJECs=True channel="tch_psd" maxEvts=-1 outputLabel="trees_T_sd_nopresel.root" sample="file:/afs/cern.ch/work/a/adeiorio/CMSSW_8_0_26_patch1/src/Analysis/NAAnaFW/src/B2GEDMNtuple_121.root" > & T_sd_nopresel.log &
#nohup cmsRun topplusdmTrees_skim_cfg.py isData=False doSynch=False doPreselection=True changeJECs=True channel="tch_sd" maxEvts=-1 outputLabel="trees_sd_presel.root" sample="file:/afs/cern.ch/work/a/adeiorio/CMSSW_8_0_26_patch1/src/Analysis/NAAnaFW/src/B2GEDMNtuple_21.root" > & sd_presel.log &
#o/oiorio/public/xWajid/synch/mc_jecv4/B2GSynchMC.root
#doSynch fa la sincronizzazione
#doPreselection fa la preselezione richiedendo un leptone isolato e almeno un jet  
#doJECs aplica le correzioni all'energia dei jets
