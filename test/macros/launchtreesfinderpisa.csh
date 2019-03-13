#cd $HOME
cd ../../../../../../CMSSW_8_0_26_patch1/src/
cmsenv
cd -

#python treesFinder.py -g gfal -F txt -f samples_edmntuple_mc_full_Summer16.tex -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mc/ -p /cms/store/user/oiorio/SingleTop/2017/July/13July/ -V 2 > & mcfinderpisa.log &


#python treesFinder.py -g gfal -F txt -f samples_data_mu_pt1_ReReReco_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/datamu/ -D true -p /cms/store/user/oiorio/SingleTop/2017/Julsy/13July/SingleMuon/ -V 2 > & datafinderpisamu1.log &

#python treesFinder.py -g gfal -F txt -f samples_data_mu_pt2_ReReReco_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/datamu/ -D true -p /cms/store/user/oiorio/SingleTop/2017/Julsy/13July/SingleMuon/ -V 2 > & datafinderpisamu2.log &

#python treesFinder.py -g gfal -F txt -f samples_data_ele_ReReReco_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/dataele/ -D true -p /cms/store/user/oiorio/SingleTop/2017/Julsy/13July/SingleElectron/ -V 2 > & datafinderpisael.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tch_sd_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsd/ -p /cms/store/user/oiorio/SingleTop/2017/Juls/25July/ -V 2 > & datafinderpisatchsd.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tch_sd_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsd_reshape_improv/ -p /cms/store/user/adeiorio/SingleTop/trees/2018/Jan/30Jan -V 2 > & datafinderpisatchpsd.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tch_sd_5FS_decay.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsd_5FS_decay/ -p /cms/store/user/adeiorio/SingleTop/trees/2018/Jan/24Jan/decay -V 2 > & datafinderpisatchsd_d_5FS.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tch_sd_5FS_prod.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsd_5FS_prod/ -p /cms/store/user/adeiorio/SingleTop/trees/2018/Jan/24Jan/prod -V 2 > & datafinderpisatchpsd_5FS.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tt_sd_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsd/  -p /cms/store/user/oiorio/SingleTop/2017/Juls/25July/ -V 2 > & datafinderpisattsd.log &


#python treesFinder.py -g gfal -F txt -f edmntupples_syst_mc.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsyst/ -p /cms/store/user/oiorio/SingleTop/2017/July/26uly/ -V 2 > & datafinderpisasyst.log &
#python treesFinder.py -g gfal -F txt -f edmntupples_syst_one_mc.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsyst/ -p /cms/store/user/oiorio/SingleTop/2017/July/26uly/ -V 2 > & datafinderpisasyst.log &


#python treesFinder.py -g gfal -F txt -f samples_mc_edmntuples_sd_loc_Summer16.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mcsd/ -p /cms/store/user/oiorio/SingleTop/2017/June/17June/ -V 2 > & mcfinderpisasdv2.log &
#Scommenta dopo

#python treesFinder.py -g gfal -F txt -f ../samples_edmntuple_mc_full_Summer16.tex -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/mc_full/ -p /cms/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/ -V 2 > & datafinderpisamc_full.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tch_sd_5FS_decay.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/ST_sd -p /cms/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/ -V 2 > & datafinderpisaST_sd_decay.log &

#python treesFinder.py -g gfal -F txt -f ../samples_mc_edmntuples_tch_sd_5FS_prod.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/ST_sd -p /cms/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/ -V 2 > & datafinderpisaST_sd_prod.log &

#python treesFinder.py -g gfal -F txt -f ../edmntupples_syst_mc.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/syst_mc/ -p /cms/store/user/adeiorio/SingleTop/trees/2018/Apr/4Apr/ -V 2 > & datafinderpisasyst_mc.log &

python treesFinder.py -g gfal -F txt -f ../edmntupleST_tch_PSQ2_fixed.txt -s stormfe1.pi.infn.it:8443/srm/managerv2 -x cms-xrd-global.cern.ch -o files/syst_mc/ -p /cms//store/user/adeiorio/SingleTop/trees/2019/Mar/09Mar/ -V 2 > & ST_psq2FIX_mc.log &


