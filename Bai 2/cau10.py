import math
def Tinh(R):
    if R <=0:
        print("Ban kinh khong hop le! Vui long nhap R > 0.")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    print(f"chu vi hinh tron:{chu_vi:.2f}")
    print(f"Dien tich hinh tron:{dien_tich:.2f}")
R = float(input("Nhap ban kinh R: "))
Tinh(R)
