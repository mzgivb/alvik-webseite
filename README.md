# 🤖 Arduino Alvik - MicroPython Lernplattform

Eine interaktive Lernplattform für den Arduino Alvik Roboter mit MicroPython, entwickelt vom **Medienzentrum Gießen-Vogelsberg**.

## 🎯 Über das Projekt

Diese Lernplattform wurde speziell für Schüler der **8. Klasse** entwickelt, um ihnen die Grundlagen der Robotik und Programmierung mit MicroPython beizubringen. Das didaktische Konzept folgt dem **Dagstuhl-Dreieck** und bietet einen strukturierten Lernpfad vom Grundverständnis bis zu komplexen Projekten wie Künstlicher Intelligenz.

### ✨ Features

- **4-Level-System mit 17 Lektionen**: Progressive Freischaltung von Inhalten (🟢 Grundlagen → 🟠 Erweiterte Projekte)
- **Fortschritts-Tracking**: Automatische Speicherung des Lernfortschritts im Browser
- **Interaktive Lektionen**: Schritt-für-Schritt Anleitungen mit ausführlichen Code-Beispielen
- **Interaktive Quizze**: Multiple-Choice-Tests mit direktem Feedback zu jedem Thema
- **Programmier-Challenges**: Praktische Aufgaben mit Musterlösungen zum Aufklappen
- **Selbsttests**: Checklisten zur Selbsteinschätzung des Lernfortschritts
- **Command Center**: Übersicht aller Alvik-API-Befehle mit Code-Beispielen
- **Copy-Paste Funktion**: Schnelles Kopieren von Code-Blöcken
- **Beispielaufgaben**: Strukturierte Test-Seite mit 3 Schwierigkeitsleveln
- **Responsive Design**: Funktioniert auf Desktop, Tablet und Smartphone
- **Dagstuhl-Dreieck Integration**:
  - 🔧 **Technologie** - Wie funktioniert's?
  - 💡 **Anwendung** - Was kann man damit machen?
  - 🌍 **Gesellschaft** - Welche Auswirkungen hat das?

## 🚀 Schnellstart

### Live-Demo
👉 [https://alvik.mzgivb.de](https://alvik.mzgivb.de)

### Lokale Installation

1. Repository klonen:
```bash
git clone https://github.com/mzgivb/alvik-webseite.git
cd alvik-webseite
```

2. Mit einem lokalen Webserver öffnen:
```bash
# Python 3
python3 -m http.server 8000

# Dann im Browser öffnen:
# http://localhost:8000
```

## 📚 Lernpfad

### Level 1: Grundlagen 🟢 (5 Lektionen)
- 🔧 **Der Aufbau** - Hardware-Komponenten des Alvik kennenlernen
- 🔧 **Alvik mit Kabel betreiben** - Erste Verbindung und Setup
- 💻 **Alvik Grundgerüst** - Struktur eines MicroPython-Programms
- 💡 **LED blinken lassen** - Erste Erfolgserlebnisse mit Output
- 🐍 **Python Werkzeugkasten** - Grundlagen: Variablen, Schleifen, Funktionen, Listen, if/else

### Level 2: Erste Bewegungen 🔵 (4 Lektionen)
- 🔧 **Alvik ohne Kabel betreiben** - Autonomer Betrieb über Batterie
- 💡 **Auf Tastendruck fahren** - Touch-Sensoren nutzen
- 🌍 **Viereck fahren** - Schleifen und geometrisches Programmieren
- 💡 **Exakt fahren** - Präzise Navigation mit move() und rotate()

### Level 3: Sensoren entdecken 🟡 (3 Lektionen)
- 🔧 **Sensoren auslesen** - Entfernungs- und Farbsensor verstehen
- 💡 **Kollisionsvermeidung** - Autonome Navigation mit Sensordaten
- 🔧 **I2C Schnittstelle testen** - Externe Sensoren anschließen

### Level 4: Erweiterte Projekte 🟠 (5 Lektionen)
- 🔧 **Alvik mit BME680 Sensor** - Temperatur, Luftfeuchtigkeit, Luftdruck messen
- 💡 **Alvik mit OLED Display** - Informationen anzeigen
- 🌍 **Alvik mit phyphox** - Daten live auf dem Smartphone visualisieren
- 🌍 **Beschleunigte Bewegung** - Physikalische Experimente durchführen
- 💡 **Mustererkennung & KI** - Machine Learning auf dem Microcontroller

### 📝 Praxis & Übungen
- **Beispielaufgaben** - Systematische Wissensüberprüfung in 3 Levels:
  - **Level 1: Python & Bewegung** - Variablen, Schleifen, Funktionen, Motorsteuerung
  - **Level 2: Sensoren & Entscheidungen** - Sensoren auslesen, if/else-Logik, LEDs steuern
  - **Level 3: Integration** - Miniprojekte mit allen gelernten Konzepten

### 📚 Referenz & Hilfe
- **Command Center** - Interaktive Übersicht aller Alvik-API-Befehle
- **API-Liste** - Vollständige Dokumentation der MicroPython-Befehle
- **Online-Kurse** - Links zu weiterführenden Ressourcen

## 🛠️ Technologie

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Design**: Glassmorphism, moderne CSS Grid/Flexbox
- **Speicherung**: LocalStorage für Fortschritt
- **Interaktivität**: Native JavaScript für Quizze und Challenges
- **Deployment**: GitHub Actions → FTP
- **Keine Dependencies**: Läuft komplett ohne externe Bibliotheken

## 🎓 Didaktisches Konzept

### Für 8. Klasse optimiert
Alle Inhalte wurden speziell für Schüler der 8. Klasse aufbereitet:
- Verständliche Sprache und Alltagsbeispiele
- Schrittweise Komplexitätssteigerung
- Visuelle Unterstützung durch Code-Beispiele
- Sofortiges Feedback durch interaktive Quizze
- Selbsteinschätzung durch Checklisten

### Interaktive Elemente
Jede Lektion enthält:
- **Theoretische Erklärungen** mit anschaulichen Beispielen
- **Interaktive Quizze** zur Wissensüberprüfung
- **Programmier-Challenges** mit Lösungen zum Aufklappen
- **Selbsttests** mit Checklisten

### Progressive Freischaltung
- Neue Level werden erst nach Abschluss von 2-3 Lektionen freigeschaltet
- Verhindert Überforderung durch zu viele Inhalte
- Motiviert durch klare Fortschrittsanzeige

## 📖 Für Lehrende

### Anpassung der Level-Freischaltung

In `js/main.js` können die Freischaltungs-Anforderungen angepasst werden:

```javascript
const LEVEL_CONFIG = {
    1: { required: 0, unlock: 0 },    // Level 1 immer offen
    2: { required: 1, unlock: 3 },    // 3 Lektionen aus Level 1
    3: { required: 2, unlock: 3 },    // 3 Lektionen aus Level 2
    4: { required: 3, unlock: 2 }     // 2 Lektionen aus Level 3
};
```

### Fortschritt zurücksetzen

Schüler können ihren Fortschritt über die Browser-Console zurücksetzen:
```javascript
alvikProgress.reset()
```

### Inhalte anpassen

Alle Lektionen sind als einzelne HTML-Dateien organisiert:
- `1_*.html` - Level 1: Grundlagen
- `2_*.html` - Level 3: Sensoren (historische Nummerierung)
- `3_*.html` - Level 4: Erweiterte Projekte (historische Nummerierung)
- `5_0_Beispielaufgaben_Alvik.html` - Übungsseite

Die Navigation wird automatisch aus den Sidebar-Einträgen generiert.

## 🤝 Beitragen

Verbesserungsvorschläge und Beiträge sind willkommen!

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/NeueLektion`)
3. Committe deine Änderungen (`git commit -m 'Füge neue Lektion hinzu'`)
4. Push zum Branch (`git push origin feature/NeueLektion`)
5. Öffne einen Pull Request

## 📜 Lizenz

Dieses Projekt steht unter der **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.

Das bedeutet:
- ✅ **Teilen** - Kopieren und Weiterverbreiten in jedem Format
- ✅ **Anpassen** - Remixen, verändern und darauf aufbauen
- ⚠️ **Namensnennung** - Angemessene Urheber- und Rechteangabe erforderlich
- ⚠️ **Weitergabe unter gleichen Bedingungen** - Bei Änderungen gleiche Lizenz verwenden

Siehe [LICENSE](LICENSE) für Details.

## 👏 Credits

**Entwickelt von:**
📍 **Medienzentrum Gießen-Vogelsberg**
🌐 [www.medienzentrum-giessen-vogelsberg.de](https://www.medienzentrum-giessen-vogelsberg.de)

**Projektleitung:**
Jochen Leeder - Direktor Medienzentrum Gießen-Vogelsberg

**Basiert auf:**
Arduino Alvik - Arduino Education
MicroPython - Python für Microcontroller

**Mit Unterstützung von:**
Claude Code - KI-gestützter Entwicklungsassistent

## 📧 Kontakt

Fragen, Anregungen oder Feedback?

- **E-Mail**: info@mzgivb.de
- **Website**: [www.medienzentrum-giessen-vogelsberg.de](https://www.medienzentrum-giessen-vogelsberg.de)
- **GitHub Issues**: [Issues auf GitHub](https://github.com/mzgivb/alvik-webseite/issues)

## 🌟 Danksagung

Besonderer Dank an:
- Die Arduino Education Community
- Alle Lehrenden, die Feedback gegeben haben
- Die Schülerinnen und Schüler der 8. Klassen, die die Plattform getestet haben
- Die Open-Source-Community für MicroPython

---

**Made with ❤️ für digitale Bildung**
