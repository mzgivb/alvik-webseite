#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_logo(content):
    pattern = r'<img src="assets/MZ_GIVB_Logo\.svg" alt="[^"]*" class="logo">'
    replacement = '<a href="index.html" style="text-decoration: none;"><img src="assets/MZ_GIVB_Logo.svg" alt="Medienzentrum Gießen-Vogelsberg" class="logo" style="cursor: pointer;"></a>'
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        return content, True
    return content, False

def add_homepage_link(content):
    if '🏠 Startseite' in content:
        return content, False
    pattern = r'</div>\s*<div class="nav-section">\s*<h3>'
    if re.search(pattern, content):
        replacement = '''</div>
<div class="nav-section">
                <ul>
                    <li><a href="index.html">🏠 Startseite</a></li>
                </ul>
            </div>
            <div class="nav-section">
                <h3>'''
        content = re.sub(pattern, replacement, content, count=1)
        return content, True
    return content, False

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original_content = content
    content, logo_updated = update_logo(content)
    content, nav_updated = add_homepage_link(content)
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, logo_updated, nav_updated
    return False, False, False

def main():
    base_dir = Path('/Users/jochenleeder/Documents/alvik-webseite')
    html_files = [f for f in base_dir.glob('*.html') if f.name != 'index.html']
    print(f"🔧 Starte Update für {len(html_files)} HTML-Dateien...")
    print("=" * 60)
    updated_count = 0
    logo_count = 0
    nav_count = 0
    for filepath in sorted(html_files):
        changed, logo_updated, nav_updated = process_file(filepath)
        if changed:
            status = []
            if logo_updated:
                status.append("Logo ✓")
                logo_count += 1
            if nav_updated:
                status.append("Nav ✓")
                nav_count += 1
            print(f"✅ {filepath.name:<40} [{', '.join(status)}]")
            updated_count += 1
        else:
            print(f"⏭️  {filepath.name:<40} [Bereits aktuell]")
    print("=" * 60)
    print(f"\n📊 Zusammenfassung:")
    print(f"   • {updated_count} Dateien aktualisiert")
    print(f"   • {logo_count} Logos klickbar gemacht")
    print(f"   • {nav_count} Navigation-Links hinzugefügt")
    if updated_count > 0:
        print(f"\n✨ Fertig!")

if __name__ == '__main__':
    main()
