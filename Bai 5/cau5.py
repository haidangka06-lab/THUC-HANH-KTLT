class DaoChuoi:
    def reverse_words(self, s):
        words = s.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words
s = 'hello .py'
dao = DaoChuoi()
print("Kết quả:", dao.reverse_words(s))

