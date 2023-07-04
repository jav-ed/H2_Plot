#  1) [220; 1000] K = [-53; 727]°C and p [0;70] MPa with 0.01%
#  2) [255; 1000] K = [-18; 727]°C and p [0;120] MPa with 0.01%
#  3) [200; 1000] K = [-73; 727]°C and p [0;200] MPa with 0.1%


from logging import raiseExceptions
import numpy as np


import pathlib
import sys

cwd = pathlib.Path.cwd()
sys.path.append(str(cwd))

from Code.methods import Helper_Methods as H_Meth

# get the constants 
a_Consts, b_Consts, c_Consts, M, R = H_Meth.get_Constants() 

# define testing known values
p_S = np.array([1,10,50,200,200])       # [MPa]
T_S = np.array([200,300,400,500,200])   # [K]
Z_Expected = np.array([1.00675450, 1.05985282, 1.24304763, \
            1.74461629, 2.85953449 ])   # [-]

rho_Expected= np.array([0.59732645, 3.78267048, 12.09449023,\
            27.57562673, 42.06006952]) #[mol/l]
 
test_Suc = True
for i, (p_Ct, T_Ct, Z_Ct) in enumerate(zip(p_S, T_S, Z_Expected)):
    
    
    # ------------------ Get compressibility factor values ------------------- #
    Z = H_Meth.calc_Compress_Z(p_Ct, 
                                T=T_Ct,
                                a_Consts = a_Consts,
                                b_Consts = b_Consts,
                                c_Consts = c_Consts,
                                )
    delta_Z = Z - Z_Ct
    delta_Threshold = 1e-5
    
    print(f'T = {T_Ct}[K],\t p= {p_Ct} [MPa],\t Z= {Z},\t delta_Z = {delta_Z}')  
    
    if np.abs(delta_Z) < delta_Threshold:
        print("Z: Works fine\n")
    else:
        print("No, there are some errors inserted - Z")
        test_Suc = False 
        raiseExceptions("No, there are some errors inserted - Z")
        


    # ---------------------------- Calc densities ---------------------------- #
    # [mol/m³] 
    rho = H_Meth.get_Dens_Over_Z(p = p_Ct,
                                    T = T_Ct,
                                    Z = Z,
                                    R = R)
    # the paper 2008_Densit_Eqs uses [mol/l] --> convert [mol/m³] --> [mol/l] 
    rho = rho * 1e-3  # [mol/l] 
    
    delta_Rho = rho_Expected[i] - rho

    print(f'T = {T_Ct}[K],\t p= {p_Ct} [MPa],\t rho= {rho},\t delta_Rho = {delta_Rho}')  

    if np.abs(delta_Rho) < delta_Threshold:
        print("RHO: Works fine")
        print("------------------------------------------------\n")
        
    else:
        print("No, there are some errors inserted - DENSITY")
        test_Suc = False 
        raiseExceptions("No, there are some errors inserted - DENSITY")
        
        
if test_Suc:
    print(f'\nAll test were passed successfully')
        
        

