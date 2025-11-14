// Alle Alvik API-Befehle
const commands = [
    // Bewegung
    {
        name: 'alvik.drive(speed, degrees)',
        category: 'bewegung',
        description: 'Bewegt den Alvik vorwärts oder rückwärts mit einer bestimmten Geschwindigkeit.',
        parameters: [
            { name: 'speed', desc: 'Geschwindigkeit (-100 bis 100), negativ = rückwärts' },
            { name: 'degrees', desc: 'Optional: Rotation in Grad (360° = 1 Umdrehung)' }
        ],
        example: `from arduino_alvik import ArduinoAlvik
alvik = ArduinoAlvik()
alvik.begin()

# Vorwärts fahren mit Geschwindigkeit 50
alvik.move(50)
alvik.brake()

# Rückwärts fahren
alvik.move(-50)
alvik.brake()`
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
        name: 'alvik.get_wheels_position(unit)',
        category: 'bewegung',
        description: 'Gibt die Position der Räder zurück (in Grad oder Umdrehungen).',
        parameters: [
            { name: 'unit', desc: 'DEGREES oder REVOLUTIONS' }
        ],
        example: `# Position in Grad abrufen
left, right = alvik.get_wheels_position(alvik.DEGREES)
print(f"Links: {left}°, Rechts: {right}°")

# Position in Umdrehungen
left, right = alvik.get_wheels_position(alvik.REVOLUTIONS)
print(f"Links: {left} U, Rechts: {right} U")`
    },
    
    // Sensoren
    {
        name: 'alvik.get_distance(unit)',
        category: 'sensoren',
        description: 'Misst die Entfernung zum nächsten Objekt mit dem Ultraschallsensor.',
        parameters: [
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
    alvik.drive(30)`
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
    alvik.drive(40)
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
        description: 'Liest alle Werte des IMU-Sensors aus (Beschleunigung, Rotation, Magnetfeld).',
        parameters: [],
        example: `# IMU-Daten abrufen
imu = alvik.get_imu()
ax, ay, az = imu.accelerations
gx, gy, gz = imu.gyro
mx, my, mz = imu.magnetic

print(f"Beschleunigung: x={ax}, y={ay}, z={az}")
print(f"Rotation: x={gx}, y={gy}, z={gz}")
print(f"Magnetfeld: x={mx}, y={my}, z={mz}")`
    },
    {
        name: 'alvik.get_touch(button)',
        category: 'sensoren',
        description: 'Prüft, ob ein Touch-Button gedrückt ist.',
        parameters: [
            { name: 'button', desc: 'TOUCH_UP, TOUCH_DOWN, TOUCH_LEFT, TOUCH_RIGHT, TOUCH_CENTER, TOUCH_OK' }
        ],
        example: `# Einzelnen Button prüfen
if alvik.get_touch(alvik.TOUCH_OK):
    print("OK-Button gedrückt!")

# Auf Button-Druck warten
while not alvik.get_touch(alvik.TOUCH_OK):
    time.sleep(0.1)
print("Los geht's!")

# Mehrere Buttons prüfen
if alvik.get_touch(alvik.TOUCH_UP):
    alvik.drive(50)
elif alvik.get_touch(alvik.TOUCH_DOWN):
    alvik.drive(-50)`
    },
    
    // LEDs
    {
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
    },
    {
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
    },
    {
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
alvik.drive(50, 360)  # Genau eine Radumdrehung`
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
