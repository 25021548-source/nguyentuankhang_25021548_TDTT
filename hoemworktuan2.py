a = float(input("nhập cạnh a: "))
b = float(input("nhập cạnh b: "))       
c = float(input("nhập cạnh c: "))
if   a + b <= c or a + c <= b or b + c <= a:
     print("Ba cạnh không thể tạo thành một tam giác.") 
elif a == b == c:
     print("Đây là tam giác đều.")   
elif a==b or b==c or a==c :
     print("đay là tam giác cân") 
else :
     print("ba cạnh này là tam giác")
s = (a+b)/2 
print("dien tich tam giac", s) 
d = a + b + c
print("chu vi la", d)
