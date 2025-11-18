def count_file(fname):
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    num_chars = len(text)
    num_words = len(text.split())
    num_lines = text.count("\n") + 1
    print("Số ký tự:", num_chars)
    print("Số từ:", num_words)
    print("Số dòng:", num_lines)
count_file("test.txt")
