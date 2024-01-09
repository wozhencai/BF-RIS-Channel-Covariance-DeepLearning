"""
Compare the sum rate between the neural network and the Zero-forcing
Author    : Khin Thandar Kyaw
Date : 21 OCT 2023
Last Modified  : 15 Nov 2023
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from NNUtils import *


# tf_version: 2.15.0
print(tf.__version__)
print("Loading...")

# --------------------------- Start --------------------------------
totalUsers = ''.join(map(str, totalUsersFunc()))
Nt, N, _, _, _, _, _ = parameters(6) # 6 is just a placeholder
snrFixed = fiexdSNR()


global_ymin = 0
global_ymax = 60


# load the data
rateNNSupercase1 = np.load(f'Plotting/{totalUsers}users/sumRateSupercase1.npy')
rateNNSupercase2 = np.load(f'Plotting/{totalUsers}users/sumRateSupercase2.npy')

rateWFcase1 = np.load(f'Plotting/{totalUsers}users/sumRateWFcase1.npy')
rateWFcase2 = np.load(f'Plotting/{totalUsers}users/sumRateWFcase2.npy')

print('Loading...')
linePrint()

plt.figure(figsize=(7, 6))  


# Plot lines
#plottingLine(rateZF60, 'ZF-SBF [N = 60]', 'dotted', 'green', '+')
plottingLine(rateWFcase1, 'ZF beam w/ WF pwr [rank = 1]', 'dashed', 'blue', '+')
plottingLine(rateWFcase2, 'ZF beam w/ WF pwr [rank = 2]', 'dashed', 'red', '+')
plottingLine(rateNNSupercase1, 'Proposed [rank = 1]', 'solid', 'blue', '|')
plottingLine(rateNNSupercase2, 'Proposed [rank = 2]', 'solid', 'red', '|')

# Legend
plt.legend(loc='upper left', ncol=1, fontsize=13)
plt.ylim([global_ymin, global_ymax])

# Axes labels
plt.rc('text', usetex=True)
plt.xlabel(r'$P_{\mathrm{T}}/\sigma_n^2$ (dB)', fontsize=12)
plt.ylabel('Approximate sum rate (bps/Hz)', fontsize=13)

# Title
plt.title(r'$N_t$ = {}, $N$ = {}, $M + K$ = {}'.format(Nt, N, totalUsers), fontsize=13)

plt.grid(True) 
plt.tight_layout()  # Adjust layout to prevent clipping of legend
plt.savefig(f'Plotting/fig4.tiff')  
plt.savefig(f'Plotting/fig4.png')  
plt.close()

print("Done!")


  
