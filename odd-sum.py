
n=int(input("Enter an integer(N) : "))
sumation = 0
result = "sumation => "

for i in range(1,n+1,2):
    sumation = sumation + i
    result = result + str(i)
    if i<n-1:
        result =result + "+"

result = result + "=" +str(sumation)
print(result)