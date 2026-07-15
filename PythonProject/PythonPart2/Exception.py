a = 1
b = 0
try:
    c = a/b
    #c = b/a
    print(c)
except Exception as e:
    print(e, "is not possible")
else:
    print("This is possible")
finally:
    print("Your program ends here")