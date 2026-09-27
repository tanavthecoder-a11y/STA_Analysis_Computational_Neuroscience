Python 

# Path to dataset (ensure the .pickle file is in the same directory as this script)
DATASET_PATH = r"c1p8_data.pickle"

#load dataset
import numpy as np
import matplotlib.pyplot as plt
import pickle
with open(DATASET_PATH, 'rb') as f:
     data = pickle.load(f)

stim = data['stim']
rho = data['rho']
#Time window to look back before each spike
time_window = 300
#Time taken between each sample (2ms)
dt=2
#number of samples taken in 300ms (150 samples)
num_samples = int(time_window/dt)

#Steps below are used for computing STA

#find index locations of all spikes
spike_indices = np.where(rho == 1)[0]
#exclude spikes that occur in the first 300 ms since they don't have 150 samples
spike_indices = spike_indices[spike_indices >= num_samples-1]
#collect 150 stimulus points preceding every valid spike
stim_windows = []
for idx in spike_indices:
     window = stim[idx - num_samples + 1 : idx + 1]
     stim_windows.append(window)

#Takes average across collected stimulus windows
sta = np.mean(stim_windows, axis=0)


#Create x-axis time points from -300ms to 0ms
time_axis = np.linspace(-time_window, 0, num_samples)

#plotting STA
plt.plot(time_axis, sta, color='black')
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel('Time preceding spike (ms)')
plt.ylabel('Average Stimulus (velocity)')
plt.title('Spike-Triggered Average (STA)')
plt.grid(True)
plt.show()
