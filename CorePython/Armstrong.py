# num = 153
# n = num
#     sum = 0
#     r = 0
#     while n > 0:
#         r = n % 10
#         sum = sum + r * r * r
#         n = n // 10
#     if sum == num:
#         print("It is an Armstrong number.")
#     else:
#         print("Not an Armstrong number.")

for num in range(1, 500):
    n = num
    sum = 0
    r = 0
    while n > 0:
        r = n % 10
        sum = sum + r * r * r
        n = n // 10
    if sum == num:
        print(num)
