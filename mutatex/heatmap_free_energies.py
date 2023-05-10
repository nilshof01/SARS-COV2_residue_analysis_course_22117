import pandas as pd
import seaborn as sns
import numpy as np

matrix = pd.read_csv(r"C:\Users\nilsh\OneDrive\Desktop\protein_modelling\energies.csv")
sns_matrix = matrix.iloc[:, 3:]
aa_wild = matrix.iloc[:, 0].tolist()
residues_var = list(sns_matrix.columns)
residues_wild = list((np.array(matrix.iloc[:, 2].tolist()) +318)) # 318 because from homology modelling the residue positions were set to 0.
merged_wild = list(zip(aa_wild, residues_wild))
sns_matrix = sns_matrix.drop(5, axis=0)
residue_aa_heat = sns.heatmap(sns_matrix,
                              cmap = "seismic",
                              center = 0,
                              xticklabels = residues_var,
                              yticklabels=merged_wild)
residue_aa_heat.set_xlabel('Amino Acid', fontsize = 16)
residue_aa_heat.set_ylabel('Residues', fontsize = 16)
colorbar = residue_aa_heat.collections[0].colorbar
colorbar.set_label('Free Energy in kcal/mol', fontsize=16)