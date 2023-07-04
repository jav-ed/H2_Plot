import numpy as np


class Helper_Methods:
    
    # ======================================================================== #
    # =========================== get_Constants(): =========================== #
    # ======================================================================== #
    @staticmethod
    def get_Constants():
        # ------------------------- Define constants A_is -------------------- #
        a1 = 0.058_884_60
        a2 = -0.061_361_11
        a3 = -0.002_650_473
        a4 = 0.002_731_125
        a5 = 0.001_802_374
        a6 = -0.001_150_707
        a7 = 0.958_852_8e-4
        a8 = -0.110_904_0e-6
        a9 = 0.126_440_3e-9
        
        a_Consts = np.array([   a1,
                                a2,
                                a3,
                                a4,
                                a5,
                                a6,
                                a7,
                                a8,
                                a9,
                            ])


        # ------------------------- Define constants B_is -------------------- #
        b1 = 1.325 
        b2 = 1.87 
        b3 = 2.5
        b4 = 2.8
        b5 = 2.938
        b6 = 3.14
        b7 = 3.37
        b8 = 3.75
        b9 = 4.0

        b_Consts = np.array([   b1,
                                b2,
                                b3,
                                b4,
                                b5,
                                b6,
                                b7,
                                b8,
                                b9,
                            ])
        
        # ------------------------- Define constants C_is -------------------- #
        c1 = 1.0
        c2 = 1.0
        c3 = 2.0
        c4 = 2.0
        c5 = 2.42
        c6 = 2.63
        c7 = 3.0
        c8 = 4.0
        c9 = 5.0
        
        
        c_Consts = np.array([   c1,
                                c2,
                                c3,
                                c4,
                                c5,
                                c6,
                                c7,
                                c8,
                                c9,
                            ])

        # Molar Mass
        M = 2.015_88 # [g/mol]

        # Universal Gas Constant
        R = 8.314_472 # [J/(mol * K)]
        
        return a_Consts, b_Consts, c_Consts, M, R

    # ======================================================================== #
    # ============================ calc_Compress_Z =========================== #
    # ======================================================================== #
    @staticmethod
    def calc_Compress_Z(p, 
                        T, 
                        a_Consts,
                        b_Consts,
                        c_Consts,
                        ):
        """_summary_
            Args:
                p (doubke): pressure [MPa]
                T (double): Temp [K]
        """
        sum_Z = np.sum( a_Consts * \
                        np.power((100/T),b_Consts) * \
                        np.power(p,c_Consts)
                        )
        
        Z = 1+ sum_Z
        
        return Z
    
    
    # ======================================================================== #
    # ============================ get_Dens_Over_Z =========================== #
    # ======================================================================== #
    @staticmethod
    def get_Dens_Over_Z(p,T,Z, R = 8.314_472 ):
        """_summary_

        Args:
            p (float): in MPa
            T (float): in K
            Z (float): [-]
            R (float, optional): _description_. Defaults to 8.314_472
        """
        # Z = p/ (rho * R *T) 
        # --> rho = p/ (Z * R *T)
        rho = p/(Z * R * T) * 1e+6 #[mol/m^3]
        
        # rho = rho * 1e-3    #[mol/liter]
        return  rho