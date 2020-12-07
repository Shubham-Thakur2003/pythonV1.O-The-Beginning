# Faulty calculator
#Calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# This program will take operator and the two numbers as input from the user
# and then return the result !!
print("Welcome to the Calculator")
print("What you want to do?" + "+,-,*,/")
operator= (input())
print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
if num1 ==45 and num2==3 and operator=='*':
    print("555")
elif num1 == 56 and num2 == 9 and operator == '+':
        print("77")
elif num1 == 56 and num2 == 6 and operator == '/':
        print("4")
elif operator=='*' :
    num4=num1*num2
    print(num4)
elif operator == '+':
    plus=num2+num1
    print(plus)
elif operator == '/':
    Dev=num2/num1
    print(Dev)
elif operator == '-':
    Dev=num2-num1
    print(Dev)
elif operator == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")
