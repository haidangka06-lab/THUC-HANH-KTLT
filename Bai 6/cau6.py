def file_read_from_tail(fname, nlines):
    with open(fname, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-nlines:]:
        print(line, end="")
file_read_from_tail("test.txt", 2)

