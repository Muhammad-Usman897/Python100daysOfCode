# ----------- Sets method in python ------------
# ......... UNION ..........
s1={1,3,5,7}
s2={2,4,5}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

# ......... INTERSECTION ..........
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
cities2={'Tokyo', 'Pesahawr', 'Delhi', 'Quetta'}
print(cities.intersection(cities2))
cities.intersection_update(cities2)
print(cities)

# ......... SYMETERIC DIFFERENCE .......... AUB - AnB
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
cities2={'Tokyo', 'Pesahawr', 'Delhi', 'Quetta'}
print(cities.symmetric_difference(cities2))
cities.symmetric_difference_update(cities2)
print(cities)


# ......... DIFFERENCE .......... A - B
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
cities2={'Tokyo', 'Pesahawr', 'Delhi', 'Quetta'}
print(cities.difference(cities2))
cities.difference_update(cities2)
print(cities)


# ......... isdisjoint .......... 
cities={'Tokyo2', 'Lahore', 'Karachi', 'Quetta2'}
cities2={'Tokyo', 'Pesahawr', 'Delhi', 'Quetta'}
print(cities.isdisjoint(cities2))


# ......... issuperset .......... 
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
cities2={'Tokyo', 'Quetta'}
cities3={'Tokyo', 'Lahore', 'Karachi'}
print(cities.issuperset(cities2))
print(cities3.issubset(cities))


# ......... add() ............
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
cities.add('Rahim yar khan')
print(cities)

# ......... remove(x) / discard()............
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
# cities.remove('Rahim yar khan') #through error
print(cities)
cities.discard('Rahim yar khan')
print(cities)

# ......... pop([i])............
cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
item=cities.pop() #randomly pop 
print(cities)
print(item)


# cities={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
# del cities #delete entire set
# print(cities)


cities5={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
cities5.clear()  #clear the items form the set
print(cities5)


cities5={'Tokyo', 'Lahore', 'Karachi', 'Quetta'}
if "Tokyo" in cities5:
    print('Yes')
else:
    print('No')