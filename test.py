print(" *** Filter only ODD number ***")
list = input("Enter some numbers: ").split()
print(list)
for n in list :
    n = int(n)
    if n%2 > 0:
        print(n,end=' ')