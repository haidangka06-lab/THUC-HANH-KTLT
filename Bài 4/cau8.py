from sequential_search import Sequential_Search
n = int(input("Nhập số phần tử của danh sách: "))
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(value)
# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: ")
found, index = Sequential_Search(dlist, item)
if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}")
else:
    print(f"Phần tử {item} không có trong danh sách.")

