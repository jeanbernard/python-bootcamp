capcom_players = {
    "Punk": "Cammy",
    "MenaRD": "Luke/Blanka",
    "Caba": "Guile"
}

nrs_players = {
    "Forever King": "Kung Lao",
    "Sonic Fox": "Sindel",
    "Semiji": "Kitana"
}

fgc = {"Capcom": capcom_players, "NRS": nrs_players}

for key in fgc:
    print(key)
    print(fgc[key])

travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "visits": 2,
    },
    {
    "country": "Germany",
    "cities_visited": ["Bferlin", "Hamburg", "Stuggart"], 
    "visits": 3
    },
]

for travel in travel_log:
    print(travel)