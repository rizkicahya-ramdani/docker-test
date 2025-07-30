from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    luas = None
    if request.method == "POST":
        try:
            r = float(request.form["jari_jari"])
            luas = 3.14 * r * r
        except:
            luas = "Input tidak valid"
    return render_template("index.html", hasil=luas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
