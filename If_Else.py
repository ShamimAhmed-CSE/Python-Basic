

a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))

if (a>b):
    if(a>c):
        print("The max number is ",a)
    else:
        print("The max number is ", c)
else:
    if (b > c):
        print("The max number is ", b)
    else:
        print("The max number is ", c)