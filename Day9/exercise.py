travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

# Write a function that will allow new countries to be added to the log
def add_new_country(country, visits, cities):
    new_entry = {}
    new_entry["country"] = country
    new_entry["visits"] = visits
    new_entry["cities"] = cities
    travel_log.append(new_entry)

add_new_country("Luxembourg", 1, ["Luxembourg City"])
print(travel_log)