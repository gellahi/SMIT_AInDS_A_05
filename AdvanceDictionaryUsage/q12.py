tuplesList=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
dictFromList={}

for x in tuplesList:
    dictFromList[x[0]]=x[1]

print(dictFromList)