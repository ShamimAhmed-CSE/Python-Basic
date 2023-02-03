

grade=int(input("Enter your grade "))

if(grade<100 and grade>=80):
    print("A+")
elif(grade<80 and grade>=70):
    print("A")
elif(grade<70 and grade>=60):
    print("A-")
elif(grade<60 and grade>=50):
    print("B")
elif(grade<50 and grade>=40):
    print("c")
else:
    print("F")