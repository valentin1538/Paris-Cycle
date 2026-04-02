# 🚴‍♂️ Paris Cycle

**Paris Cycle** est une Progressive Web Application (PWA) développée en 1 jour et demi pour centraliser et consulter les données liées à l'usage du vélo à Paris. Ce projet s'appuie sur le framework Django et les API ouvertes de **Paris Data**.

## 🎯 Objectif du Projet
Créer une plateforme conviviale et intuitive, installable sur mobile (PWA), permettant aux utilisateurs parisiens de :
- Visualiser les stations Vélib' et leur disponibilité en temps réel.
- Consulter les dernières actualités sur les aménagements cyclables.
- Bénéficier d'une interface respectant scrupuleusement la charte graphique de la Ville de Paris (Couleur Bleu, Typographie Montserrat).

---

## ✨ Fonctionnalités Principales

* **🗺️ Cartographie Interactive :** Utilisation de Leaflet.js pour afficher les stations de vélos parisiens avec un code couleur dynamique selon la disponibilité.
* **📡 Données en Temps Réel :** Connexion directe à l'API *Paris Data* pour des informations toujours à jour sans surcharger la base de données.
* **📱 Progressive Web App (PWA) :** Application installable sur smartphone (iOS/Android) avec un manifeste configuré et un Service Worker gérant la mise en cache.
* **📰 Module d'Actualités :** Interface d'administration Django permettant l'ajout, la modification et la suppression d'articles et de visuels.

---

## 🛠️ Technologies Utilisées

* **Backend :** Python 3, Django 6
* **Base de données :** SQLite (par défaut pour le développement)
* **Frontend :** HTML5, CSS3 (Grid/Flexbox), JavaScript (Vanilla)
* **Cartographie :** Leaflet.js, API OpenStreetMap / CARTO
* **PWA :** django-pwa
* **Gestion des images :** Pillow

---

## 🚀 Installation et Lancement (Local)

Suivez ces instructions pour faire tourner le projet sur votre machine locale.

### 1. Cloner le dépôt

    git clone https://github.com/votre-compte/Paris-Cycle.git
    cd Paris-Cycle

### 2. Installer les dépendances
Assurez-vous d'avoir Python installé, puis exécutez :

    pip install -r requirements.txt

### 3. Configurer la base de données
Appliquez les migrations pour créer la structure de la base de données (notamment pour les actualités) :

    python manage.py makemigrations
    python manage.py migrate

### 4. Créer un compte Administrateur
Pour pouvoir ajouter des actualités depuis le back-office :

    python manage.py createsuperuser

*(Suivez les instructions à l'écran pour définir un pseudo et un mot de passe).*

### 5. Collecter les fichiers statiques
Indispensable pour l'affichage correct du design, des logos et de l'administration Django :

    python manage.py collectstatic

*(Répondez "yes" si on vous demande de confirmer).*

### 6. Lancer le serveur

    python manage.py runserver

Rendez-vous ensuite sur http://127.0.0.1:8000/ pour voir l'application, et sur http://127.0.0.1:8000/admin/ pour gérer les actualités.

---

## 👥 Équipe du Projet (1.5 jours)

Ce projet a été réalisé en mode commando par une équipe de 3 développeurs :
* **Valentin PREVOT :** Lead Backend Django, Base de données & Module Actualités.
* **Mathéa GAVERIAUX :** Frontend, API Paris Data & Cartographie Leaflet.
* **Marietou BARO :** PWA, Intégration Design & UX Mobile.
