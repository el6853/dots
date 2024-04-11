class Känny:
    def __init__(self, merkki, malli, vuosi):
        self.merkki = merkki
        self.malli = malli
        self.vuosi = vuosi
        self.akku = 100

    def someta(self):
        if self.akku > 0:
            self.akku -= 10
            return True
        else:
            return False

    def tubeta(self):
        if self.akku > 0:
            self.akku -= 20
            return True
        else:
            return False

    def lataa(self):
        if self.akku < 100:
            self.akku += 30
            return True
        else:
            return False



class Kahvinkeitin:
    def __init__(self, valmistaja, malli, teho):
        self.valmistaja = valmistaja
        self.malli = malli
        self.teho = teho
        self.päällä = False

    def keitä_kahvia(self):
        if not self.päällä:
            print("Kahvinkeitin ei ole päällä. Käynnistä se ensin.")
        else:
            print("Kahvia valmistetaan...")

    def käynnistä(self):
        if self.päällä:
            print("Kahvinkeitin on jo päällä.")
        else:
            self.päällä = True
            print("Kahvinkeitin on käynnistetty.")

    def sammuta(self):
        if not self.päällä:
            print("Kahvinkeitin on jo sammutettu.")
        else:
            self.päällä = False
            print("Kahvinkeitin on sammutettu.")