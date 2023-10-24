height = int(input("Enter height: "))

# วนลูปสร้างแต่ละบรรทัดของรูปสามเหลี่ยม
for i in range(height):
    spaces = ' ' * (height - i - 1)
    dots = '.' * (2 * i)
    slashes = '/' + '.' * (2 * (height - i - 1)) + '\\'
    if i == height - 1:
        bottom_line = '/' + '_' * (2 * i) + '\\'
        print(spaces + bottom_line)
    else:
        print(spaces + slashes)

# พิมพ์ข้อความ "===== End of program ====="
print("===== End of program =====")
