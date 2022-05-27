

num1, oper, num2 = input('Enter Calculation: ').split()

num1 = int(num1)
num2 = int(num2)

if (oper == '+'):
    result = num1 + num2
    print(' {} {} {} = {} '.format(num1, oper, num2, result))
elif (oper == '-'):
    result = num1 - num2
    print(' {} {} {} = {} '.format(num1, oper, num2, result))
elif (oper == '*'):
    result = num1 * num2
    print(' {} {} {} = {} '.format(num1, oper, num2, result))
elif (oper == '/'):
    result = num1 / num2
    print(' {} {} {} = {} '.format(num1, oper, num2, result))
elif (oper == '%'):
    result = num1 % num2
    print(' {} {} {} = {} '.format(num1, oper, num2, result))
else:
    print('invalid operators')