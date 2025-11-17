#!/bin/bash

# Commit-Script für Level-System Update
# Datum: 2025-11-17

cd /Users/jochenleeder/Documents/alvik-webseite

echo "📦 Füge Änderungen hinzu..."
git add index.html
git add index_backup_20251117.html
git add js/main.js
git add js/main_backup_20251117.js
git add update_navigation_level_system.py

echo "💾 Committe Änderungen..."
git commit -m "Füge Level-basiertes Fortschritts-System hinzu

- ✨ Neue Navigation mit 4-Level-Struktur (Grundlagen, Bewegung, Sensoren, Projekte)
- 📊 Fortschrittsanzeige mit localStorage-Tracking
- 🔒 Level-Freischaltungs-System (Level 2-4 gesperrt am Start)
- 🔺 Dagstuhl-Dreieck Integration (🔧💡🌍)
- ✅ Checkboxen für abgeschlossene Lektionen
- 🎮 'Lektion abschließen' Button auf allen Seiten
- 📝 Update-Script für Navigation auf allen Seiten
- 💾 Backups der originalen Dateien erstellt

Das System ermöglicht gamifiziertes Lernen und führt Schüler
progressiv von einfachen zu komplexen Aufgaben."

echo "🚀 Pushe zu GitHub..."
git push

echo ""
echo "✅ Fertig! Änderungen wurden gepusht."
echo ""
echo "📋 Nächste Schritte:"
echo "1. Führe aus: python3 update_navigation_level_system.py"
echo "2. Committe die aktualisierten HTML-Dateien"
echo "3. Pushe erneut"
echo "4. Prüfe GitHub Actions: https://github.com/mzgivb/alvik-webseite/actions"
echo "5. Teste live: http://alvik.mzgivb.de/"
