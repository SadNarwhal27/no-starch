import plotly.express as px
from die import Die

# Create the d6
die_1 = Die()
die_2 = Die()

# Make rolls and store results
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize results.
title = 'Results of Rolling 2d6 1000 Times'
labels = {'x': 'Results', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html('dice_visual.html')