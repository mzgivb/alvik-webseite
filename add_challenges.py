#!/usr/bin/env python3
"""
Challenge-Generator für Alvik Lernplattform
Fügt interaktive Challenges zu allen Lektionen hinzu
"""

from pathlib import Path
import re

# Basis-Verzeichnis
html_dir = Path(__file__).parent

# Challenge-Daten organisiert nach Dateinamen-Pattern
CHALLENGES = [
    {
        "pattern": r"1_2.*Grundger.*\.html",
        "title": "Challenge: Dein erstes Alvik-Programm",
        "tasks": [
            "Erstelle eine neue Datei mit einem sinnvollen Namen",
            "Importiere die Alvik-Bibliothek korrekt",
            "Initialisiere den Roboter",
            "Lasse alle LEDs in verschiedenen Farben leuchten",
            "Füge aussagekräftige Kommentare hinzu"
        ],
        "hints": [
            "💡 Nutze <code>from arduino_alvik import ArduinoAlvik</code>",
            "💡 Vergiss nicht <code>import time</code> für Pausen",
            "💡 Die LED-Befehle findest du in der API-Dokumentation"
        ],
        "expected": [
            "Programm läuft ohne Fehler",
            "LEDs leuchten nacheinander in unterschiedlichen Farben",
            "Code ist gut kommentiert und strukturiert"
        ]
    },
    {
        "pattern": r"1_3_Alvik_mit_Kabel.*\.html",
        "title": "Challenge: Verkabelter Testlauf",
        "tasks": [
            "Verbinde Alvik korrekt per USB-C mit dem Computer",
            "Erstelle ein Test-Programm mit LED-Blinksequenz",
            "Lade das Programm auf Alvik",
            "Beobachte die Ausführung über die serielle Konsole",
            "Dokumentiere den Ablauf"
        ],
        "hints": [
            "💡 Prüfe in Thonny, ob der Port korrekt erkannt wurde",
            "💡 Nutze <code>print()</code> für Statusmeldungen",
            "💡 Die serielle Konsole zeigt dir alle Ausgaben"
        ],
        "expected": [
            "Stabile USB-Verbindung",
            "Programm wird erfolgreich übertragen",
            "Statusmeldungen sind in der Konsole sichtbar"
        ]
    },
    {
        "pattern": r"1_3_1.*LED.*\.html",
        "title": "Challenge: LED-Lichtshow",
        "tasks": [
            "Erstelle eine for-Schleife für 10 Durchgänge",
            "Lasse die LEDs in allen Farben des Regenbogens blinken",
            "Füge variable Pausenzeiten ein (schneller werdend)",
            "Erstelle ein Schlusslicht-Muster",
            "Bonus: Implementiere ein SOS-Signal"
        ],
        "hints": [
            "💡 RGB-Werte: Rot (255,0,0), Grün (0,255,0), Blau (0,0,255)",
            "💡 Nutze eine Liste für die Farben",
            "💡 <code>time.sleep()</code> für unterschiedliche Geschwindigkeiten"
        ],
        "expected": [
            "Flüssige Farbübergänge",
            "Programmschleife läuft korrekt",
            "SOS-Muster: 3x kurz, 3x lang, 3x kurz"
        ]
    },
    {
        "pattern": r"1_4.*ohne_Kabel.*\.html",
        "title": "Challenge: Autonomer Batteriebetrieb",
        "tasks": [
            "Lade ein Programm mit 5-Sekunden-Verzögerung auf Alvik",
            "Trenne das USB-Kabel und starte per Touch-Button",
            "Programmiere eine 30-Sekunden-Routine",
            "Teste verschiedene Bewegungsmuster",
            "Dokumentiere die Batterielaufzeit"
        ],
        "hints": [
            "💡 Nutze <code>time.sleep(5)</code> am Programmstart",
            "💡 Der Touch-Button startet das Programm automatisch",
            "💡 Kombiniere Bewegung und LED-Signale"
        ],
        "expected": [
            "Programm startet nach Trennen vom Kabel",
            "Alvik führt Routine vollständig aus",
            "Batteriestatus bleibt im grünen Bereich"
        ]
    },
    {
        "pattern": r"1_5_Alvik_ein_Viereck.*\.html",
        "title": "Challenge: Präzises Viereck",
        "tasks": [
            "Programmiere ein exaktes Quadrat (30cm Seitenlänge)",
            "Nutze die Gyro-Daten für exakte 90°-Drehungen",
            "Miss die tatsächlichen Positionen aus",
            "Optimiere die Parameter für Präzision",
            "Teste auf verschiedenen Untergründen"
        ],
        "hints": [
            "💡 <code>alvik.rotate(90)</code> für die Drehung",
            "💡 <code>alvik.move(30)</code> für die Bewegung",
            "💡 Kalibriere mit kleineren Testfahrten"
        ],
        "expected": [
            "Abweichung unter 2cm pro Seite",
            "Start- und Endposition sind identisch",
            "Funktioniert auf Teppich und Laminat"
        ]
    },
    {
        "pattern": r"1_5_1.*exakt.*\.html",
        "title": "Challenge: Präzisionsnavigation",
        "tasks": [
            "Erstelle eine Strecke mit 5 Wegpunkten",
            "Programmiere exakte Bewegungen zwischen den Punkten",
            "Miss die Genauigkeit mit einem Maßband",
            "Dokumentiere Abweichungen",
            "Optimiere durch Parameterjustierung"
        ],
        "hints": [
            "💡 Nutze die Encoderdaten zur Kontrolle",
            "💡 <code>alvik.get_imu_gyro()</code> für die Orientierung",
            "💡 Teste schrittweise und korrigiere"
        ],
        "expected": [
            "Maximale Abweichung: ±3cm",
            "Wiederholgenauigkeit gegeben",
            "Dokumentation mit Messwerten"
        ]
    },
    {
        "pattern": r"1_5_2.*Tastendruck.*\.html",
        "title": "Challenge: Interaktive Steuerung",
        "tasks": [
            "Programmiere 4 verschiedene Bewegungsmuster",
            "Jedes Muster startet mit einer Touch-Button-Berührung",
            "Füge visuelle LED-Rückmeldungen hinzu",
            "Implementiere eine Pause-Funktion",
            "Teste alle Muster nacheinander"
        ],
        "hints": [
            "💡 <code>alvik.get_touch_ok()</code> für Touch-Button",
            "💡 Nutze verschiedene LED-Farben pro Muster",
            "💡 <code>while True:</code> mit Bedingungen"
        ],
        "expected": [
            "Alle 4 Muster funktionieren zuverlässig",
            "LEDs geben klare Statusinfo",
            "Pause-Funktion unterbricht korrekt"
        ]
    },
    {
        "pattern": r"1_5_3.*Collision.*\.html",
        "title": "Challenge: Intelligente Hindernisvermeidung",
        "tasks": [
            "Nutze die ToF-Sensoren für Hinderniserkennung",
            "Implementiere ein Ausweichverhalten",
            "Programmiere eine Raumexploration (2x2m)",
            "Dokumentiere die Hindernis-Reaktionen",
            "Optimiere für schnelle Reaktionszeit"
        ],
        "hints": [
            "💡 <code>alvik.get_distance()</code> für Sensordaten",
            "💡 Schwellwert bei ca. 20cm setzen",
            "💡 Nutze Zufallsdrehungen für Exploration"
        ],
        "expected": [
            "Keine Kollision mit Hindernissen",
            "Flüssige Ausweichmanöver",
            "Exploration deckt >80% der Fläche ab"
        ]
    },
    {
        "pattern": r"2_0.*I2C.*\.html",
        "title": "Challenge: I2C-Geräteerkennung",
        "tasks": [
            "Scanne den I2C-Bus nach allen Geräten",
            "Identifiziere die Adresse des BME680",
            "Teste die Kommunikation mit einem Ping",
            "Dokumentiere alle gefundenen Adressen",
            "Erstelle eine Tabelle mit Gerätenamen"
        ],
        "hints": [
            "💡 Nutze den I2C-Scan aus dem Beispielcode",
            "💡 BME680-Adresse: meist 0x76 oder 0x77",
            "💡 <code>hex()</code> für leserliche Adressen"
        ],
        "expected": [
            "Mindestens 3 I2C-Geräte gefunden",
            "BME680 erfolgreich identifiziert",
            "Dokumentation als Tabelle oder Liste"
        ]
    },
    {
        "pattern": r"2_1.*bme680.*\.html",
        "title": "Challenge: Umwelt-Datenlogger",
        "tasks": [
            "Lese alle 4 Sensorwerte vom BME680 aus",
            "Speichere die Daten über 10 Minuten",
            "Erstelle eine CSV-Datei mit Zeitstempel",
            "Visualisiere die Daten in einem Diagramm",
            "Analysiere Temperatur- und Luftdruckverlauf"
        ],
        "hints": [
            "💡 <code>time.time()</code> für Zeitstempel",
            "💡 Nutze eine Liste zum Sammeln der Daten",
            "💡 <code>with open('data.csv', 'w')</code> zum Speichern"
        ],
        "expected": [
            "Datei mit 60+ Messungen",
            "Alle Werte sind plausibel",
            "Diagramm zeigt klare Trends"
        ]
    },
    {
        "pattern": r"3_0.*Sensoren.*\.html",
        "title": "Challenge: Sensor-Dashboard",
        "tasks": [
            "Erstelle ein Live-Dashboard aller Sensoren",
            "Zeige Encoderdaten, IMU, ToF und BME680",
            "Update alle 100ms",
            "Füge Warnmeldungen bei Grenzwerten hinzu",
            "Bonus: Speichere die Daten in einer JSON-Datei"
        ],
        "hints": [
            "💡 Nutze <code>print('\\033[2J')</code> zum Löschen",
            "💡 F-Strings für formatierte Ausgabe",
            "💡 <code>json.dumps()</code> für JSON-Export"
        ],
        "expected": [
            "Dashboard aktualisiert flüssig",
            "Alle Sensoren werden angezeigt",
            "Warnungen bei kritischen Werten"
        ]
    },
    {
        "pattern": r"3_3.*Oled.*\.html",
        "title": "Challenge: Interaktives Display-Menü",
        "tasks": [
            "Erstelle ein 3-Menü-System auf dem OLED",
            "Menü 1: Sensor-Live-Daten",
            "Menü 2: Batteriestatus mit Grafik",
            "Menü 3: Bewegungsprotokoll",
            "Navigation mit Touch-Buttons"
        ],
        "hints": [
            "💡 Nutze die I2C-Bibliothek für OLED",
            "💡 <code>display.text()</code> für Text",
            "💡 Touch-Buttons für Menü-Navigation"
        ],
        "expected": [
            "3 Menüs sind anwählbar",
            "Anzeige ist gut lesbar",
            "Navigation funktioniert intuitiv"
        ]
    }
]


def generate_challenge_html(challenge_data):
    """Generiert den HTML-Code für eine Challenge"""
    tasks_html = "\n".join([f"                    <li>{task}</li>" for task in challenge_data["tasks"]])
    hints_html = "\n".join([f"                    <li>{hint}</li>" for hint in challenge_data["hints"]])
    expected_html = "\n".join([f"                    <li>{result}</li>" for result in challenge_data["expected"]])
    
    return f'''
        <!-- Challenge Section -->
        <div class="challenge-box">
            <h3>🎯 {challenge_data["title"]}</h3>
            
            <div class="challenge-section">
                <h4>📝 Aufgaben:</h4>
                <ol class="challenge-list">
{tasks_html}
                </ol>
            </div>
            
            <div class="challenge-section">
                <h4>💡 Hilfestellungen:</h4>
                <ul class="challenge-list">
{hints_html}
                </ul>
            </div>
            
            <div class="challenge-section">
                <h4>✅ Erwartetes Ergebnis:</h4>
                <ul class="challenge-list">
{expected_html}
                </ul>
            </div>
            
            <div class="challenge-tips">
                <strong>🎓 Tipp:</strong> Teste deinen Code schrittweise und dokumentiere deine Lösungen. 
                Vergleiche mit anderen Lernenden und diskutiere verschiedene Lösungsansätze!
            </div>
        </div>
        <!-- Ende Challenge Section -->'''


def add_challenge_to_file(file_path, challenge_data):
    """Fügt Challenge zu einer HTML-Datei hinzu"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Prüfe ob Challenge bereits vorhanden
        if '<!-- Challenge Section -->' in content or '🎯 Challenge:' in content:
            return False, "Challenge bereits vorhanden"
        
        # Generiere Challenge HTML
        challenge_html = generate_challenge_html(challenge_data)
        
        # Suche nach </main> vor </div> oder back-to-top
        if '</main>' in content:
            new_content = content.replace('</main>', f'{challenge_html}\n        </main>')
        elif '<a href="#" class="back-to-top">↑</a>' in content:
            new_content = content.replace(
                '</div>\n\n    <a href="#" class="back-to-top">↑</a>',
                f'</div>\n{challenge_html}\n\n    <a href="#" class="back-to-top">↑</a>'
            )
        else:
            # Fallback: vor </body>
            new_content = content.replace('</body>', f'{challenge_html}\n</body>')
        
        if content != new_content:
            file_path.write_text(new_content, encoding='utf-8')
            return True, "Challenge hinzugefügt"
        else:
            return False, "Konnte Challenge nicht einfügen"
            
    except Exception as e:
        return False, f"Fehler: {e}"


# Hauptprogramm
if __name__ == "__main__":
    print("🎯 Füge Challenges zu den restlichen 12 Lektionen hinzu")
    print("=" * 70)
    print("")
    
    # Finde alle HTML-Dateien
    html_files = list(html_dir.glob("*.html"))
    
    updated = 0
    skipped = 0
    
    # Durchlaufe alle Challenge-Pattern
    for challenge_data in CHALLENGES:
        pattern = challenge_data["pattern"]
        matched = False
        
        # Suche passende Datei
        for html_file in html_files:
            if re.search(pattern, html_file.name, re.IGNORECASE):
                matched = True
                success, message = add_challenge_to_file(html_file, challenge_data)
                
                if success:
                    print(f"✅ {html_file.name:55} → {message}")
                    updated += 1
                else:
                    print(f"⏭️  {html_file.name:55} → {message}")
                    skipped += 1
                break
        
        if not matched:
            print(f"⚠️  Pattern '{pattern[:30]}...' → Keine passende Datei gefunden")
            skipped += 1
    
    print("")
    print("=" * 70)
    print(f"✅ Aktualisiert: {updated}")
    print(f"⏭️  Übersprungen: {skipped}")
    print(f"📊 Gesamt: {len(CHALLENGES)}")
    print("=" * 70)
    print("")
    print("🎉 Alle Challenges hinzugefügt!")
    print("")
    print("💡 Nächste Schritte:")
    print("   1. Teste ein paar Lektionen im Browser")
    print("   2. Falls alles passt:")
    print("      cd ~/Documents/alvik-webseite")
    print("      git add *.html")
    print("      git commit -m 'Füge Challenges zu allen Lektionen hinzu'")
    print("      git push")
    print("")
    print("🏆 Die Lernplattform ist jetzt komplett mit interaktiven Challenges!")
