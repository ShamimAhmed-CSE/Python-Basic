num=int(input("Enter the num upto : "))

n1,n2=0,1
count=0

while count<num:

    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1