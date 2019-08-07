# Jake Son
# UNMC August 7, 2019

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

wd = os.getcwd() + '/CUDIT_Project'
os.chdir(wd)

# Epoch from -800 to 2900 ms
# Baseline from -700 to -300 ms

### Relative Power

user_df = pd.read_csv('User_RelPower.csv', header=None)
nonuser_df = pd.read_csv('Nonuser_RelPower.csv', header=None)

# Subset one orientation

user_df = user_df.loc[0:user_df.shape[0]/2-1]
nonuser_df = nonuser_df.loc[0:nonuser_df.shape[0]/2-1]

user_df_avg = list(user_df.mean())
nonuser_df_avg = list(nonuser_df.mean())

# Plot

time = np.linspace(-800, 2900, len(user_df_avg))

plt.figure()
plt.title('Relative Power of CUD vs Control')
plt.xlabel('Index')
plt.ylabel('Relative Power (%)')
plt.plot(time, user_df_avg, color='blue', label='User')
plt.plot(time, nonuser_df_avg, color='red', label='Nonuser')
plt.axvline(x=0, color='black', alpha=.5)
plt.axvline(x=500, color='black', alpha=.5)
plt.legend()
plt.show()

### Absolute Power

user_df = pd.read_csv('User_AbsPower.csv', header=None)
nonuser_df = pd.read_csv('Nonuser_AbsPower.csv', header=None)

# Subset one orientation

user_df = user_df.loc[0:user_df.shape[0]/2-1]
nonuser_df = nonuser_df.loc[0:nonuser_df.shape[0]/2-1]

user_df_avg = list(user_df.mean())
nonuser_df_avg = list(nonuser_df.mean())

user_df_avg = [x*x for x in user_df_avg]
nonuser_df_avg = [x*x for x in nonuser_df_avg]

# Plot

time = np.linspace(-800, 2900, len(user_df_avg))

plt.figure()
plt.title('Absolute Power of CUD vs Control')
plt.xlabel('Index')
plt.ylabel('Absolute Power')
plt.plot(time, user_df_avg, color='blue', label='User')
plt.plot(time, nonuser_df_avg, color='red', label='Nonuser')
plt.axvline(x=0, color='black', alpha=.5)
plt.axvline(x=500, color='black', alpha=.5)
plt.legend()
plt.show()






