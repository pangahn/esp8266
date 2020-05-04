import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



df = pd.read_csv('data.csv')
df.time = pd.to_datetime(df.time)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.plot(df['time'], df['temperature'], color=color, linewidth=2)
ax1.grid(True, linestyle='-.')

ax1.set_xlabel('Time', fontsize=18)

ax1.set_ylabel('Temperature / ℃', fontsize=18, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax1.yaxis.set_tick_params(labelsize=18)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.plot(df['time'], df['humidity'], color=color, linewidth=2)

ax2.set_ylabel('Humidity / %', fontsize=18, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.yaxis.set_tick_params(labelsize=18)

locator = mdates.HourLocator(interval=1)
ax1.xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%H")
ax1.xaxis.set_major_formatter(formatter)

fig.tight_layout()
plt.show()