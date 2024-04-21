days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # lists

print(days_of_week.count("Mon"))
days_of_week.reverse()

print(days_of_week)

# print("cuma".capitalize()) 

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") # tuples 불변함
print(days[2])

player = { #Dictionary
    "name": "Zeno",
    "age": 20,
    "height": 170,
    "weight": 70,
    "position": "Forward",
    "fav_food": ["pizza","hamburger"]
}

print(player)
print(player["name"])
print(player["fav_food"])
player["fav_food"].append("ice cream")
print(player.get("fav_food"))
