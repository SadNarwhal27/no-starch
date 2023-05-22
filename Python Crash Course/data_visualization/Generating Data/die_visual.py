import plotly.express as px
from die import Die

# Create a d6
die = Die()

# Make rolls and store results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze results.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results.
title = 'Results of Rolling 1d6 1000 Times'
labels = {'x': 'Results', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()