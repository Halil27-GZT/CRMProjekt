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

    # Überprüfe, ob der Kunde bereits existiert (Annahme: Name ist eindeutig)
    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return # Beende die Funktion, wenn der Kunde schon da ist

    # Füge den neuen Kunden zum 'kunden'-Dictionary hinzu
    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")

# Test der Funktion (wird später durch ein Menü ersetzt)
kunde_hinzufuegen()
kunden_anzeigen()

