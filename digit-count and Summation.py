#Check is Integer ?
while True:
    number = (input("Enter Number : "))
    if number.isdigit():
        break
    else:
        print("Plese Enter Integer")

#put (,)
formatted_number = '{:,}'.format(int(number))

#Determine length
length = len(number)

#Summation
summation = sum(int(digit) for digit in number)

print("Entered number = ",formatted_number)
print("Total digits are :",length)
print("Summation :",summation)
