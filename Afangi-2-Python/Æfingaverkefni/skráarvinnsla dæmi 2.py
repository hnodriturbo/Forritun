notendur=[]# skilgreini listann
with open("files/lykilord.txt", "r", encoding="utf-8") as file:
    skra = file.read()#les innihald textaskráinnar
    print(skra)#gott að skoða þetta
    notendur = skra.split("\n")# býr til lista. Hér nafn og lykilorð
    #print(notendur)# gott að skoða þetta
    notendur.pop()

listi=[]#listi af listum
for lina in notendur:
    listi.append(lina.split(";"))#splitum listann notendur á ";" og búum til lista af listum
#print(listi)#gott að skoða þetta

print("listi", listi)

# # Setja í texta skrá:
# for lina in notendur:
#     print(lina)
    
#     lina.strip()
#     listi.append(lina.split(";"))#splitum listann notendur á ";" og búum til lista af listum
# listi.pop()
# # print(listi)#gott að skoða þetta
# #setja í skránna


listi.append(a)
#Skrifa allan listann í skránna
with open("files/lykilord.txt","w",encoding="utf-8") as f:
    for x in listi:
        f.write(x[0]+";"+x[1]+"\n")
print("Bættum við í skránna...")
"""
#Bæta við skrá:
with open("files/lykilord.txt","a",encoding="utf-8") as f:
    for x in listi:
        f.write(x[0]+";"+x[1]+"\n")
"""