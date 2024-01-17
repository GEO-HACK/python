from pathlib import Path
import csv
import seaborn as sns
from datetime import datetime

import matplotlib.pyplot as plt

path = Path ('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


# for index, column_header in enumerate(header_row):#the enumarate function returns the index and the value as it loops through a list.
#     print(index, column_header)
#Extract high temparatures
dates,highs,lows =[], [], []# an epmty lost is formed called highs
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int (row[4])#showing the position of the data in the row 
    low = int (row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)  
#plot the high temparatures
sns.set_style('darkgrid')
fig,ax = plt.subplots()
ax.plot(dates,highs,c = 'blue',alpha =0.5)
ax.plot(dates,lows,c ='red',alpha = 0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#format the plot
ax.set_title("Daily High  and Low Temperatures, July 2021",fontsize = 24)
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temeprature(f)',fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()