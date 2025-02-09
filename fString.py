# ------- fStrings in python ---------
letter='Hey my Name is {1} and i am from {0}'
name='Usman'
country='Pakistan'

print(letter.format(country,name))
print(f"Hey my Name is {name} and i am from {country}")

price=48.8766
txt=f"for only {price:.2f} dollors"
print(txt)
