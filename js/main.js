// Fortschritts- und Level-System für Arduino Alvik Lernplattform

// Konfiguration
const TOTAL_LESSONS = 16;
const LEVEL_CONFIG = {
    1: { required: 0, unlock: 0 },    // Level 1 immer offen
    2: { required: 1, unlock: 3 },    // Level 2 nach 3 aus Level 1
    3: { required: 2, unlock: 3 },    // Level 3 nach 3 aus Level 2
    4: { required: 3, unlock: 2 }     // Level 4 nach 2 aus Level 3
};

// LocalStorage Schlüssel
const STORAGE_KEY = 'alvik_progress';

// ===== FORTSCHRITTSVERWALTUNG =====

// Fortschritt laden
function loadProgress() {
    const stored = localStorage.getItem(STORAGE_KEY);
    return stored ? JSON.parse(stored) : { completed: [], currentPage: null };
}

// Fortschritt speichern
function saveProgress(progress) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
}

// Seite als abgeschlossen markieren
function markPageCompleted(pageUrl) {
    const progress = loadProgress();
    if (!progress.completed.includes(pageUrl)) {
        progress.completed.push(pageUrl);
        saveProgress(progress);
    }
    return progress;
}

// Prüfen ob Seite abgeschlossen ist
function isPageCompleted(pageUrl) {
    const progress = loadProgress();
    return progress.completed.includes(pageUrl);
}

// ===== LEVEL-VERWALTUNG =====

// Anzahl abgeschlossener Lektionen in einem Level zählen
function countCompletedInLevel(level) {
    const progress = loadProgress();
    const levelSection = document.querySelector(`[data-level="${level}"]`);
    if (!levelSection) return 0;
    
    const pages = levelSection.querySelectorAll('[data-page]');
    let count = 0;
    pages.forEach(item => {
        const pageUrl = item.dataset.page;
        if (progress.completed.includes(pageUrl)) {
            count++;
        }
    });
    return count;
}

// Prüfen ob Level freigeschaltet ist
function isLevelUnlocked(level) {
    const config = LEVEL_CONFIG[level];
    if (!config) return false;
    if (config.required === 0) return true; // Level 1 immer offen
    
    const completedInPreviousLevel = countCompletedInLevel(config.required);
    return completedInPreviousLevel >= config.unlock;
}

// Level freischalten
function unlockLevels() {
    document.querySelectorAll('.nav-section[data-level]').forEach(section => {
        const level = parseInt(section.dataset.level);
        const isUnlocked = isLevelUnlocked(level);
        
        if (isUnlocked) {
            section.classList.remove('locked');
            
            // Lock-Icon entfernen
            const lockIcon = section.querySelector('.lock-icon');
            if (lockIcon) {
                lockIcon.textContent = '✅';
            }
            
            // Links aktivieren
            section.querySelectorAll('.locked-link').forEach(link => {
                link.classList.remove('locked-link');
            });
        } else {
            section.classList.add('locked');
            
            // Lock-Icon setzen
            const lockIcon = section.querySelector('.lock-icon');
            if (lockIcon) {
                lockIcon.textContent = '🔒';
            }
            
            // Links deaktivieren
            section.querySelectorAll('a').forEach(link => {
                if (!link.classList.contains('locked-link')) {
                    link.classList.add('locked-link');
                }
            });
        }
    });
}

// ===== UI-UPDATES =====

// Fortschrittsanzeige aktualisieren
function updateProgressDisplay() {
    const progress = loadProgress();
    const completed = progress.completed.length;
    const percentage = Math.round((completed / TOTAL_LESSONS) * 100);
    
    const progressBar = document.getElementById('progress-bar');
    const progressPercentage = document.getElementById('progress-percentage');
    const progressText = document.getElementById('progress-text');
    
    if (progressBar) progressBar.style.width = `${percentage}%`;
    if (progressPercentage) progressPercentage.textContent = `${percentage}%`;
    if (progressText) progressText.textContent = `${completed} von ${TOTAL_LESSONS} Lektionen`;
}

// Checkboxen in Navigation aktualisieren
function updateCheckboxes() {
    const progress = loadProgress();
    
    document.querySelectorAll('[data-page]').forEach(item => {
        const pageUrl = item.dataset.page;
        const checkbox = item.querySelector('.completion-check');
        
        if (checkbox) {
            if (progress.completed.includes(pageUrl)) {
                checkbox.textContent = '✅';
                item.classList.add('completed');
            } else {
                checkbox.textContent = '⬜';
                item.classList.remove('completed');
            }
        }
    });
}

// ===== SEITEN-FUNKTIONEN =====

// "Lektion abschließen" Button zu Seiten hinzufügen
function addCompletionButton() {
    const currentPage = window.location.pathname.split('/').pop();
    
    // Nur auf Lektionsseiten, nicht auf index.html oder command-center.html
    if (currentPage === 'index.html' || currentPage === '' || 
        currentPage === 'command-center.html' || 
        currentPage.includes('5_1_')) { // Keine Completion für Lösungsseiten
        return;
    }
    
    const mainContent = document.querySelector('.main-content');
    if (!mainContent) return;
    
    // Prüfen ob Seite schon abgeschlossen ist
    const isCompleted = isPageCompleted(currentPage);
    
    // Button erstellen
    const buttonContainer = document.createElement('div');
    buttonContainer.style.cssText = 'text-align: center; margin: 3rem 0; padding: 2rem; background: linear-gradient(135deg, rgba(227, 6, 19, 0.05), rgba(103, 116, 122, 0.05)); border-radius: 16px;';
    
    const button = document.createElement('button');
    button.id = 'complete-lesson-btn';
    button.style.cssText = `
        padding: 1rem 2rem;
        background: ${isCompleted ? 'linear-gradient(135deg, #22c55e, #16a34a)' : 'linear-gradient(135deg, var(--primary-color), var(--secondary-color))'};
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1.1rem;
        cursor: ${isCompleted ? 'default' : 'pointer'};
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    `;
    button.textContent = isCompleted ? '✅ Lektion abgeschlossen!' : '✓ Lektion abschließen';
    
    if (!isCompleted) {
        button.addEventListener('click', function() {
            markPageCompleted(currentPage);
            this.textContent = '✅ Lektion abgeschlossen!';
            this.style.background = 'linear-gradient(135deg, #22c55e, #16a34a)';
            this.style.cursor = 'default';
            
            // Zeige Erfolgsmeldung
            showSuccessMessage();
            
            // Update UI
            setTimeout(() => {
                window.location.reload();
            }, 2000);
        });
        
        button.addEventListener('mouseover', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
        });
        
        button.addEventListener('mouseout', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'none';
        });
    }
    
    buttonContainer.appendChild(button);
    mainContent.appendChild(buttonContainer);
}

// Erfolgsmeldung anzeigen
function showSuccessMessage() {
    const message = document.createElement('div');
    message.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1.5rem 2rem;
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: white;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(34, 197, 94, 0.3);
        font-weight: 600;
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    message.textContent = '🎉 Super! Lektion abgeschlossen!';
    
    document.body.appendChild(message);
    
    setTimeout(() => {
        message.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => message.remove(), 300);
    }, 2000);
}

// ===== SUCHFUNKTION =====

// Suche in Navigation
function initSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;
    
    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        
        document.querySelectorAll('.nav-section li').forEach(item => {
            const link = item.querySelector('a');
            if (!link) return;
            
            const text = link.textContent.toLowerCase();
            if (text.includes(query)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    });
}

// ===== INITIALISIERUNG =====

document.addEventListener('DOMContentLoaded', function() {
    // Fortschritt laden und UI aktualisieren
    updateProgressDisplay();
    updateCheckboxes();
    unlockLevels();
    
    // Completion-Button hinzufügen
    addCompletionButton();
    
    // Suche initialisieren
    initSearch();
    
    // Back-to-top Button
    const backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTop.style.display = 'block';
            } else {
                backToTop.style.display = 'none';
            }
        });
        
        backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});

// ===== ANIMATIONS =====

// CSS Animationen hinzufügen
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
    
    .back-to-top {
        display: none;
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        text-align: center;
        line-height: 50px;
        font-size: 1.5rem;
        text-decoration: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
        z-index: 1000;
    }
    
    .back-to-top:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.25);
    }
`;
document.head.appendChild(style);

// ===== EXPORT FÜR DEBUGGING =====

// Funktionen für Console verfügbar machen
window.alvikProgress = {
    load: loadProgress,
    save: saveProgress,
    reset: function() {
        if (confirm('Möchtest du wirklich deinen gesamten Fortschritt zurücksetzen?')) {
            localStorage.removeItem(STORAGE_KEY);
            window.location.reload();
        }
    },
    markCompleted: markPageCompleted,
    isCompleted: isPageCompleted,
    countInLevel: countCompletedInLevel
};
