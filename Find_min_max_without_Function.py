n=int(input("Enter  a number for loop : "))
list=[]
for i in range(0,n):
    print("Enter num in possition ",i)
    v=int(input())
    list.append(v)
print(list)

max = list[0]
min = list[0]
for x in list:
    if x > max:
        max = x
    elif x < min:
        min = x
print(max)
print(min)