# .... There are four type of Function Arguments


#     Default Argument
def average(a=10,b=9):
    print('The average of is: ', (a+b)/2)
    
average()
average(9)
average(b=10)


#     keywords Argument ----Order does not matter
def average(a,b):
    print('The average of is: ', (a+b)/2)
    
average(b=12,a=8)


#     Required Argument
def average(a,b,c=3):
    print('The average of is: ', (a+b+c)/2)
    
average(6,4)


#     length-Variable Argument
def average(*number): #Convert it into tuple
    print(type(number))
    sum=0;
    for i in number:
        sum=sum+i;
    print('The average is: ', sum/len(number))


average(6,4,3)


#     Return Statement
def average(a,b,c=3):
    return (a+b+c)/2
    
x=average(6,4)
print(x)