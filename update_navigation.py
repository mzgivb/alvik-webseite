#!/usr/bin/env python3
"""
Script to add Command Center link to all HTML files
"""
import os
import glob

# Der Text, nach dem wir suchen
search_text = '<li><a href="1_1_Alvik_API.html"'

# Der Link, den wir hinzufügen wollen
command_center_link = '    <li><a href="command-center.html">🚀 Command Center</a></li>\n'

# Alle HTML-Dateien im Verzeichnis finden
html_files = glob.glob('*.html')

print(f"Gefunden: {len(html_files)} HTML-Dateien\n")

updated_count = 0

for html_file in html_files:
    # Command Center selbst überspringen
    if html_file == 'command-center.html':
        print(f"⏭️  Überspringe: {html_file}")
        continue
    
    try:
        # Datei einlesen
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Prüfen, ob Command Center Link schon existiert
        if 'command-center.html' in content:
            print(f"✅ Bereits aktualisiert: {html_file}")
            continue
        
        # Prüfen, ob die Suchzeile existiert
        if search_text not in content:
            print(f"⚠️  Suchtext nicht gefunden in: {html_file}")
            continue
        
        # Link nach der API-Liste Zeile einfügen
        lines = content.split('\n')
        new_lines = []
        
        for line in lines:
            new_lines.append(line)
            if search_text in line:
                # Die nächste Zeile sollte </li> sein, danach fügen wir ein
                new_lines.append(command_center_link.rstrip())
        
        # Datei mit neuem Inhalt schreiben
        new_content = '\n'.join(new_lines)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Aktualisiert: {html_file}")
        updated_count += 1
        
    except Exception as e:
        print(f"❌ Fehler bei {html_file}: {e}")

print(f"\n🎉 Fertig! {updated_count} Dateien wurden aktualisiert.")
