a={"A+" : 4.5, "A" : 4.0, "B+" : 3.5}
a["B-"] = 3.5
print(a)
print(a["A"])
a['test']='abcd'
print(a)
del a["B+"]
print(a)
print(a.keys())
print(a.values())
print(list(a.keys()))
print(list(a.items()))
print(4.5 in a)
print("A" in a)