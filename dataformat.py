# upwork project

'''
    This is a very simple job where I need someone to clean up the data formatting in a collection of 2,639 files. The files are in Markdown format (.md) which is just simple text.

    The "fonts:" section of the file needs to be reformatted from this...

    fonts:
      - 'Proxima Nova'
      - Grad

    To this...

    fonts:
      - proxima-nova
      - grad

    1) Remove all quotes from any font names.
    2) Change all uppercase letters to lowercase.
    3) Replace all spaces with hyphens.
'''

import sys
import glob

def dataformat(filename):
    lines = open(filename, 'r').readlines()
    i = 0
    for line in lines:
        #print(line[:4])
        if(line[:4]) == "  - ":
            line = line.lower()
            modifiedLine = line[:4] + line[4:].replace(" ","-").replace("'","")
            #print(modifiedLine)
            lines[i] = modifiedLine
        i += 1

    '''
    for line in lines:
        print(line)
    '''

    out = open("./site-of-the-day_test/" + filename.split("/")[2], 'w+')
    out.writelines(lines)
    out.close()

# ======== main ===========
mdfilepattern = r"./site-of-the-day/*.md"
filelist = glob.glob(mdfilepattern)

for afile in filelist:
    #print(afile[18:])
    dataformat(afile)
