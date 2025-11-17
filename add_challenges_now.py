#!/usr/bin/env python3
from pathlib import Path

html_dir = Path.cwd()

# Challenge HTML für 1_5_2
challenge_html = '''
    <!-- Challenge-Bereich -->
    <div class="challenge-box" style="margin: 4rem 0 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, rgba(227, 6, 19, 0.08), rgba(103, 116, 122, 0.08)); border-radius: 20px; border: 3px solid var(--primary-color); box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
        <div class="challenge-header" style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid var(--primary-color);">
            <span style="font-size: 3rem;">🎯</span>
            <div>
                <h2 style="margin: 0; font-size: 2rem; color: var(--primary-color);">Challenge: Touch-gesteuerte Bewegung</h2>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.8;">Erstelle ein interaktives Steuersystem!</p>
            </div>
        </div>
        <p>Test erfolgreich!</p>
    </div>
    <!-- Ende Challenge-Bereich -->
'''

# Teste mit einer Datei
file = html_dir / '1_5_2_Alvik_fa_hrt_auf_Tastendruck.html'
if file.exists():
    content = file.read_text(encoding='utf-8')
    if 'challenge-box' not in content.lower():
        new_content = content.replace('        </main>', challenge_html + '        </main>')
        file.write_text(new_content, encoding='utf-8')
        print('✅ Challenge hinzugefügt zu 1_5_2')
    else:
        print('⏭️  Challenge bereits vorhanden')
else:
    print('❌ Datei nicht gefunden')
