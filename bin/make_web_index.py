#!/usr/bin/env python
import argparse
import sys
import os
import datetime
import subprocess

now = datetime.datetime.now()

"""
Setting up argument parser
"""

parser = argparse.ArgumentParser(description="the script drils from top to down and plances and index.html file in each directory and than uses firefox to display the pnd/pdf one can use something like python make_web_index -o index.html -p /home/student/Desktop/plots")
parser.add_argument("-p","--topDirectory", help="top directory, one above that contains the pdf/png files")
parser.add_argument("-o", "--outputFilename", default="index.html", help="output file placed in each directory")
parser.add_argument("-v", "--verbosity", default=1, help="output verbosity level")
parser.add_argument("-i", "--info", default='Short description of plots can be added here', help="Plots description", type=str)
args = parser.parse_args()

fileList = []
dirName = []
folderpath = ''

for currentDir, subdirs, files in os.walk(args.topDirectory):
    if args.verbosity == 1:
        print('Current directory: {}'.format(currentDir))
    for f in files:
        if f.endswith('png'):
            folderpath = currentDir
            fileList.append(f)

folderName = (folderpath.split('/')[5])

with open(args.outputFilename, 'w') as outfilename:
    outfilename.write('''<html> <head> <title> Plots from analyses </title> \n''')
    outfilename.write('''<style> html { font-family: sans-serif; } img { border: 0; } a { text-decoration: none; font-weight: bold; } </style>\n''')
    outfilename.write('''<script type="text/x-mathjax-config"> MathJax.Hub.Config({tex2jax: {inlineMath: [["$","$"]]}}); </script>\n''')
    outfilename.write('''<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n''')
    outfilename.write('''</head> <body><h2>Plots from analyses</h2>\n''')
    outfilename.write('''<h3><a href="'''+folderName+'''/'''+args.outputFilename+'''" style="text-decoration:none;">Click here: /'''+folderName+'''</a></h3>\n''')
    outfilename.write('''<p style="font-size:smaller;">\n''')
    outfilename.write(''' '''+args.info+'''\n''')
    outfilename.write('''<p>'''+'''-------------------------------------------------'''+'''</p>\n''')
    outfilename.write('''</p>\n''')
    outfilename.write('''<br><p>''')
    outfilename.write('''Generated at ''' + now.strftime('%A') + ', '+str(now.day)+'. '+now.strftime('%b')+' '+ now.strftime('%Y %H:%M') + now.strftime('%P').upper()+'\n')
    outfilename.write('''</p> </body> </html>\n''')
outfilename.close()

if args.verbosity == 1:
    print('Current dir: {}'.format(args.topDirectory))
    print('Output filename: {}'.format(args.outputFilename))


with open(os.path.join(folderpath, args.outputFilename), 'w') as outfilename:
    outfilename.write('''<html> <head> <title> Plots from analyses </title> \n''')
    outfilename.write('''<style> html { font-family: sans-serif; } img { border: 0; } a { text-decoration: none; font-weight: bold; } </style>\n''')
    outfilename.write('''<script type="text/x-mathjax-config"> MathJax.Hub.Config({tex2jax: {inlineMath: [["$","$"]]}}); </script>\n''')
    outfilename.write('''<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n''')
    outfilename.write('''</head>\n''')
    outfilename.write('''<body>\n''')
    outfilename.write('''<h3>'''+folderName+'''</h3>\n''')
    outfilename.write('''<p><a href="../'''+args.outputFilename+'''">Back to index</a></p>\n''')
    outfilename.write(''' '''+args.info+'''\n''')
    outfilename.write('''<p>'''+'''-------------------------------------------------'''+'''</p>\n''')
    outfilename.write('''<div style="float:none; overflow:auto; width:100%">\n''')
    
    for fileName in fileList:
        outfilename.write('''\t<div style="float:left; font-size:smaller; font-weight:bold;">\n ''')

        PDF = fileName.split('.')[1].replace('png','pdf')
        fileNamePDF = fileName.split('.')[0]+'.'+PDF

        outfilename.write('''\t<a href="#'''+folderName+'''-'''+ fileName.split('.')[0] +'''">&#11015;</a><a href="'''+fileNamePDF+'''"></a> '''+fileNamePDF+''':<br/>\n''')
        outfilename.write('''\t\t<a name="'''+folderName+'''-'''+ fileName.split('.')[0]+ '''"><a href="'''+fileNamePDF+'''">\n''')
        outfilename.write('''\t\t<img src="'''+fileName+'''">\n''')
        outfilename.write('''\t\t</a></a>\n''')
        outfilename.write('''\t</div>\n''')
    
    outfilename.write('''<div style="float:none"><p> Generated at ''' + now.strftime('%A') + ', '+str(now.day)+'. '+now.strftime('%b')+' '+ now.strftime('%Y %H:%M') + now.strftime('%P').upper() + '''</p>\n''')
    outfilename.write('''</body>\n</html>\n</div>''')
outfilename.close()

subprocess.call('firefox '+folderName+'/'+args.outputFilename,shell=True)    

