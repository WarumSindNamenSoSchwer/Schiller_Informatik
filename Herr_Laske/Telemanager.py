import pickle

class Telemanager:
    def __init__(self, datei: str) -> None:
        self.datei: str = datei
        self.telefonbuch: dict = self.erzeug_telebuch(self.datei)
        self.begruesung()
        self.menue()

    def begruesung(self) -> None:
        print("+--------------------------+\n|Willkommen im Telemanager!|\n+--------------------------+\n")

    
    def telenummer_hinzufügen(self) -> None:

        while True:
            
            name: str = input("Geben sie den Namen ein: ")
            if name in self.telefonbuch.keys():
                print("Es gibt schon eine Person mit diesem Namen.")

                wahl = input("Wollen sie die Nummer wechseln? (y/n):")
                if wahl in "yY":
                    telefonnummer: str = input("Geben sie die neue Nummer ein: ")

                    self.telefonbuch[name] = telefonnummer
                else:
                    self.verabschiedung()
                    break
            else:               
                telefonnummer: str = input("Geben sie die dazugehoerige Telefonnummer ein: ")
                            
                self.telefonbuch[name] = telefonnummer
            
                print(str(self.telefonbuch)) 
        
                with open(self.datei, "wb") as datei:
                    pickle.dump(self.telefonbuch, datei)
                break
            
                                
    def verabschiedung(self):
        print("Danke für das Benutzen unseres Telemanagers!\nSchönen Tag noch.")


    def erzeug_telebuch(self, datei_name: str) -> dict:
        try:
            # Wenn Datei -> return daten aus datei als dict
            
            with open(datei_name, "rb") as geladene_datei:
                return pickle.load(geladene_datei)
        except:
            # Wenn keine Datei -> init Datei mit init_daten
            init_daten = {"Init_Name" : 000000000000}
            with open(self.datei, "wb") as datei:
                pickle.dump(init_daten, datei)
            return init_daten

    def zeige_telefonbuch(self) -> None:
        """Displays all contacts in a formatted table."""
        if not self.telefonbuch:
            print("Das Telefonbuch ist leer.")
        else:
            print("\n+----------------+----------------+")
            print("|     Name       | Telefonnummer  |")
            print("+----------------+----------------+")
            for name, nummer in self.telefonbuch.items():
                print(f"| {name:<14} | {nummer:<14} |")
            print("+----------------+----------------+\n")

    def menue(self) -> None:
        menue_text: str = """\nBitte waehlen Sie! :

(Z)eige das ganze Telefonbuch an
(R)ufe Telefonnummer auf        
(N)eue Telefonnummer        
(L)oesche Telefonnummer
(E)xit Programm

Ihre Wahl? : """

        wahl: str = "_"

        if len(self.telefonbuch) > 1:
            while wahl not in "eE":
                wahl = input(menue_text)

                #NOTE das ist zum debuggen
                print(f"User input: {wahl}")

                # (E)xit Programm
                if wahl in "eE":
                    self.verabschiedung()
                    break

                if wahl in "zZ":
                    self.zeige_telefonbuch()

                # (R)ufe Telefonnummer auf
                if wahl in "rR":
                    gesuchter_name: str = input("Geben Sie den Namen der gewuenschten Telefonnummer ein! : ")

                    if gesuchter_name in self.telefonbuch:
                        print(f"Die Nummer von '{gesuchter_name}' ist {str(self.telefonbuch[gesuchter_name])}")
                    else:
                        print(f"Der Name '{gesuchter_name}' ist nicht im Telefonbuch.")

                        wahl = input("\nWollen sie diesen hinzufügen? (y/n): ")

                        if wahl in "yY":
                            self.telenummer_hinzufügen()                            
                        else:
                            self.verabschiedung()                            
                            
                # (N)eue Telefonnummer
                if wahl in "nN":
                    self.telenummer_hinzufügen()

                # (L)oesche Telefonnummer
                if wahl in "lL":
                    wahl = input("\nWelchen Kontakt wollen sie entfernen?: ")
                    self.telefonbuch.pop(wahl, None) # Ohne None -> KeyError
                    print(f"{wahl} wurde gelöscht.")
                    with open(self.datei, "wb") as datei:
                        pickle.dump(self.telefonbuch, datei)

        else:
            
            wahl = input("\nDas Telefonbuch hat noch keine Einträge, wollen sie eine Nummer hinzufuegen? (y/n): ")
            
            if wahl in "yY":
                self.telenummer_hinzufügen()
                self.menue()
            else:
                self.verabschiedung()
            

def main():
    telemanager = Telemanager("Telefonbuch.json")

if __name__ == "__main__":
    main()
