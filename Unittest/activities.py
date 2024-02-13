def eat(food, is_healthy):
    ending = "I need biceps"
    if is_healthy:
        ending = "I need belly muscle"
    return f"I'm eating {food} because, {ending}"
def nap(num_hours):
    if num_hours >= 2:
        return f"I've slept for too long, It's been over {num_hours} hours"
    return f"Sleep is for the weak, its only {num_hours} hour!"