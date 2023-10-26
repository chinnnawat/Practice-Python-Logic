height = int(input("Enter height: "))
first_char = ord('z')
for i in range(height):
    space = " " * (height - i - 1)
    chars = [chr(first_char) for j in range(i * 2 + 1)]
    first_char = first_char-1
    print(space + "".join(chars))