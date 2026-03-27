# union and intersection in set

s1 = { 1,2,3,4,5}
s2 = {5,6,7,8,9}

print(s1.union(s2))
print(s1.intersection(s2))
# below both give difference
print(s1-s2) 
print(s1.difference(s2)) 
# does not support print(s1+s2)

print({2,4}.issubset(s1)) #true or false
print(s2.issuperset({1,8}))  #true or false
