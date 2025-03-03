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


@app.route("/api/wine/taster")
def get_taster():
    df2 = df[["taster_name", "taster_twitter_handle"]].drop_duplicates()
    data = df2.to_dict(orient='records')
    return data

@app.route("/api/tasters/<name>/wines")
def wine_tested(name):
     df2 = df[["name","price"]].loc[(df["taster_name"] == name)]
     result = df2.to_dict(orient="records")
     return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True,port=5000)