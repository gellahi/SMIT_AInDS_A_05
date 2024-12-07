myDict={'a': 1, 'b': 2, 'c': 3}
reverseDict={}
for x,y in myDict.items():
    reverseDict[y]=x
    
print(reverseDict)