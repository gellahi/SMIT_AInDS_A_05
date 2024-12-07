dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4} 

dict3={}
for x,y in dict1.items():
    dict3[x]=y
for x,y in dict2.items():
    dict3[x]=y
    
print(dict3)