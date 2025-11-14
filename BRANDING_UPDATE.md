# 🎨 Medienzentrum Gießen-Vogelsberg Branding Update

## 📦 Was wurde vorbereitet?

1. ✅ **MZ_GIVB_Logo.svg** - Dein Logo ist bereit zum Download
2. ✅ **update_branding.sh** - Automatisches Update-Script
3. ✅ **HEADER_TEMPLATE.html** - Neue Header-Vorlage
4. ✅ **Neue Farbpalette** basierend auf eurem Logo

## 🎨 Neue Farben (aus eurem Logo)

- **Primär:** #004a95 (Dunkelblau) 🔵
- **Sekundär:** #51b047 (Grün) 🟢
- **Akzent:** #ef7e26 (Orange) 🟠
- **Rot:** #e30613 (Rot) 🔴

## 🚀 Schnell-Anleitung

### Option 1: Automatisches Update (Empfohlen)

```bash
cd ~/Documents/alvik-webseite

# 1. Logo herunterladen und ins Verzeichnis kopieren
# (Das Logo findest du in Claude - einfach runterladen)

# 2. Script ausführbar machen
chmod +x update_branding.sh

# 3. Script ausführen
./update_branding.sh
```

Das Script macht automatisch:
- ✅ Logo ins assets-Verzeichnis kopieren
- ✅ Alle Farben im CSS anpassen
- ✅ Header in allen HTML-Dateien aktualisieren
- ✅ Gradient-Farben auf Medienzentrum-Farben ändern

### Option 2: Manuelle Anpassung

Falls das Script nicht funktioniert:

#### Schritt 1: Logo kopieren
```bash
cp MZ_GIVB_Logo.svg ~/Documents/alvik-webseite/assets/
```

#### Schritt 2: CSS-Farben anpassen

Öffne `css/style.css` und ersetze im `:root` Block:

```css
--primary-color: #004a95;        /* alt: #0EA5E9 */
--primary-dark: #003366;         /* alt: #0284C7 */
--secondary-color: #51b047;      /* alt: #8B5CF6 */
--accent-color: #ef7e26;         /* alt: #F59E0B */
--accent-dark: #dd2e34;          /* alt: #D97706 */
```

Gradient-Hintergrund ändern:
```css
body {
    background: linear-gradient(135deg, #004a95 0%, #51b047 100%);
}
```

#### Schritt 3: Header in HTML-Dateien anpassen

In allen `*.html` Dateien:

**Alt:**
```html
<img src="assets/C500-AKX00066_10.EXTRA.jpg" alt="Arduino Alvik" class="logo">
<div>
    <h1>Arduino Alvik</h1>
    <p>MicroPython Lernplattform</p>
</div>
```

**Neu:**
```html
<img src="assets/MZ_GIVB_Logo.svg" alt="Medienzentrum Gießen-Vogelsberg" class="logo" style="width: 120px; height: auto; border-radius: 8px; background: white; padding: 8px;">
<div>
    <h1>Arduino Alvik</h1>
    <p>MicroPython Lernplattform<br>
    <small style="font-size: 0.85em; opacity: 0.95; font-weight: 500;">Medienzentrum Gießen-Vogelsberg</small></p>
</div>
```

## ✅ Checkliste

- [ ] Logo heruntergeladen
- [ ] Logo in `assets/` Verzeichnis kopiert
- [ ] Script ausgeführt ODER manuell angepasst
- [ ] Webseite im Browser getestet
- [ ] Sieht alles gut aus? → Zum Git-Push!

## 🚀 Deployment

Wenn alles gut aussieht:

```bash
cd ~/Documents/alvik-webseite

git add .
git commit -m "🎨 Update branding for Medienzentrum Gießen-Vogelsberg"
git push origin main
```

## 🎯 Was wird sich ändern?

### Vorher:
- Türkis/Lila Farben
- Arduino Alvik Logo
- "MicroPython Lernplattform"

### Nachher:
- Blau/Grün Farben (Medienzentrum)
- Euer MZ Gießen-Vogelsberg Logo
- "Arduino Alvik - MicroPython Lernplattform<br>Medienzentrum Gießen-Vogelsberg"

## 💡 Hinweise

- Das alte Arduino-Logo bleibt im assets-Ordner (wird nicht gelöscht)
- Ein Backup des CSS wird automatisch erstellt (`style.css.backup`)
- Bei Problemen: Backup zurückkopieren

## 📞 Support

Falls etwas nicht funktioniert, kannst du jederzeit:
1. Das Backup wiederherstellen: `cp css/style.css.backup css/style.css`
2. Mich (Claude) wieder fragen 😊

Viel Erfolg! 🎉
