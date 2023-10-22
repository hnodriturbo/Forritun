########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
############## Ágúst 2023 ##############

import csv

# Klasinn Verkalýðsfélag
class verkalydsfelag:
    def __init__(self, nr, nafn, kennitala, laun):
        self.nr = nr
        self.nafn = nafn
        self.kennitala = kennitala
        self.laun = laun
        
    def __str__(self) -> str:
        return f"Félagsnúmer: {self.nr}\nNafn: {self.nafn}\nKennitala: {self.kennitala}\nLaun: {self.laun}\n"

    # Bætti þessum við til að gera afrit - nota í breyta meðlim hlutanum
    def copy(self):
        return verkalydsfelag(self.nr, self.nafn, self.kennitala, self.laun)
    
    
    def skatt(self):
        return int(self.laun) * 0.36

    
    def utborgud_laun(self):
        result = int(self.laun) - self.skatt()
        return f"{result:.1f}"
    

# Gerði klasa sem opnar skránna og skrifar skránna
class medhondlaSkra:
    def opnaSkra(skra):
        felagsmennObjectListi = []
        with open(skra, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                felagsmennObjectListi.append(verkalydsfelag(*row))
            return felagsmennObjectListi

    def skrifaSkra(felagsmennObjectListi, skra):
        with open(skra, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nr", "Nafn", "Kennitala", "Laun"])
            for felagsmadur in felagsmennObjectListi:
                writer.writerow([felagsmadur.nr,felagsmadur.nafn, felagsmadur.kennitala, felagsmadur.laun])
        return True




