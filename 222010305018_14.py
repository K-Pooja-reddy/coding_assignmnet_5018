def ant_probability():
    probability_not_colliding = 1 / 4
    rounded_probability = round(probability_not_colliding, 2)
    return rounded_probability
result = ant_probability()
print("Probability:", result)