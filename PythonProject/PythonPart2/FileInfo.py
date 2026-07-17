def fileinfo():
    file = open("C:/Users/LENOVO/OneDrive/Desktop/hello.txt", "r")
    print("File Name:", file.name)
    print("File mode:", file.mode)
    print("is closed:", file.closed)
    file.close()
    print("File is closed:", file.closed)

fileinfo()