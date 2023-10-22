########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########
 
from datetime import datetime

 # Nema klasinn
class nemi:
  def __init__(self, kennitala, nafn, kyn, simanumer) -> None:
    self.kennitala = kennitala
    self.nafn = nafn
    self.kyn = kyn
    self.simanumer = simanumer
    
  def __str__(self) -> str:
    return f"Kennitala: {self.kennitala}\nNafn: {self.nafn}\nKyn: {self.kyn}\nSímanúmer: {self.simanumer}"
  
  def setKennitala(self, kennitala):
    self.kennitala = kennitala

  def setNafn(self, nafn):
    self.nafn = nafn
    
  def setKyn(self, kyn):
    self.kyn = kyn
  
  def setSimanumer(self, simanumer):
    self.simanumer = simanumer
    
  def getKennitala(self):
    return self.kennitala
  
  def getNafn(self):
    return self.nafn
  
  def getKyn(self):
    return self.kyn

  def getSimanumer(self):
    return self.simanumer
    
    

class hermannanemi(nemi):
  hermannanemar = []
  
  def __init__(self, kennitala, nafn, kyn, simanumer, adstandandi, bekkur, onn) -> None:
    super().__init__(kennitala, nafn, kyn, simanumer)
    self.adstandandi = adstandandi
    self.bekkur = bekkur
    self.onn = onn
    
    # Ég var læra að með því að appenda hverju instance sem er búið til af hermannanemi þá er alltaf 
    # til listi sem er fullur af öllum instönsum sem til eru
    hermannanemi.hermannanemar.append(self)
  
  def __str__(self) -> str:
    parent_string = super().__str__()
    return f"\n{parent_string}\nAðstandandi: {self.adstandandi}\nBekkur: {self.bekkur}\nÖnn: {self.onn}"
  
  def to_list(self):
        return [self.kennitala, self.nafn, self.kyn, self.simanumer, self.adstandandi, self.bekkur, self.onn]
  
  def setAdstandandi(self, adstandandi):
    self.adstandandi = adstandandi
    
  def setBekkur(self, bekkur):
    self.bekkur = bekkur
  
  def setOnn(self, onn):
    self.onn = onn
  
  def getAdstandandi(self):
    return self.adstandandi
  
  def getBekkur(self):
    return self.bekkur
  
  def getOnn(self):
    return self.onn

  # Mér finnst þetta fall eigi að vera hérna innan í klasanum
  def telja_kyn(instance_data):
    kk_listi = []
    kvk_listi = []
    other_listi = []
    kyn = {"kk": 0, "kvk": 0, "other": 0}
    for hermannanemi in instance_data:
        kyn_herm = hermannanemi.kyn
        if kyn_herm == 'kk':
            kyn['kk'] += 1
            kk_listi.append(hermannanemi)
        elif kyn_herm == 'kvk':
            kyn['kvk'] += 1
            kvk_listi.append(hermannanemi)
        else:
            kyn['other'] += 1
            other_listi.append(hermannanemi)
    print(f"\nÞað eru {kyn['kk']} KK í hópnum")
    print(f"\nÞað eru {kyn['kvk']} KVK í hópnum")
    print(f"\nÞað eru {kyn['other']} Other í hópnum")
    return kk_listi, kvk_listi, other_listi

    
  
  
  
class flokkstjoranemi(nemi):
  def __init__(self, kennitala, nafn, kyn, simanumer, her, herdeild='Landher') -> None:
    super().__init__(kennitala, nafn, kyn, simanumer)
    self.herdeild = herdeild
    self.her = her
  def __str__(self) -> str:
    parent_string = super().__str__()
    return f"\n{parent_string}\nHerdeild: {self.herdeild}\nHer: {self.her}"

  def to_list(self):
      return [self.kennitala, self.nafn, self.kyn, self.simanumer, self.her, self.herdeild]

  def setHer(self, her):
    self.her = her
  
  def setHerdeild(self, herdeild):
    self.herdeild = herdeild
  
  def getHer(self):
    return self.her
  
  def getHerdeild(self):
    return self.herdeild
  
  # Mér finnst þetta eiga líka að vera innan í klasanum
  def finnaAldur(self):
    kennitala = self.kennitala

    nuverandi_ar = datetime.now().year
    
    faedingarar = kennitala[4:6]
    fyrstiTolustafur = faedingarar[0]
    faedingarar = int(faedingarar)
    fyrstiTolustafur = int(fyrstiTolustafur)
    if fyrstiTolustafur < 3:
        faedingarar += 1900
    else:
        faedingarar += 2000
    aldur = faedingarar - nuverandi_ar
    
    return aldur


  
class foringjanemi(nemi):
  def __init__(self, kennitala, nafn, kyn, simanumer, stigNams, namslaun, herlan) -> None:
    super().__init__(kennitala, nafn, kyn, simanumer)
    self.stigNams = stigNams
    self.namslaun = namslaun
    self.herlan = herlan
  def __str__(self) -> str:
    parent_string = super().__str__()
    return f"\n{parent_string}\nStig Náms: {self.stigNams}\nNámslaun: {self.namslaun}\nHerlán: {self.herlan}"
  
  # Nota þetta til að setja instance í sér lista til að auðvelda að skrifa instönsin í skránna aftur
  def to_list(self):
        return [self.kennitala, self.nafn, self.kyn, self.simanumer, self.stigNams, self.namslaun, self.herlan]
      
  def setStigNams(self, stigNams):
    self.stigNams = stigNams
    
  def setNamslaun(self, namslaun):
    self.namslaun = namslaun
    
  def setHerlan(self, herlan):
    self.herlan = herlan
    
  def getStigNams(self):
    return self.stigNams
  
  def getNamslaun(self):
    return self.namslaun
  
  def getHerlan(self):
    return self.herlan