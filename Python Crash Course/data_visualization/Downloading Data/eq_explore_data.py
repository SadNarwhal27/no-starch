from pathlib import Path
import json
import plotly.express as px

# Read data as a str and convert to a Python object.
path = Path('Python Crash Course\data_visualization\Downloading Data\eq_data\eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Exampine all earthquakes in the dataset.
all_eq_data = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_data:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags, color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'}, projection='natural earth',
                     hover_name=eq_titles)
fig.show()