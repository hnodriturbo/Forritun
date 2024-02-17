    
def opnaSkra():
    felagsmennObjectListi = []
    #Þetta fall opnar skránna
    #les skránna og býr til tilvik(object) úr hverri línu skráarinnar og
    #setur í lista. listinn inniheldur þá hluti sem gerðir eru úr klasanum
    #verkalýsfélag
    #fallilð skilar síðan lista af félagsmönnum
    try:
        with open("verkalydsfelag.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader) # Skippa efstu röðinni
            for row in reader:
                nr = row[0]
                nafn = row[1]
                kennitala = row[2]
                laun = row[3]
                felagsmadur = Skil2_class.verkalydsfelag(nr, nafn, kennitala, laun)
                felagsmennObjectListi.append(felagsmadur)
                
        # Returna félagsmönnunum sem objects í lista
        return felagsmennObjectListi
    
    # Ef það kemur villa kasta ég henni yfir í hitt skjalið
    except Exception as error:
        raise error
    # Skrifa listann í skránna
def skrifaSkra(felagsmennObjectListi):
    try: 
        with open("verkalydsfelag.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nr", "Nafn", "Kennitala", "Laun"])
            for felagsmadur in felagsmennObjectListi:
                nr = felagsmadur.nr
                nafn = felagsmadur.nafn
                kennitala = felagsmadur.kennitala
                laun = felagsmadur.laun
                writer.writerow([nr, nafn, kennitala, laun])
        
        # Ef allt gengur upp þá returna ég fallinu sem True
        return True
    
    # Raise error og kasta því yfir í try-execptið sem er í program skránni           
    except Exception as error:
        raise error