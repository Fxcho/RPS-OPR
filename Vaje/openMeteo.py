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
        if n == 24:
            tedn.append(round(vs/24,2))
            vs = 0
            n = -1
        vs += i
        n +=1
    return tedn

print(tedntemp(46.2259,14.6121))
