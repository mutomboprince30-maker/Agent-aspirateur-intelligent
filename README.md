# Agent Aspirateur Intelligent  – Simulation Pygame

Ce projet est une **simulation visuelle d’un agent aspirateur intelligent** réalisée avec **Python et Pygame**.
L’agent analyse l’environnement (deux chambres), détecte celles qui sont sales et se déplace automatiquement pour les nettoyer.

## 🧠 Fonctionnalités principales

* Deux chambres (A et B), propres ou sales.
* Animation fluide via **Pygame**.
* L’agent se déplace automatiquement vers la pièce sale.
* Déclenchement d’un son d’aspirateur pendant le nettoyage.
* Animation de poussière (particules dynamiques).
* Nettoyage progressif (transition de couleur + disparition des poussières).
* Ré-salissure automatique toutes les 10 secondes si toutes les chambres sont propres.
* Interface graphique : statut des chambres, action en cours, particules animées.

---

## 📂 Structure du projet

```
agent-aspirateur/
│── agent.py
│── vacuum.wav        # son optionnel
│── README.md
│── requirements.txt
```

---

## ▶️ Exécution du programme

Assurez-vous d’avoir **Python 3.8+** puis exécutez :

```bash
python agent.py
```

---

## 📦 Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/TON-UTILISATEUR/agent-aspirateur.git
cd agent-aspirateur
```

### 2️⃣ Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux / macOS
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🔊 Fichier audio

Le projet utilise un son `vacuum.wav`.
Il doit être placé **dans le même dossier** que `agent.py`.
Si le fichier n’existe pas, le programme continue sans son.

---

## 🛠 Technologies utilisées

* **Python**
* **Pygame** (graphismes + sons)
* **Math**, **Random**, **Time**

---

## ⚠️ Problèmes courants

### ✔ Erreur : "No module named pygame"

Installez Pygame :

```bash
pip install pygame
```

### ✔ Pas de son pendant le nettoyage

* Vérifiez que `vacuum.wav` existe.
* Vérifiez que le volume de votre système n’est pas à zéro.

---

## 📜 Licence

Libre pour l'apprentissage, les projets scolaires et les démonstrations en IA.
