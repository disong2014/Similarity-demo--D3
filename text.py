#!/usr/bin/python

import sys
import json

links = []
nodes = []
inputFile = input('Enter the file name you want to convert from(.txt): ')
outputFile = input('Convert to file name (.json): ')
with open(inputFile) as f:
   content = f.readlines()
for idx in range(len(content)):
   arrItem = content[idx].split()
   objLine = {'source':idx+1,'target':0,'value':arrItem[2]}
   links.append(objLine)
   if idx == 0:
      node = {'name':arrItem[0],'type':'exe','group':1,'size':'10k'}
      nodes.append(node)
      node = {'name':arrItem[1],'type':'exe','group':2,'size':'10k'}
      nodes.append(node)
   else:
      node = {'name':arrItem[1],'type':'exe','group':2,'size':'10k'}
      nodes.append(node)
   
ret = {'nodes':nodes,'links':links}
with open(outputFile,'w') as outfile:
   json.dump(ret,outfile)

print ('Export file successfully!')

   

