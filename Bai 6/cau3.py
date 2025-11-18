def read_all(fname):
    with open(fname, "r", encoding="utf-8") as f:
        print(f.read())
read_all("test.txt")
