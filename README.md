# 🌍 EcoPoints – Gamification per l'Ambiente

**EcoPoints** è una Web App sviluppata in Python con il framework **Flask**.  
Il progetto nasce per incentivare comportamenti eco-sostenibili attraverso un sistema di punteggio (gamification), rendendo divertente e motivante l’adozione di abitudini rispettose dell’ambiente.

---

## ✨ Funzionalità principali

- **Autenticazione Utente**  
  Sistema completo di Sign-up e Login con password criptate (Werkzeug) e database SQLite.

- **Sistema di Punti (Quests)**  
  Tre missioni interattive che aggiornano il punteggio dell’utente in tempo reale:
  - ♻️ **Riciclo**
  - 🚲 **Mobilità Sostenibile**
  - 🚫 **No Plastica**

- **AI Eco-Advisor**  
  Un consulente ambientale integrato che utilizza logica di analisi semantica per consigliare il corretto smaltimento dei rifiuti.

- **Interfaccia Responsive**  
  Design fluido e moderno basato su CSS Flexbox, ottimizzato sia per desktop che per dispositivi mobile.

---

## 🛠️ Tech Stack

| Tecnologia       | Utilizzo                          |
|------------------|-----------------------------------|
| **Python**       | Linguaggio principale             |
| **Flask**        | Backend web framework             |
| **SQLAlchemy**   | ORM e gestione database (SQLite)  |
| **Jinja2**       | Template engine                   |
| **HTML5 + CSS3** | Frontend (design fluido)          |
| **Werkzeug**     | Hashing sicuro delle password     |

---

## 📝 Nota sullo sviluppo (AI-Assisted)

Questo progetto è stato realizzato con il supporto di un’Intelligenza Artificiale per:

- La migrazione dell’architettura da FastAPI a Flask
- La risoluzione di bug relativi alla persistenza dei dati e alle sessioni utente
- La progettazione del layout responsive e della logica dell’AI Advisor

*Tutto il codice è stato revisionato e testato per garantire la conformità con gli obiettivi didattici della lezione.*

---

## 🚀 Come avviare il progetto

### 1. Clona il repository
```bash
git clone https://github.com/TUO-USERNAME/EcoPoints.git
cd EcoPoints