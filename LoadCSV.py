#!/usr/bin python
#coding: utf-8
import sys

argvs = sys.argv
if(len(argvs) < 2):
    print "select csv file"
    sys.exit()
flg = False
dict = {}
for line in open(argvs[1], 'r'):
    strs = line[:-1].split(',')
    if (len(strs) < 2):
        flg = False
    if (flg == True):
        if (dict.has_key(strs[4])):
            dict[strs[4]] = dict[strs[4]] + int(strs[5])
        else:
            dict[strs[4]] = int(strs[5])
    if (strs[0] == "明細No."):
        flg = True

f = open("CardHistorySum.csv", 'w')
for key in dict:
    print key + ", " + str(dict[key])
    f.write(key + ", " + str(dict[key]) + "\n")
f.close()
