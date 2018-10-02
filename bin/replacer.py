import os
import optparse 
import os.path
import optparse
import subprocess
import sys
import glob
from utils import *
import commands
import re
#Usage:python script_replacexrd.py -f ./files/renamed/ -o files/final -x xrootd.ba.infn.it -P ST,VV,VJ,TT,SingleMuon 

usage = 'python replacer.py -f filepath -o oldstring -n newstring'
parser = optparse.OptionParser(usage)

parser.add_option('-f', '--filepath',        dest='filepath',  type='string',     default = './MVA/')
parser.add_option('-n', '--new',        dest='new',  type='string',     default = 'trees_lumi', help="new string" )
parser.add_option('-o', '--old',        dest='old',  type='string',     default = 'provatreeslumi', help="old string" )
#parser.add_option('-o', '--outputpath',        dest='outputpath',  type='string',     default = './files/trees/mc/newxrd/')
#parser.add_option('-P', '--process',        dest='process',  type='string',     default = 'all', help="samples to add, according to the convention in 'script_rename.py'. Options are: 'All','ST','VJ','VV','QCDMu','QCDEle', or '_'+specific process, e.g. _ST_T_tch to add only the _ST_T_tch. Accepts also multiple processes, separated by comma, e.g. -P ST,_TT,VJ will select the V+jets samples and single top sample sets, as well as the one sample named TT.")

(opt, args) = parser.parse_args()

filenames = []
filenames.append("cfgST_vs_TT_mtweta")
filenames.append("cfgST_vs_VJ_mtweta")
filenames.append("cfgSTsd_vs_All_sr")
filenames.append("cfgSTsd_vs_ST_sr")
filenames.append("cfgST_vs_TT_mtweta_3j1t")
filenames.append("cfgST_vs_VJ_mtweta_3j1t")
filenames.append("cfgSTsd_vs_All_sr_3j1t")
filenames.append("cfgSTsd_vs_ST_sr_3j1t")
filenames.append("cfgST_vs_TT_3j2t")
'''
filenames.append("cfgST_vs_TT_mtweta_E")
filenames.append("cfgST_vs_VJ_mtweta_E")
filenames.append("cfgSTsd_vs_All_sr_E")
filenames.append("cfgSTsd_vs_ST_sr_E")
filenames.append("cfgST_vs_TT_mtweta_3j1t_E")
filenames.append("cfgST_vs_VJ_mtweta_3j1t_E")
filenames.append("cfgSTsd_vs_All_sr_3j1t_E")
filenames.append("cfgSTsd_vs_ST_sr_3j1t_E")
filenames.append("cfgST_vs_TT_3j2t_E")
'''

#repldict = {'zero':'0', 'one':'1' ,'temp':'bob','garage':'nothing'}
newstring = opt.new
oldstring = opt.old

#oldstring = "muon.root events_3j1t Training"
#newstring = "muon_train.root events_3j1t Training"
#oldstring = "electron.root events_3j1t Training"
#newstring = "electron_train.root events_3j1t Training"

repldict = {oldstring:newstring}
def replfunc(match):
    return repldict[match.group(0)]
def move(fpath):
    os.system("mv "+fpath+'_2.txt ' +fpath+'.txt')

for fn in filenames:
    fpath = opt.filepath+"/"+fn
    regex = re.compile('|'.join(re.escape(x) for x in repldict))
    with open(fpath+'.txt') as fin, open(fpath+'_2.txt','w') as fout:
        for line in fin:
            fout.write(regex.sub(replfunc,line))
    move(fpath)
