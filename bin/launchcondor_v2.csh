set ORES="$EOSSPACE/it_Feb19"
set TREES="$EOSSPACE/it_Feb19/trees"

#python new_singletop_condor.py --t3batch -f files/pisanew/renamed/ -P SingleMuon -o $ORES/ -t $TREES/   -S 4 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c muon &
python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c muon &
#python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c muon &

#python new_singletop_condor.py --t3batch -f files/pisanew/renamed/ -P SingleElectron -o $ORES/ -t $TREES/   -S 4 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c electron &
python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c electron &
#python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c electron &

#python new_singletop_condor.py --t3batch -f files/pisanew/renamed/ -P SingleMuon,SingleElectron -o $ORES/ -t $TREES/   -S 4 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c muonantiiso &

#electronantiiso
#python new_singletop_condor.py --t3batch -f files/pisanew/renamed/ -P SingleMuon,SingleElectron -o $ORES/ -t $TREES/   -S 4 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P TT -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P VV -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
python new_singletop_condor.py --t3batch -f files/final/ -P SystsTop -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_p_sd -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P ST_sd -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P VJ -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &
#python new_singletop_condor.py --t3batch -f files/final/ -P WJets_ext -o $ORES/ -t $TREES/   -S 2 -c electronantiiso &



