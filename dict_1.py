d ={}
print(type(d))

d1 = {1:"first",2:"Second",3:"Third",4:{"l":"qe","b":"sdf"}}
d1[5] = "Fifth"
d1[6] = "Sixth"

print(d1)

print(d1.get(1))

d1.update({7:"Seventh"})
print(d1)
print(d1.keys())
print(d1.items())