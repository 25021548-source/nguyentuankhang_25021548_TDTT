ten = input("Nhập tên của 3 người bạn (cách nhau bởi dấu cách): ")
names_list = ten.split()
if len(names_list) == 3:
    reversed_names = names_list[::-1]
    output = f"{reversed_names[0]}, {reversed_names[1]}, and {reversed_names[2]}."
    
    print(f"Đầu ra theo thứ tự ngược: {output}")
else:
    print("Vui lòng nhập đúng 3 tên.")

 