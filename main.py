# 1
class Xodim:
    def __init__(self, ism, lavozim):
        self.ism = ism
        self.__lavozim = lavozim 

    def lavozim_kor(self):
        return f"Lavozim: {self.__lavozim}"

    def lavozim_ozgartir(self, yangi_lavozim):
        self.__lavozim = yangi_lavozim

x1 = Xodim("Aziz", "Dasturchi")

print(x1.ism)
print(x1.lavozim_kor())

x1.lavozim_ozgartir("Senior dasturchi")
print(x1.lavozim_kor())


# 2
class Eksponat:
    def __init__(self, nom, yil):
        self.nom = nom
        self.yil = yil


class Muzey:
    def __init__(self):
        self.eksponatlar = []

    def eksponat_qosh(self, eksponat):
        self.eksponatlar.append(eksponat)

    def yil_eksponatlari(self, yil):
        return [e.nom for e in self.eksponatlar if e.yil == yil]

e1 = Eksponat("Qadimiy idish", 1850)
e2 = Eksponat("Temir qilich", 1900)

muzey = Muzey()
muzey.eksponat_qosh(e1)
muzey.eksponat_qosh(e2)

print(muzey.yil_eksponatlari(1900))
