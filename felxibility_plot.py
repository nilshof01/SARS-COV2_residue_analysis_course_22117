import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


residues = ["417","445", "449","484","501"]
flex_wild = [0.994, 4.588, 2.988, 2.130,2.373]
flex_omikron = [0.797, 2.503, 1.354, 1.523, 1.134]

fig, ax = plt.subplots()

bar_width = 0.25
x1_positions = np.arange(0.375, len(residues), 1)
x2_positions = np.arange(0.375, len(residues), 1)
x3_positions = [x + bar_width for x in x2_positions]

ax.bar(x2_positions, flex_wild, width=bar_width, label='Wildtype')
ax.bar(x3_positions, flex_omikron, width=bar_width, label='B.1.1.529')
ax.set_xticks([x + bar_width for x in x1_positions])
ax.set_xticklabels(residues)
plt.legend()
plt.xlabel("Residues")
plt.ylabel("RMSF")
