import requests
from pprint import pprint
import html
import random as r
 
vpr = int(input("Koliko vprašanj želiš? "))
url = f"https://opentdb.com/api.php?amount={vpr}&type=multiple"
klic = requests.get(url).json()
 
vprasanja = klic["results"]
t = 0
for v in vprasanja:

    print(html.unescape(v["question"]))
    prav = v["correct_answer"]
    odgovori = list(v["incorrect_answers"])
    odgovori.append(prav)
    r.shuffle(odgovori)
    for i, o in enumerate(odgovori):
        print(f"{i+1} - {o}")
    odgovor = int(input("Odgovor: "))
    if prav == odgovori[odgovor-1]:
        print(True)
        t +=1
    else:
        print(False)

print(f"{t}/{vpr} odgovorov si odgovoril pravilno.")
"""
VPRAŠANJE?
 
ODGOVOR 1
ODGOVOR 2
ODGOVOR 3
ODGOVOR 4
 
Odgovor: ??
 
Pravilno/napačno
BONUS: število točk
"""