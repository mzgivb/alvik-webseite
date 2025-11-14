#!/usr/bin/env python3
# Korrigiert die Parameter und Beispiele für get_wheels_position() und get_distance()

with open('/Users/jochenleeder/Documents/alvik-webseite/js/commands.js', 'r', encoding='utf-8') as f:
    content = f.read()

# get_wheels_position - Parameter und Beispiel ersetzen
old_wheels_block = """        parameters: [
            { name: 'unit', desc: 'DEGREES oder REVOLUTIONS' }
        ],
        example: `# Position in Grad abrufen
left, right = alvik.get_wheels_position(alvik.DEGREES)
print(f"Links: {left}°, Rechts: {right}°")

# Position in Umdrehungen
left, right = alvik.get_wheels_position(alvik.REVOLUTIONS)
print(f"Links: {left} U, Rechts: {right} U")`"""

new_wheels_block = """        parameters: [],
        example: `# Position in Grad abrufen (Standard)
left, right = alvik.get_wheels_position()
print(f"Links: {left}°, Rechts: {right}°")

# Mehrere Positionen vergleichen
for i in range(5):
    left, right = alvik.get_wheels_position()
    print(f"Messung {i+1}: L={left}°, R={right}°")
    alvik.move(10)`"""

content = content.replace(old_wheels_block, new_wheels_block)

# get_distance - Parameter und Beispiel ersetzen
old_distance_block = """        parameters: [
            { name: 'unit', desc: 'CM (Zentimeter) oder INCH (Zoll)' }
        ],
        example: `# Entfernung in Zentimetern messen
distance = alvik.get_distance(alvik.CM)
print(f"Entfernung: {distance} cm")

# Kollisionsvermeidung
while True:
    distance = alvik.get_distance(alvik.CM)
    if distance < 20:
        alvik.brake()
        print("Hindernis erkannt!")
        break
    alvik.move(30)`"""

new_distance_block = """        parameters: [],
        example: `# Entfernung in Zentimetern messen (Standard)
distance = alvik.get_distance()
print(f"Entfernung: {distance} cm")

# Kollisionsvermeidung
while True:
    distance = alvik.get_distance()
    if distance < 20:
        alvik.brake()
        print("Hindernis erkannt!")
        break
    alvik.move(10)`"""

content = content.replace(old_distance_block, new_distance_block)

with open('/Users/jochenleeder/Documents/alvik-webseite/js/commands.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Parameter und Beispiele korrigiert!")
print("   • get_wheels_position() - keine Parameter, Standardwert in Grad")
print("   • get_distance() - keine Parameter, Standardwert in cm")
