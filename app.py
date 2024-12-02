from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "cdc262fa3b11d3d4f87bfbd12105fb0f" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    if city:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") != 200:
            error_message = response.get("message", "Something went wrong.")
            return render_template("index.html", error=error_message)

        weather_data = {
            "city": response["name"],
            "temperature": response["main"]["temp"],
            "description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"]
        }
        return render_template("result.html", weather=weather_data)
    return render_template("index.html", error="Please enter a city.")

if __name__ == "__main__":
    app.run(debug=True)
