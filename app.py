import modules.ui as ui
import modules.storage as storage
import modules.workout as workout
import modules.viz as viz

# Dateiname für die Datenspeicherung wird aus storage importiert
DATEI_PFAD = storage.DATA_PATH

def training_eintragen():
    """
    Funktion 1: Neues Training erfassen.
    """
    print("\n--- Training eintragen ---")
    
    datum = ui.frage_datum()
    uebung_name, kcal_faktor = ui.frage_uebung(workout.UEBUNGEN_KALORIEN)
    dauer = ui.frage_dauer()
    
    kalorien = workout.berechne_kalorien(dauer, kcal_faktor)
    
    # Daten speichern
    # Format: Datum, Übung, Dauer, Kalorien
    eintrag = [str(datum), str(uebung_name), str(dauer), str(kalorien)]
    storage.speichere_eintrag(DATEI_PFAD, eintrag)
    
    print(f"\nErfolg: {uebung_name} für {dauer} Min ({kalorien} kcal) am {datum} gespeichert.")

def training_bearbeiten():
    """
    Funktion 2: Training bearbeiten.
    """
    print("\n--- Training bearbeiten ---")
    
    alle_daten = storage.lade_daten(DATEI_PFAD)
    
    if not alle_daten:
        print("Keine Daten vorhanden.")
        return

    while True:
        datum = ui.frage_datum_oder_abbruch()
        
        if datum is None:
            print("Abbruch.")
            return
            
        treffer = workout.filtere_daten_nach_datum(alle_daten, datum)

        if treffer:
            break
        
        print(f"Keine Einträge für den {datum} gefunden.")

    auswahl = ui.zeige_bearbeitungs_menue(treffer)
    
    if auswahl == 0:
        print("Abbruch.")
        return

    # Index des zu bearbeitenden Eintrags in der Gesamtliste
    index_to_edit = treffer[auswahl - 1][0]
    aktueller_eintrag = alle_daten[index_to_edit]
    
    # Temporäre Variablen für die Bearbeitung initialisieren
    neu_datum = aktueller_eintrag[0]
    neu_uebung = aktueller_eintrag[1]
    neu_dauer = int(aktueller_eintrag[2])
    
    # Kcal-Faktor für die aktuelle Übung finden, um Kalorien neu berechnen zu können
    # Wir müssen den Faktor rückwärts finden oder einfach beibehalten, wenn Übung nicht geändert wird.
    # Einfacher: Wir suchen den Faktor anhand des Namens.
    current_kcal_faktor = 0
    for key, val in workout.UEBUNGEN_KALORIEN.items():
        if val["name"] == neu_uebung:
            current_kcal_faktor = val["kcal_pro_min"]
            break
            
    while True:
        # Wir bauen den Eintrag temporär zusammen für die Anzeige
        temp_kalorien = workout.berechne_kalorien(neu_dauer, current_kcal_faktor)
        temp_eintrag = [str(neu_datum), str(neu_uebung), str(neu_dauer), str(temp_kalorien)]
        
        feld_wahl = ui.zeige_feld_auswahl_menue(temp_eintrag)
        
        if feld_wahl == 0:
            break
        elif feld_wahl == 1:
            neu_datum = ui.frage_datum()
        elif feld_wahl == 2:
            neu_uebung, current_kcal_faktor = ui.frage_uebung(workout.UEBUNGEN_KALORIEN)
        elif feld_wahl == 3:
            neu_dauer = ui.frage_dauer()
            
    # Speichern
    kalorien = workout.berechne_kalorien(neu_dauer, current_kcal_faktor)
    finaler_eintrag = [str(neu_datum), str(neu_uebung), str(neu_dauer), str(kalorien)]
    
    alle_daten = workout.aktualisiere_eintrag(alle_daten, index_to_edit, finaler_eintrag)
    storage.speichere_daten(DATEI_PFAD, alle_daten)
    print("Eintrag erfolgreich aktualisiert.")

def training_loeschen():
    """
    Funktion 3: Training löschen.
    """
    print("\n--- Training löschen ---")
    
    alle_daten = storage.lade_daten(DATEI_PFAD)
    
    if not alle_daten:
        print("Keine Daten vorhanden.")
        return

    while True:
        datum = ui.frage_datum_oder_abbruch()
        
        if datum is None:
            print("Abbruch.")
            return
            
        treffer = workout.filtere_daten_nach_datum(alle_daten, datum)

        if treffer:
            break
        
        print(f"Keine Einträge für den {datum} gefunden.")

    auswahl = ui.zeige_loesch_menue(treffer)
    
    if auswahl == 0:
        print("Abbruch.")
        return

    # Löschen durchführen
    index_to_delete = treffer[auswahl - 1][0]
    alle_daten = workout.loesche_eintrag(alle_daten, index_to_delete)
    storage.speichere_daten(DATEI_PFAD, alle_daten)
    print("Eintrag gelöscht.")

def historie_einsehen():
    """
    Funktion 4: Historie einsehen.
    """
    print("\n--- Historie einsehen ---")
    
    daten = storage.lade_daten(DATEI_PFAD)
    
    while True:
        # Filter abfragen (Smart Filter)
        monat = ui.frage_monat_oder_abbruch()
        
        if monat is False:
            # User hat 0 eingegeben → Abbruch
            print("Abbruch.")
            return
        
        if monat is None:
            # Kein Filter → Alles zeigen
            print("\nZeige alle Einträge:")
            ui.zeige_historie(daten)
            return
        
        # Prüfen, welche Jahre verfügbar sind
        jahre = workout.ermittle_jahre_fuer_monat(daten, monat)
        
        if jahre:
            if len(jahre) > 1:
                # Mehrere Jahre gefunden → User fragen
                jahr = ui.frage_jahr(jahre)
                filter_str = f"{monat}.{jahr}"
            else:
                # Nur ein Jahr gefunden → Automatisch wählen
                filter_str = f"{monat}.{jahre[0]}"
                
            daten_gefiltert = workout.filtere_daten_nach_monat(daten, filter_str)
            monat_name = workout.MONAT_NAMEN.get(monat, monat)
            print(f"\nZeige Einträge für {monat_name}"
                  f" {jahre[0] if len(jahre) == 1 else jahr}:")
            ui.zeige_historie(daten_gefiltert)
            return
        else:
            monat_name = workout.MONAT_NAMEN.get(monat, monat)
            print(f"Keine Einträge für den Monat {monat_name} gefunden.")

def assistent_starten():
    """
    Funktion 5: Assistent starten (ehemals Kalorienrechner aus Meeting neu gedacht dank Aydin).
    """
    print("\n--- Workout-Assistent ---")
    
    ziel = ui.frage_kalorien_ziel()
    
    while True:
        mix = workout.generiere_workout_mix(ziel)
        
        print("\nHier ist meine Empfehlung mit dem perfekten Workout-Mix für heute!")
        ui.zeige_historie(mix)
        
        wahl = ui.zeige_empfehlung_menue()
        
        if wahl == '1':
            # Speichern
            for eintrag in mix:
                storage.speichere_eintrag(DATEI_PFAD, eintrag)
            print("Workout gespeichert, Viel Spass!")
            break
        elif wahl == '2':
            # Neu generieren -> Loop continues weiter
            continue
        elif wahl == '0':
            # Abbruch
            break

def analytiken():
    """
    Called viz.py als Standalone Lösung, da es nicht offiziell zum Projekt gehört,
    sondern wie als Extra wie 'Easteregg' angezeigt wird.
    """
    daten = storage.lade_daten(DATEI_PFAD)
    viz.zeige_analytik_menue(daten)

def main():
    """
    Hauptfunktion mit Menüschleife.
    """
    print(f"DEBUG: Datei wird gespeichert in: {DATEI_PFAD}")
    print("Willkommen beim Workout-Tracker!")
    
    while True:
        ui.zeige_hauptmenue()
        wahl = input("Ihre Wahl: ")
        
        if wahl == '1':
            training_eintragen()
        elif wahl == '2':
            training_bearbeiten()
        elif wahl == '3':
            training_loeschen()
        elif wahl == '4':
            historie_einsehen()
        elif wahl == '5':
            assistent_starten()
        elif wahl == '6':
            analytiken()
        elif wahl == '0':
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie 0-6.")
            

if __name__ == "__main__":
    main()
