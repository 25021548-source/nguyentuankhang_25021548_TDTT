#bài 1
a = float(input("nhập cạnh a: "))
b = float(input("nhập cạnh b: "))       
c = float(input("nhập cạnh c: "))
if   a + b <= c or a + c <= b or b + c <= a:
     print("Ba cạnh không thể tạo thành một tam giác.") 
elif a == b == c:
     print("Đây là tam giác đều.")   
elif a==b or b==c or a==c :
     print("đay là tam giác cân") 
if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
     print("đây là tam giác vuông")
elif a==b or b==c or a==c and (a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2):
        print("đây là tam giác vuông cân")
else :
     print("ba cạnh này là tam giác")
s = (a*b)/2 or (a*c)/2 or (b*c)/2
print("dien tich tam giac", s) 
d = a + b + c
print("chu vi la", d)
#bài 2
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
s=-b/a
if b != 0:
    print("ax+b có nghiệm là", '%.2f' % s
          )
else:
    print("phương trình vô nghiệm")
#bài 3
a = float(input("nhập hệ số a: "))
b = float(input("nhập hệ số b: "))
c = float(input("nhập hệ số c: "))
d = b**2 - 4*a*c
if d < 0:
    print("phương trình vô nghiệm")
elif d == 0:
    x = -b / (2*a)
    print("phương trình có nghiệm kép x1 = x2 =", '%.2f' % x)
else :
     x1 = (-b + d**0.5) / (2*a)
     x2 = (-b - d**0.5) / (2*a)
     print("phương trình có hai nghiệm phân biệt:")
     print("x1 =", '%.2f' % x1)
     print("x2 =", '%.2f' % x2)
#bài 4
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))
d = float(input("nhập số d: "))
số_lớn_nhất = a
if b > số_lớn_nhất:
    số_lớn_nhất = b
if c > số_lớn_nhất:
    số_lớn_nhất = c
if d > số_lớn_nhất:
    số_lớn_nhất = d
print("Số lớn nhất là:", số_lớn_nhất)
#bài 5  
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))
d = float(input("nhập số d: "))
m = float(input("nhập số m: "))
n = float(input("nhập số n: "))
D = (a*d-b*c)
Dx = (m*d - b*n)
Dy = (a*n - m*c)
if D == 0:
    print("Hệ phương trình vô nghiệm hoặc vô số nghiệm.")
else:
    x = Dx / D
    y = Dy / D
    print("Nghiệm của hệ phương trình là:")
    print("x =", '%.2f' % x)
    print("y =", '%.2f' % y)
#bài 6
a = int(input("nhập số giây: "))
giờ = a // 3600
phút = (a % 3600) // 60
if a == 0:
    thời_gian = "không có thời gian"
else:
    gio = int(giờ)
    phut = int(phút)
    thời_gian = f"{gio} giờ {phut} phút"
print("thời gian là:", thời_gian)
#bài 7
str_x = float(input("nhập điểm tâm x của hình tròn: "))
str_y = float(input("nhập điểm tâm y của hình tròn: "))
r = float(input("nhập bán kính r của hình tròn: "))
str_x1 = float(input("nhập điểm x1 của điểm cần kiểm tra: "))
str_y1 = float(input("nhập điểm y1 của điểm cần kiểm tra: "))
khoảng_cách = (((str_x1-str_x))**2 + ((str_y1-str_y))**2)**0.5 - r
if khoảng_cách < 0:
    print("Điểm nằm trong hình tròn.")
elif khoảng_cách == 0:
    print("Điểm nằm trên đường tròn.")
else:
    print("Điểm nằm ngoài hình tròn.")
#bài 8
a = float(input("nhập số x: "))
b = float(input("nhập số y: "))
s = a**b
print("kết quả là:", s)
#bài 9
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))    
d = float(input("nhập số d: "))
số_nhỏ_nhất = a 
if b < số_nhỏ_nhất:
    số_nhỏ_nhất = b
elif c < số_nhỏ_nhất:
    số_nhỏ_nhất = c
elif d < số_nhỏ_nhất:
    số_nhỏ_nhất = d
else :
    số_nhỏ_nhất = a
print("số nhỏ nhất là:", số_nhỏ_nhất)


    