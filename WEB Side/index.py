from flask import Flask,render_template,request,redirect,Response
from flask import url_for
import json
import time
import catchWeatherData as cw
import unity as ut
import getArduinoValue as gav
import serial
app = Flask(__name__)
@app.route("/")
def index():
    country = request.args.get("country")

    return render_template("index.html",country=country)
@app.route("/submit",methods=["POST"])
def post_submit():
    try:
        country = request.form.get("selectedCountry")
        print(country)
        weatherDatas = cw.catchTheDatas(country)
        print(weatherDatas)
        country = weatherDatas
    except:
        country = "您的縣市不對"
    return redirect(url_for("index",country=json.dumps(country),location=json.dumps(request.form.get("selectedCountry"))))

@app.route("/arduionDatas",methods=["POST"])
def fuckTest():

    datas = {
        "Temp": 0,
        "Humi": 0
    }
    try:
        ser = serial.Serial('COM6', 9600, timeout=1000)
        # read one byte

        x = ser.read()
        datas = gav.getArduinoDatas(ser,x)
        ser.close()
    except Exception as e:
        print(e)
        datas = {
            "Temp": 0,
            "Humi": 0
        }
    res = Response('sensor get!')
    print(datas)

    res.set_cookie(key='Temp', value=str(datas["Temp"]), expires=time.time() + 6 * 60)
    res.set_cookie(key='Humi',value=str(datas["Humi"]),expires=time.time() + 6 * 60)
    return res

if __name__=="__main__":
    app.run(debug=False)
