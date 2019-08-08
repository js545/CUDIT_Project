# Jake Son
# UNMC August 7, 2019

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

wd = os.getcwd()
os.chdir(wd)

# Epoch from -800 to 2900 ms
# Baseline from -700 to -300 ms

### Relative Power

user_df = pd.read_csv('User_RelPower.csv', header=None)
nonuser_df = pd.read_csv('Nonuser_RelPower.csv', header=None)

# Subset one orientation

user_df = user_df.loc[0:user_df.shape[0]/2-1]
nonuser_df = nonuser_df.loc[0:nonuser_df.shape[0]/2-1]

# Remove outlier participants

average_per_trial = user_df.mean(axis=1).tolist()
total_average_trial = user_df.mean(axis=1).mean()
stdev_trial = user_df.mean(axis=1).std()

removed_trials = []

for i in range(len(average_per_trial)):

    if average_per_trial[i] > total_average_trial + 3*stdev_trial:

        removed_trials.append(i)

user_df = user_df.drop(index=removed_trials)

average_per_trial = nonuser_df.mean(axis=1).tolist()
total_average_trial = nonuser_df.mean(axis=1).mean()
stdev_trial = nonuser_df.mean(axis=1).std()

removed_trials = []

for i in range(len(average_per_trial)):

    if average_per_trial[i] > total_average_trial + 3*stdev_trial:

        removed_trials.append(i)

nonuser_df = nonuser_df.drop(index=removed_trials)

# Calculate mean waveform

user_df_avg = [x*100 for x in list(user_df.mean())]
nonuser_df_avg = [x*100 for x in list(nonuser_df.mean())]

# Plot

time = np.linspace(-800, 2900, len(user_df_avg))

plt.figure()
plt.title('Relative Power of CUD vs Control')
plt.xlabel('Time (ms)')
plt.ylabel('Relative Power (%)')
plt.plot(time, user_df_avg, color='blue', label='User')
plt.plot(time, nonuser_df_avg, color='red', label='Nonuser')
plt.axvline(x=0, color='black', alpha=.5)
plt.axvline(x=500, color='black', alpha=.5)
plt.legend()
plt.savefig('/Users/jakeson/Desktop/UNMC/CUDIT_Project/relative.png', dpi=600)
plt.show()




### Absolute Power

user_df = pd.read_csv('User_AbsPower.csv', header=None)
nonuser_df = pd.read_csv('Nonuser_AbsPower.csv', header=None)

# Subset one orientation

user_df = user_df.loc[0:user_df.shape[0]/2-1]
nonuser_df = nonuser_df.loc[0:nonuser_df.shape[0]/2-1]

# Remove outlier participants

average_per_trial = user_df.mean(axis=1).tolist()
total_average_trial = user_df.mean(axis=1).mean()
stdev_trial = user_df.mean(axis=1).std()

removed_trials = []

for i in range(len(average_per_trial)):

    if average_per_trial[i] > total_average_trial + 3*stdev_trial:

        removed_trials.append(i)

user_df = user_df.drop(index=removed_trials)

average_per_trial = nonuser_df.mean(axis=1).tolist()
total_average_trial = nonuser_df.mean(axis=1).mean()
stdev_trial = nonuser_df.mean(axis=1).std()

removed_trials = []

for i in range(len(average_per_trial)):

    if average_per_trial[i] > total_average_trial + 3*stdev_trial:

        removed_trials.append(i)

nonuser_df = nonuser_df.drop(index=removed_trials)

# Calculate mean waveform

user_df_avg = list(user_df.mean())
nonuser_df_avg = list(nonuser_df.mean())

user_df_avg = [x*x for x in user_df_avg]
nonuser_df_avg = [x*x for x in nonuser_df_avg]

# Plot

time = np.linspace(-800, 2900, len(user_df_avg))

plt.figure()
plt.title('Absolute Power of CUD vs Control')
plt.xlabel('Time (ms)')
plt.ylabel('Absolute Power')
plt.plot(time, user_df_avg, color='blue', label='User')
plt.plot(time, nonuser_df_avg, color='red', label='Nonuser')
plt.axvline(x=0, color='black', alpha=.5)
plt.axvline(x=500, color='black', alpha=.5)
plt.legend()
plt.savefig('/Users/jakeson/Desktop/UNMC/CUDIT_Project/absolute.png', dpi=600)
plt.show()


### Relative power somatogating ratios from 0-50 ms

# Determine peaks for first stimulus

first_user_peaks = []
first_nonuser_peaks = []

for val in user_df.index:

    individ_timeseries = [x*100 for x in user_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[32:35])
    first_user_peaks.append(peak_val)

for val in nonuser_df.index:

    individ_timeseries = [x*100 for x in nonuser_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[32:35])
    first_nonuser_peaks.append(peak_val)

# Determine peaks for second stimulus

second_user_peaks = []
second_nonuser_peaks = []

for val in user_df.index:

    individ_timeseries = [x*100 for x in user_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[52:55])
    second_user_peaks.append(peak_val)

for val in nonuser_df.index:

    individ_timeseries = [x*100 for x in nonuser_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[52:55])
    second_nonuser_peaks.append(peak_val)













