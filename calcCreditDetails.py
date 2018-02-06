#!/usr/bin python
#coding: utf-8
import sys

# check argv length
argvs = sys.argv
if(len(argvs) != 2):
    print "usage: python calcCreditDetails.py target.csv"
    print "4th col:dest, 5th col:amount"
    sys.exit()

# loop each csv line
dict = {}
for line in open(argvs[1], 'r'):
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
    f.write(result)
f.close()
