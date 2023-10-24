# Get integer
number = int(input("Enter an integer(n) : "))
# check number<10
if number<10:
    for i in range(1,13):
        space = ' '
        multiple = number * i
        if i < 10:
            if multiple < 10 :
                print(space+str(number) +' x '+space +str(i) + ' = '+space + str(multiple))
            else:
                print(space+str(number) +' x '+space +str(i) + ' = ' + str(multiple))
        else:
            print(space+str(number) +' x ' +str(i) + ' ='+space + str(multiple))
else:
    for i in range(1,13):
        space = ' '
        multiple = number * i
        if i < 10:
            if multiple < 10 :
                print(str(number) +' x '+space +str(i) + ' = '+space + str(multiple))
            else:
                print(str(number) +' x '+space +str(i) + ' = ' + str(multiple))
        else:
            print(str(number) +' x ' +str(i) + ' ='+space + str(multiple))