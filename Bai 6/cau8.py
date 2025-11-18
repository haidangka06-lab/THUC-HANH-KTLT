def write_list_to_file(fname, mylist):
    with open(fname, "w", encoding="utf-8") as f:
        for item in mylist:
            f.write(item + "\n")
write_list_to_file("list.txt", ["Python", "Java", "C++", "PHP"])

