ds=input("Nhap cac so, cach nhau bang dau phay:").split(',')
le=[int(x) for x in ds if int(x) % 2 !=0]
print("Cac so le la:",le)
