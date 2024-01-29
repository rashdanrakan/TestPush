from sys import displayhook
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

rdf_data_FG_1_1 = np.loadtxt('1_1_FlowGradient.txt')
rdf_data_FG_1_2 = np.loadtxt('1_2_FlowGradient.txt')
rdf_data_FG_2_2 = np.loadtxt('2_2_FlowGradient.txt')
rdf_data_FV_1_1 = np.loadtxt('1_1_FlowVorticity.txt')
rdf_data_FV_1_2 = np.loadtxt('1_2_FlowVorticity.txt')
rdf_data_FV_2_2 = np.loadtxt('2_2_FlowVorticity.txt')

start_strain = 990 # start strain.
end_strain = 1000 # stop  strain.  Here it corresponds to strain of 1
interval_step = 1 # Strain intervals used in the g(r) data.  By default this corresponds to strain 0.001.
number_of_strains = int((end_strain-start_strain)/interval_step) + 1
step_range = np.linspace(start_strain, end_strain, number_of_strains) # create an  array to store the strains.
max_gr_values_FG_1_1 = np.zeros(number_of_strains)
max_gr_values_FG_1_2 = np.zeros(number_of_strains)
max_gr_values_FG_2_2 = np.zeros(number_of_strains)
max_gr_values_FV_1_1 = np.zeros(number_of_strains)
max_gr_values_FV_1_2 = np.zeros(number_of_strains)
max_gr_values_FV_2_2 = np.zeros(number_of_strains)
for strain_index in range(number_of_strains):
    strain_data_FG_1_1 = rdf_data_FG_1_1[:, strain_index + 1]
    max_gr_values_FG_1_1[strain_index] = np.max(strain_data_FG_1_1)

    strain_data_FG_1_2 = rdf_data_FG_1_2[:, strain_index + 1]
    max_gr_values_FG_1_2[strain_index] = np.max(strain_data_FG_1_2)

    strain_data_FG_2_2 = rdf_data_FG_2_2[:, strain_index + 1]
    max_gr_values_FG_2_2[strain_index] = np.max(strain_data_FG_2_2)

    strain_data_FV_1_1 = rdf_data_FV_1_1[:, strain_index + 1]
    max_gr_values_FV_1_1[strain_index] = np.max(strain_data_FV_1_1)

    strain_data_FV_1_2 = rdf_data_FV_1_2[:, strain_index + 1]
    max_gr_values_FV_1_2[strain_index] = np.max(strain_data_FV_1_2)

    strain_data_FV_2_2 = rdf_data_FV_2_2[:, strain_index + 1]
    max_gr_values_FV_2_2[strain_index] = np.max(strain_data_FV_2_2)
 

combined_data_1_1 = np.column_stack((step_range, max_gr_values_FG_1_1, max_gr_values_FV_1_1))
np.savetxt("max_gr_results_1_1.txt", combined_data_1_1,fmt='%.6f')
combined_data_1_2 = np.column_stack((step_range, max_gr_values_FG_1_2, max_gr_values_FV_1_2))
np.savetxt("max_gr_results_1_2.txt", combined_data_1_2,fmt='%.6f')
combined_data_2_2 = np.column_stack((step_range, max_gr_values_FG_2_2, max_gr_values_FV_2_2))
np.savetxt("max_gr_results_2_2.txt", combined_data_2_2,fmt='%.6f')

fig, ax = plt.subplots(dpi=1200)
ax.plot(step_range, max_gr_values_FG_1_1, label='FG_1_1')
ax.plot(step_range, max_gr_values_FG_1_2, label='FG_1_2')
ax.plot(step_range, max_gr_values_FG_2_2, label='FG_2_2')
ax.plot(step_range, max_gr_values_FV_1_1, label='FV_1_1')
ax.plot(step_range, max_gr_values_FV_1_2, label='FV_1_2')
ax.plot(step_range, max_gr_values_FV_2_2, label='FV_2_2')
ax.set_xlabel('Strain')
ax.set_ylabel('Max g(r) Value')
ax.set_title('Strain vs Max g(r) Values')
ax.legend()