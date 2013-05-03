#/bin/
# encoding = utf-8

dict = {}

f = open("CardHistorySum.csv", 'r')
for line in f:
    strs = line.split(',')
    if (dict.has_key(strs[0])):
        dict[strs[0]] = dict[strs[0]] + int(strs[1])
    else:
        dict[strs[0]] = int(strs[1])
f.close()

f = open("CardHistorySum.csv", 'w')
for key in dict:
    print key + ", " + str(dict[key])
    f.write(key + ", " + str(dict[key]) + "\n")
f.close()
