
try:
    giờ = int(input("Nhập số giờ: "))
    phút = int(input("Nhập số phút: "))
    giờ_giây = giờ * 3600
    phút_giây = phút * 60
    giây = giờ_giây + phút_giây
    print(f"{giờ} giờ và {phút} phút bằng tổng cộng {giây} giây.")
    
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên cho giờ và phút.")
    