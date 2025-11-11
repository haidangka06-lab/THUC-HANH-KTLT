import numpy as np
students = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]
dtype = [('name', 'U10'), ('class', int), ('height', float)]
arr = np.array(students, dtype=dtype)
sorted_arr = np.sort(arr, order=['class', 'height'])
print("Kết quả sắp xếp:")
print(sorted_arr)


