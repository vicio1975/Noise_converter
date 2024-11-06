# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def con():
    #from m/s2 to dB
    U = float(input("Please add the noise value in m*s^-2 = "))
    U0 = 1
    SdB = 20 *np.log10(U/U0)
    print("The noise value in m s^-2 is = ",U)
    return SdB
if __name__ == '__main__':
    noise = con()
    print("\nThe relative value in dB is = ",noise)
    w = input("\nPlease press any button to close")
    