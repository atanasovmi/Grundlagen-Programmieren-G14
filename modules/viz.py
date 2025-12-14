import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Modul für Visualisierungen und Analytik
# Erstellt sowie "Spotify Wrapped" Highlights für unseren Workout-Tracker

# Farbpalette
FARBE_HINTERGRUND = "#EFEDE9"
FARBE_PRIMAER = "#007B88"
FARBE_SEKUNDAER = "#FFB603"
FARBE_HIGHLIGHT = "#FF5A5F"
FARBE_GRAU = "#AAAAAA"

# Wochentag-Namen für Charts
WOCHENTAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

# Nur eine Schriftart die wechselt
# plt.rcParams['font.family'] = ['Segoe UI Emoji', 'DejaVu Sans', 'sans-serif']
# plt.rcParams['axes.unicode_minus'] = False  # Solves related glyph issue regarding emojis font

# plt.rcParams['font.size'] = 16        # Standard-Schriftgrösse
# plt.rcParams['axes.titlesize'] = 24     # für suptitle / Titel
# plt.rcParams['axes.labelsize'] = 18
# plt.rcParams['font.weight'] = 'bold'  # Alles fett (Titel, Labels, etc.)
# plt.rcParams['axes.labelweight'] = 'bold'

def zeige_analytik_menue(daten):
    """
    Zeigt das Analytik-Menü an und steuert die Visualisierungen.
    Erwartet die Rohdaten als Liste von Listen: [Datum, Übung, Dauer, Kalorien].
    """
    if not daten:
        print("\nKeine Daten für Analytik vorhanden.")
        return

    df = _bereite_dataframe_vor(daten)

    if df.empty:
        print("\nKeine gültigen Daten für Analytik vorhanden.")
        return

    while True:
        print("\n--- Analytiken ---")
        print("1. Highlights anzeigen (KPIs)")
        print("2. Übungsverteilung (Radar vs. Vormonat)")
        print("3. Jahres-Heatmap (Kalorien)")
        print("4. Wochenbericht (Minuten)")
        print("0. Zurück zum Hauptmenü")

        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            _zeige_kpi_kacheln(df)
        elif wahl == '2':
            _zeige_radar_verteilung(df)
        elif wahl == '3':
            _zeige_jahres_heatmap(df)
        elif wahl == '4':
            _zeige_wochen_bericht(df)
        elif wahl == '0':
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie 0-4.")


def _bereite_dataframe_vor(daten):
    """
    Konvertiert die Rohdaten in ein pandas DataFrame.
    Bereinigt Datentypen (Datum, Zahlen).
    """
    try:
        df = pd.DataFrame(daten, columns=['Datum', 'Uebung', 'Dauer', 'Kalorien'])

        # Datum im Format TT.MM.JJJJ
        df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y', errors='coerce')

        # Zahlen konvertieren
        df['Dauer'] = pd.to_numeric(df['Dauer'], errors='coerce')
        df['Kalorien'] = pd.to_numeric(df['Kalorien'], errors='coerce')

        # Ungültige Zeilen entfernen
        df = df.dropna()

        # Nach Datum sortieren
        df = df.sort_values(by='Datum')

        return df
    except Exception as e:
        print(f"Fehler bei der Datenaufbereitung: {e}")
        return pd.DataFrame()


def _berechne_laengste_streak(df):
    """
    Berechnet die längste Serie aufeinanderfolgender Trainingstage.
    """
    if df.empty:
        return 0

    # Eindeutige Trainingstage
    trainingstage = df['Datum'].dt.date.unique()
    trainingstage = sorted(trainingstage)

    if len(trainingstage) == 0:
        return 0

    laengste = 1
    aktuell = 1

    for i in range(1, len(trainingstage)):
        diff = (trainingstage[i] - trainingstage[i - 1]).days
        if diff == 1:
            aktuell += 1
            laengste = max(laengste, aktuell)
        else:
            aktuell = 1

    return laengste


def _zeige_kpi_kacheln(df):
    """
    Rendert die KPI-Kacheln (Key Performance Indicator) basierend auf den aggregierten
    Daten im DataFrame. Zeigt KPI-Highlights als grafisches Dashboard (Matplotlib) an.
    Nutzt ausnahmsweise 'patches' for a nicer card-like look.

    Note: This function's implementation was primarily developed using Perplexity AI
    and subsequently validated/refined by the author due to it's
    uncasualty of creating cards on matplot - this goes beyond our personal knowledge
    """
    try:
        heute = datetime.now()
        
        # Berechnungen
        start_woche = heute - timedelta(days=heute.weekday())
        df_woche = df[df['Datum'] >= start_woche.strftime('%Y-%m-%d')]
        trainings_woche = len(df_woche)
        kcal_woche = int(df_woche['Kalorien'].sum())

        start_monat = heute.replace(day=1)
        df_monat = df[df['Datum'] >= start_monat.strftime('%Y-%m-%d')]
        minuten_monat = int(df_monat['Dauer'].sum())
        
        streak = _berechne_laengste_streak(df)
        avg_dauer = int(df['Dauer'].mean()) if not df.empty else 0

        if not df.empty:
            beliebteste = df['Uebung'].value_counts().idxmax()
        else:
            beliebteste = "-"

        # Daten für die Kacheln
        # Style: 'normal' oder 'highlight' (dunkler Hintergrund)
        kacheln = [
            {"titel": "Trainings (Woche)", "wert": str(trainings_woche), "farbe": FARBE_PRIMAER, "bg": "white", "text_color": FARBE_PRIMAER},
            {"titel": "Kalorien (Woche)", "wert": f"{kcal_woche}", "farbe": "white", "bg": FARBE_SEKUNDAER, "text_color": "white"},
            {"titel": "Minuten (Monat)", "wert": f"{minuten_monat}", "farbe": FARBE_SEKUNDAER, "bg": "white", "text_color": FARBE_SEKUNDAER},
            {"titel": "Längster Streak", "wert": f"{streak} Tage", "farbe": "white", "bg": FARBE_HIGHLIGHT, "text_color": "white"},
            {"titel": "Ø Dauer", "wert": f"{avg_dauer} min", "farbe": FARBE_PRIMAER, "bg": "white", "text_color": FARBE_PRIMAER},
            {"titel": "Lieblingsübung", "wert": beliebteste, "farbe": "white", "bg": FARBE_PRIMAER, "text_color": "white", "custom_size": 30}
        ]

        # Plot erstellen
        fig, axes = plt.subplots(2, 3, figsize=(14, 7))
        fig.canvas.manager.set_window_title('Fitness Highlights')
        fig.patch.set_facecolor(FARBE_HINTERGRUND)
        
        fig.suptitle("🚀 DEINE FITNESS HIGHLIGHTS 🚀", fontsize=30, fontweight='bold',fontfamily='Segoe UI Emoji', color='#333333', y=0.96)

        axes = axes.flatten()

        for i, ax in enumerate(axes):
            kachel = kacheln[i]
            
            # Achsen komplett ausblenden
            ax.axis('off')
            
            # Card Background (Rounded Rect)
            # Koordinaten sind 0,0 bis 1,1 im Axis-System
            rect = mpatches.FancyBboxPatch(
                (0.05, 0.05), 0.9, 0.9,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                ec="none",
                fc=kachel["bg"],
                transform=ax.transAxes,
                zorder=1
            )
            ax.add_patch(rect)
            
            # Titel (oben)
            titel_col = "#666666" if kachel["bg"] == "white" else "white"
            ax.text(0.5, 0.75, kachel["titel"].upper(), 
                    ha='center', va='center', fontsize=20, fontweight='bold',
                    color=titel_col, transform=ax.transAxes, zorder=2)
            
            # Wert (mitte)
            if "custom_size" in kachel:
                schrift_groesse = kachel["custom_size"]
            else:
                schrift_groesse = 30 if len(kachel["wert"]) < 12 else 22

            ax.text(0.5, 0.45, kachel["wert"], 
                    ha='center', va='center', fontsize=schrift_groesse, fontweight='bold', 
                    color=kachel["text_color"], transform=ax.transAxes, zorder=2)

        plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.05, wspace=0.1, hspace=0.1)
        
        print("Highlights werden angezeigt...")
        plt.show()

    except Exception as e:
        print(f"Fehler beim Erstellen der Grafik: {e}")


def _zeige_radar_verteilung(df):
    """
    Zeigt einen Radar-Plot der Übungsverteilung:
    Aktuelle 30 Tage vs. Vorherige 30 Tage (Vergleich).
    """
    try:
        heute = datetime.now()
        
        # Zeitfenster definieren
        start_aktuell = heute - timedelta(days=30)
        start_vorher = start_aktuell - timedelta(days=30)
        
        # Dataframes filtern
        df_aktuell = df[(df['Datum'] >= start_aktuell) & (df['Datum'] <= heute)]
        df_vorher = df[(df['Datum'] >= start_vorher) & (df['Datum'] < start_aktuell)]

        # Alle bekannten Übungen sicherstellen
        alle_uebungen = ["Joggen", "Schwimmen", "Radfahren", "Krafttraining", "Yoga"]
        
        # Counts berechnen
        counts_aktuell = df_aktuell['Uebung'].value_counts()
        werte_aktuell = [counts_aktuell.get(u, 0) for u in alle_uebungen]
        
        counts_vorher = df_vorher['Uebung'].value_counts()
        werte_vorher = [counts_vorher.get(u, 0) for u in alle_uebungen]

        # Wenn gar keine Daten => Abbruch mit Meldung
        if sum(werte_aktuell) == 0 and sum(werte_vorher) == 0:
            print("\nKeine Trainingsdaten in den letzten 60 Tagen.")
            return

        # Radar-Daten vorbereiten (Winkel)
        anzahl = len(alle_uebungen)
        winkel = np.linspace(0, 2 * np.pi, anzahl, endpoint=False).tolist()

        # Kreis schliessen (ersten Wert am Ende anhängen)
        werte_aktuell += werte_aktuell[:1]
        werte_vorher += werte_vorher[:1]
        winkel += winkel[:1]

        # Plot Setup
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor(FARBE_HINTERGRUND)
        ax.set_facecolor(FARBE_HINTERGRUND)

        # Plot: Vorherige Periode (Hintergrund, grau/gelb)
        ax.plot(winkel, werte_vorher, '--', linewidth=1.5, color=FARBE_SEKUNDAER, label="Vormonat")
        ax.fill(winkel, werte_vorher, alpha=0.1, color=FARBE_SEKUNDAER)
        
        # Plot: Aktuelle Periode (Vordergrund, teal)
        ax.plot(winkel, werte_aktuell, 'o-', linewidth=2.5, color=FARBE_PRIMAER, label="Letzte 30 Tage")
        ax.fill(winkel, werte_aktuell, alpha=0.25, color=FARBE_PRIMAER)

        # Labels
        ax.set_xticks(winkel[:-1])
        ax.set_xticklabels(alle_uebungen, fontsize=11)
        ax.set_title("Übungs-Check: Trend der letzten 30 Tage", fontsize=14, pad=20)
        
        # Legende
        ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

        plt.tight_layout()
        print("Grafik wird angezeigt...")
        plt.show()
    except Exception as e:
        print(f"Fehler beim Erstellen der Grafik: {e}")


def _zeige_jahres_heatmap(df):
    """
    Zeigt eine Jahres-Heatmap der Kalorien pro Tag.
    Layout: X-Achse = Kalenderwochen, Y-Achse = Wochentage.
    """
    try:
        # Aktuelles Jahr
        jahr = datetime.now().year
        df_jahr = df[df['Datum'].dt.year == jahr]

        if df_jahr.empty:
            print(f"\nKeine Daten für {jahr} vorhanden.")
            return

        # Kalorien pro Tag aggregieren
        daily = df_jahr.groupby(df_jahr['Datum'].dt.date)['Kalorien'].sum()

        # Kalender-Daten vorbereiten (alle Tage des Jahres)
        start = datetime(jahr, 1, 1)
        end = datetime(jahr, 12, 31)
        alle_tage = pd.date_range(start, end, freq='D')

        # Woche und Wochentag berechnen
        data = []
        for tag in alle_tage:
            # isocalendar gibt (Jahr, Woche, Tag) zurück. Woche 1-52/53
            woche = tag.isocalendar()[1]
            wochentag = tag.weekday() # 0=Mo, 6=So
            kcal = daily.get(tag.date(), 0)
            data.append({'Woche': woche, 'Wochentag': wochentag, 'Kalorien': kcal})

        heatmap_df = pd.DataFrame(data)

        # Pivot für Heatmap (Wochentag x Woche)
        pivot = heatmap_df.pivot_table(
            index='Wochentag', columns='Woche', values='Kalorien', aggfunc='sum'
        ).fillna(0)

        # Sicherstellen, dass alle Wochentage da sind (0-6)
        for i in range(7):
            if i not in pivot.index:
                pivot.loc[i] = 0
                
        pivot = pivot.sort_index()

        # Plot
        fig, ax = plt.subplots(figsize=(16, 4))
        fig.patch.set_facecolor(FARBE_HINTERGRUND)
        ax.set_facecolor(FARBE_HINTERGRUND)

        # Heatmap zeichnen
        im = ax.imshow(
            pivot.values,
            aspect='auto', # Rechteckige Zellen (passen sich der Breite an)
            cmap='GnBu', 
            vmin=0,
            vmax=pivot.values.max() if pivot.values.max() > 0 else 1
        )

        # Achsen
        ax.set_yticks(range(7))
        ax.set_yticklabels(WOCHENTAGE)
        ax.set_ylabel("")
        
        # X-Achse: Wochen-Nummern (5, 10, 15, 20...)
        x_ticks = range(4, pivot.shape[1], 5)  # Index 4 = Woche 5
        x_labels = [pivot.columns[i] for i in x_ticks]
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_labels, fontsize=9)
        ax.set_xlabel("Kalenderwoche")
        
        ax.set_title(f"Jahres-Check {jahr}: Konsistenz", fontsize=14, pad=15)

        # Spines entfernen
        for spine in ax.spines.values():
            spine.set_visible(False)
            
        ax.tick_params(axis=u'both', which=u'both',length=0) # Ticks verstecken

        # Colorbar
        cbar = plt.colorbar(im, ax=ax, shrink=0.7, pad=0.02)
        cbar.set_label("Kalorien")

        plt.tight_layout()
        print("Grafik wird angezeigt...")
        plt.show()
    except Exception as e:
        print(f"Fehler beim Erstellen der Grafik: {e}")


def _zeige_wochen_bericht(df):
    """
    Zeigt ein Balkendiagramm der Trainingsminuten pro Tag (letzte 7 Tage).
    """
    try:
        heute = datetime.now().date()
        vor_7_tagen = heute - timedelta(days=6)

        # Alle 7 Tage vorbereiten
        tage = [(vor_7_tagen + timedelta(days=i)) for i in range(7)]
        labels = [WOCHENTAGE[t.weekday()] for t in tage]

        # Minuten pro Tag
        minuten = []
        for tag in tage:
            tag_df = df[df['Datum'].dt.date == tag]
            minuten.append(int(tag_df['Dauer'].sum()))

        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor(FARBE_HINTERGRUND)
        ax.set_facecolor(FARBE_HINTERGRUND)

        bars = ax.bar(labels, minuten, color=FARBE_SEKUNDAER, alpha=0.9, edgecolor='black', linewidth=0.5)

        # Werte über Balken
        for bar, m in zip(bars, minuten):
            if m > 0:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 2,
                    str(m) + " min",
                    ha='center',
                    va='bottom',
                    fontsize=10,
                    fontweight='bold',
                    color='#333333'
                )

        ax.set_xlabel("Tag")
        ax.set_ylabel("Minuten")
        ax.set_title("Wochen-Fokus: Trainingszeit (letzte 7 Tage)", fontsize=14)
        ax.grid(axis='y', linestyle='--', alpha=0.4, color=FARBE_GRAU)
        
        # Spines anpassen für cleaner look
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.tight_layout()
        print("Grafik wird angezeigt...")
        plt.show()
    except Exception as e:
        print(f"Fehler beim Erstellen der Grafik: {e}")
