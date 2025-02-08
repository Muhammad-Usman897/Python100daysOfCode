# ----------------- TUPLES -------------------
# * Tuple are ordered collection of data items
# * They are store multiple items in a single variable and enclosed with a () round brackets
# * Tuples are Immutable 

tuple1=(1,2,3,4,5,6,7)
tuple2=('Muhammad', 'Usman', 'Furqan')
print(type(tuple1), tuple1)
print(type(tuple2), tuple2)

print(tuple1[0])
print(tuple1[1])
print(tuple1[-2])
print(tuple1[-3])
print(tuple1[1:5])

if 5 in tuple1:
    print('Yes')
else:
    print('No')
