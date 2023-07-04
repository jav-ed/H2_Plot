import dataclasses
import numpy as np
import plotly.graph_objects as go

from Code.Visual.Helper.html_Methods import HT_Meth



@dataclasses.dataclass
class Plt_Z:
    
    pv:any
    Tv:any
    Z:any
    
    def __post_init__(self):
        
        fig = go.Figure()
        
        # --------------------- compressibility factor Z --------------------- #
        fig.add_trace(go.Surface(
            x = self.pv,
            y = self.Tv,
            z = self.Z,
            colorbar_title = dict(
                            side= "top",
                            text ="compressibility factor",
                            ),

            # equal colorbar
            cmin = np.min([1, np.min(self.Z)]),
            cmax = np.max(self.Z)

        ))
            
        # ------------------- compressibility factor Z = 1 ------------------- #
        fig.add_trace(go.Surface(
            x = self.pv,
            y = self.Tv,
            z = np.ones(self.Z.shape),
            showscale= False,
            
            # equal colorbar
            cmin = np.min([1, np.min(self.Z)]),
            cmax = np.max(self.Z)

        ))
        
        
        # -------------- Get contours --> const p, Z, and Temo -------------- #
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
                          )
        
        # layout styling
        fig.update_layout( # add default dark theme
                        template ="plotly_dark",
                        
                        title = r"$\text{Compressibility of H}_2:\, Z(p, T)$",
                        title_x = 0.5,
                        
                        scene_xaxis_title=r"pressure [MPa]",
                        scene_yaxis_title=r"temperature [K]",
                        scene_zaxis_title=r"compressibility factor [-]", 
                        
                        # camera settings
                        #x-y plane
                        scene_camera= dict(
                            eye = dict(x= 0.5,
                                       y= -2.5,
                                       z= 1),
                            
                                    ),
                         
                          
                        )
        
        fig.update_traces(
                        # customdata= custom_Data,
                        hovertemplate=
                            f'<b>H2-Modeler</b>'+
                            '<br>pressure: %{x:.3f} [MPa]'+ 
                            '<br>temp: %{y:.3f} [K]'+
                            '<br>Z: %{z:.3f} [-]'+
                            '<extra></extra>',
                            
        )
        
        # get the dark mode switcher
        fig = HT_Meth.add_Dark_Mode(fig)
        
        # save as html
        HT_Meth.gen_HTML(fig, "./Output/","z_Compres_Fact")
        
        


    