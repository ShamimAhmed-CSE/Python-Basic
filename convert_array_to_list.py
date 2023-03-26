import array

user_input = input("Enter the array: ")
arr = array.array('i', map(int, user_input.split()))

lst = arr.tolist()

print(lst)
