import matplotlib.pyplot as plt
import numpy as np
import Mod1

Simulation_BGS_address='D:/USER/YJH/program/BOCDA simulation/AI for BOCDA/bgs2d.txt'
measured_BGS_address='D:/USER/YJH/DATA/BOCDA/AI/DATA4/BOCDA_meas_DATA4_2.txt'

a=Mod1.Import_file(Simulation_BGS_address,0,'t')
b=Mod1.Normalization(a)

c=Mod1.Import_file(measured_BGS_address,0)[10:1011]
d=Mod1.Normalization(c)

plt.plot(b,'r',d,'b')
plt.show()