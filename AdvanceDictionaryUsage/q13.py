myDict={'z': 1, 'a': 2, 'c': 3}
keysList=list(myDict.keys())
keysList.sort()

sortedDict={}
for x in keysList:
    sortedDict[x]=myDict[x]

print(sortedDict)