#Hreiðar Pétursson
#10.1.2023
#If - elif - else verkefni heima
import math
import random

#Liður 1 - verkefni if elif else
"""
heiltala1 = int(input("Sláðu inn heiltölu 1"))
heiltala2 = int(input("Sláðu inn heiltölu 2"))

if heiltala1 == heiltala2:
    print("Tölurnar eru jafnstórar")
else:
    print(Tölurnar eru ekki jafnstórar)

"""
"""
#Liður 2 - verkefni if elif else

nafnmanadar = input("Sláðu inn nafn mánaðar")

if nafnmanadar == "janúar":
    print("Þetta er mánuður númer 1")
elif nafnmanadar == "febrúar":
    print("Þetta er mánuður númer 2")
elif nafnmanadar == "mars":
    print("Þetta er mánuður númer 3")
elif nafnmanadar == "apríl":
    print("Þetta er mánuður númer 4")
elif nafnmanadar == "maí":
    print("Þetta er mánuður númer 5")
elif nafnmanadar == "júní":
    print("Þetta er mánuður númer 6")
elif nafnmanadar == "júlí":
    print("Þetta er mánuður númer 7")
elif nafnmanadar == "ágúst":
    print("Þetta er mánuður númer 8")
elif nafnmanadar == "september":
    print("Þetta er mánuður númer 9")
elif nafnmanadar == "október":
    print("Þetta er mánuður númer 10")
elif nafnmanadar == "nóvember":
    print("Þetta er mánuður númer 11")
elif nafnmanadar == "desember":
    print("Þetta er mánuður númer 12")
else:
    print("Þekki ekki þennan mánuð")
"""
"""
#liður 3 - verkefni if elif else

aldurnot = int(input("sláður inn aldur"))

if aldurnot >= 0 and aldurnot < 7:
    print("nú svo þú ferð að byrja í skóla")
elif aldurnot >= 7 and aldurnot < 16:
    spurning = input("ætlaru í menntaskóla já eða nei")
    if spurning == "já":
        print("frábært hjá þér")
    elif spurning == "nei":
        print("þú ættir kannski að huga að því")
    else:
        print("verður að svara já eða nei")
elif aldurnot >= 16 and aldurnot < 106:
    print("gangi þér vel í framtíðinni")
else:
    print("þú hefur svarað spurningunni vitlaust")
    
"""

#Liður 4 - verkefni if elif else

tala = int(input("Sláðu inn tölu á bilinu 0-25"))
if tala < 0 and tala > 25:
    print("rangur innsláttur")
else:
    margfeldi = float(tala * 1.7)
    print(margfeldi)