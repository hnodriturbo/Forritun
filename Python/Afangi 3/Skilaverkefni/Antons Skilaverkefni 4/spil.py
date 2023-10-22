# Skilaverkefni 3 - Liður 2
# 22/09/2023 - 12/10/2023
# Anton Smári Gunnarsson

# Klasi fyrir ógilt spil exception eins og um var rætt okkar á milli
class OgiltSpilException(Exception):
    pass

# Klasi fyrir Spil
class Spil:
    # Sortir í boði
    HJARTA = 0
    SPADI = 1
    TIGULL = 2
    LAUF = 3

    TROMP = -1

    # Sortir í boði (textastrengir til útprentunar)
    SORTIR = ['♥ Hjarta', '♠ Spaða', '♦ Tígul', '♣ Laufa']
    SORTIR_2 = ['♥ Hjarta', '♠ Spaði', '♦ Tígull', '♣ Lauf']

    spilaTala: int
    spilaTegund: int

    spilaStig: int

    # Hér er spilið búið til
    def __init__(self, spilaTala, spilaTegund):
        if spilaTala < 2 or spilaTala > 14:
            raise OgiltSpilException("Ógilt nr spils, má bara vera frá 1 til 13!")

        if spilaTegund not in [Spil.HJARTA, Spil.SPADI, Spil.TIGULL, Spil.LAUF]:
            raise OgiltSpilException("Ógild tegund spils, má bara vera Hjarta, Spaði, Tígull eða Lauf...")

        self.spilaTala = spilaTala
        self.spilaTegund = spilaTegund

        if self.spilaTala == 10:
            self.spilaStig = 10
        elif self.spilaTala == 11:
            self.spilaStig = 20
        elif self.spilaTala == 12:
            self.spilaStig = 30
        elif self.spilaTala == 13:
            self.spilaStig = 40
        elif self.spilaTala == 14:
            self.spilaStig = 50
        else:
            self.spilaStig = 0

    # Svona er spilið convertað í streng
    def __str__(self):
        if self.spilaTala == 11:
            prentTala = "Gosi"
        elif self.spilaTala == 12:
            prentTala = "Drottning"
        elif self.spilaTala == 13:
            prentTala = "Kóngur"
        elif self.spilaTala == 14:
            prentTala = "Ás"
        else:
            prentTala = str(self.spilaTala)

        return self.SORTIR[self.spilaTegund] + " " + prentTala

    # Hér eru stig spilsins reiknuð út
    def __int__(self):
        return self.spilaStig

    # Þetta er samanburðarfall til að sannreyna að Spil(11, Spil.HJARTA) == Spil(11, Spil.HJARTA) þó þau séu ekki sama tilvikið af spilinu
    def __eq__(self, annadSpil):
        if not isinstance(annadSpil, Spil):
            return False
        return self.spilaTala == annadSpil.spilaTala and self.spilaTegund == annadSpil.spilaTegund

    # Þetta er notað til þess að bera saman heilu settin af spilum á auðveldan hátt
    def __hash__(self):
        return hash((self.spilaTegund, self.spilaTala))

    # Hér er reiknað út hver vinnur hvern slag, 0 er sá sem setti út fyrst á meðan 1 er sá sem þurfti að svara fyrir sig
    def hverVinnur(self, annadSpil):
        if self.spilaTegund == Spil.TROMP and annadSpil.spilaTegund == Spil.TROMP:
            if self.spilaTala > annadSpil.spilaTala:
                return 0
            else:
                return 1
        elif self.spilaTegund == Spil.TROMP and annadSpil.spilaTegund != Spil.TROMP:
            return 0
        elif self.spilaTegund != Spil.TROMP and annadSpil.spilaTegund == Spil.TROMP:
            return 1
        elif self.spilaTegund == annadSpil.spilaTegund:
            if self.spilaTala > annadSpil.spilaTala:
                return 0
            else:
                return 1
        else:
            return 0