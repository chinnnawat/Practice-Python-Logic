list_number = input("enter some number :").split()
print(list_number)
for n in list_number:
    n = int(n)
    if int(n)%2 != 0:
        print(n,end =" ")


