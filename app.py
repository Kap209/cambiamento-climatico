from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    # In Flask passiamo i dati semplicemente come argomenti di funzione
    return render_template("index.html", punti=0)

if __name__ == "__main__":
    app.run(debug=True)