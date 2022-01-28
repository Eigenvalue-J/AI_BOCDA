import numpy as np

def Import_file(address,line_number,transpose='n'):
    a=np.loadtxt(address)
    if transpose=='n':
        return a[line_number]
    else:
        return np.transpose(a)[line_number]

def Normalization(input_array):
    return input_array/np.max(input_array)

Simulation_BGS_address='D:/USER/YJH/program/BOCDA simulation/AI for BOCDA/bgs2d.txt'

if __name__ == "__main__":
    a=Import_file(Simulation_BGS_address,0,1)
    print(a)
    print(Normalization(a))