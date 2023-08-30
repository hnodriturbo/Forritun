#Hreiðar Pétursson
#5janúar2023
#Byrjun

nafnkk = input("Hvað heitir karlinn ?")
nafnkvk = input("Hvað heitir konan ?")
nafndrykkur = input("Hvað heitir drykkurinn")

print(nafnkk,"og",nafnkvk,"eru hjón")
print("óttalega mikil flón")
print("Þau eru bæði sæt og fín")
print("og þau drekka",nafndrykkur)


# Forrit tekur inn tvÃ¦r tÃ¶lur og leggur saman
# Notum format() til aÃ° forma strengin Ã­ print
tala1 = int(input("SlÃ¡Ã°u inn tÃ¶lu 1: "))
tala2 = int(input("SlÃ¡Ã°u inn tÃ¶lu 2: "))
print("({} + {}) = {}".format(tala1,tala2,tala1+tala2))
#print("(",tala1," + ",tala2,") =",tala1+tala2)
"""
"""
# Forrit sem tekur inn lengd Ã­ cm og finnur
# fjÃ¶lda metra, dm og cm Ã­ lengdinni
tala = int(input("SlÃ¡Ã°u inn lengd Ã­ cm: "))

m = tala // 100 # athuga hversu margir metrar er
print(m ," metrar")

tala = tala % 100 # tek Ã­ burtu meter
dm = tala // 10
print(dm ," desimetrar")

tala = tala % 10 # tek Ã­ burtu desimetrar og Ã¾Ã¡ standa eftir centimetrar
print(tala ," centimetrar")