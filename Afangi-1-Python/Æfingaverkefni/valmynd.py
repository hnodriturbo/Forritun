########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########

try:
        
    while True:

        print("1. Prenta út alla í skránni")
        print("2. Bæta við notanda í skránna")
        print("3. Heildaraldur")
        print("4. Yngri en 50 ára")
        print("5. Símanúmer sem byrjar á 8")
        
        print("\n0. Hætta")

        val = input("Hvað viltu gera?")

        if val == "1":
            pass

        elif val == "2":
            pass

        elif val == "3":
            pass

        elif val == "4":
            pass

        elif val == "5":
            pass

        elif val == "0":
            break
        else:
            print("þú hefur ekki valið rétt")

    print("Takk fyrir að nota forritið mitt")

except Exception as error:
    print(f"Það hefur komið upp einhver villa. Gripin villa : \n{error}")