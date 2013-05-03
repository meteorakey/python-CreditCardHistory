#!/usr/bin python
# encoding: utf-8
# 引数に指定したディレクトリ内のLifeCardの明細を利用先別に合算
# 第二引数に true を指定すると金額順にソート．それ以外は利用先順
# TODO:明細No.の行が二つあるから上手いこと無視する修正
import os
import sys
import glob

def loadCSV():
    dict = {}
    flg = False

    files = glob.glob(sys.argv[1] + "/lifecard_meisai_*.csv")
    for file in files:
        os.system("nkf -w -Lu --overwrite %s" % file)
        f = open(file, 'r')
        for line in f:
            strs = line[:-1].split(',')
            if (len(strs) < 2):
                flg = False
            elif (flg == True):
                if (dict.has_key(strs[4])):
                    dict[strs[4]] = dict[strs[4]] + int(strs[5])
                else:
                    dict[strs[4]] = int(strs[5])
            elif (strs[0] == "明細No."):
                flg = True

        f.close()
    return dict

def writeCSV(dict, flg):
    f = open("CardHistorySum.csv", 'w')
    if (flg == True):
        for k, v in sorted(dict.items(), key=lambda x:x[1], reverse=True):
            f.write(k + ", " + str(v) + "\n")
    else:
        for k, v in sorted(dict.items()):
            f.write(k + ", " + str(v) + "\n")
    f.close()

if (len(sys.argv) == 3):
    if (sys.argv[2] == "true"):
        print "true"
        writeCSV(loadCSV(), True)
    else:
        print "oshii"
        writeCSV(loadCSV(), False)
else:
    print "false"
    writeCSV(loadCSV(), False)

