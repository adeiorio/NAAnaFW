from utils import *

TTbar = sample()
TTbar.files = outlist (d,"TT")
#TTbar.files = TTbar.files[:1]
TTbar.jpref = jetLabel 
TTbar.jp = jetLabel 
TTbar.skimEff = 1.
TTbar.sigma = 831.76
TTbar.color = ROOT.kOrange
TTbar.style = 1
TTbar.fill = 1001
TTbar.leglabel = "t#bar{t}"
TTbar.label = "TT"

TT = sample()
TT.leglabel = "t#bar{t}"
TT.color = ROOT.kOrange
TT.components = [TTbar]
