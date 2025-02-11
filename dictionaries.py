# ----------------- DICTIONARIES -------------------
# * dict are ordered collection of data items
# * They are store multiple items in a single variable and enclosed with a {} curly brackets

regNo={
    520: 'Syed Abdul Rehman',
    566: 'Muhammad Aamir',
    568: 'Muhammad Usman'
}
print(regNo)
# print(regNo[569]) #Through errors
print(regNo.get(569))
print(regNo.keys()) #accessing keys
print(regNo.values()) #accessing values
print(regNo.items()) #accessing key-values pairs

