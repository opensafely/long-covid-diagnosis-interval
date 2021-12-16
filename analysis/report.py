import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("output/input.csv")

data['covid_date'] = pd.to_datetime(data['covid_date'])
data['long_covid_date'] = pd.to_datetime(data['long_covid_date'])

data['time'] = data['long_covid_date'] - data['covid_date']

data['time'] = data['time'].dt.days

times = data['time'].to_numpy()

hist = plt.hist(times)

plt.xlabel("Days between Covid-19 and Long Covid diagnosis")
plt.ylabel("Frequency")

plt.savefig('output/histogram.jpg')
