def eat_junk(food):
    assert food in [
        "pizza",
        "candy",
        'beer'
    ], 'yuuuuu!'
    return f"MMM what a tasty {food}."

food = input("What do you want to eat: ")
print(eat_junk(food))