n=int(input("Nhap n: "))
row = [1]
for i in range(n):
    print(row)
    row=[1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
