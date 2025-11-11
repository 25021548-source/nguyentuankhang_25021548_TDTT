print("Hello world")
name = input("Vui lòng nhập tên của bạn: ")
print(f"Chào mừng bạn, {name}!")
try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    if b == 0:
        print("Lỗi: Không thể chia cho 0 (b phải khác 0).")
    else:
        tong = a + b
        hieu = a - b
        tich = a * b
        phan_nguyen = a // b
        phan_du = a % b
        print(f"Tổng: {a} + {b} = {tong}")
        print(f"Hiệu: {a} - {b} = {hieu}")
        print(f"Tích: {a} * {b} = {tich}")
        print(f"Phần nguyên (a // b): {phan_nguyen}")
        print(f"Phần dư (a % b): {phan_du}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ cho a và b.")