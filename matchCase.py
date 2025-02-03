# Match Case Statements in python

x=int(input('Enter the Number: '))
match x:
    case 0:
        print('Case is 0')
    case 1:
        print('Case is 1')
    case 2:
        print('Case is 2')
    case 3:
        print('Case is 3')
    case 4:
        print('Case is 4')
    case 5:
        print('Case is 5')
    case _: #Default case
        print(x)