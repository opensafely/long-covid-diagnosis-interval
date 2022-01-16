import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("output/input.csv")

data['covid_date'] = pd.to_datetime(data['covid_date'])
data['long_covid_date'] = pd.to_datetime(data['long_covid_date'])

data['time'] = data['long_covid_date'] - data['covid_date']

data['time'] = data['time'].dt.days

def wave(x):
    if (x > pd.to_datetime('2020-02-01')) & (x < pd.to_datetime('2020-06-30')):
        return 1
    elif (x > pd.to_datetime('2020-10-01')) & (x < pd.to_datetime('2021-03-30')):
        return 2
    elif (x > pd.to_datetime('2021-07-01')) & (x < pd.to_datetime('2021-11-30')):
        return 3
    elif (x > pd.to_datetime('2021-11-30')) & (x < pd.to_datetime('2022-01-15')):
        return 4

data['wave'] = data['covid_date'].apply(wave)

########## overall plot ##########
times = data['time'].to_numpy()

plt.hist(times)
plt.xlabel('Days between Covid-19 and Long Covid diagnosis')
plt.ylabel('Frequency')

plt.savefig('output/all.jpg')

plt.clf()

########## age plot ###########
ages = data['age'].to_numpy()

plt.scatter(ages, times)
plt.xlabel('Age')
plt.ylabel('Days between Covid-19 and Long Covid diagnosis')

plt.savefig('output/age.jpg')

plt.clf()

########## gender plot ###########
data_male = data[data['sex'] == 'M']
data_female = data[data['sex'] == 'F']

times_male = data_male['time'].to_numpy()
times_female = data_female['time'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_male)
ax2.hist(times_female)

ax.set_xlabel('Days between Covid-19 and Long Covid diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('Male')
ax2.set_title('Female')

plt.savefig('output/gender.jpg')

plt.clf()

########### ethnicity plot ###########
data_white = data[data['ethnicity'] == 1]
data_mixed = data[data['ethnicity'] == 2]
data_asian = data[data['ethnicity'] == 3]
data_black = data[data['ethnicity'] == 4]
data_other = data[data['ethnicity'] == 5]

times_white = data_white['time'].to_numpy()
times_mixed = data_mixed['time'].to_numpy()
times_asian = data_asian['time'].to_numpy()
times_black = data_black['time'].to_numpy()
times_other = data_other['time'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_white)
ax2.hist(times_asian)
ax3.hist(times_black)
ax4.hist(times_mixed)
ax5.hist(times_other)

ax.set_xlabel('Days between Covid-19 and Long Covid diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('White')
ax2.set_title('Asian')
ax3.set_title('Black')
ax4.set_title('Mixed')
ax5.set_title('Other')

plt.savefig('output/ethnicity.jpg')

plt.clf()

########### imd plot ###########
data_imd1 = data[data['imd'] == 1]
data_imd2 = data[data['imd'] == 2]
data_imd3 = data[data['imd'] == 3]
data_imd4 = data[data['imd'] == 4]
data_imd5 = data[data['imd'] == 5]

times_imd1 = data_imd1['time'].to_numpy()
times_imd2 = data_imd2['time'].to_numpy()
times_imd3 = data_imd3['time'].to_numpy()
times_imd4 = data_imd4['time'].to_numpy()
times_imd5 = data_imd5['time'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_imd1)
ax2.hist(times_imd2)
ax3.hist(times_imd3)
ax4.hist(times_imd4)
ax5.hist(times_imd5)

ax.set_xlabel('Days between Covid-19 and Long Covid diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('IMD 1')
ax2.set_title('IMD 2')
ax3.set_title('IMD 3')
ax4.set_title('IMD 4')
ax5.set_title('IMD 5')

plt.savefig('output/imd.jpg')

plt.clf()

########### region plot ###########
data_London = data[data['region'] == "London"]
data_SE = data[data['region'] == "South East"]
data_SW = data[data['region'] == "South West"]
data_East = data[data['region'] == "East"]
data_EM = data[data['region'] == "East Midlands"]
data_WM = data[data['region'] == "West Midlands"]
data_YH = data[data['region'] == "Yorkshire and The Humber"]
data_NE = data[data['region'] == "North East"]
data_NW = data[data['region'] == "North West"]

times_London = data_London['time'].to_numpy()
times_SE = data_SE['time'].to_numpy()
times_SW = data_SW['time'].to_numpy()
times_East = data_East['time'].to_numpy()
times_EM = data_EM['time'].to_numpy()
times_WM = data_WM['time'].to_numpy()
times_YH = data_YH['time'].to_numpy()
times_NE = data_NE['time'].to_numpy()
times_NW = data_NW['time'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(331)
ax2 = fig.add_subplot(332)
ax3 = fig.add_subplot(333)
ax4 = fig.add_subplot(334)
ax5 = fig.add_subplot(335)
ax6 = fig.add_subplot(336)
ax7 = fig.add_subplot(337)
ax8 = fig.add_subplot(338)
ax9 = fig.add_subplot(339)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_London)
ax2.hist(times_SE)
ax3.hist(times_SW)
ax4.hist(times_East)
ax5.hist(times_EM)
ax6.hist(times_WM)
ax7.hist(times_YH)
ax8.hist(times_NE)
ax9.hist(times_NW)

ax.set_xlabel('Days between Covid-19 and Long Covid diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('London')
ax2.set_title('SE')
ax3.set_title('SW')
ax4.set_title('East')
ax5.set_title('EM')
ax6.set_title('WM')
ax7.set_title('YH')
ax8.set_title('NE')
ax9.set_title('NW')

plt.savefig('output/region.jpg')

plt.clf()

########### wave plot ###########
data_wave1 = data[data['wave'] == 1]
data_wave2 = data[data['wave'] == 2]
data_wave3 = data[data['wave'] == 3]
data_wave4 = data[data['wave'] == 4]

times_wave1 = data_wave1['time'].to_numpy()
times_wave2 = data_wave2['time'].to_numpy()
times_wave3 = data_wave3['time'].to_numpy()
times_wave4 = data_wave4['time'].to_numpy()

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax1.hist(times_wave1)
ax2.hist(times_wave2)
ax3.hist(times_wave3)
ax4.hist(times_wave4)

ax.set_xlabel('Days between Covid-19 and Long Covid diagnosis')
ax.set_ylabel('Frequency')

ax1.set_title('Wave 1')
ax2.set_title('Wave 2')
ax3.set_title('Wave 3')
ax4.set_title('Wave 4')

plt.savefig('output/wave.jpg')

plt.clf()