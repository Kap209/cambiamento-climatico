from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chiave_segreta_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utenti.db'
db = SQLAlchemy(app)

# Modello del Database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    punti = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

# --- FUNZIONE AGGIUNGI PUNTI (La logica del bottone) ---
@app.route("/aggiungi_punti/<int:valore>")
def aggiungi_punti(valore):
    if 'user_id' in session:
        utente = User.query.get(session['user_id'])
        utente.punti += valore
        db.session.commit()
    return redirect(url_for('home'))

# --- ROTTE PAGINE ---
@app.route("/")
def home():
    punti_attuali = 0
    if 'user_id' in session:
        utente = User.query.get(session['user_id'])
        punti_attuali = utente.punti
    return render_template("index.html", punti=punti_attuali)

@app.route("/ai-advisor", methods=['GET', 'POST'])
def ai_advisor():
    consiglio = ""
    if request.method == 'POST':
        oggetto = request.form.get('oggetto').lower()
        if "plastica" in oggetto: consiglio = "Va nel bidone GIALLO! (+10 punti)"
        elif "carta" in oggetto: consiglio = "Va nel bidone BLU! (+10 punti)"
        else: consiglio = "Chiedi al tuo comune, l'IA è incerta."
    return render_template("ai_advisor.html", consiglio=consiglio)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            session['user_id'] = user.id
            session['user'] = user.username
            return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256')
        nuovo = User(username=request.form.get('username'), password=hashed_pw)
        db.session.add(nuovo)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/negozio")
def negozio():
    punti = 0
    if 'user_id' in session:
        punti = User.query.get(session['user_id']).punti
    return render_template("negozio.html", punti=punti)

if __name__ == "__main__":
    app.run(debug=True)