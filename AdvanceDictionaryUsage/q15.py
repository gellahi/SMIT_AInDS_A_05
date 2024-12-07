dict1={'z': 1, 'a': 2, 'c': 3}
dict2={'a': 2,'z': 1, 'c': 3}

NotFound=False
if len(dict1)==len(dict2):
    for x,y in dict1.items():
        if x not in dict2.keys() or y not in dict2.values():
            NotFound=True
    if NotFound==False:
        print("Identical")
    else:
        print("Not Identical")
else:
    print("Not Identical")
    