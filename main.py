import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/<pays>")
def vine_region(pays):
    df = pd.read_csv("wines.csv")
    df1= df[["country","name","price","province","points"]].loc[(df["country"]==pays) & (df["points"] == 100)]
    result = df1.to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True,port=5000)