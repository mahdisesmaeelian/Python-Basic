class Fraction:

    def __init__(self, s, m):
        self.surat = s
        self.makhraj = m

    def sum(self,guest):
        result = Fraction(None , None)
        result.surat = self.surat*guest.makhraj + self.makhraj*guest.surat
        result.makhraj= self.makhraj * guest.makhraj
        return result

    def min(self , guest):
        result = Fraction(None , None)
        result.surat = self.surat*guest.makhraj - self.makhraj*guest.surat
        result.makhraj= self.makhraj * guest.makhraj
        return result

    def mul(self, guest):
        result = Fraction(None , None)
        result.surat = self.surat * guest.surat
        result.makhraj = self.makhraj * guest.makhraj
        return result

    def div(self , guest):
        result = Fraction(None , None)
        result.surat = self.surat / guest.surat
        result.makhraj = self.makhraj / guest.makhraj
        return result

    def show(self):
        print(self.surat, '/', self.makhraj)

a = Fraction(12, 5)
b = Fraction(6, 8)

print("The sum of the fractions are: ")
a.sum(b).show()

print("The min of the fractions are: ")
a.min(b).show()

print("The multiply of the fractions are: ")
a.mul(b).show()

print("The divide of the fractions are: ")
a.div(b).show()