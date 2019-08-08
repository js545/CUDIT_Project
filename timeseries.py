# Jake Son
# UNMC August 7, 2019

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

wd = '/Users/jakeson/Desktop/UNMC/CUDIT_Project/'
os.chdir(wd)

# Epoch from -800 to 2900 ms
# Baseline from -700 to -300 ms


def subset_orientation(df):

    df = df.loc[0:df.shape[0] / 2 - 1]

    return df


def remove_outliers(df):

    average_per_trial = df.mean(axis=1).tolist()
    total_average_trial = df.mean(axis=1).mean()
    stdev_trial = df.mean(axis=1).std()

    removed_trials = []

    for i in range(len(average_per_trial)):

        if average_per_trial[i] > total_average_trial + 3 * stdev_trial:
            removed_trials.append(i)

    df = df.drop(index=removed_trials)

    return df


def load_relative_data():

    user_df = pd.read_csv('User_RelPower.csv', header=None)
    nonuser_df = pd.read_csv('Nonuser_RelPower.csv', header=None)
    user_df = subset_orientation(user_df)
    nonuser_df = subset_orientation(nonuser_df)
    user_df = remove_outliers(user_df)
    nonuser_df = remove_outliers(nonuser_df)

    return user_df, nonuser_df


def load_absolute_data():

    user_df = pd.read_csv('User_AbsPower.csv', header=None)
    nonuser_df = pd.read_csv('Nonuser_AbsPower.csv', header=None)
    user_df = subset_orientation(user_df)
    nonuser_df = subset_orientation(nonuser_df)
    user_df = remove_outliers(user_df)
    nonuser_df = remove_outliers(nonuser_df)

    return user_df, nonuser_df


def relative_mean_waveform(df):

    df = [x * 100 for x in list(df.mean())]

    return df


def absolute_mean_waveform(df):

    df = [x * x for x in list(df.mean())]

    return df


########################################################################################################################
### Relative Power

user_df, nonuser_df = load_relative_data()

# Calculate mean waveform

user_df_avg = relative_mean_waveform(user_df)
nonuser_df_avg = relative_mean_waveform(nonuser_df)

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

########################################################################################################################
### Absolute Power

user_df, nonuser_df = load_absolute_data()

# Calculate mean waveform

user_df_avg = absolute_mean_waveform(user_df)
nonuser_df_avg = absolute_mean_waveform(nonuser_df)

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


########################################################################################################################
### Relative power somatogating ratios from 0-50 ms

# Determine peaks for first stimulus

first_user_peaks = []
first_nonuser_peaks = []

for val in user_df.index:

    individ_timeseries = [x*x for x in user_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[32:35])
    first_user_peaks.append(peak_val)

for val in nonuser_df.index:

    individ_timeseries = [x*x for x in nonuser_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[32:35])
    first_nonuser_peaks.append(peak_val)

# Determine peaks for second stimulus

second_user_peaks = []
second_nonuser_peaks = []

for val in user_df.index:

    individ_timeseries = [x*x for x in user_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[52:55])
    second_user_peaks.append(peak_val)

for val in nonuser_df.index:

    individ_timeseries = [x*x for x in nonuser_df.loc[val].tolist()]
    peak_val = np.max(individ_timeseries[52:55])
    second_nonuser_peaks.append(peak_val)


########################################################################################################################
### Plot individual timeseries

user_df, nonuser_df = load_relative_data()

plt.figure()

for val in user_df.index:

    participant_timeseries = user_df.loc[val]
    plt.plot(range(len(participant_timeseries)), participant_timeseries, alpha=.5)

plt.show()














