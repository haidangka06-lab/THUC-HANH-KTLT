def count_lines(fname):
    with open(fname, "r", encoding="utf-8") as f:
        print("Số dòng:", len(f.readlines()))
count_lines("test.txt")

