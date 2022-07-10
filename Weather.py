# Weather based background changer

import requests
import time
import datetime
import ctypes

api_key = "acff1d09d7ab4553bd8234828220707"


def main():
    json_data = requests.get(api_key).json()
    W_data = json_data["Weather"][0]["main"]
    Night_time = datetime.time(0, 6)
    Sunrise_time = datetime.time(7, 9)
    Noon_Time = datetime.time(10, 15)
    Evening_Time = datetime.time(16, 23)


def Weather():
    if W_data == "Rain":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\Rain.jpg", 0)
    elif W_data == "Sunshine":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\Sunshine.jpg", 0)
    elif W_data == "Cloudy":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\Cloudy.jpg", 0)


def Time():
    if Night_time:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\night.jpg", 0)
    elif Sunrise_time:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\Sunrise.jpg", 0)
    elif Noon_Time:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\evening.jpg", 0)
    elif Evening_Time:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\taran\Downloads\noon.jpg", 0)
