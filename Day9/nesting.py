# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Nice", "Bordeaux"],
    "Greece": "Oia",
    "England": "London",
    "Spain": ["Barcelona", "Madrid"]
}

# Nesting a List in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Nice", "Bordeaux"],
        "total_visits": 7
    },
    "Greece": {
        "steps_taken_each_day": 20000,
        "favorite_foods": ["olives", "fish", "greek yogurt"]
    },
    "England": "London",
    "Spain": ["Barcelona", "Madrid"]
}

# Nest Dictionary in a List
travel_log2 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lyon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Hamburg"],
        "total_visits": 9
    }
]