#!/usr/bin/env python3
# Korrigiert alle API-Aufrufe basierend auf der offiziellen API-Liste

with open('/Users/jochenleeder/Documents/alvik-webseite/js/commands.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. get_imu() korrigieren - gibt Tuple zurück, nicht Objekt
old_imu = """        example: `# IMU-Daten abrufen
imu = alvik.get_imu()
ax, ay, az = imu.accelerations
gx, gy, gz = imu.gyro
mx, my, mz = imu.magnetic

print(f"Beschleunigung: x={ax}, y={ay}, z={az}")
print(f"Rotation: x={gx}, y={gy}, z={gz}")
print(f"Magnetfeld: x={mx}, y={my}, z={mz}")`"""

new_imu = """        example: `# IMU-Daten abrufen (gibt 6 Werte zurück)
ax, ay, az, gx, gy, gz = alvik.get_imu()

print(f"Beschleunigung: x={ax}, y={ay}, z={az}")
print(f"Gyroskop: x={gx}, y={gy}, z={gz}")

# Einzelne Sensoren abrufen
ax, ay, az = alvik.get_accelerations()  # Nur Beschleunigung
gx, gy, gz = alvik.get_gyros()          # Nur Gyroskop`"""

content = content.replace(old_imu, new_imu)

# 2. get_imu() Beschreibung aktualisieren
content = content.replace(
    "description: 'Liest alle Werte des IMU-Sensors aus (Beschleunigung, Rotation, Magnetfeld).'",
    "description: 'Liest alle IMU-Werte aus: Beschleunigung (ax, ay, az) und Gyroskop (gx, gy, gz).'"
)

# 3. get_distance() korrigiert - gibt 5 Werte zurück!
old_distance = """        example: `# Entfernung in Zentimetern messen (Standard)
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

new_distance = """        example: `# Entfernungen in cm messen (gibt 5 Werte zurück!)
left, center_left, center, center_right, right = alvik.get_distance()
print(f"Links: {left}, Mitte: {center}, Rechts: {right} cm")

# Kollisionsvermeidung mit mittlerem Sensor
while True:
    _, _, center, _, _ = alvik.get_distance()
    if center < 20:
        alvik.brake()
        print("Hindernis erkannt!")
        break
    alvik.move(10)`"""

content = content.replace(old_distance, new_distance)

# 4. get_distance() Beschreibung aktualisieren
content = content.replace(
    "description: 'Misst die Entfernung zum nächsten Objekt mit dem Ultraschallsensor in cm (Standard).'",
    "description: 'Misst 5 Entfernungen mit TOF-Sensoren: links (45°), center_left (22°), center (0°), center_right (22°), rechts (45°) in cm.'"
)

# 5. get_touch() Funktionen korrigieren - richtige Namen
content = content.replace(
    "name: 'alvik.get_touch(button)'",
    "name: 'alvik.get_touch_ok() / get_touch_up() etc.'"
)

old_touch_desc = "description: 'Prüft, ob ein Touch-Button gedrückt ist.'"
new_touch_desc = "description: 'Prüft, ob ein Touch-Button gedrückt ist. Verschiedene Funktionen für jeden Button.'"
content = content.replace(old_touch_desc, new_touch_desc)

old_touch_params = """        parameters: [
            { name: 'button', desc: 'TOUCH_UP, TOUCH_DOWN, TOUCH_LEFT, TOUCH_RIGHT, TOUCH_CENTER, TOUCH_OK' }
        ],"""
new_touch_params = """        parameters: [],"""
content = content.replace(old_touch_params, new_touch_params)

old_touch_example = """        example: `# Einzelnen Button prüfen
if alvik.get_touch(alvik.TOUCH_OK):
    print("OK-Button gedrückt!")

# Auf Button-Druck warten
while not alvik.get_touch(alvik.TOUCH_OK):
    time.sleep(0.1)
print("Los geht's!")

# Mehrere Buttons prüfen
if alvik.get_touch(alvik.TOUCH_UP):
    alvik.move(50)
elif alvik.get_touch(alvik.TOUCH_DOWN):
    alvik.move(-50)`"""

new_touch_example = """        example: `# Einzelne Button-Funktionen verwenden
if alvik.get_touch_ok():
    print("OK-Button gedrückt!")

# Auf Button-Druck warten
while not alvik.get_touch_ok():
    time.sleep(0.1)
print("Los geht's!")

# Mehrere Buttons prüfen
if alvik.get_touch_up():
    alvik.move(50)
elif alvik.get_touch_down():
    alvik.move(-50)
elif alvik.get_touch_left() or alvik.get_touch_right():
    print("Links oder Rechts gedrückt")`"""

content = content.replace(old_touch_example, new_touch_example)

with open('/Users/jochenleeder/Documents/alvik-webseite/js/commands.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Alle API-Aufrufe korrigiert!")
print("   • get_imu() - gibt Tuple mit 6 Werten zurück")
print("   • get_distance() - gibt Tuple mit 5 Werten zurück")
print("   • get_touch_*() - separate Funktionen, keine Parameter")
