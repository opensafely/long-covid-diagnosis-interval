import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("output/input.csv")

data['covid_date'] = pd.to_datetime(data['covid_date'])
data['long_covid_date'] = pd.to_datetime(data['long_covid_date'])

data['time'] = data['long_covid_date'] - data['covid_date']

data['time'] = data['time'].dt.days

data_male = data[data['sex'] == 'M']
data_female = data[data['sex'] == 'F']

times_male = data_male['time'].to_numpy()
times_female = data_female['time'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)    # The big subplot
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_male)
ax2.hist(times_female)

# Set common labels
ax.set_xlabel('Days between Covid-19 and Long Covid diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('Male')
ax2.set_title('Female')

plt.savefig('output/gender.jpg')

plt.clf()

ages = data['age'].to_numpy()
times = data['time'].to_numpy()

plt.scatter(ages, times)

plt.savefig('output/age.jpg')