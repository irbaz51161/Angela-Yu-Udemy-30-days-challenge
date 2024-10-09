#Nested dictionary in a dictionary

travel_log = {
    "Pakistan": {"cities_visited": ["Lahore", "Islamabad", "Attock"], "total_visites": 12},
    "Korea": {"cities_visited": ["Seoul", "Jeju Island"], "total_visiters": 2}
}

#nesting dictionary in a List

travel_log1 = [
    {
        "country": "Pakistan",
        "cities_visited": ["Lahore", "Islamabad", "Attock"],
        "total_visites": 12
        },
    {
        "country": "Korea",
        "cities_visited": ["Seoul", "Jeju Island"],
        "total_visiters": 2
        }
]
print(travel_log1[1])