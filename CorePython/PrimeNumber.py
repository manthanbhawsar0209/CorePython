n = int(input("Enter a number: "))
for i in range(2,n):
    if n % i == 0:
        print("It is not a prime number")
    else:
        print("It is a prime number")
