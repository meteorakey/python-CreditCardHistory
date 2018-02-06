#!/usr/bin python
#coding: utf-8
import sys

argvs = sys.argv
flg = False
dict = {}

# check argv length
if(len(argvs) != 2):
    print "usage: python calcCreditDetails.py target.csv"
    print "4th col:dest, 5th col:amount"
    sys.exit()

# loop each csv line
for line in open(argvs[1], 'r'):
    strs = line[:-1].split(',')
    if (dict.has_key(strs[4])):
        dict[strs[4]] = dict[strs[4]] + int(strs[5])
    else:
        dict[strs[4]] = int(strs[5])

# output result data
f = open("./result.csv", "w")
for key in dict:
    result = key + ",  " + str(dict[key])
    print result
    f.write(result)
f.close()
