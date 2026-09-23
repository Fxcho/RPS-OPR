# imena = ["a","b","c","d"]
#AgifyAPI
#Najdi najstarejše ime v seznamu

import requests


def imena(names):
    najstarejse = 0
    ime = ""

    for i in names:
        response = requests.get("https://api.agify.io", params={"name": i}).json()
        if response["age"] > najstarejse:
            najstarejse = response["age"]
            ime = i

    print(ime, najstarejse)


imena(("Luka", "Maja", "Nika", "Filip", "Lara", "Tim", "Eva", "Nejc", "Sara", "Vid", "Tia", "Jure", "Klara", "Lan", "Ana", "Gal", "Zoja", "Mark", "Ela"))

