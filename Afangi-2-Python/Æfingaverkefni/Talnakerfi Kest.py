# ---------------     Hreiðar Pétursson     ---------------
# ---- 14 apríl 2023 Sem er afmælisdagurinn minn!!!! vúp vúp ! -----
#---------------  Talnakerfi - Kerfisstjórnum  ------------

valmynd = True
while valmynd == True:
    print("Velkominn í talnakerfisreiknivélina mína")
    print("Skrifaðu hjálp til að fá hjálp")
    print("Sláðu inn 0 til að hætta")
    teljari = 1
    strengur = input("Sláðu inn hvað þú vilt reikna")
    for x in strengur:
        if x == " ":
            teljari += 1
    if strengur == "hjálp":
        print("Notkun: <bin|oct|dec|hex> <tala> <bin|oct|dec|hex")
        print("Dæmi um rétt slegið inn: bin 1001 dec")
    elif strengur == "0":
        valmynd = False
    elif teljari != 3:
        print("Lengd inntaksins verður að vera rétt. 3 mismundandi strengir")
    else:
        try:
            fyrstaord = strengur.split(" ")[0]
            annadord = strengur.split(" ")[1]
            thridjaord = strengur.split(" ")[2]
            if fyrstaord == thridjaord:
                print("ekki skrifa sama orð")
            elif fyrstaord in ["bin", "oct", "dec", "hex"] and thridjaord in ["bin", "oct", "dec", "hex"]:
                if fyrstaord == "bin":
                    if thridjaord == "dec":
                        tala = int(annadord, 2)
                        print("binary talan", annadord, "er:", tala, "í tíundakerfinu(dec)")
                    elif thridjaord == "oct":
                        tala = int(annadord, 2)
                        tala2 = oct(tala)
                        tala3 = tala2.replace("0o","")
                        print("Binary talan", annadord,"er",tala3,"í áttundakerfinu")
                    elif thridjaord == "hex":
                        tala = int(annadord, 2)
                        tala2 = hex(tala)
                        tala3 = tala2.replace("0x","")
                        print("Binary talan", annadord,"er",tala3,"í sextándakerfinu")
                elif fyrstaord == "oct":
                    if thridjaord == "bin":
                        tala = int(annadord, 8)
                        tala2 = bin(tala)
                        tala3 = tala2.replace("0b","")
                        print("Áttundakerfistalan",annadord,"er:",tala3,"í tvíundakerfinu")
                    elif thridjaord == "dec":
                        tala = int(annadord,8)
                        print("Áttundakerfistalan",annadord,"er:",tala,"í tíundakerfinu")
                    elif thridjaord == "hex":
                        tala = int(annadord, 8)
                        tala2 = hex(tala)
                        tala3 = tala2.replace("0x","")
                        print("Áttundakerfistalan",annadord,"er:",tala3,"í sextándakerfinu")
                elif fyrstaord == "dec":
                    if thridjaord == "bin":
                        tala = int(annadord, 10)
                        tala2 = bin(tala)
                        tala3 = tala2.replace("0b","")
                        print("Tíundakerfistalan",annadord,"er:",tala3,"í tvíundakerfinu")
                    elif thridjaord == "oct":
                        tala = int(annadord, 10)
                        tala2 = oct(tala)
                        tala3 = tala2.replace("0o","")
                        print("Tíundakerfistalan",annadord,"er:",tala3,"í áttundakerfinu")
                    elif thridjaord == "hex":
                        tala = int(annadord, 10)
                        tala2 = hex(tala)
                        tala3 = tala2.replace("0x","")
                        print("Tíundakerfistalan",annadord,"er:",tala3,"í sextándakerfinu")
                elif fyrstaord == "hex":
                    if thridjaord == "bin":
                        tala = int(annadord, 16)
                        tala2 = bin(tala)
                        tala3 = tala2.replace("0b","")
                        print("Sextándakerfistalan",annadord,"er:",tala3,"í tvíundakerfinu")
                    elif thridjaord == "oct":
                        tala = int(annadord, 16)
                        tala2 = oct(tala)
                        tala3 = tala2.replace("0o","")
                        print("Sextántakerfistalan",annadord,"er:",tala3,"í áttundakerfinu")
                    elif thridjaord == "dec":
                        tala = int(annadord, 16)
                        print("Sextándakerfistalan",annadord,"er:",tala,"í tíundakerfinu")
            else:
                print("Annaðhvort",fyrstaord,"eða",thridjaord,"er ekki rétt slegið inn. Eða jafnvel bæði ?")
        except ValueError:
            print("Ógilt inntak. Vinsamlegast sláðu inn viðeigandi tölur")

print("Takk fyrir að nota reiknivélina mína")


