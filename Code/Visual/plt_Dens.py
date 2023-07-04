import dataclasses
import numpy as np
import plotly.graph_objects as go

from Code.Visual.Helper.html_Methods import HT_Meth



@dataclasses.dataclass
class Plt_Dens:
    
    pv:any
    Tv:any
    rho:any
    
    # denisity obained by using the ideal gas
    rho_Ideal_Gas:any
    
    # the factor which translated from ideal gas to real gas
    Z:any
    
    
    def __post_init__(self):
        
        fig = go.Figure()
        
        # real gas eqs -> no use of ideal gas
        fig.add_trace(go.Surface(
            x = self.pv,
            y = self.Tv,
            z = self.rho,
            name = "real h2",
            showlegend = True,
            colorbar_title = dict(
                            side= "top",
                            text ="[kg/m³]",
                            ),
            
            hovertemplate=
                '<b>Real H2-Density</b>'+
                '<br>pressure: %{x:.3f} [MPa]'+ 
                '<br>temp: %{y:.3f} [K]'+
                '<br>dens: %{z:.3f} [kg/m³]'+
                '<extra></extra>',

        ))
        
        # ----------------------------- Ideal gas ---------------------------- #
        fig.add_trace(go.Surface(
            x = self.pv,
            y = self.Tv,
            z = self.rho_Ideal_Gas,
            name = "ideal gas",
            showlegend=True,
            showscale = False,
            
            hovertemplate=
                '<b>Ideal H2-Density</b>'+
                '<br>pressure: %{x:.3f} [MPa]'+ 
                '<br>temp: %{y:.3f} [K]'+
                '<br>dens: %{z:.3f} [kg/m³]'+
                '<extra></extra>',
            
        ))
        
        
        # -------------- Get contours --> const p, rho and Temo -------------- #
        fig.update_traces(contours_x=dict(show=True, 
                                          usecolormap=True,
                                          highlightcolor="limegreen",
                                          project_z=True
                                        ),
                          contours_y=dict(show=True, 
                                          usecolormap=True,
                                          highlightcolor="dodgerblue",
                                          project_z=True
                                          ),
                          contours_z=dict(show=True, 
                                          usecolormap=True,
                                          highlightcolor="firebrick",
                                          project_z=True
                                          ),
                          
                        # equal colorbar
                        cmin = np.min([np.min(self.rho), np.min(self.rho_Ideal_Gas)]),
                        
                        cmax = np.max(self.rho_Ideal_Gas)
                          )
        
        # layout styling
        fig = HT_Meth.update_Layout(fig)
        
        # additional data
        temp_Celcius = self.Tv + 273.15
        den_Gramm = self.rho * 1000
        
        
        # get the dark mode switcher
        fig = HT_Meth.add_Dark_Mode(fig)
        
        # save as html
        HT_Meth.gen_HTML(fig, "./Output/","h2_Desnity_Plt")
        
        


    