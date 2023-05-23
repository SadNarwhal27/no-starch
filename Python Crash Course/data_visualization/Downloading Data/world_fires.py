from pathlib import Path
import csv
import plotly.express as px

path = Path('Python Crash Course\data_visualization\Downloading Data\eq_data\world_fires_7_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, highs, and low temps.
lons, lats, brightness = [], [], []
station_name_text = ''
for row in reader:
    lons.append(float(row[1]))
    lats.append(float(row[0]))
    brightness.append(float(row[2]))

title = 'Global Fires'
fig = px.scatter_geo(lat=lats, lon=lons, size=brightness, title=title,
                     color=brightness, color_continuous_scale='Viridis',
                     labels={'color':'Brightness'}, projection='natural earth',)
fig.show()