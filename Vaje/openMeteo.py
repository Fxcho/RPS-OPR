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
print(tedntemp(46.2259,14.6121))

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







