#
#Izpiši temperaturo za poljuben kraj
import requests
def curtemp(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    return call["current"]["temperature_2m"]
#print(curtemp(45.12,14.5))



def tedntemp(lat,lon):
    baseurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    call = requests.get(baseurl).json()
    tedn = []
    temp = call["hourly"]["temperature_2m"]
    vs = 0
    n = 0
    for i in temp:
        if n == 23:
            tedn.append(round(vs/24,2))
            vs = 0
            n = -1
        vs += i
        n +=1
    return tedn
#print(tedntemp(46.2259,14.6121))

def največ():
    baseurl = "https://api.open-meteo.com/v1/forecast?latitude=46.2259&longitude=14.6121&daily=temperature_2m_max,temperature_2m_min"
    call = requests.get(baseurl).json()
    maxt = call["daily"]["temperature_2m_max"]
    dan = call["daily"]["time"]
    mint = call["daily"]["temperature_2m_min"]
    i = 0
    u = 0
    while True:
        if maxt[i] == max(maxt):
            break
        i += 1
    while True:
        if mint[u] == min(mint):
            break
        u += 1
    
    return max(maxt),f"{dan[i]} je najtoplejsi",min(mint),f"{dan[u]} je najhladnejsi"
                   
#print(največ())


def razl():
    baseurl = "https://api.open-meteo.com/v1/forecast?latitude=46.2259&longitude=14.6121&daily=temperature_2m_max,temperature_2m_min"
    call = requests.get(baseurl).json()
    maxt = call["daily"]["temperature_2m_max"]
    mint = call["daily"]["temperature_2m_min"]
    raz = 0
    for i in range(len(maxt)):
        if maxt[i]-mint[i] > raz:
            raz = maxt[i]-mint[i]


    return round(raz,1)

#print(razl())


def curtemp2(lat,lon):
    baseurl = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : lat,
            "longitude" : lon,
            "current" : "temperature_2m",
            "timezone" : "auto",
            "forecast_days" : 1
            }
    call = requests.get(baseurl, params=params)
    print(call.url)

#curtemp2(45.12,14.5)


def naj10(lat,lon):
    baseurl = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude" : lon,
        "daily" : "temperature_2m_max",
        "forecast_days" : 1
    }
    call = requests.get(baseurl, params=params).json()
    maxt = call["daily"]["temperature_2m_max"]
    return maxt

def dezevje(lat,lon):
    baseurl = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : lat,
            "longitude" : lon,
            "daily" : "rain_sum",
            "forecast_days" : 1}
    call = requests.get(baseurl, params=params).json()
    maxd = call["daily"]["rain_sum"]
    return maxd

def vetr(lat,lon):
    baseurl = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : lat,
     "longitude" : lon,
     "daily" : "wind_speed_10m_max",
     "forecast_days" : 1}
    call = requests.get(baseurl, params=params).json()
    maxv = call["daily"]["wind_speed_10m_max"]
    return maxv


mesta = [
    ("Ljubljana",46.05108,14.50513),
    ("Maribor",46.55583,15.64593),
    ("Celje",46.23092,15.26044),
    ("Kranj",46.23887,14.35561),
    ("Koper",45.54820,13.72963),
    ("Novo mesto",45.80397,15.16886),
    ("Velenje",46.35719,15.11277),
    ("Ptuj",46.42005,15.87018),
    ("Trbovlje",46.15500,15.05333),
    ("Kamnik",46.22587,14.61207)]

temperature = []
dez = []
vetr1 = []
"""
for m in mesta:
    temp = naj10(m[1], m[2])
    temperature.append((temp, m[0]))
print(max(temperature),"max", min(temperature,"min")
"""
"""
for m in mesta:
    dz = dezevje(m[1], m[2])
    dez.append((dz, m[0]))
print(max(dez),"max", min(dez),"min")
"""
for m in mesta:
    veter = vetr(m[1], m[2])
    vetr1.append((veter, m[0]))
print(max(vetr1),"max", min(vetr1),"min")


