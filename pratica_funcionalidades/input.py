num = input("Type a number: ")

if not(num.isnumeric()):
    print("Not a number")
elif (int(num)%2 == 0):
    print("It's an even number!")
else:
    print("It's an odd number!")