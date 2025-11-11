try:
    X = float(input("Nhập giá đồng hồ Movado (USD): "))
    shipping_fee = 10.00
    tax_rate = 0.30  # 30% Thuế nhập khẩu
    vat_rate = 0.10  # 10% VAT
    total_cost = X * (1 + tax_rate + vat_rate) + shipping_fee
    total_cost_rounded = round(total_cost, 2) 
    print(f"Tổng số tiền Đạt phải trả (USD): {total_cost_rounded}")
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập giá trị số cho giá đồng hồ.")