#
#Izpiši temperaturo za poljuben kraj
import requests
def curtemp(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    return call["current"]["temperature_2m"]
    


print(curtemp(45.12,14.5))

