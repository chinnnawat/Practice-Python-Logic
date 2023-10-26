height = int(input("Enter height: "))
first_char = ord('z')
for i in range(0, height, 1):
    space = " " * (height - i - 1)
    print(end=space)
    for j in range(2 * i + 1):
        char = chr(first_char)
        first_char = first_char - 1
        print(char, end="")
        if first_char < ord('a'):
            first_char = ord('z')
    print()
