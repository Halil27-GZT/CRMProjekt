# Dein Kundenmanagement-System

kunden = {} # Ein Dictionary zum Speichern der Kunden. Schlüssel: Kundenname, Wert: Dictionary mit Details

def kunden_anzeigen():
    if not kunden:
        print("Der Katalog ist leer.")
        return

    print("\n--- Deine Kundenliste ---")
    for name, details in kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_hinzufuegen():
    print("\n--- Kunden hinzufügen ---")
    name = input("Name des Kunden: ")
    email = input("E-Mail des Kunden: ")
    telefon = input("Telefonnummer des Kunden: ")

    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return

    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")

def kunde_suchen():
    print("\n--- Kunden suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff (Name oder E-Mail) ein: ").lower()
    gefundene_kunden = {}

    for name, details in kunden.items():
        if suchbegriff in name.lower() or suchbegriff in details.get('email', '').lower():
            gefundene_kunden[name] = details

    if not gefundene_kunden:
        print(f"Keine Kunden gefunden, die '{suchbegriff}' im Namen oder in der E-Mail enthalten.")
        return

    print(f"\n--- Gefundene Kunden für '{suchbegriff}' ---")
    for name, details in gefundene_kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_aktualisieren():
    print("\n--- Kunden aktualisieren ---")
    name_zu_aktualisieren = input("Name des zu aktualisierenden Kunden: ")

    if name_zu_aktualisieren not in kunden:
        print(f"Fehler: Kunde '{name_zu_aktualisieren}' nicht im Katalog gefunden.")
        return

    print(f"Aktuelle Daten für {name_zu_aktualisieren}:")
    print(f"  E-Mail: {kunden[name_zu_aktualisieren]['email']}")
    print(f"  Telefon: {kunden[name_zu_aktualisieren]['telefon']}")

    neue_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
    neue_telefon = input("Neue Telefonnummer (leer lassen für keine Änderung): ")

    if neue_email:
        kunden[name_zu_aktualisieren]['email'] = neue_email
    if neue_telefon:
        kunden[name_zu_aktualisieren]['telefon'] = neue_telefon

    print(f"Kunde '{name_zu_aktualisieren}' wurde aktualisiert.")

def kunde_loeschen(): # NEU
    print("\n--- Kunden löschen ---")
    name_zu_loeschen = input("Name des zu löschenden Kunden: ")
    if name_zu_loeschen in kunden:
        del kunden[name_zu_loeschen]
        print(f"Kunde '{name_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Kunde '{name_zu_loeschen}' nicht im Katalog gefunden.")

def zeige_menue():
    print("\n--- CRM Menü ---")
    print("1. Kunde hinzufügen")
    print("2. Kunden anzeigen")
    print("3. Kunde suchen")
    print("4. Kunde aktualisieren")
    print("5. Kunde löschen") # GEÄNDERT
    print("6. Beenden")      # GEÄNDERT
    print("----------------")

def main():
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            kunde_hinzufuegen()
        elif wahl == '2':
            kunden_anzeigen()
        elif wahl == '3':
            kunde_suchen()
        elif wahl == '4':
            kunde_aktualisieren()
        elif wahl == '5': # GEÄNDERT
            kunde_loeschen()
        elif wahl == '6': # GEÄNDERT
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()


# Test der Funktion (wird später durch ein Menü ersetzt)
# kunde_hinzufuegen()
# kunden_anzeigen()

