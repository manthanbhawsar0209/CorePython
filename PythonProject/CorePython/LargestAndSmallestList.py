number = [10,6,25,2,23,18,19,1]
largest = 0
for n in number:
    if n > largest:
        largest = n
print("Largest number is ", largest)
smallest = largest
for n in number:
    if n < smallest:
        smallest = n
print("Smallest number is ", smallest)