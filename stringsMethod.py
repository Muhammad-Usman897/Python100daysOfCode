# Strings Are immutable in python

name='Muhammad Usman!!'
print(name.upper())
print(name.lower())
print(name.rstrip('!')) #removes any trailing Character
print(name.replace("Muhammad", 'Usman'))
print(name.split(' ')) #he convert the strings into the list
print(name.count('m'))

intro='introduction tO jS'
print(intro.capitalize()) #Capitalize() method only first character of the string to uppercase and rest of the other character of the string are turned to lowercase

str1='WelCome to the Console!!'
print(str1.center(50))
print(str1.endswith("!!"))
print(str1.endswith('to',4,10))


str2="He's Name is Dan, he is an Honest man"
print(str2.find("ishh"))
print(str2.index("is"))

str3='WelComeToTheConsole'
print(str3.isalnum()) #A-Z a-z 0-9
print(str3.isalpha()) #A-Z a-z

str4="hey usman"
print(str4.isupper())
print(str4.islower())
print(str4.isprintable())

str5="          "
print(str5.isspace())

str6="Welcome to The Organization"
print(str6.istitle())
print(str6.title())
print(str6.startswith('Welcome'))
print(str6.swapcase())