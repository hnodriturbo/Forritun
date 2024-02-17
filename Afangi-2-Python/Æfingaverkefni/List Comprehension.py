import random
pow2 = [x ** 2 for x in range(10)]
print(pow2)

pow2 = [2 ** x for x in range(10)]
print(pow2)

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)

setningar = [x+y for x in ["Python ","C "] for y in ["Language","Programming"]]
print(setningar)

#Liður 1
listic = [3 ** x for x in range(10,20)]
print(listic)

#Liður 2
listi = [x for x in range(1,1000) if x % 5 == 0 and x % 2 == 1]
print(listi)

#Liður 3
listi = []
listi2 = []
for x in range(100):
    tala = random.randint(200,800)
    listi.append(tala)
for x in listi:
    tala = str(x)
    if tala[-1] == "4":
        listi2.append(tala)
print(listi2)


listicomp = [random.randint(200,800) for x in range(100)]
print(listicomp)
#Liður 3

listicomp2 = [x for x in listicomp if str(x)[-1] == "4"]
print(listicomp2)

#Liður 4
listi1 = ["Hreiðar", "Gunnar", "Jónas", "Andri", "Pétur", "Anton"]
listi2 = ["Jóna", "Gunna", "Hnoðrína", "Diljá", "Eva", "Erna"]
danspor = [listi1[x]+" dansar við "+listi2[x] for x in range(len(listi1))]
print(danspor)

#Liður 1
listi = [x for x in range(1,11)]
print(listi)
#Liður 2
listi = [x for x in range(20,0,-2)]
print(listi)
listi = [x for x in range(19) if x % 3 == 0]
print(listi)
strengur1 = "Gaman"
strengur2 = "Saman"
listi = [["Gaman" for x in range(5)]+["Saman" for x in range(5)]]
print(listi)
listi = ["gaman" if x % 2 == 0 else "saman" for x in range(100)]
print(listi)

strengur = "Nú Er Gaman"
listi = [x for x in strengur]
print(listi)

listi = [x.swapcase() for x in strengur]
print(listi)

textastrengur = input("Sláðu inn textastreng til að sigta úr allar tölur")
listi = [x for x in textastrengur if x.isalpha()]
print(listi)
