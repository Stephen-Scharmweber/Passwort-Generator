# Single Password Generator / Einzelner Passwort-Generator

`A lightweight GUI for secure passwords / Leichtgewichtige GUI für sichere Passwörter`

## Features / Funktionen

- Custom length (8-64 chars) / Länge (8-64 Zeichen)
- Numbers toggle / Zahlen ein-ausschalten
- Special characters / Sonderzeichen
- One-click copy / Ein-Klick-Kopieren
- Clean interface / Übersichtliches Design

## Requirements / Voraussetzungen

- Python 3.x
- Tkinter (usually included) / Tkinter (meist vorinstalliert)

`1. Run script / Skript starten:
   python password_generator.py

2. Configure / Einstellen:
   - LENGTH: 12 (default) / Standard: 12
   - NUMBERS: ☑ (0-9)
   - SPECIAL CHARS: ☑ (!@#$%)

3. Click "GENERATE" / "GENERIEREN"
4. Click "COPY" / "KOPIEREN"`

`Customize / Anpassen:
# In code / Im Code:
length_entry.insert(0, "12")  # Default length
special_chars = "!@#$%"  # Custom symbols
font = "Arial"  # Schriftart`

`How it works / Funktionsweise:
1. Generates using:
   - Letters (always) / Buchstaben (immer)
   - Numbers (optional) / Zahlen (optional)
   - Symbols (optional) / Zeichen (optional)
2. Copy logic / Kopier-Logik:
   - Auto-generates if empty / Erstellt bei Leere
   - Copies to clipboard / In Zwischenablage
   - Shows confirmation / Bestätigung anzeigen`

`License / Lizenz:
MIT License - Free use / Freie Nutzung`
