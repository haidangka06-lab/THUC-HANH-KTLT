def positions_of_min_max(lst):
    if not lst:
        return[], []
    mn=min(lst)
    mx=max(lst)
    pos_min=[i for i, v in enumerate(lst) if v ==mn]
    pos_max=[i for i, v in enumerate(lst) if v ==mx]
    return pos_min, pos_max
    lst=[3, 7, 2, 9, 2, 9]
    pos_min, pos_max=positions_of_min_max(lst)
    print("Danh sach:", lst)
    print("Gia tri nho nhat:", min(lst), "o vi tri 0-based:", pos_min, "va 1-based:",[p+1 for p in pos_min])
    print("Gia tri lon nhat:", max(lst), "o vi tri 0-based:", pos_max, "va 1-based:",[p+1 for p in pos_max])
