from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('Python Crash Course\data_visualization\Downloading Data\weather_data\death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Automatically finds indexs for max temp, min temp, and station name
tmax, tmin, station_name, temp_date = '', '', '', ''
for index, column_header in enumerate(header_row):
    if column_header.lower() == 'tmax':
        tmax = index
    if column_header.lower() == 'tmin':
        tmin = index
    if column_header.lower() == 'name':
        station_name = index
    if column_header.lower() == 'date':
        temp_date = index

# Extract dates, highs, and low temps.
dates, highs, lows = [], [], []
station_name_text = ''
for row in reader:
    current_date = datetime.strptime(row[temp_date], '%Y-%m-%d')

    try:
        high = int(row[tmax])
        low = int(row[tmin])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    station_name_text = row[station_name]
    

# Plot temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title(f"Daily High and Low Temps, 2021\n{station_name_text}", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temp (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()