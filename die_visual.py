from die import Die


die = Die()

# Моделировние серии бросков
results = []
for roll_number in range(100):
    result = die.roll()
    results.append(result)
print(results)
