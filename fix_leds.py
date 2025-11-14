#!/usr/bin/env python3
# Korrigiert alle LED-Funktionen basierend auf der offiziellen API-Liste

with open('/Users/jochenleeder/Documents/alvik-webseite/js/commands.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. set_leds() korrigieren - drei separate Parameter, keine Strings!
old_set_leds = """    {
        name: 'alvik.set_leds(color)',
        category: 'leds',
        description: 'Setzt die Farbe beider LEDs gleichzeitig.',
        parameters: [
            { name: 'color', desc: 'Farbe als Name (z.B. "red") oder RGB-Tupel' }
        ],
        example: `# Vordefinierte Farben verwenden
alvik.set_leds("red")
alvik.set_leds("green")
alvik.set_leds("blue")

# RGB-Werte verwenden (0-255)
alvik.set_leds((255, 128, 0))  # Orange
alvik.set_leds((255, 0, 255))  # Magenta

# LEDs ausschalten
alvik.set_leds("off")`
    },"""

new_set_leds = """    {
        name: 'alvik.left_led.set_color(r, g, b)',
        category: 'leds',
        description: 'Setzt die Farbe der linken LED. Werte von 0 (aus) bis 1 (voll an).',
        parameters: [
            { name: 'r', desc: 'Rotwert (0.0 - 1.0)' },
            { name: 'g', desc: 'Grünwert (0.0 - 1.0)' },
            { name: 'b', desc: 'Blauwert (0.0 - 1.0)' }
        ],
        example: `# Farben setzen (0 = aus, 1 = voll an)
alvik.left_led.set_color(1, 0, 0)  # Rot
alvik.right_led.set_color(0, 1, 0)  # Grün

# Orange (Rot + etwas Grün)
alvik.left_led.set_color(1, 0.5, 0)

# LEDs ausschalten
alvik.left_led.set_color(0, 0, 0)
alvik.right_led.set_color(0, 0, 0)`
    },"""

content = content.replace(old_set_leds, new_set_leds)

# 2. left_led.set_color() korrigieren
old_left_led = """    {
        name: 'alvik.left_led.set_color(color)',
        category: 'leds',
        description: 'Steuert nur die linke LED.',
        parameters: [
            { name: 'color', desc: 'Farbe als Name oder RGB-Tupel' }
        ],
        example: `# Linke LED rot
alvik.left_led.set_color("red")

# Rechte LED grün
alvik.right_led.set_color("green")

# Blinkmuster erstellen
while True:
    alvik.left_led.set_color("red")
    time.sleep(0.5)
    alvik.left_led.set_color("off")
    time.sleep(0.5)`
    },"""

new_left_led = """    {
        name: 'alvik.right_led.set_color(r, g, b)',
        category: 'leds',
        description: 'Setzt die Farbe der rechten LED. Werte von 0 (aus) bis 1 (voll an).',
        parameters: [
            { name: 'r', desc: 'Rotwert (0.0 - 1.0)' },
            { name: 'g', desc: 'Grünwert (0.0 - 1.0)' },
            { name: 'b', desc: 'Blauwert (0.0 - 1.0)' }
        ],
        example: `# Blinkmuster erstellen
import time

while True:
    # Rot blinken
    alvik.left_led.set_color(1, 0, 0)
    time.sleep(0.5)
    alvik.left_led.set_color(0, 0, 0)  # Aus
    time.sleep(0.5)
    
# Beide LEDs unterschiedlich
alvik.left_led.set_color(1, 0, 0)   # Links rot
alvik.right_led.set_color(0, 0, 1)  # Rechts blau`
    },"""

content = content.replace(old_left_led, new_left_led)

# 3. set_illuminator() korrigieren - nimmt bool, nicht 0-100!
old_illuminator = """    {
        name: 'alvik.set_illuminator(brightness)',
        category: 'leds',
        description: 'Steuert die Helligkeit der weißen Beleuchtungs-LED.',
        parameters: [
            { name: 'brightness', desc: 'Helligkeit von 0 (aus) bis 100 (maximum)' }
        ],
        example: `# Volle Helligkeit
alvik.set_illuminator(100)

# Halbe Helligkeit
alvik.set_illuminator(50)

# Ausschalten
alvik.set_illuminator(0)

# Dimmen
for i in range(0, 101, 10):
    alvik.set_illuminator(i)
    time.sleep(0.1)`
    },"""

new_illuminator = """    {
        name: 'alvik.set_illuminator(value)',
        category: 'leds',
        description: 'Schaltet die weiße Beleuchtungs-LED ein oder aus.',
        parameters: [
            { name: 'value', desc: 'True = EIN, False = AUS' }
        ],
        example: `# LED einschalten
alvik.set_illuminator(True)

# LED ausschalten
alvik.set_illuminator(False)

# Blinken lassen
import time
for i in range(5):
    alvik.set_illuminator(True)
    time.sleep(0.5)
    alvik.set_illuminator(False)
    time.sleep(0.5)`
    },"""

content = content.replace(old_illuminator, new_illuminator)

with open('/Users/jochenleeder/Documents/alvik-webseite/js/commands.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Alle LED-Funktionen korrigiert!")
print("   • left_led.set_color(r, g, b) - drei separate Float-Parameter (0-1)")
print("   • right_led.set_color(r, g, b) - drei separate Float-Parameter (0-1)")
print("   • set_illuminator(bool) - True/False, keine Helligkeitswerte")
