def file_append_and_show(fname):
    with open(fname, "a", encoding="utf-8") as f:
        f.write("Python Exercises\n")
        f.write("Java Exercises\n")
    with open(fname, "r", encoding="utf-8") as f:
        print(f.read())
file_append_and_show("abc.txt")
