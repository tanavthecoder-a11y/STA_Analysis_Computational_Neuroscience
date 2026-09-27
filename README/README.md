# Fly H1 Neuron - Spike-Triggered Average (STA)

A computational neuroscience project analyzing real experimental recordings from the blowfly H1 motion-sensitive visual neuron.

## Project Overview
This script calculates the **Spike-Triggered Average (STA)** to determine the average visual motion stimulus that precedes an action potential (spike).

## Findings
- **Integration Window:** The H1 neuron integrates motion stimulus over a window of approximately 300 ms.
- **Peak Sensitivity:** The peak stimulus feature triggering a spike occurs roughly 15–40 ms prior to firing.

## Results
![STA Plot](Figure_1.png)

## Tech Stack
- Python 3
- NumPy (Array manipulation and slicing)
- Matplotlib (Data visualization)
- Pickle (Data loading)

## Dataset
The analysis uses the `c1p8` dataset from the *Computational Neuroscience* course (University of Washington / Coursera), containing recordings of response spikes (`rho`) from a blowfly H1 neuron during visual motion stimulation (`stim`).

*Note: The raw `.pickle` file is not included in this repository. To run the analysis, download `c1p8.pickle` and place it in the root folder of this project.*

## How to Run
1. Place the dataset `c1p8_data.pickle` in the project directory.
2. Run `python sta_analysis.py`.
