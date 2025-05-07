#
l=[2,4,3,2,6]
print(l)
l.append(7)
print(l)
l.reverse()
print(l)
print(l.index(2))

m= l
m[0]=7
print(l)

m= l.copy()
m[1]=3
print(l)

l.insert(1,899)
print(l)

mk=[435,42,65]
l.extend(mk)
print(l)
k=mk+l
print(k)