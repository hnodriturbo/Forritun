#Hreiðar Pétursson
#8/6 2023
#Password Generator

import random

def buatilpassword(lengd):
    leyfdirstafir = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ123456789"
    password = ""
    for x in range(lengd):
        password += random.choice(leyfdirstafir)
    return password

spurjaumpasswordlengd = int(input("Hvað viltu hafa passwordið langt ?"))

buatilpassword2 = buatilpassword(spurjaumpasswordlengd)

print(buatilpassword2)