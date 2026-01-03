from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    usage_df = pd.read_csv("../data/final_dataset.csv")
    rec_df = pd.read_csv("../data/recommendations.csv")
    forecast_df = pd.read_csv("../data/cost_forecast.csv")

    return render_template(
        "index.html",
        usage=usage_df.to_dict(orient="records"),
        recommendations=rec_df.to_dict(orient="records"),
        forecast=forecast_df.to_dict(orient="records")[0]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
