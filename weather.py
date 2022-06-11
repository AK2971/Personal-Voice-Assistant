import imp
import requests
from ss import *


api_addr = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid='+key2
json_data=requests.get(api_addr).json()


def temp():
    temperature=round(json_data["main"]["temp"]-271,1)
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description

# print(temp())
# print(des())    