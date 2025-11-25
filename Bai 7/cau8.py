from tkinter import *
root = Tk()
root.title("Thông Tin Cá Nhân")
root.geometry("350x250")
# ----- Nhãn -----
Label(root, text="Họ và tên:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Label(root, text="Ngày sinh:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Label(root, text="MSSV:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
Label(root, text="Ngành học:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
# ----- Ô nhập -----
entry_name = Entry(root, width=30)
entry_dob = Entry(root, width=30)
entry_mssv = Entry(root, width=30)
entry_major = Entry(root, width=30)
entry_name.grid(row=0, column=1, pady=5)
entry_dob.grid(row=1, column=1, pady=5)
entry_mssv.grid(row=2, column=1, pady=5)
entry_major.grid(row=3, column=1, pady=5)
root.mainloop()

