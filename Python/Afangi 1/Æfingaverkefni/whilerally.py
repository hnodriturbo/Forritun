#Hreiðar Pétursson
#16janúar
#While æfingaverkefni rallý

#Liður 1 - while
teljari = 20

while teljari < 41:
    print(teljari, end=" ")
    teljari = teljari+2


#liður 2 - while æfingaverkefni
teljari = 15
summa = 0
while teljari < 346:
    summa = summa + teljari
    teljari = teljari + 2
    print(summa)


#liður 3
tala = int(input("Sláðu inn tölu undir 100"))

while tala < 101:
    print(tala)
    tala = tala+1


#liður 4
tala = int(input("Sláðu inn tölu yfir 100"))

while tala > 99:
    print(tala)
    tala = tala-1
#liður 5 - æfingaverkefni
tala = int(input("Sláðu inn tölu til að athuga hve oft tala 9 og 5 gengur upp í hana"))

tala9 = tala // 9
tala5 = tala // 9

if tala9 % 9 == 0:
    print("talan gengur upp í 9")
else:
    print("talan gengur ekki upp í 9")


if tala5 % 5 == 0:
    print("Talan gengur upp í 5")
else:
    print("tala gengur ekki upp í 5")

print("9 gengur upp í töluna",tala9,"sinnum")
print("5 gengur upp í töluna",tala5,"sinnum")


#liður6 - æfingaverkefni
kommutala = float(input("Sláðu inn kommutölu 1"))
kommutala2 = float(input("Sláðu inn kommutölu 2"))

utkoma = kommutala2 / kommutala

print("útkoman er",round(utkoma,5))


#liður 7 - æfingaverkefni
#athuga hvaða tölur 15 gengur upp í og talan 18
tala = 0
while tala < 1001:
    tala=tala+1
    if tala % 15 == 0 and tala % 18 == 0:
        print(tala)


#liður 8 - æfingaverkefni
texti = 0

while texti < 6:
    print("barbara "* texti)
    texti = texti + 1

teljari = 0
texti = "barbara "
while teljari < 5:
    print(texti +"barbara ")
    teljari = teljari + 1

