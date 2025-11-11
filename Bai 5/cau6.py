class StringProcessor:
    def __init__(self):
        self.s = ""
    def get_String(self):
        self.s = input("Nhập chuỗi: ")
    def print_String(self):
        print("Chuỗi in hoa:", self.s.upper())
sp = StringProcessor()
sp.get_String()
sp.print_String()

