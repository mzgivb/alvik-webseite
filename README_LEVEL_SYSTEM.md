# 🚀 Level-System Implementation - Arduino Alvik Lernplattform

**Datum:** 17. November 2025  
**Status:** Bereit für Deployment

---

## ✅ Was wurde gemacht?

### 1. Neue Dateien erstellt:
- ✅ `index.html` - Neue Startseite mit Level-System
- ✅ `js/main.js` - JavaScript mit Fortschritts-Tracking
- ✅ `update_navigation_level_system.py` - Script zum Update aller Seiten
- ✅ `deploy_level_system.sh` - Deployment-Script
- ✅ Backups: `index_backup_20251117.html`, `js/main_backup_20251117.js`

### 2. Features implementiert:
- 🎯 **4-Level-Struktur** (Grün → Blau → Gelb → Orange)
- 📊 **Fortschrittsanzeige** (0-100% mit localStorage)
- 🔒 **Level-Freischaltung** (3 Lektionen → nächstes Level)
- 🔺 **Dagstuhl-Dreieck** (🔧 Technologie, 💡 Anwendung, 🌍 Gesellschaft)
- ✅ **Checkboxen** (⬜ → ✅ bei Abschluss)
- 🎮 **"Lektion abschließen" Button** auf jeder Seite

---

## 📋 Deployment-Schritte

### Schritt 1: Erste Änderungen pushen

```bash
cd /Users/jochenleeder/Documents/alvik-webseite

# Script ausführbar machen
chmod +x deploy_level_system.sh

# Deployment ausführen
./deploy_level_system.sh
```

**Das passiert:**
- Git add & commit der neuen Dateien
- Push zu GitHub
- GitHub Actions deployed automatisch

### Schritt 2: Navigation auf allen Seiten aktualisieren

```bash
# Python-Script ausführen
python3 update_navigation_level_system.py
```

**Das passiert:**
- Script liest alle *.html Dateien
- Ersetzt alte Navigation durch neue Level-Navigation
- Fügt CSS-Styles hinzu
- Zeigt Fortschritt in der Console

### Schritt 3: Aktualisierte Seiten pushen

```bash
git add *.html
git commit -m "Aktualisiere Navigation auf allen Seiten mit Level-System"
git push
```

---

## 🧪 Testen

### Lokal testen (vor dem Push):
1. Öffne `index.html` in Browser
2. Prüfe ob:
   - Fortschrittsanzeige sichtbar ist
   - Level 2-4 gesperrt sind (🔒)
   - Dagstuhl-Legende angezeigt wird
3. Öffne eine Lektionsseite (z.B. `1__Welcome_Alvik_.html`)
4. Klicke "Lektion abschließen"
5. Prüfe ob:
   - ✅ erscheint in Navigation
   - Fortschrittsbalken steigt
   - Nach 3 Lektionen Level 2 freigeschaltet wird

### Live testen (nach dem Push):
1. Warte ~60 Sekunden (GitHub Actions Deployment)
2. Öffne: http://alvik.mzgivb.de/
3. Hard Reload: `Cmd + Shift + R`
4. Wiederhole die Tests von oben

---

## 🔧 Konfiguration anpassen

### Freischaltungs-Anforderungen ändern:
In `js/main.js` Zeile ~6-11:

```javascript
const LEVEL_CONFIG = {
    1: { required: 0, unlock: 0 },    // Level 1 immer offen
    2: { required: 1, unlock: 3 },    // 3 aus Level 1 → Level 2 öffnet
    3: { required: 2, unlock: 3 },    // 3 aus Level 2 → Level 3 öffnet
    4: { required: 3, unlock: 2 }     // 2 aus Level 3 → Level 4 öffnet
};
```

### Anzahl Lektionen ändern:
In `js/main.js` Zeile ~5:

```javascript
const TOTAL_LESSONS = 16;  // Hier Zahl anpassen
```

### Farben ändern:
In `index.html` im `<style>` Bereich die Hex-Codes anpassen:
- Level 1: `#4ade80` (Grün)
- Level 2: `#60a5fa` (Blau)
- Level 3: `#facc15` (Gelb)
- Level 4: `#fb923c` (Orange)

---

## 🐛 Troubleshooting

### Problem: Python-Script findet keine Dateien
**Lösung:**
```bash
# Prüfe aktuelles Verzeichnis
pwd

# Sollte sein: /Users/jochenleeder/Documents/alvik-webseite
# Falls nicht, navigiere dorthin:
cd /Users/jochenleeder/Documents/alvik-webseite
```

### Problem: Fortschritt wird nicht gespeichert
**Lösung:**
1. Browser Console öffnen (F12)
2. Eingeben: `alvikProgress.load()`
3. Prüfe localStorage: `localStorage.getItem('alvik_progress')`
4. Falls leer: Browser erlaubt localStorage?

### Problem: Level bleiben gesperrt
**Lösung:**
```javascript
// In Browser Console:
alvikProgress.countInLevel(1)  // Sollte Anzahl zeigen
alvikProgress.load()            // Zeigt abgeschlossene Seiten
```

### Problem: Deployment schlägt fehl
**Lösung:**
1. GitHub Actions prüfen: https://github.com/mzgivb/alvik-webseite/actions
2. Logs lesen
3. Falls FTP-Fehler: Prüfe ob `FTP_PASSWORD` Secret gesetzt ist

---

## 📁 Dateistruktur

```
alvik-webseite/
├── index.html                              ✅ NEU (mit Level-System)
├── index_backup_20251117.html              🔒 BACKUP
├── js/
│   ├── main.js                             ✅ NEU (mit Fortschritt)
│   └── main_backup_20251117.js             🔒 BACKUP
├── update_navigation_level_system.py       ✅ NEU (Update-Script)
├── deploy_level_system.sh                  ✅ NEU (Deploy-Script)
└── README_LEVEL_SYSTEM.md                  📖 Diese Datei
```

---

## 🎓 Für Schüler: Fortschritt zurücksetzen

Falls ein Schüler von vorne anfangen möchte:

1. Browser öffnen auf der Alvik-Seite
2. F12 drücken (Developer Tools)
3. Console-Tab öffnen
4. Eingeben: `alvikProgress.reset()`
5. Seite neu laden

---

## 📊 Monitoring

### Fortschritt überprüfen:
```javascript
// In Browser Console:
alvikProgress.load()           // Zeigt alle abgeschlossenen Seiten
alvikProgress.countInLevel(1)  // Zeigt Anzahl in Level 1
```

### Einzelne Seite als abgeschlossen markieren (zum Testen):
```javascript
alvikProgress.markCompleted('1__Welcome_Alvik_.html')
window.location.reload()
```

---

## 🔗 Wichtige Links

- **GitHub Repo:** https://github.com/mzgivb/alvik-webseite
- **GitHub Actions:** https://github.com/mzgivb/alvik-webseite/actions
- **Live-Seite:** http://alvik.mzgivb.de/
- **Skill-Dokumentation:** `/mnt/skills/user/alvik-webseite/SKILL.md`

---

## ✨ Nächste Schritte (Optional)

### Kurzfristig:
- [ ] Navigation auf allen Seiten aktualisieren (Python-Script ausführen)
- [ ] Mit Schülern testen
- [ ] Feedback sammeln

### Mittelfristig:
- [ ] 2-3 neue Testszenarien als HTML-Seiten erstellen
- [ ] Lösungen in Aufgabenseiten als Spoiler einbauen
- [ ] Mobile-Ansicht optimieren

### Langfristig:
- [ ] Zertifizierungs-Challenge implementieren
- [ ] Leaderboard (optional)
- [ ] Export/Import von Fortschritt

---

## 🆘 Bei Problemen

1. **Zuerst:** Browser Console checken (F12)
2. **Dann:** GitHub Actions Logs prüfen
3. **Falls nötig:** Backup-Dateien zurückkopieren:
   ```bash
   cp index_backup_20251117.html index.html
   cp js/main_backup_20251117.js js/main.js
   git add .
   git commit -m "Rollback zum vorherigen Stand"
   git push
   ```

---

**Viel Erfolg mit dem Level-System! 🚀**

*Bei Fragen einfach diese README nochmal durchlesen oder in der Browser-Console experimentieren.*
