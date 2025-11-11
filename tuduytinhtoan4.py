try:
    n = int(input("Nhập độ dài cạnh khối Rubik (n): "))
    if n > 0:
        stickers = 6 * (n ** 2)
        print(f"Số lượng miếng dán riêng lẻ cần thiết là: {stickers}")
    else:
        print("Độ dài cạnh phải là số nguyên dương.")
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")