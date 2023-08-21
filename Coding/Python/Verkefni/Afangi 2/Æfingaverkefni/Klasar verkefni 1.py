# Hreiðar Pétursson
# 24.apríl 2023
# Klasar verkefni 1 OG 2



# ----------------  VERKEFNI 1 ---------------

class persona(object):
    def __init__(self,nafn,aldur):
        self.nafn = nafn
        self.aldur = aldur

    def __str__(self):
        return f"Nafn:{self.nafn} Aldur:{self.aldur}"

    def aldursmunur(self,tilvik2):

        if self.aldur > tilvik2.aldur:
            aldursmunur = self.aldur - tilvik2.aldur
            return f"Aldursmunurinn er {aldursmunur}"
        elif self.aldur < tilvik2.aldur:
            aldursmunur = tilvik2.aldur - self.aldur
            return f"Aldursmunurinn er {aldursmunur}"
        else:
            return "Þessir aðilar eru jafngamlir"

hreidar = persona("Hreiðar",36)
gunnar = persona("Gunnar",38)
jonas = persona("Jónas",56)

# Þetta tvennt gerir það sama því __str__ s
print(hreidar.__str__())
print(hreidar)


aldursmunur1 = hreidar.aldursmunur(gunnar)
aldursmunur2 = gunnar.aldursmunur(hreidar)
aldursmunur3 = jonas.aldursmunur(gunnar)
aldursmunur4 = jonas.aldursmunur(hreidar)

print(aldursmunur1)
print(aldursmunur2)
print(aldursmunur3)
print(aldursmunur4)

class annarklasi:
    def __init__(self,t1,t2,t3):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
    def __str__(self):
        return f"{self.t1} {self.t2} {self.t3}"

    def samlagning(self):

        return self.t1 + self.t2 + self.t3

    def margfoldun(self):
        return self.t1 * self.t2 * self.t3
    def annadveldi(self):
        listi = []
        annadveldi1 = self.t1 ** 2
        listi.append(annadveldi1)
        annadveldi2 = self.t2 ** 2
        listi.append(annadveldi2)
        annadveldi3 = self.t3 ** 2
        listi.append(annadveldi3)
        return listi
t1 = int(input("Sláðu inn tölur"))
t2 = int(input("Sláðu inn tölu 2"))
t3 = int(input("Sláðu inn tölu 3"))
tolur = annarklasi(t1,t2,t3)

print(tolur.samlagning())
print(tolur.margfoldun())
print(tolur.annadveldi())

# -------------- VERKEFNI 2 ------------------

class setning:
    def __init__(self,strengur=""):
        self.strengur = strengur

    def fall1(self):
        self.strengur = input("Sláðu inn streng")

    def __str__(self):
        return "strengurinn er: " + self.strengur

# Verð að kalla á klasann með breytu
s = setning()
# Sæki fallið innan klasans svo
#s.fall1()
# Og prenta
#print(s)


class adili:
    def __init__(self,nafn,gsm,heimasimi,email):
        self.nafn = nafn
        self.gsm = gsm
        self.heimasimi = heimasimi
        self.email = email

    def breytanafn(self,nafn):
        self.nafn = nafn

    def breytagsm(self,gsm):
        self.gsm = gsm

    def breytaheimasimi(self,heimasimi):
        self.heimasimi = heimasimi

    def breytaemail(self,email):
        self.email = email

    def __str__(self):
        return f"Nafn: {self.nafn}\n" \
               f"gsm: {self.gsm}\n" \
               f"Heimasími: {self.heimasimi}\n" \
               f"Email: {self.email}"
listi = []
adili1 = adili("Hreiðar",7617603,7617603,"hreidar1987@gmail.com")
adili2 = adili("Gunnar",5648976,8976589,"blabla@blabla.com")
adili3 = adili("Jónas",1234567,7654321,"jonas@island.is")
listi.append(adili1)
listi.append(adili2)
listi.append(adili3)
for adili in listi:
    print(adili)
    print("")



adili1.breytaemail("nyttemail@email.com")
adili2.breytagsm(8978976548)
