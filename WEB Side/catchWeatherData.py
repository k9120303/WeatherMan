import urllib
import numpy as np
from bs4 import BeautifulSoup
import json

from urllib.request import urlopen
countrysName = [
    "Taipei_City",
    "New_Taipei_City",
    "Taoyuan_City",
    "Taichung_City",
    "Tainan_City",
    "Kaohsiung_City",
    "Keelung_City",
    "Hsinchu_City",
    "Miaoli_County",
    "Changhua_County",
    "Nantou_County",
    "Yunlin_County",
    "Chiayi_City",
    "Chiayi_County",
    "Pingtung_County",
    "Yilan_County",
    "Hualien_County",
    "Taitung_County",
    "Kinmen_County"
]
CountryList = {
    "臺北市":"Taipei_City",
    "新北市":"New_Taipei_City",
    "桃園市":"Taoyuan_City",
    "臺中市":"Taichung_City",
    "臺南市":"Tainan_City",
    "高雄市":"Kaohsiung_City",
    "基隆市":"Keelung_City",
    "新竹市":"Hsinchu_City",
    "苗栗縣":"Miaoli_County",
    "彰化縣":"Changhua_County",
    "南投縣":"Nantou_County",
    "雲林縣":"Yunlin_County",
    "嘉義市": "Chiayi_City",
    "嘉義縣":"Chiayi_County",
    "屏東縣":"Pingtung_County",
    "宜蘭縣":"Yilan_County",
    "花蓮縣":"Hualien_County",
    "臺東縣":"Taitung_County",
    "金門縣":"Kinmen_County"
}
def catchTheDatas(countryName):
    returnDatas = {}
    res = urlopen("http://www.cwb.gov.tw/V7/forecast/taiwan/"+countryName+".htm")
    #print(res)
    soup = BeautifulSoup(res, "html.parser")

    #print(soup.select("#ContainerInOne"))

    count = 1
    CrewlerDatas = soup.select("#ContainerInOne")[0].select(".FcstBoxTable01")[0].text.split("\n")


    WeatherDatas = [x for x in CrewlerDatas if x]



    return{
        "country": WeatherDatas[0],
        "sections":{
          "section1":WeatherDatas[5],
          "section2": WeatherDatas[9],
          "section3": WeatherDatas[13]
        },
        "section1":{#第一個時段
            "Temp":WeatherDatas[6],
            "Confid":WeatherDatas[7],
            "Rain":WeatherDatas[8]
        },
        "section2":{#第二個時段
            "Temp": WeatherDatas[10],
            "Confid": WeatherDatas[11],
            "Rain": WeatherDatas[12]
        },
        "section3":{#第三個時段
            "Temp": WeatherDatas[14],
            "Confid": WeatherDatas[15],
            "Rain": WeatherDatas[16]
        }
    }
def run():
    AllCountryWeatherDatas = {}
    for i in countrysName:
        AllCountryWeatherDatas[i] = (catchTheDatas(i))
        #print(catchTheDatas(i))
    return AllCountryWeatherDatas

if __name__ == '__main__':
    strings = run()
    json_str = json.dumps(run(),ensure_ascii=False).encode("utf-8")
    print(json.loads(json_str))