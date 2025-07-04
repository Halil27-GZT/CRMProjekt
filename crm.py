import json
import re # NEU: Für E-Mail-Validierung

"""
Ein einfaches Python-Programm zur Verwaltung eines Kundenmanagement-Systems (CRM).
Es ermöglicht das Hinzufügen, Anzeigen, Suchen, Aktualisieren und Löschen von Kunden
sowie das Speichern und Laden der Kundendaten in/aus einer JSON-Datei.
"""

# Dein Kundenmanagement-System
# Globale Variable zum Speichern der Kundendaten
# Schlüssel: Kundenname (String), Wert: Dictionary mit Kundendetails

kunden = {} # Ein Dictionary zum Speichern der Kunden. Schlüssel: Kundenname, Wert: Dictionary mit Details
DATEINAME = "kunden.json" # Dateiname für die Speicherung des Katalogs

def kunden_anzeigen():
    """
    Zeigt alle Kunden im aktuellen CRM-Katalog an.
    Gibt eine Meldung aus, wenn der Katalog leer ist.
    """
    if not kunden:
        print("Der Katalog ist leer.")
        return

    print("\n--- Deine Kundenliste ---")
    for name, details in kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_hinzufuegen(): # GEÄNDERT: Mit Validierung
    """
    Fügt einen neuen Kunden zum CRM-Katalog hinzu.
    Fragt den Benutzer nach Name, E-Mail und Telefonnummer.
    Validiert die Eingaben für E-Mail und Telefonnummer.
    Verhindert das Hinzufügen von Kunden mit bereits existierendem Namen.
    """
    print("\n--- Kunden hinzufügen ---")
    name = input("Name des Kunden: ")

    # Validierung für E-Mail: Schleife, bis ein gültiges Format eingegeben wird
    while True:
        email = input("E-Mail des Kunden: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email): # Einfache E-Mail-Validierung
            break
        else:
            print("Ungültiges E-Mail-Format. Bitte versuchen Sie es erneut.")

    # Validierung für Telefonnummer: Schleife, bis nur Ziffern (optional mit +) eingegeben werden
    while True:
        telefon = input("Telefonnummer des Kunden: ")
        if telefon.replace('+', '').isdigit() and (telefon.startswith('+') or not telefon.startswith('+')):
            break
        else:
            print("Ungültige Telefonnummer. Bitte geben Sie nur Ziffern ein (optional mit + am Anfang).")

    # Überprüfe, ob der Name bereits existiert, um Duplikate zu vermeiden
    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return
    # Speichere die Kundendetails als verschachteltes Dictionary
    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")

def kunde_suchen():
    """
    Sucht Kunden im Katalog basierend auf einem Teil des Namens oder der E-Mail-Adresse.
    Zeigt alle passenden Kunden mit ihren Details an.
    """
    print("\n--- Kunden suchen ---")
    # Suchbegriff in Kleinbuchstaben umwandeln für case-insensitive Suche
    suchbegriff = input("Geben Sie einen Suchbegriff (Name oder E-Mail) ein: ").lower()
    gefundene_kunden = {}
    # Iteriere durch alle Kunden im Katalog
    for name, details in kunden.items():
        # Überprüfe, ob der Suchbegriff im Namen oder in der E-Mail enthalten ist
        if suchbegriff in name.lower() or suchbegriff in details.get('email', '').lower():
            gefundene_kunden[name] = details
    # Wenn keine Kunden gefunden wurden, gib eine entsprechende Nachricht aus
    # Andernfalls zeige die gefundenen Kunden an
    if not gefundene_kunden:
        print(f"Keine Kunden gefunden, die '{suchbegriff}' im Namen oder in der E-Mail enthalten.")
        return

    print(f"\n--- Gefundene Kunden für '{suchbegriff}' ---")
    for name, details in gefundene_kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

def kunde_aktualisieren(): # GEÄNDERT: Mit Validierung
    """
    Aktualisiert die E-Mail-Adresse und/oder Telefonnummer eines bestehenden Kunden.
    Fragt den Benutzer nach dem Kundennamen und dann nach den neuen Daten.
    Leere Eingaben für E-Mail/Telefon lassen die bestehenden Werte unverändert.
    """
    print("\n--- Kunden aktualisieren ---")
    name_zu_aktualisieren = input("Name des zu aktualisierenden Kunden: ")

    if name_zu_aktualisieren not in kunden:
        print(f"Fehler: Kunde '{name_zu_aktualisieren}' nicht im Katalog gefunden.")
        return

    print(f"Aktuelle Daten für {name_zu_aktualisieren}:")
    print(f"  E-Mail: {kunden[name_zu_aktualisieren]['email']}")
    print(f"  Telefon: {kunden[name_zu_aktualisieren]['telefon']}")

    neue_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
    if neue_email: # Nur validieren und aktualisieren, wenn eine Eingabe gemacht wurde
        while not re.match(r"[^@]+@[^@]+\.[^@]+", neue_email):
            print("Ungültiges E-Mail-Format. Bitte versuchen Sie es erneut.")
            neue_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
        kunden[name_zu_aktualisieren]['email'] = neue_email

    neue_telefon = input("Neue Telefonnummer (leer lassen für keine Änderung): ")
    if neue_telefon: # Nur validieren und aktualisieren, wenn eine Eingabe gemacht wurde
        while not (neue_telefon.replace('+', '').isdigit() and (neue_telefon.startswith('+') or not neue_telefon.startswith('+'))):
            print("Ungültige Telefonnummer. Bitte geben Sie nur Ziffern ein (optional mit + am Anfang).")
            neue_telefon = input("Neue Telefonnummer (leer lassen für keine Änderung): ")
        kunden[name_zu_aktualisieren]['telefon'] = neue_telefon

    print(f"Kunde '{name_zu_aktualisieren}' wurde aktualisiert.")

def kunde_loeschen():
    """
    Löscht einen Kunden aus dem Katalog anhand seines Namens.
    Gibt eine Fehlermeldung aus, wenn der Kunde nicht gefunden wird.
    """
    print("\n--- Kunden löschen ---")
    name_zu_loeschen = input("Name des zu löschenden Kunden: ")
    if name_zu_loeschen in kunden:
        del kunden[name_zu_loeschen] # Entferne den Kunden aus dem Dictionary
        print(f"Kunde '{name_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Kunde '{name_zu_loeschen}' nicht im Katalog gefunden.")

def katalog_speichern():
    """
    Speichert den aktuellen Kundenkatalog in einer JSON-Datei.
    Der Dateiname wird durch die globale Variable DATEINAME definiert.
    Behandelt IOError bei Problemen mit der Dateispeicherung.
    """
    try:
        # Öffne die Datei im Schreibmodus ('w') mit UTF-8-Kodierung
        with open(DATEINAME, 'w', encoding='utf-8') as f:
            # Speichere das 'kunden'-Dictionary als JSON in der Datei
            # indent=4 für schöne Formatierung, ensure_ascii=False für Umlaute
            json.dump(kunden, f, indent=4, ensure_ascii=False)
        print(f"Katalog erfolgreich in '{DATEINAME}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern des Katalogs: {e}")

def katalog_laden():
    """
    Lädt den Kundenkatalog aus einer JSON-Datei.
    Der Dateiname wird durch die globale Variable DATEINAME definiert.
    Initialisiert den Katalog neu, wenn die Datei nicht gefunden wird
    oder ungültiges JSON enthält.
    """
    global kunden # Erlaube den Zugriff auf die globale 'kunden'-Variable
    try:
        # Versuche, die Datei im Lesemodus ('r') zu öffnen
        with open(DATEINAME, 'r', encoding='utf-8') as f:
            kunden.update(json.load(f)) # Lade die JSON-Daten in das 'kunden'-Dictionary
        print(f"Katalog erfolgreich aus '{DATEINAME}' geladen.")
    except FileNotFoundError:
        # Wenn die Datei nicht existiert, ist das normal beim ersten Start
        print("Keine vorhandene Katalogdatei gefunden. Starte mit leerem Katalog.")
        kunden.clear() # Leere das Dictionary, falls es Reste enthält
    except json.JSONDecodeError as e:
        # Wenn die Datei existiert, aber kein gültiges JSON enthält
        print(f"Fehler beim Laden des Katalogs (ungültiges JSON): {e}. Starte mit leerem Katalog.")
        kunden.clear()
    except Exception as e:
        # Fange alle anderen unerwarteten Fehler ab
        print(f"Ein unerwarteter Fehler beim Laden ist aufgetreten: {e}. Starte mit leerem Katalog.")
        kunden.clear()

def zeige_menue():
    print("\n--- CRM Menü ---")
    print("1. Kunde hinzufügen")
    print("2. Kunden anzeigen")
    print("3. Kunde suchen")
    print("4. Kunde aktualisieren")
    print("5. Kunde löschen")
    print("6. Beenden")
    print("----------------")

def main():
    """
    Die Hauptfunktion des Programms.
    Lädt den Katalog beim Start, zeigt das Menü an und verarbeitet Benutzereingaben.
    Speichert den Katalog beim Beenden.
    """
    katalog_laden() # Katalog beim Start laden
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
        elif wahl == '5':
            kunde_loeschen()
        elif wahl == '6':
            katalog_speichern() # Katalog vor dem Beenden speichern
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()

# Test der Funktion (wird später durch ein Menü ersetzt)
# kunde_hinzufuegen()
# kunden_anzeigen()

