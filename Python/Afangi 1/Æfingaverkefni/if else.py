#HreiðarPéturssdon
#æfingaverkefni if else
#10janúar2023

#Minnsta talan liður 1 verkefni

tala1 = int(input("Sláðu inn tölu 1"))
tala2 = int(input("Sláðu inn tölu 2"))


if tala1 < tala2:
    print("Talan er minni en tala 2")
elif tala2 < tala1:
    print("Talan er minni en tala 1")
else:
    print("Tolur eru jafn storar")


#Númer mánaðar verkefni liður 2

manudur = input("Sláðu inn nafn mánaðar:")

if manudur == "Janúar":
    print("þessi mánuður er númer 1")
elif manudur == "febrúar":
    print("þessi mánuður er númer 2")
elif manudur == "mars":
    print("þessi mánuður er númer 3")
elif manudur == "apríl":
    print("þessi mánuður er númer 4")
elif manudur == "maí":
    print("þessi mánuður er númer 5")
elif manudur == "júní":
    print("þessi mánuður er númer 6")
elif manudur == "júlí":
    print("þessi mánuður er númer 7")
elif manudur == "ágúst":
    print("þessi mánuður er númer 8")
elif manudur == "september":
    print("þessi mánuður er númer 9")
elif manudur == "október":
    print("þessi mánuður er númer 10")
elif manudur == "nóvember":
    print("þessi mánuður er númer 11")
elif manudur == "desember":
    print("þessi mánuður er númer 12")

else:
    print("Þekki ekki þennan mánuð")
    


#Liður 3 verkefni aldur

aldur = int(input("Sláðu inn aldur:"))

if aldur >= 0 and aldur < 7:
    print("nú svo þú ferð að byrja í skóla")

elif aldur >= 7 and aldur < 16:

    svar = input("ætlar þú í framhaldsskóla? já eða nei svar takk")

    if svar == "já":
        print("gangi þér vel í skólanum")
    elif svar == "nei":
        print("vona þér gangi samt vel")
    else:
        print("verður að svara mér já eða nei :)")

elif aldur >= 16 and aldur < 105:
    print("gangi þér vel í framtíðinni")
else:
    print("þú hefur svarað spurningunni vitlaust")



#verkefni liður 4 margfaldafasta

tala = int(input("sláðu inn tölu á bilinu 0-25"))

if tala > 0 and tala < 25:
    margfeldi = float(tala * 1.7)
    print("útkoman er",margfeldi)
else:
    print("rangur innsláttur")


brandari = input("Viltu fá brandara?")

if brandari == "já":
    print("tómatur labbar yfir götuna og keyrt yfir hann og annar tómatur segir komdu hérna tómatsósan þín! hahahaha! :D")
elif brandari == "nei":
    print("allt í lagi, kannski bara seinna")

