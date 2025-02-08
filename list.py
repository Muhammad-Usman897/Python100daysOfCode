# ----------------- LIST -------------------
# * List are ordered collection of data items
# * They are store multiple items in a single variable and enclosed with a [] square brackets
# * List are mutable 

marks=[3,5,6, 'Usman',12,14]  # A single list can contain items of different data types  
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[-3])
print(marks[1:6])
print(marks[1:6:2]) # Jumping index

# Check whether an item present in the list?
marks=[3,5,6, 'Usman']
if 7 in marks:
    print('Yes!')
else:
    print('No')
    
# -------- List Comprehension ---------- 
lst=[i*i for i in range(4)]
print(lst)

