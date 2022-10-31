# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:44:29 2021

@author: Adm
"""

import os
import sys
import fileinput

print ("Text to search for:")
textToSearch = input( "> " )

print ("Text to replace it with:")
textToReplace = input( "> " )

print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )
#fileToSearch = 'D:\dummy1.txt'

tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()


input( '\n\n Press Enter to exit...' )
    
