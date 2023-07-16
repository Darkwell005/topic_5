colors: list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# temp = colors[0]
# colors[0] = colors[-1]
# colors[-1] = temp

colors[0], colors[-1] = colors[-1], colors[0]

print(colors)
