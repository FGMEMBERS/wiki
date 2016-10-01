#!/usr/bin/python
import sys

#read repository-list
repolist=open(sys.argv[1], 'r')
with repolist as f:
    contents = [x.strip('\n') for x in f.readlines()]

def chunks(l, n):
    "Yield successive n-sized chunks from l."
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def aircraftItem (name):
    "concatenates aircraft information"
    sys.stdout.write(''.join(['**',name,'** <br> <img src="https://github.com/FGMEMBERS/',name,'/blob/master/thumbnail.jpg" width="171"> <br> [Development](https://github.com/FGMEMBERS/',name,') <br> [Releases](https://github.com/FGMEMBERS/',name,'/releases)']))
    return

def aircraftItemNonGPL (name):
    "concatenates nonGPL aircraft information"
    sys.stdout.write(''.join(['**',name,'** <br> <img src="https://github.com/FGMEMBERS-NONGPL/',name,'/blob/master/thumbnail.jpg" width="171"> <br> [Development](https://github.com/FGMEMBERS-NONGPL/',name,') <br> [Releases](https://github.com/FGMEMBERS-NONGPL/',name,'/releases)']))
    return

def tableRow(list):
    "Manages the table row output"
    print ('| '),
    try:
        aircraftItem(list[0]),
    except IndexError:
        print (' '),
    print (' | '),
    try:
        aircraftItem(list[1]),
    except IndexError:
        print (' '), 
    print (' | '),
    try:
        aircraftItem(list[2]),
    except IndexError:
        print (' '), 
    print (' | '),
    try:
        aircraftItem(list[3]),
    except IndexError:
        print (' '), 
    print (' | ')
    return

def tableRowNonGPL(list):
    "Manages the table row output, receives list of up-to-four elements"
    print ('| '),
    try:
        aircraftItemNonGPL(list[0]),
    except IndexError:
        print (' '),
    print (' | '),
    try:
        aircraftItemNonGPL(list[1]),
    except IndexError:
        print (' '), 
    print (' | '),
    try:
        aircraftItemNonGPL(list[2]),
    except IndexError:
        print (' '), 
    print (' | '),
    try:
        aircraftItemNonGPL(list[3]),
    except IndexError:
        print (' '), 
    print (' | ')
    return

def table(chunks):
    "Produces the table contents"
    for row in chunks:
        tableRow(row)
    return

def tableNonGPL(chunks):
    "Produces the table contents"
    for row in chunks:
        tableRowNonGPL(row)
    return

def wikiHeader():
    "creates the WikiHeader"
    print("# FGMEMBERS: FligthGear Aircrafts Available")
    print("|               |               |       |       |")
    print("| -------------  |-------------| -----| -----|")
    return

def wikiHeaderNonGPL():
    "creates the WikiHeader"
    print("# FGMEMBERS-NONGPL: FligthGear Non GPL Aircrafts Available")
    print("|               |               |       |       |")
    print("| -------------  |-------------| -----| -----|")
    return

def wikiEnd():
   "creates the wikiClose"
   print(" ")
   print("***")
   print(" ")
   return

def mainGPL(acftList):
  "outputs list of GPL"
  #Create the aircraftList as chunks of 4
  acft=list(chunks(acftList,4))
  wikiHeader()
  table(acft)
  wikiEnd()
  return

def mainNonGPL(acftList):
  "outputs list of NonGPL"
  #Create the aircraftList as chunks of 4
  acft=list(chunks(acftList,4))
  wikiHeaderNonGPL()
  tableNonGPL(acft)
  wikiEnd()
  return

mainGPL(contents)
#mainNonGPL(contents)

