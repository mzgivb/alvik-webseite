#!/bin/bash
# Script zum Update des Designs auf Medienzentrum Gießen-Vogelsberg

echo "🎨 Aktualisiere Design für Medienzentrum Gießen-Vogelsberg..."

cd ~/Documents/alvik-webseite

# 1. Logo ins assets-Verzeichnis kopieren (wenn noch nicht geschehen)
if [ -f "MZ_GIVB_Logo.svg" ]; then
    cp MZ_GIVB_Logo.svg assets/
    echo "✅ Logo kopiert"
fi

# 2. Farben in CSS anpassen
echo "🎨 Passe Farbpalette an..."

# Backup erstellen
cp css/style.css css/style.css.backup

# Farben ersetzen
sed -i '' 's/#0EA5E9/#004a95/g' css/style.css
sed -i '' 's/#0284C7/#003366/g' css/style.css
sed -i '' 's/#8B5CF6/#51b047/g' css/style.css
sed -i '' 's/#F59E0B/#ef7e26/g' css/style.css
sed -i '' 's/#D97706/#dd2e34/g' css/style.css
sed -i '' 's/#10B981/#51b047/g' css/style.css
sed -i '' 's/#EF4444/#e30613/g' css/style.css

echo "✅ Farben aktualisiert"

# 3. Gradient-Farben anpassen
sed -i '' 's/667eea/004a95/g' css/style.css
sed -i '' 's/764ba2/51b047/g' css/style.css

echo "✅ Gradients aktualisiert"

# 4. Header in allen HTML-Dateien aktualisieren
echo "🔄 Aktualisiere Header in allen Seiten..."

for file in *.html; do
    # Altes Logo mit neuem ersetzen
    sed -i '' 's|assets/C500-AKX00066_10.EXTRA.jpg|assets/MZ_GIVB_Logo.svg|g' "$file"
    
    # Untertitel ändern
    sed -i '' 's|<p>MicroPython Lernplattform</p>|<p>MicroPython Lernplattform<br><small style="font-size: 0.8em; opacity: 0.9;">Medienzentrum Gießen-Vogelsberg</small></p>|g' "$file"
done

echo "✅ Header in allen Seiten aktualisiert"

echo ""
echo "🎉 Fertig! Design wurde erfolgreich auf Medienzentrum Gießen-Vogelsberg angepasst!"
echo ""
echo "📋 Nächste Schritte:"
echo "   1. Öffne eine Seite im Browser und prüfe das Design"
echo "   2. Wenn alles gut aussieht:"
echo "      git add ."
echo "      git commit -m '🎨 Update design for Medienzentrum Gießen-Vogelsberg'"
echo "      git push origin main"
