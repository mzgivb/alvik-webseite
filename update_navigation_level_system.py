#!/usr/bin/env python3
"""
Script zum Aktualisieren der Navigation auf allen HTML-Seiten
der Arduino Alvik Lernplattform mit dem neuen Level-System.
"""

import os
import re
from pathlib import Path

# Projektverzeichnis
PROJECT_DIR = Path("/Users/jochenleeder/Documents/alvik-webseite")

# Neue Navigation (Sidebar) Template
NEW_NAVIGATION = '''        <aside class="sidebar">
            <h2>Navigation</h2>
            
            <!-- Fortschrittsanzeige -->
            <div style="background: linear-gradient(135deg, rgba(227, 6, 19, 0.1), rgba(103, 116, 122, 0.1)); padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-weight: 600; font-size: 0.9rem;">Dein Fortschritt</span>
                    <span id="progress-percentage" style="font-weight: 700; color: var(--primary-color);">0%</span>
                </div>
                <div style="background: rgba(255,255,255,0.5); border-radius: 8px; height: 10px; overflow: hidden;">
                    <div id="progress-bar" style="background: linear-gradient(90deg, #4ade80, #22c55e); height: 100%; width: 0%; transition: width 0.3s ease;"></div>
                </div>
                <div style="font-size: 0.75rem; color: #666; margin-top: 0.5rem;">
                    <span id="progress-text">0 von 16 Lektionen</span>
                </div>
            </div>
            
            <!-- Dagstuhl-Dreieck Legende -->
            <div class="dagstuhl-legend">
                <h4>🔺 Dagstuhl-Dreieck</h4>
                <div class="dagstuhl-item">
                    <span>🔧</span>
                    <span><strong>Wie funktioniert's?</strong> (Technologie)</span>
                </div>
                <div class="dagstuhl-item">
                    <span>💡</span>
                    <span><strong>Wie nutze ich's?</strong> (Anwendung)</span>
                </div>
                <div class="dagstuhl-item">
                    <span>🌍</span>
                    <span><strong>Warum ist's wichtig?</strong> (Gesellschaft)</span>
                </div>
            </div>
            
            <div class="search-box">
                <input type="text" id="search-input" placeholder="Suche...">
            </div>
            
            <div class="nav-section">
                <ul>
                    <li><a href="index.html" class="active" style="background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); color: white; font-weight: 600;">🏠 Startseite</a></li>
                </ul>
            </div>
            
            <!-- Level 1: Grundlagen -->
            <div class="nav-section" data-level="1">
                <h3 style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="background: #4ade80; color: white; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 700;">1</span>
                    Level 1: Grundlagen
                    <span style="font-size: 1.2rem;">🟢</span>
                </h3>
                <ul>
                    <li data-page="1__Welcome_Alvik_.html">
                        <a href="1__Welcome_Alvik_.html">
                            <span class="completion-check">⬜</span>
                            🔧 Der Aufbau
                        </a>
                    </li>
                    <li data-page="1_3_Alvik_mit_Kabel_betreiben.html">
                        <a href="1_3_Alvik_mit_Kabel_betreiben.html">
                            <span class="completion-check">⬜</span>
                            🔧 Alvik mit Kabel betreiben
                        </a>
                    </li>
                    <li data-page="1_2_Alvik_Grundgeru_st.html">
                        <a href="1_2_Alvik_Grundgeru_st.html">
                            <span class="completion-check">⬜</span>
                            💻 Alvik Grundgerüst
                        </a>
                    </li>
                    <li data-page="1_3_1_LED_blinken_lassen.html">
                        <a href="1_3_1_LED_blinken_lassen.html">
                            <span class="completion-check">⬜</span>
                            💡 LED blinken lassen
                        </a>
                    </li>
                </ul>
            </div>
            
            <!-- Level 2: Erste Bewegungen -->
            <div class="nav-section locked" data-level="2" data-required-level="1" data-required-count="3">
                <h3 style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="background: #60a5fa; color: white; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 700;">2</span>
                    Level 2: Erste Bewegungen
                    <span style="font-size: 1.2rem;">🔵</span>
                    <span class="lock-icon" style="font-size: 1rem; margin-left: auto;">🔒</span>
                </h3>
                <ul>
                    <li data-page="1_4_Alvik_ohne_Kabel_betreiben.html">
                        <a href="1_4_Alvik_ohne_Kabel_betreiben.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🔧 Alvik ohne Kabel betreiben
                        </a>
                    </li>
                    <li data-page="1_5_2_Alvik_fa_hrt_auf_Tastendruck.html">
                        <a href="1_5_2_Alvik_fa_hrt_auf_Tastendruck.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            💡 Auf Tastendruck fahren
                        </a>
                    </li>
                    <li data-page="1_5_Alvik_ein_Viereck_fahren_lassen.html">
                        <a href="1_5_Alvik_ein_Viereck_fahren_lassen.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🌍 Viereck fahren
                        </a>
                    </li>
                    <li data-page="1_5_1_Alvik_exakt_fahren_lassen.html">
                        <a href="1_5_1_Alvik_exakt_fahren_lassen.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            💡 Exakt fahren
                        </a>
                    </li>
                </ul>
            </div>
            
            <!-- Level 3: Sensoren entdecken -->
            <div class="nav-section locked" data-level="3" data-required-level="2" data-required-count="3">
                <h3 style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="background: #facc15; color: white; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 700;">3</span>
                    Level 3: Sensoren entdecken
                    <span style="font-size: 1.2rem;">🟡</span>
                    <span class="lock-icon" style="font-size: 1rem; margin-left: auto;">🔒</span>
                </h3>
                <ul>
                    <li data-page="3_0_Alvik_Sensoren_auslesen.html">
                        <a href="3_0_Alvik_Sensoren_auslesen.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🔧 Sensoren auslesen
                        </a>
                    </li>
                    <li data-page="1_5_3_Alvik_API_Collisionsvermeidung.html">
                        <a href="1_5_3_Alvik_API_Collisionsvermeidung.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            💡 Kollisionsvermeidung
                        </a>
                    </li>
                    <li data-page="2_0_Alvik_I2C_testen.html">
                        <a href="2_0_Alvik_I2C_testen.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🔧 I2C Schnittstelle testen
                        </a>
                    </li>
                </ul>
            </div>
            
            <!-- Level 4: Erweiterte Projekte -->
            <div class="nav-section locked" data-level="4" data-required-level="3" data-required-count="2">
                <h3 style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="background: #fb923c; color: white; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 700;">4</span>
                    Level 4: Erweiterte Projekte
                    <span style="font-size: 1.2rem;">🟠</span>
                    <span class="lock-icon" style="font-size: 1rem; margin-left: auto;">🔒</span>
                </h3>
                <ul>
                    <li data-page="2_1_Alvik_mit_bme680.html">
                        <a href="2_1_Alvik_mit_bme680.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🔧 Alvik mit BME680 Sensor
                        </a>
                    </li>
                    <li data-page="3_3_Alvik_mit_Oled_Display.html">
                        <a href="3_3_Alvik_mit_Oled_Display.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            💡 Alvik mit OLED Display
                        </a>
                    </li>
                    <li data-page="3_1_Alvik_mit_phyphox.html">
                        <a href="3_1_Alvik_mit_phyphox.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🌍 Alvik mit phyphox
                        </a>
                    </li>
                    <li data-page="3_2_Physik_Beispiel_Alvik.html">
                        <a href="3_2_Physik_Beispiel_Alvik.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            🌍 Beschleunigte Bewegung
                        </a>
                    </li>
                    <li data-page="6_0_Mustererkennung.html">
                        <a href="6_0_Mustererkennung.html" class="locked-link">
                            <span class="completion-check">⬜</span>
                            💡 Mustererkennung & KI
                        </a>
                    </li>
                </ul>
            </div>
            
            <!-- Referenz & Hilfe -->
            <div class="nav-section">
                <h3>📚 Referenz & Hilfe</h3>
                <ul>
                    <li><a href="command-center.html">🚀 Command Center</a></li>
                    <li><a href="1_1_Alvik_API.html">📖 API-Liste</a></li>
                    <li><a href="4_0_Alvik_Kurse_online.html">🌐 Online-Kurse</a></li>
                </ul>
            </div>
            
            <!-- Praxis & Übungen -->
            <div class="nav-section">
                <h3>✏️ Praxis & Übungen</h3>
                <ul>
                    <li><a href="5_0_Beispielaufgaben_Alvik.html">📝 Beispielaufgaben</a></li>
                </ul>
            </div>
        </aside>'''

# CSS Styles die im <head> hinzugefügt werden müssen
ADDITIONAL_STYLES = '''
        /* Level-System Styles */
        .nav-section.locked h3 {
            opacity: 0.6;
        }
        
        .nav-section.locked a.locked-link {
            opacity: 0.5;
            pointer-events: none;
            color: #999;
        }
        
        .completion-check {
            font-size: 0.9rem;
            margin-right: 0.3rem;
        }
        
        .completed .completion-check {
            color: #22c55e;
        }
        
        /* Dagstuhl Legende */
        .dagstuhl-legend {
            background: linear-gradient(135deg, rgba(227, 6, 19, 0.05), rgba(103, 116, 122, 0.05));
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            font-size: 0.85rem;
        }
        
        .dagstuhl-legend h4 {
            margin: 0 0 0.5rem 0;
            font-size: 0.9rem;
        }
        
        .dagstuhl-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 0.25rem 0;
        }'''


def update_html_file(filepath):
    """Aktualisiert eine HTML-Datei mit der neuen Navigation"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip index.html - wurde schon manuell aktualisiert
        if filepath.name == 'index.html':
            print(f"⏭️  Überspringe {filepath.name} (schon aktualisiert)")
            return False
        
        # Finde und ersetze die alte Sidebar
        # Pattern: Alles zwischen <aside class="sidebar"> und </aside>
        pattern = r'(<aside class="sidebar">)(.*?)(</aside>)'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print(f"⚠️  Keine Sidebar gefunden in {filepath.name}")
            return False
        
        # Ersetze die alte Navigation
        new_content = re.sub(pattern, NEW_NAVIGATION + r'\3', content, flags=re.DOTALL)
        
        # Füge CSS Styles hinzu, falls noch nicht vorhanden
        if "Level-System Styles" not in new_content:
            # Suche nach </style> Tag
            style_pattern = r'(</style>)'
            if re.search(style_pattern, new_content):
                new_content = re.sub(style_pattern, ADDITIONAL_STYLES + r'\n    \1', new_content)
        
        # Schreibe die aktualisierte Datei
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Aktualisiert: {filepath.name}")
        return True
        
    except Exception as e:
        print(f"❌ Fehler bei {filepath.name}: {e}")
        return False


def main():
    """Hauptfunktion: Aktualisiert alle HTML-Dateien"""
    print("🚀 Starte Navigation-Update für alle HTML-Seiten...\n")
    
    # Finde alle HTML-Dateien (außer in Unterverzeichnissen)
    html_files = list(PROJECT_DIR.glob("*.html"))
    
    updated = 0
    skipped = 0
    errors = 0
    
    for html_file in html_files:
        result = update_html_file(html_file)
        if result is True:
            updated += 1
        elif result is False and "Überspringe" in str(html_file):
            skipped += 1
        else:
            errors += 1
    
    print(f"\n📊 Zusammenfassung:")
    print(f"   ✅ Aktualisiert: {updated} Dateien")
    print(f"   ⏭️  Übersprungen: {skipped} Dateien")
    print(f"   ❌ Fehler: {errors} Dateien")
    print(f"\n🎉 Fertig!")


if __name__ == "__main__":
    main()
