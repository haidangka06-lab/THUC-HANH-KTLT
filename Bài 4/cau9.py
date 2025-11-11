from binary_search import binary_search
n = int(input("Nhập số phần tử của danh sách: "))
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)
lst.sort()
value = int(input("Nhập phần tử cần tìm: "))
found = binary_search(lst, value)
print(f"Danh sách sau khi sắp xếp: {lst}")
if found:
    print(f"Phần tử {value} được tìm thấy trong danh sách.")
else:
    print(f"Phần tử {value} không có trong danh sách.")


