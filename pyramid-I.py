height = int(input("Enter height : "))
for i in range(0,height,1):
    space = " " * (height-i-1)
    star = "*" * (2*i+1)
    print(space+star)