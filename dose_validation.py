# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:11:13 2023

@author: ychoi
"""

import numpy as np
import matplotlib.pyplot as plt

point_dose = [8.3588e-16, 3.3328e-16, 1.9778e-16, 1.2544e-16, 8.2363e-17]
lab_dose = [14.7, 3.3, 1.4, 0.65, 0.37]
distance = [10, 20, 30, 40, 50]

def unit_convert(gray_dose):
    converted = gray_dose * 164650 * 0.805 * 3600 * (1e6)
    return converted

converted_point_dose = []

for i in point_dose:
    converted = unit_convert(i)
    converted_point_dose.append(converted)
    

def dose_rate_plot(distance, dose, color1, color2, label):
    plt.plot(distance, dose, color = color1, label = label) #, marker = 'o')
    for i in range(len(dose)):
        plt.plot(distance[i], dose[i], marker = 'o', color = color2)

    plt.xlabel('Distance from a point source (in cm)', fontsize = 15)
    # plt.xticks(5)
    plt.ylabel('Dose Rate ($\mu$Sv/hr)', fontsize = 15)
    plt.title( 'Dose Rate at Each Distance', fontsize = 20)
    plt.ylim(0,16)
    plt.legend()

    plt.grid('True')

dose_rate_plot(distance, lab_dose,'blue', 'red', 'Environmental measurement within the lab' )
dose_rate_plot(distance, converted_point_dose, 'green', 'orange', 'Measurement with a point Cs-137 source')


