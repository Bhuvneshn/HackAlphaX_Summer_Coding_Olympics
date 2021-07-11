from functools import reduce
import time
def userguide():
    print(' ' + '✽' * 34)
    print('✽'+'User Guide'.center(50,' ')+'✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽'+'You will be prompted to enter the numbers and'.center(50,' ')+'✽')
    print('✽' + 'the operator. Use commas between all the inputs'.center(50, ' ') + '✽')
    print('✽' + 'and make sure to write the operator at the end.'.center(50, ' ') + '✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽' + 'Following is the list of operator keywords:'.center(50, ' ') + '✽')
    print('✽' + '1. Addition : add, sum or +'.center(50, ' ') + '✽')
    print('✽' + '2. Subtraction: subtract, minus or - '.center(50, ' ') + '✽')
    print('✽' + '3. Multiplication: multiply, product, x or *'.center(50, ' ') + '✽')
    print('✽' + '4. Division: divide,÷ or /'.center(50, ' ') + '✽')
    print('✽' + '5. Exponent: power, exponent, ^ or **'.center(50, ' ') + '✽')
    print('✽' + '6. Factorial : factorial or !'.center(50, ' ') + '✽')
    print('✽' + '7. Square Root : square root, sqrt or √'.center(50, ' ') + '✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽' + 'Upon completing a calculation and before starting,'.center(50, ' ') + '✽')
    print('✽' + 'you will be asked if you wish to continue. '.center(50, ' ') + '✽')
    print('✽' + ' ' * 50 + '✽')
    print('✽' + 'You can either enter Y to continue or N to stop '.center(50, ' ') + '✽')
    print('✽' + ' ' * 50 + '✽')
    print(' ' + '✽' * 34)
    time.sleep(2)

def Factorial(x):
    if x<0:
        print("Negative Numbers don't have Factorials")
    elif x==0 or x==1:
        return 1
    else:
        return x*Factorial(x-1)

def IfContinue():
    n = input('Would you like to do some calculations? (y/n):')
    n=n.lower().strip()
    while n != 'y' and n != 'n':
        print('Please enter a valid value.')
        n = input('Would you like to do some calclations? (y/n):')
    return n

def Calculate():
    Add = ['+', 'add', 'sum']
    Subtract = ['-', 'subtract', 'minus']
    Divide = ['÷', 'divide', '/']
    Multiply = ['x', 'multiply', 'product', '*']
    Exponent = ['^', 'power', 'exponent', '**']
    Factorialxx = ['!', 'factorial']
    SquareRoot = ['√', 'square root','sqrt','squareroot']

    result = ''
    print('')
    print('')
    text='HAXCodingOlympics'
    width2=((len(text))*2)+7
    lis=[range(7),range(13),range(17)]
    temp=0
    for i in lis:
        for j in i:
            if j%2==0:
                print('-',end='')
            else:
                print('+',end='')
        print(' '*2,end='')
    print('')
    for i in text:
        temp+=2
        print('|'+i,end='')
        if temp in [6,15,18,34]:
            print('|',' ',end='')
    print('')
    for i in lis:
        for j in i:
            if j%2==0:
                print('-',end='')
            else:
                print('+',end='')
        print(' '*2,end='')
    print('')
    print('')
    print('')

    width=20
    # formatting the welcome message
    print('','✽'*(width+2))
    print('✽',' '*31,'✽')
    print('✽',"Welcome to Team 37's Calculator".center(29,' '),'✽')
    print('✽',' '*31,'✽')
    print('','✽'*(width+2))
    print('')
    print('')

    width = 20
    order=IfContinue()

    while order=='y':
        result=''
        args = input('Enter the numbers and the operation, all separated by commas: \n')
        args = args.split(',')
        oper = str(args[-1])
        oper = oper.lower()
        del [args[-1]]
        args = list(map(int, args))

        if oper in Exponent:
            if len(args)>2:
                print('Sorry, Exponent Function takes only 2 values')
            else:
                result=(args[0])**(args[1])
        elif oper in Factorialxx:
            if len(args)>1:
                print('Sorry, Factorial Function takes only 1 value')
            else:
                result= Factorial(args[0])
        elif oper in Add:
            result= sum(args)
        elif oper in Subtract:
            lis=list(map(lambda x : x*-1,args))
            lis[0]=-1*(lis[0])
            result= sum(lis)
        elif oper in Divide:
            temp=args[0]
            for i in range(1,len(args)):
                if args[i]==0:
                    print()
                    print('Calculation failed: You cannot divide by 0.')
                    print()
                    result=''
                    break
                else:
                    result=temp/args[i]
                    temp=result
        elif oper in Multiply:
            result = reduce((lambda x,y:x*y),args)
        elif oper in SquareRoot:
            if len(args)>1:
                print('Sorry, Square-Root Function takes only 1 value')
            else:
                result=(args[0])**(1/2)
        else:
            print('Invalid Operator')
            result=''
        if result != '':
            print(' ' + '✽' * (width - 3))
            print('✽' + ' ' * 25 + '✽')
            print('✽'+'Your Answer is:'.center(25,' ')+'✽')
            # print('✽'+(str(x)+' '+str(o)+' '+str(y)+' is :').center(18,' ')+'✽')
            print('✽' + ' ' * 25 + '✽')
            print('✽' + (str(result)).center(25, ' ') + '✽')
            print('✽' + ' ' * 25 + '✽')
            print(' ' + '✽' * (width - 3))
        order=IfContinue()



    print()
    print()
    print()
    print('','✽'*(width+4))
    print('✽',' '*34,'✽')
    print('✽','Thank You for Using Our Calculator'.center(34,' '),'✽')
    print('✽',' '*34,'✽')
    print('','✽'*(width+4))
userguide()
Calculate()
    








