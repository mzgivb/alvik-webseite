# 🤖 Arduino Alvik - MicroPython Lernplattform

Eine interaktive Lernplattform für den Arduino Alvik Roboter mit MicroPython, entwickelt vom **Medienzentrum Gießen-Vogelsberg**.

## 🎯 Über das Projekt

Diese Lernplattform wurde speziell für Schüler der 8. Klasse entwickelt, um ihnen die Grundlagen der Robotik und Programmierung mit MicroPython beizubringen. Das didaktische Konzept folgt dem **Dagstuhl-Dreieck** und bietet einen strukturierten Lernpfad vom Grundverständnis bis zu komplexen Projekten.

### ✨ Features

- **4-Level-System**: Progressive Freischaltung von Inhalten (🟢 Grundlagen → 🟠 Erweiterte Projekte)
- **Fortschritts-Tracking**: Automatische Speicherung des Lernfortschritts
- **Interaktive Lektionen**: Schritt-für-Schritt Anleitungen mit Code-Beispielen
- **Copy-Paste Funktion**: Schnelles Kopieren von Code-Blöcken
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

### Level 1: Grundlagen 🟢
- Der Aufbau des Alvik
- Erste Schritte mit MicroPython
- LED-Steuerung
- Grundlegende Bewegungen

### Level 2: Erste Bewegungen 🔵
- Kabellose Steuerung
- Interaktive Fahrprogramme
- Präzise Navigation
- Geometrisches Fahren

### Level 3: Sensoren entdecken 🟡
- Sensor-Integration
- Kollisionsvermeidung
- I2C-Kommunikation

### Level 4: Erweiterte Projekte 🟠
- BME680 Umweltsensor
- OLED-Display Ansteuerung
- phyphox Integration
- Physikalische Experimente
- Mustererkennung & KI

## 🛠️ Technologie

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Design**: Glassmorphism, moderne CSS Grid/Flexbox
- **Speicherung**: LocalStorage für Fortschritt
- **Deployment**: GitHub Actions → FTP
- **Keine Dependencies**: Läuft komplett ohne externe Bibliotheken

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

## 📧 Kontakt

Fragen, Anregungen oder Feedback?

- **E-Mail**: kontakt@medienzentrum-giessen-vogelsberg.de
- **Website**: [www.medienzentrum-giessen-vogelsberg.de](https://www.medienzentrum-giessen-vogelsberg.de)

## 🌟 Danksagung

Besonderer Dank an:
- Die Arduino Education Community
- Alle Lehrenden, die Feedback gegeben haben
- Die Schülerinnen und Schüler, die die Plattform getestet haben

---

**Made with ❤️ für digitale Bildung**
