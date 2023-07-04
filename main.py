'''
author: Javed Arshad Butt
find additional information at: 
https://jav-ed.github.io/H2O_Plot/ and
https://github.com/jav-ed/H2O_Plot
'''
# ------------------ Infos about hydrogen density accuaracy ------------------ #
#  1) [220; 1000] K = [-53; 727]°C and p [0;70] MPa with 0.01%
#  2) [255; 1000] K = [-18; 727]°C and p [0;120] MPa with 0.01%
#  3) [200; 1000] K = [-73; 727]°C and p [0;200] MPa with 0.1%


import numpy as np

from Code.methods import Helper_Methods as H_Meth
from Code.Visual.plt_Dens import Plt_Dens
from Code.Visual.plt_Z import Plt_Z
 
# Pressure in [MPa]
p_Min = 0
p_Max = 200
step_P = 2

# Temperature in [K]
T_Min = 200
T_Max = 1000
step_T = 2

p = np.arange(p_Min, p_Max, step_P)
T = np.arange(T_Min, T_Max, step_T)
pv,Tv = np.meshgrid(p,T, indexing='xy')

# placeholders
rho = np.empty((T.size, p.size))
rho_Ideal_Gas = np.empty((T.size, p.size))

# compression factor
Z = np.empty((T.size, p.size))

# get the constants 
# M = [g/mol]
# R = [J/(mol ⋅ K)]
a_Consts, b_Consts, c_Consts, M, R = H_Meth.get_Constants() 

for i, T_Ct in enumerate(T):
    for j, p_Ct in enumerate(p):
        
        Z_Ct = H_Meth.calc_Compress_Z(p_Ct, 
                                      T = T_Ct,
                                      a_Consts = a_Consts,
                                      b_Consts = b_Consts,
                                      c_Consts = c_Consts,
                                )
        Z[i,j] = Z_Ct
        
        # note i = in the y direction = Temperature
        # and j = in the x direction = pressure
        # get the density as [kg/m³] --> [mol/m³]* [g/mol]
        rho[i,j] = H_Meth.get_Dens_Over_Z(p = p_Ct,
                                          T = T_Ct,
                                          Z = Z_Ct,
                                          R = R) * M * 1e-3
        
        # get the density when applying the ideal gas eqs = rho = p/(R T)
        rho_Ideal_Gas[i,j] = p_Ct/(R * T_Ct) * 1e+6 * M * 1e-3

# ---------------------------- Plot the densities ---------------------------- #
Plt_Dens(pv,
         Tv,
         rho,
         rho_Ideal_Gas, 
         Z)

# ------------------------- plot compressibility fact ------------------------ #
Plt_Z(pv,
      Tv,
      Z )

