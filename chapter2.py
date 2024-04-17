# my_name = "chacha"
# my_age = 70
# my_hobby = "coding"

# print(f"Hello my name is {my_name}, I'm {my_age} years old. and my hobby is {my_hobby}.")

def make_juice(fruit):
    return f"Here is your {fruit} juice!🥤"

def add_ice(juice):
    return f"{juice} +🧊"

def add_sugar(iced_juice):
    return f"{iced_juice} +🍬"

def add_milk(sugared_juice):
    return f"{sugared_juice} +🥛"

juice = make_juice("banana")
iced_juice = add_ice(juice)
sugared_juice = add_sugar(iced_juice)
perfect_juice = add_milk(sugared_juice)

print(perfect_juice)