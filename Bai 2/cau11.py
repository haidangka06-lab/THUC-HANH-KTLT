def benefit(t, n, k):
    A=n*(1+t/100) ** k
    return A
t= float(input("Nhap lai suat (%/thang): "))
n= float(input("Nhap so tien ban dau: "))
k= int(input("Nhap so thang gui: "))
tong_tien = benefit(t, n, k)
print(f"so tien nhan duoc sau{k} thang la: {tong_tien:.2f}")
