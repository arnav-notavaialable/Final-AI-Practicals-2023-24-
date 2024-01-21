#Check if the number entered by the user is positive, negative or zero.

def pnz(x):
    if x == 0:
        print('The given number is 0')
    elif x>0:
        print('The given number is positive')    
    else:
        print('The given number is negative')

#pnz(x)is a function which checks if a number stored in the variable x is positive,negative or zero

x = float(input('Enter any number you want :'))

pnz(x)