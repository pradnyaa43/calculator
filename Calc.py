

def add(a,b):
    ans = a+b
    print('Addition = ',ans ,"\nThat's your answer!")
def sub(a,b):
    ans = a-b
    print('Subtraction = ',ans ,"\nThat's your answer!")
def mul(a,b):
    ans = a*b
    print('Multiplication = ',ans ,"\nThat's your answer!")
def div(a,b):
    ans = a/b
    print('Division = ',ans ,"\nThat's your answer!")
def mod(a,b):
    ans = a%b
    print('Remainder = ',ans ,"\nThat's your answer!")
def roundoff(a,b):
    ans = a//b
    print('Roundoff = ',ans ,"\nThat's your answer!")
def exp(a,b):
    ans = a**b
    print('Final ans = ',ans ,"\nThat's your answer!")

while True:
    op=input('\n*MENU* \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Remainder \n6. Roundoff \n7. Exponentiation \n8. Exit \nSelect an option: \n')
    if op == '1':
        print('You chose addition. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        add(n1,n2)
    elif op == '2':
        print('You chose Subtraction. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        sub(n1,n2)
    elif op == '3':
        print('You chose Multipliction. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        mul(n1,n2)
    elif op == '4':
        print('You chose Division. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        div(n1,n2)
    elif op == '5':
        print('You chose finding remainder. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        mod(n1,n2)
    elif op == '6':
        print('You chose Rounding-off. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        roundoff(n1,n2)
    elif op == '7':
        print('You chose Exponentiation. So: ')
        n1=int(input('Enter your first number: '))
        n2=int(input('Enter your second number: '))
        exp(n1,n2)
    elif op == '8':
        print('You chose to exit.')
        break
    else:
        print('Invalid choice. Please select an appropriate option.')

