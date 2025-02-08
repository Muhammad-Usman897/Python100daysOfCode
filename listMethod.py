l = [45,11,4,6,9,12,21,11]
print(l)
l.append(34)
l.sort()
l.reverse()
print(l.index(4))
print(l.count(11))

m=l.copy()
m[0]=0

k=l+m;
print(k)

l.extend(m)
print(l)