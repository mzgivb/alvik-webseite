// Alle Alvik API-Befehle
const commands = [
    // Bewegung
    {
        name: 'alvik.move(distance)',
        category: 'bewegung',
        description: 'Bewegt den Alvik eine bestimmte Strecke vorwärts oder rückwärts.',
        parameters: [
            { name: 'distance', desc: 'Wegstrecke in cm (positiv = vorwärts, negativ = rückwärts)' }
        ],
        example: `from arduino_alvik import ArduinoAlvik
alvik = ArduinoAlvik()
alvik.begin()

# 50 cm vorwärts fahren
alvik.move(50)

# 30 cm rückwärts fahren
alvik.move(-30)

# Quadrat fahren (mit rotate)
for i in range(4):
    alvik.move(40)    # 40 cm vorwärts
    alvik.rotate(90)  # 90° rechts drehen`
    },
    {
        name: 'alvik.rotate(degrees)',
        category: 'bewegung',
        description: 'Dreht den Alvik um einen bestimmten Winkel. Positiv = rechts, negativ = links.',
        parameters: [
            { name: 'degrees', desc: 'Drehwinkel in Grad (positiv = rechts, negativ = links)' }
        ],
        example: `# 90° nach rechts drehen
alvik.rotate(90)

# 180° nach links drehen
alvik.rotate(-180)

# Vollständige Drehung
alvik.rotate(360)`
    },
    {
        name: 'alvik.set_wheels_speed(left, right)',
        category: 'bewegung',
        description: 'Steuert beide Räder individuell für präzise Manöver und Kurven.',
        parameters: [
            { name: 'left', desc: 'Geschwindigkeit linkes Rad (-100 bis 100)' },
            { name: 'right', desc: 'Geschwindigkeit rechtes Rad (-100 bis 100)' }
        ],
        example: `# Scharfe Rechtskurve
alvik.set_wheels_speed(50, 20)

# Auf der Stelle drehen
alvik.set_wheels_speed(50, -50)

# Geradeaus fahren
alvik.set_wheels_speed(50, 50)`
    },
    {
        name: 'alvik.brake()',
        category: 'bewegung',
        description: 'Stoppt beide Motoren sofort und hält die Position.',
        parameters: [],
        example: `# Fahren und stoppen
alvik.move(50)
time.sleep(2)
alvik.brake()  # Sofortiger Stopp`
    },
    {
        name: 'alvik.get_wheels_position()',
        category: 'bewegung',
        description: 'Gibt die Position der Räder zurück in Grad (Standard).',
        parameters: [],
        example: `# Position in Grad abrufen (Standard)
left, right = alvik.get_wheels_position()
print(f"Links: {left}°, Rechts: {right}°")

# Mehrere Positionen vergleichen
for i in range(5):
    left, right = alvik.get_wheels_position()
    print(f"Messung {i+1}: L={left}°, R={right}°")
    alvik.move(10)`
    },
    
    // Sensoren
    {
        name: 'alvik.get_distance()',
        category: 'sensoren',
        description: 'Misst 5 Entfernungen mit TOF-Sensoren: links (45°), center_left (22°), center (0°), center_right (22°), rechts (45°) in cm.',
        parameters: [],
        example: `# Entfernungen in cm messen (gibt 5 Werte zurück!)
left, center_left, center, center_right, right = alvik.get_distance()
print(f"Links: {left}, Mitte: {center}, Rechts: {right} cm")

# Kollisionsvermeidung mit mittlerem Sensor
while True:
    _, _, center, _, _ = alvik.get_distance()
    if center < 20:
        alvik.brake()
        print("Hindernis erkannt!")
        break
    alvik.move(10)`
    },
    {
        name: 'alvik.get_line_sensors()',
        category: 'sensoren',
        description: 'Liest die drei Liniensensoren aus (links, mitte, rechts). Werte von 0 (hell) bis 100 (dunkel).',
        parameters: [],
        example: `# Liniensensoren auslesen
left, center, right = alvik.get_line_sensors()
print(f"L: {left}, M: {center}, R: {right}")

# Linienfolger
left, center, right = alvik.get_line_sensors()
if center > 50:  # Linie in der Mitte
    alvik.move(40)
elif left > 50:  # Linie links
    alvik.set_wheels_speed(20, 50)
elif right > 50:  # Linie rechts
    alvik.set_wheels_speed(50, 20)`
    },
    {
        name: 'alvik.get_color()',
        category: 'sensoren',
        description: 'Liest die erkannte Farbe mit dem Farbsensor aus. Gibt eine Farbnummer zurück.',
        parameters: [],
        example: `# Farbe erkennen
color = alvik.get_color()
colors = {
    0: "Unbekannt", 1: "Rot", 2: "Grün",
    3: "Blau", 4: "Gelb", 5: "Magenta",
    6: "Cyan", 7: "Weiß"
}
print(f"Erkannte Farbe: {colors.get(color, 'Unbekannt')}")

# Auf bestimmte Farbe reagieren
if color == 1:  # Rot
    alvik.brake()
    print("Rote Fläche erkannt - Stopp!")`
    },
    {
        name: 'alvik.get_color_raw()',
        category: 'sensoren',
        description: 'Gibt die rohen RGB-Werte des Farbsensors zurück.',
        parameters: [],
        example: `# RGB-Werte auslesen
red, green, blue = alvik.get_color_raw()
print(f"R: {red}, G: {green}, B: {blue}")

# Helligkeit berechnen
brightness = (red + green + blue) / 3
print(f"Helligkeit: {brightness}")`
    },
    {
        name: 'alvik.get_imu()',
        category: 'sensoren',
        description: 'Liest alle IMU-Werte aus: Beschleunigung (ax, ay, az) und Gyroskop (gx, gy, gz).',
        parameters: [],
        example: `# IMU-Daten abrufen (gibt 6 Werte zurück)
ax, ay, az, gx, gy, gz = alvik.get_imu()

print(f"Beschleunigung: x={ax}, y={ay}, z={az}")
print(f"Gyroskop: x={gx}, y={gy}, z={gz}")

# Einzelne Sensoren abrufen
ax, ay, az = alvik.get_accelerations()  # Nur Beschleunigung
gx, gy, gz = alvik.get_gyros()          # Nur Gyroskop`
    },
    {
        name: 'alvik.get_touch_ok() / get_touch_up() etc.',
        category: 'sensoren',
        description: 'Prüft, ob ein Touch-Button gedrückt ist. Verschiedene Funktionen für jeden Button.',
        parameters: [],
        example: `# Einzelne Button-Funktionen verwenden
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
    print("Links oder Rechts gedrückt")`
    },
    
    // LEDs
    {
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
    },
    {
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
    },
    {
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
    },
    
    // Servo
    {
        name: 'alvik.set_servo_position(servo, angle)',
        category: 'servo',
        description: 'Stellt einen Servo-Motor auf einen bestimmten Winkel ein.',
        parameters: [
            { name: 'servo', desc: 'SERVO_A oder SERVO_B' },
            { name: 'angle', desc: 'Winkel in Grad (0-180)' }
        ],
        example: `# Servo A auf 90° positionieren
alvik.set_servo_position(alvik.SERVO_A, 90)

# Servo B durchschwenken
for angle in range(0, 181, 10):
    alvik.set_servo_position(alvik.SERVO_B, angle)
    time.sleep(0.1)

# Zurück zur Mittelstellung
alvik.set_servo_position(alvik.SERVO_A, 90)
alvik.set_servo_position(alvik.SERVO_B, 90)`
    },
    
    // System
    {
        name: 'alvik.begin()',
        category: 'system',
        description: 'Initialisiert den Alvik. Muss am Anfang jedes Programms aufgerufen werden.',
        parameters: [],
        example: `from arduino_alvik import ArduinoAlvik
import time

alvik = ArduinoAlvik()
alvik.begin()  # Wichtig: Initialisierung!

# Jetzt kann der Alvik verwendet werden
alvik.set_leds("green")
print("Alvik bereit!")`
    },
    {
        name: 'alvik.reset_pose()',
        category: 'system',
        description: 'Setzt die Position des Alvik auf (0, 0) zurück.',
        parameters: [],
        example: `# Position zurücksetzen
alvik.reset_pose()

# Neue Fahrt starten
alvik.move(50, 360)  # Genau eine Radumdrehung`
    },
    {
        name: 'alvik.get_battery_charge()',
        category: 'system',
        description: 'Gibt den Batterieladezustand in Prozent zurück.',
        parameters: [],
        example: `# Batterie prüfen
battery = alvik.get_battery_charge()
print(f"Batterie: {battery}%")

# Warnung bei niedrigem Ladestand
if battery < 20:
    alvik.set_leds("red")
    print("⚠️ Batterie fast leer!")
else:
    alvik.set_leds("green")`
    },
    {
        name: 'alvik.get_version()',
        category: 'system',
        description: 'Gibt die Firmware-Version des Alvik zurück.',
        parameters: [],
        example: `# Firmware-Version anzeigen
version = alvik.get_version()
print(f"Alvik Firmware: {version}")

# Systeminfo ausgeben
print(f"Firmware: {alvik.get_version()}")
print(f"Batterie: {alvik.get_battery_charge()}%")`
    }
];

// Elemente
const commandsContainer = document.getElementById('commands-container');
const searchInput = document.getElementById('command-search');
const filterButtons = document.querySelectorAll('.filter-btn');
const noResults = document.getElementById('no-results');
const totalCommandsEl = document.getElementById('total-commands');
const foundCommandsEl = document.getElementById('found-commands');

// Aktueller Filter
let currentCategory = 'all';
let currentSearch = '';

// Initialisierung
document.addEventListener('DOMContentLoaded', function() {
    totalCommandsEl.textContent = commands.length;
    renderCommands();
});

// Filter-Buttons
filterButtons.forEach(btn => {
    btn.addEventListener('click', function() {
        filterButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        currentCategory = this.dataset.category;
        renderCommands();
    });
});

// Suche
searchInput.addEventListener('input', function(e) {
    currentSearch = e.target.value.toLowerCase();
    renderCommands();
});

// Commands rendern
function renderCommands() {
    const filtered = commands.filter(cmd => {
        const matchesCategory = currentCategory === 'all' || cmd.category === currentCategory;
        const matchesSearch = currentSearch === '' || 
            cmd.name.toLowerCase().includes(currentSearch) ||
            cmd.description.toLowerCase().includes(currentSearch) ||
            cmd.category.toLowerCase().includes(currentSearch);
        return matchesCategory && matchesSearch;
    });
    
    foundCommandsEl.textContent = filtered.length;
    
    if (filtered.length === 0) {
        commandsContainer.style.display = 'none';
        noResults.style.display = 'block';
        return;
    }
    
    commandsContainer.style.display = 'grid';
    noResults.style.display = 'none';
    
    commandsContainer.innerHTML = filtered.map(cmd => createCommandCard(cmd)).join('');
    
    // Copy-Button Funktionalität
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const code = this.parentElement.querySelector('code').textContent;
            navigator.clipboard.writeText(code).then(() => {
                const originalText = this.textContent;
                this.textContent = '✓ Kopiert!';
                this.classList.add('copied');
                setTimeout(() => {
                    this.textContent = originalText;
                    this.classList.remove('copied');
                }, 2000);
            });
        });
    });
}

// Command-Card erstellen
function createCommandCard(cmd) {
    const categoryLabels = {
        'bewegung': '🚗 Bewegung',
        'sensoren': '📡 Sensoren',
        'leds': '💡 LEDs',
        'servo': '🎮 Servo',
        'system': '⚙️ System'
    };
    
    const parametersHtml = cmd.parameters.length > 0 ? `
        <div class="parameters">
            <div class="parameters-title">Parameter:</div>
            ${cmd.parameters.map(p => `
                <div class="parameter">
                    <span class="parameter-name">${p.name}:</span>
                    <span class="parameter-desc">${p.desc}</span>
                </div>
            `).join('')}
        </div>
    ` : '';
    
    return `
        <div class="command-card">
            <div class="command-header">
                <div class="command-name">${cmd.name}</div>
                <div class="command-category">${categoryLabels[cmd.category]}</div>
            </div>
            <div class="command-description">${cmd.description}</div>
            ${parametersHtml}
            <div class="command-example">
                <button class="copy-btn">📋 Kopieren</button>
                <code>${escapeHtml(cmd.example)}</code>
            </div>
        </div>
    `;
}

// HTML escapen
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
