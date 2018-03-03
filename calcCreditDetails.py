#!/usr/bin python
#coding: utf-8
import sys
import subprocess

# check argv length
argvs = sys.argv
if(len(argvs) != 2):
    print "usage: python calcCreditDetails.py target.csv"
    print "4th col:dest, 5th col:amount"
    sys.exit()

# convert csv utf-8, LF
csv = argvs[1]
_nkf = 'nkf -wd --overwrite ' + csv
subprocess.check_call(_nkf, shell=True) 

# loop each csv line
dict = {}
for line in open(csv, 'r'):
    strs = line[:-1].split(',')
    if (dict.has_key(strs[4])):
        dict[strs[4]] = dict[strs[4]] + int(strs[5])
    else:
        dict[strs[4]] = int(strs[5])

# output result data
f = open("./result.csv", "w")
for k,v in sorted(dict.items()):
    result = str(k) + ",  " + str(v)
    print result
    f.write(result + "\n")
f.close()
