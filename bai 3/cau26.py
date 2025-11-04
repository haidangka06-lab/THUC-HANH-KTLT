tong_tien=0
print("Nhap nhat ky giao dich (D so hoac w so).Nhap trong de dung:")
while True:
    nhap=input()
    if not nhap:
        break
    parts = nhap.split()
    if len(parts) !=2:
        continue
    lenh, so=parts[0],int(parts[1])
    if lenh.uppre() == 'D':
        tong_tien += so
    elif lenh.upper() == 'w':
        tong_tien -= so
print("So du cuoi cung la:",tong_tien)        
