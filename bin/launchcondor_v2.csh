set ORES="$EOSSPACE/it_Mar19/files_11Mar"
set TREES="$EOSSPACE/it_Mar19/files_11Mar/trees"

#nohup python new_singletop_condor.py --t3batch -f files/final/ -P SingleMuon -o $ORES/ -t $TREES/ -S 4 -c muon -d DATA
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c muon &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c muon &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c muon &
nohup python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c muon 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c muon 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c muon 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c muon &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c muon 

#nohup python new_singletop_condor.py --t3batch -f files/final/ -P SingleElectron -o $ORES/ -t $TREES/  -S 2 -c electron -d DATA
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c electron &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c electron &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c electron &
nohup python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c electron 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c electron 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c electron 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c electron &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c electron 

#nohup python new_singletop_condor.py --t3batch -f files/final/ -P SingleMuon -o $ORES/ -t $TREES/   -S 4 -c muonantiiso -d DATA
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
nohup python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c muonantiiso
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c muonantiiso
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c muonantiiso 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c muonantiiso

#electronantiiso
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P SingleElectron -o $ORES/ -t $TREES/ -S 2 -c electronantiiso  -d DATA
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
nohup python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c electronantiiso 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c electronantiiso 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c electronantiiso 
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#nohup python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c electronantiiso 



