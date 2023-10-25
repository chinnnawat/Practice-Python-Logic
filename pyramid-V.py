height = int(input("Enter height: "))
# วนลูปสร้างแต่ละบรรทัดของรูปสามเหลี่ยม
for i in range(height):
    spaces = ' ' * (height - i - 1)
    dots = '.' * (2 * i)
    slashes = '/'
    backslashes = '\\'
    underline = '_'* (2 * i)
    if i == height - 1:
        print(spaces + slashes + underline +backslashes)
    else:
        print(spaces + slashes + dots +backslashes)
# พิมพ์ข้อความ "===== End of program ====="
print("===== End of program =====")