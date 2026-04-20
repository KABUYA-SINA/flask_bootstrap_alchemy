# 🔐 Flask User Management App

## 🚀 Description

Cette application est un projet backend développé avec **Flask** permettant de gérer des utilisateurs avec un système d’authentification simple, des sessions et une base de données SQL.

Elle permet aux utilisateurs de se connecter, d’enregistrer leurs informations (nom et email), et de consulter la liste des utilisateurs enregistrés.

---

## 🎯 Objectif du projet

* Mettre en place une application web backend avec Flask
* Gérer des utilisateurs avec sessions
* Utiliser une base de données relationnelle (SQLAlchemy)
* Apprendre la gestion des routes et des formulaires
* Manipuler les cookies et sessions utilisateur

---

## 🛠️ Technologies utilisées

* Python
* Flask
* Flask-SQLAlchemy
* HTML / Templates Jinja2
* dotenv (variables d’environnement)

---

## ⚙️ Fonctionnalités

* 🔑 Système de login avec session
* 👤 Création automatique d’utilisateur en base
* ✉️ Ajout et modification d’email utilisateur
* 📋 Affichage de tous les utilisateurs
* 🚪 Logout avec suppression de session
* 🧠 Gestion des messages flash

---

## 🗄️ Base de données

Le projet utilise SQLAlchemy avec une base de données SQLite par défaut.

Table principale :

* `User`

  * id
  * name
  * email

---

## ▶️ Lancer le projet

```bash
pip install -r requirements.txt
python app.py
```

---

## 🌐 Routes principales

* `/` → Accueil
* `/login` → Connexion utilisateur
* `/user` → Profil utilisateur
* `/all` → Liste des utilisateurs
* `/logout` → Déconnexion

---

## 🧠 Compétences développées

* Développement backend avec Flask
* Gestion des sessions utilisateur
* CRUD avec base de données SQL
* Architecture MVC simple
* Sécurité basique des sessions

---

## 👨‍💻 Auteur

**Sina Kabuya**
GitHub : https://github.com/KABUYA-SINA
Portfolio : https://kabuya-sina.github.io/Portfolio-SK/

---
