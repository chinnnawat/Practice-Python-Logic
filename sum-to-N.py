number = int(input('Sum from 1 to :'))
summation = 0
if number <= 0:
    print("Input Error")
else:
    for i in range(1,number+1,1):
        summation = summation + i

    print(f'Sum from 1 to {number} is {summation}')