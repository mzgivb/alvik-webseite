#!/bin/bash
# Script um Command Center Link in alle HTML-Dateien einzufügen

cd ~/Documents/alvik-webseite

echo "🔧 Füge Command Center Link in alle HTML-Dateien ein..."

# Alle HTML-Dateien finden und bearbeiten
find . -maxdepth 1 -name "*.html" ! -name "command-center.html" -type f | while read file; do
    # Prüfen ob Link schon existiert
    if grep -q 'command-center.html' "$file"; then
        echo "✅ Bereits aktualisiert: $file"
        continue
    fi
    
    # Link nach der API-Liste Zeile einfügen
    if grep -q '1_1_Alvik_API.html' "$file"; then
        # Auf Mac (BSD sed) brauchen wir -i '' für in-place editing
        sed -i '' '/1_1_Alvik_API.html/a\
    <li><a href="command-center.html">🚀 Command Center</a></li>
' "$file"
        echo "✅ Aktualisiert: $file"
    else
        echo "⚠️  Keine API-Liste gefunden in: $file"
    fi
done

echo ""
echo "🎉 Fertig! Jetzt kannst du committen und pushen:"
echo ""
echo "git add ."
echo 'git commit -m "Add Command Center link to all pages"'
echo "git push origin main"
