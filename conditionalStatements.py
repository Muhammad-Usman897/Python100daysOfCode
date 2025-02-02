# CONDITIONAL OPERATORS =,<=,>=,==,!=

a=int(input('Enter your Age: '))
print('Your Age is:',a)

if(a>18):
    print('You Can Drive') #In python this space is called, indentation
else:
    print('You Cannot Drive')
    
    
#if,elif statments
num=int(input('Enter the value of num: '))    
if(num<0):
    print('Number is Negative')
elif(num==0):
    print('Number is zero')
else:
    print('Number is positive')
    
    
# NESTED IF,ELSE STATEMENTS
num1=int(input('Enter the value of num: '))    
if(num1<0):
    print('Number is Negative')
elif(num1>0):
    if(num1<=10):
        print('Number is between 1-10')
    elif(num1>10 and num1<=20):
        print('Number is between 11 to 20')
    else:
        print('Number greater than the 20')
else:
    print('Number is zero')