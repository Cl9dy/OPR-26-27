# slovarji (dictionary)

d = {1 : "a",
      2 : "b",
        3 : "c#"}

print(d[2])

#raznoliki slovar

r = {"št" : 6, "ime" : "Cl9dy", "seznam" : [1,2,3,4], "slovar" : {"firma" : "lexus LFA", "engine" : "6L V10 supercharged"}}

print(r["slovar"]["firma"])

# Open Meteo API

import requests

base_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&daily=rain_sum&timezone=Europe%2FBerlin"
temp_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&daily=temperature_2m_max&current=temperature_2m&timezone=Europe%2FBerlin"
temp2_url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&daily=temperature_2m_max,temperature_2m_min&current=temperature_2m&timezone=Europe%2FBerlin"

call = requests.get(base_url).json()
#print(call["daily"]["rain_sum"][0])
call2 = requests.get(temp_url).json()
call3 = requests.get(temp2_url).json()
print(call2["current"]["temperature_2m"])
print(call2["daily"]["temperature_2m_max"])
a = max(call2["daily"]["temperature_2m_max"])
print(a, (call2["daily"]["time"][(call2["daily"]["temperature_2m_max"].index(a))]))

d = call3["daily"]["temperature_2m_max"]
n = call3["daily"]["temperature_2m_min"]
biggestDif = 0

for i in range(len(d)):
    dif =d[i] - n[i]
    if dif > biggestDif:
        biggestDif = dif
        indeks = i
print("razlika: ", biggestDif, "dan: ", call3["daily"]["time"][indeks])

k1 = requests.get("https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&daily=temperature_2m_max,rain_sum,wind_speed_10m_max&timezone=Europe%2FBerlin").json()
