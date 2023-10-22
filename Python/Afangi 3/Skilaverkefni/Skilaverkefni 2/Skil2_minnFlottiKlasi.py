import Skil2_class
# Flotti klasinn minn - Hér bjó ég til hin ýmsu föll sem eru í sumum tilfellum
# kjarni keyrðs falls. Bjó til velja félaga prógram, validation program,
# breyta meðlim prógram og það flottasta og besta er leitarvélin sem ég gerði
class minnKlasi:
    
    # Sækja hæðsta númer af félagsmanni og skila einni tölu hærra
    def get_haedsta_nr(felagsmennObjectListi):
        haedsta_nr = int(felagsmennObjectListi[-1].nr)
        haedsta_nr += 1
        return haedsta_nr
    
    # föll sem sækja upplýsingar í gegnum input og validate-a input
    def get_nafn():
        nafn = minnKlasi.get_input(
        "Vinsamlegast sláðu inn fullt nafn : ", 
        "Þú verður að stimpla inn nafn (bara stafir leyfðir) : ",
        minnKlasi.validate_nafn 
        )
        return nafn
    def get_kt():
        kt = minnKlasi.get_input(
        "Vinsamlegast sláðu inn kennitölu : ",
        "Verður að slá inn kennitölu á réttu formi - 10 tölustafir (ath ekkert bandstrik leyft) : ",
        minnKlasi.validate_kt
        ) 
        return kt
    def get_laun():
        laun = minnKlasi.get_input(
        "Vinsamlegast sláðu inn laun : ",
        "Verður að slá inn laun á töluformi : ",
        minnKlasi.validate_tala
        )
        return laun
    def get_tala():
        tala = minnKlasi.get_input(
            "Vinsamlegast sláðu inn tölu : ",
            "Verður að slá inn tölu á töluformi : ",
            minnKlasi.validate_tala
        )
        return tala
    
    # Prompta input þangað til user skrifar inn valid gildi
    def get_input(spurning, villuskilabod, validation=None):
        value = input(spurning)
        while not value or (validation and not validation(value)):
            value = input(villuskilabod)
        return value
    
    # Validate velja meðlim
    def validate_val(val):
        return val.isdigit()
    
    # Validate nafn - Splitta orðunum í nafninu og ath hvert orð hvort það sé alpha
    def validate_nafn(nafn):
        for ord in nafn.split(" "):
            if not ord.isalpha():
                return False
        return True
    
    # Validate kennitala - Returnar True ef kt er isdigit og lengd 10 tölustafir
    def validate_kt(kt):
        return kt.isdigit() and len(kt) == 10
    
    # Validate laun - Returnar True ef stimpluð laun eru í tölustafaformi
    def validate_tala(tala):
        return tala.isdigit()

        
    # Fallið mitt sem fær data um nýjann félagsmann
    def add_medlimur_program(haedsta_nr):
        while True:
            print('\nVelkomin/n í "bæta við félagsmanneskju" hlutann\n')
            
            nafn = minnKlasi.get_nafn()
            kt = minnKlasi.get_kt()
            laun = minnKlasi.get_laun()
            
            felagsmannaUpplysingar = [nafn, kt, laun]
                 
            print(f"\nTakk fyrir ! Þú slóst inn þessar upplýsingar :\n")
            print(f"Nafn : {felagsmannaUpplysingar[0]}")
            print(f"Kennitala : {felagsmannaUpplysingar[1]}")
            print(f"Laun : {felagsmannaUpplysingar[2]}")
            
            stadfesta = input("\nVeldu 1 til að staðfesta\nVeldu 2 til að byrja uppá nýtt\nVeldu 9 til að hætta við")
            while stadfesta not in ["1","2","9"]:
                stadfesta = input("\nVerður að velja! 1 = Staðfesta || 2 = Byrja uppá nýtt || 9 = hætta")
            if stadfesta == "1":
                nyr_felagsmadur = [str(haedsta_nr), *felagsmannaUpplysingar]
                return nyr_felagsmadur
            elif stadfesta == "2":
                continue
            elif stadfesta == "9":
                return False
            
    # Fallið mitt sem er til að velja félagsmann úr listanum og skila honum
    def velja_medlim_program(felagsmennObjectListi):
        while True:
            print("\nVelkomin/n í að velja meðlim prógrammið! Hér er listi til að velja úr")
            for felagsmadur in felagsmennObjectListi:
                print(felagsmadur)
            valMedlimsNr = minnKlasi.get_input(
                "\nVinsamlegast veldu númer meðlims sem þú vilt velja: (Getur valið 0 til að hætta)",
                "\nÞú verður að slá inn númer á töluformi",
                minnKlasi.validate_val
                # Nota lambda hér svo ég geti sett tvær færibreytur sem eina
                # lambda value: minnKlasi.validate_val(value, len(felagsmennObjectListi))
            )
            
            if valMedlimsNr == "0":
                print("\nÞú hefur hætt við að velja meðlim")
            else:
                #valMedlimsNr = int(valMedlimsNr)
                felagsmadurObject = None
                for felagsmadur in felagsmennObjectListi:
                    if felagsmadur.nr == valMedlimsNr:
                        felagsmadurObject = felagsmadur
                        break
                if felagsmadurObject == None:
                    print(f"\nÞað er ekki til félagsmaður með nr {valMedlimsNr}, vinsamlegast reyndu aftur")
                    input(f"Ýttu á einhvern takka til að halda áfram og reyna aftur")
                    continue
                           
                print(f"\nÞú valdir :\n{felagsmadurObject}")
                stadfestaVal = input("\nVeldu 1 til að staðfesta valið\nVeldu 2 til að velja annan aðila\nVeldu 9 til að hætta")
                while stadfestaVal not in ["1","2","9"]:
                    stadfestaVal = input("Verður að velja annaðhvort 1, 2 eða 9")
                if stadfestaVal == "1":
                    return felagsmadurObject
                elif stadfestaVal == "2":
                    continue
                elif stadfestaVal == "9":
                    print("\nÞú valdir að hætta")
                    return False
     
    # Fallið mitt sem breytir félagsmanni
    def breyta_medlim_program(valinnFelagsmadur):
        # Byrja á að taka afrit ef user vill hætta við breytingarnar
        valinnFelagsmadurCopy = valinnFelagsmadur.copy()
        
        while True:
            print(f"\nVelkomin/n í 'Breyta félagsmanni' prógrammið mitt.\n")
            print(f"Veldu 1 til að breyta nafni (Núverandi nafn: {valinnFelagsmadur.nafn})")
            print(f"Veldu 2 til að breyta kennitölu (Núverandi kennitala: {valinnFelagsmadur.kennitala})")
            print(f"Veldu 3 til að breyta launum (Núverandi laun: {valinnFelagsmadur.laun})")
            print(f"\nVeldu 9 til að hætta og staðfesta breytingarnar")
            print(f"Veldu 0 til að hætta án þess að vista breytingar sem hafa mögulega verið gerðar")
            
            valBreyting = input("\nVeldu hvað þú vilt gera :")
            while valBreyting not in ["1","2","3","9","0"]:
                valBreyting = input("\nVerður að velja tölurnar 1,2,3 eða 9 :")
                            
            if valBreyting == "1":
                nafn = minnKlasi.get_nafn()
                valinnFelagsmadur.nafn = nafn
                print(f"\nNafni félagsmanns hefur verið breytt í {valinnFelagsmadur.nafn}")
            elif valBreyting == "2":
                kt = minnKlasi.get_kt()
                valinnFelagsmadur.kennitala = kt
                print(f"\nKennitölu félagsmanns hefur verið breytt í {valinnFelagsmadur.kennitala}")
            elif valBreyting == "3":
                laun = minnKlasi.get_laun()
                valinnFelagsmadur.laun = laun
                print(f"\nLaunum félagsmanns hefur verið breytt í {valinnFelagsmadur.laun}")
            elif valBreyting == "9":
                return True
            elif valBreyting == "0":
                valinnFelagsmadur = valinnFelagsmadurCopy
                return False
            
     
    # Flotta fallið mitt (eitt af þeim allavega)
    # Ég ákvað að búa til eins fullkomna leitarvél og ég gat búið til. Er stoltur af henni og reyndi koma öllu í eins fáar línur og ég gat mögulega
    def Flotta_Leitarvel_Hreidars(felagsmennObjectListi, nafn=None,nr=None,kt=None,laun_min=None,laun_max=None):
        leitarnidurstodur = []
        for felagsmadur in felagsmennObjectListi:
            if(nafn and nafn.lower() in felagsmadur.nafn.lower()) or \
                (nr and nr in felagsmadur.nr) or \
                    (kt and kt in felagsmadur.kennitala) or \
                        (laun_min is not None and laun_max is not None and laun_min <= int(felagsmadur.laun) <= laun_max):
                            leitarnidurstodur.append(felagsmadur)
        return leitarnidurstodur
    
    # Prógram leitarvélarinnar minnar
    def flotta_leitarvelin_min_program():
        while True:
            felagsmennObjectListi = Skil2_class.medhondlaSkra.opnaSkra("verkalydsfelag.csv")
            print("\nVelkomin/n í leitarvélina mína.")
            print("\n1. Leita eftir númeri")
            print("2. Leita eftir nafni")
            print("3. Leita eftir kennitölu")
            print("4. Leita eftir launum á einhverju bili")
            val = input("Veldu nú (veldu 0 til að hætta)")
            while val not in ["1","2","3","4","0"]:
                val = input("verður að velja einhvern kostinn")
            if val == "1":
                print("Sláðu inn nr félagsmanns eða bara hluta af því")
                leit = minnKlasi.get_tala()
                leitarnidurstada = minnKlasi.Flotta_Leitarvel_Hreidars(felagsmennObjectListi, None, leit, None, None, None)
                minnKlasi.print_results(leitarnidurstada,"Nr:", leit, None)
            elif val == "2":
                print("Getur slegið inn hluta úr nafni líka")
                leit = minnKlasi.get_nafn()
                leitarnidurstada = minnKlasi.Flotta_Leitarvel_Hreidars(felagsmennObjectListi, leit, None, None, None, None)
                minnKlasi.print_results(leitarnidurstada, "Nafn:", leit, None)
            elif val == "3":
                print("Sláðu inn heila kennitölu eða bara hluta af henni")
                leit = minnKlasi.get_tala()
                leitarnidurstada = minnKlasi.Flotta_Leitarvel_Hreidars(felagsmennObjectListi,None,None,leit,None,None)
                minnKlasi.print_results(leitarnidurstada, "Kennitala:", leit, None)
            elif val == "4":
                print("Þú valdir að leita að launum á bili. Sláðu inn tvær tölur og niðurstaðan verður öll laun á því bili")
                leit = int(minnKlasi.get_tala())
                leit2 = int(minnKlasi.get_tala())
                if leit < leit2:
                    laun_min = leit
                    laun_max = leit2
                elif leit > leit2:
                    laun_min = leit2
                    laun_max = leit
                else:
                    print("\nÞú slóst inn tvær sömu tölur og verður leitað í samræmi við það")
                leitarnidurstada = minnKlasi.Flotta_Leitarvel_Hreidars(felagsmennObjectListi,None,None,None,laun_min,laun_max)  
                minnKlasi.print_results(leitarnidurstada, "Laun:", leit, leit2)
            elif val == "0":
                break
            leita_aftur = input("Viltu leita aftur || 1=Já || 2=Nei ||")
            while leita_aftur not in ["1","2"]:
                leita_aftur = input("Viltu leita aftur || 1=Já || 2=Nei ||")
            if leita_aftur == "1":
                continue
            elif leita_aftur == "2":
                break
        print("Takk fyrir að nota leitarvélina mína!")
    
    # Fallið sem prentar út niðurstöðurnar
    def print_results(leitarnidurstada, leitarskilyrdi, leit, leit2):
        if not leitarnidurstada:
            print(f"\nÞað fannst enginn félagsmaður með leitarskilyrðinu: {leitarskilyrdi} - {leit} {leit2}")
        else:
            print(f"\nÞað fundust {len(leitarnidurstada)} niðurstöður.")
            for nr, felagsmadur in enumerate(leitarnidurstada):
                print(f"\nLeitarniðurstaða {nr+1}:")
                print(felagsmadur)  

    
    # Fann þetta lambda á netinu. Skil það ekki alveg en finn svona hæðstu útborgun laun
    # og hæðstu heildarlaun og lægstu útborguð laun. Nota þetta samt ekki  
    def haedstu_utborgud_laun(felagsmennObjectListi):
        return max(felagsmennObjectListi, lambda felagsmadur: felagsmadur.utborgud_laun())
    
    def haedstu_heildarlaun(felagsmennObjectListi):
        return max(felagsmennObjectListi, lambda felagsmadur: felagsmadur.laun)
    
    def laegstu_utborgud_laun(felagsmennObjectListi):
        return min(felagsmennObjectListi, lambda felagsmadur: felagsmadur.utborgud_laun())
    