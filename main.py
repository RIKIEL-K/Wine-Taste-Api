import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)
df = pd.read_csv("wines.csv")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/<pays>")
def vine_region(pays):
    df1= df[["country","name","price","province","points"]].loc[(df["country"]==pays) & (df["points"] == 100)]
    result = df1.to_dict(orient="records")
    return result

@app.route("/api/<pays>/<price>")
def vine_price(pays,price):
    df2= df[["country","name","price","province","points"]].loc[(df["country"]==pays) & (df["price"] == float(price))]
    result = df2.to_dict(orient="records")
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True,port=5000)