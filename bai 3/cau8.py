words=input("Nhap day tu:").split()
max_len=max(len(w)for w in words)
for w in words:
    if lem(w)==max_len:
        print(w)
