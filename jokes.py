import requests


url_add = "https://official-joke-api.appspot.com/random_joke"
json_data=requests.get(url_add).json()


arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]


def joke():
    return arr