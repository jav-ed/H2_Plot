
import warnings
import pathlib
import plotly.io as pio
import plotly.express as px

import numpy

# ============================================================================ #
# ============================ HT_Meth ======================================= #
# ============================================================================ #
class HT_Meth:

    # ======================================================================
    # ============================ Generate HTML ===========================
    # ======================================================================
    @staticmethod
    def gen_HTML(fig, save_Loc, file_Name):
                 
        # fig.show
        # store the figure as html
        save_Loc = f"{save_Loc}/{file_Name}.html"
        
        # include_mathjax --> Latex abilities
        # local load --> requires all folder --> would only work on prepared computers
        base = pathlib.Path.cwd()
        ajax_Load_Local = str(base / "Code/Help_Files/Visual/Dependencies/0_Mathjax/MathJax.js")
        
        # pass link --> latex is only available if pc is connected to net
        ajax_Load_Online = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js'
 
        pio.write_html(fig, file= save_Loc, auto_open=False, include_mathjax = ajax_Load_Online,  include_plotlyjs="cdn")
        
                
    # ======================================================================
    # =========================== Dark Mode ================================
    # ======================================================================
    # if the html file shall be able to switch between 
    # templates (dark and light)   
    @staticmethod
    def add_Dark_Mode(fig):
        
        # get the templates
        template_Dark = pio.templates["plotly_dark"]
        template_Plotly = pio.templates["plotly"]
        # plotly_Dark.layout
        # plotly_Plotly.layout
                
        fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=["template", template_Dark],
                                    label="Dark",
                                    method="relayout"
                                ),
                                dict(
                                    args=["template", template_Plotly],
                                    label="Presentation",
                                    method="relayout"
                                ),


                            ]),
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                            x=0,
                            xanchor="left",
                            y=  1.01,
                            yanchor="top"
                        ),
                    ]
                )
        return fig
    
    
    
    # ==========================================================================
    # =========================== Layout =======================================
    # ==========================================================================
    # if the html file shall be able to switch between 
    # templates (dark and light)   
    @staticmethod
    def update_Layout(fig,
                      ):

        
        fig.update_layout(
            
                        # add default dark theme
                        template ="plotly_dark",
                        
                        title = r"$\text{Density of H}_2:\, \rho\,(p, T)$",
                        title_x = 0.5,
                        
                        scene_xaxis_title=r"pressure [MPa]",
                        scene_yaxis_title=r"temperature [K]",
                        scene_zaxis_title=r"density [kg/m³]",  
                          
                        # camera settings
                        #x-y plane
                        scene_camera= dict(
                            eye = dict(x= 0.5,
                                       y= -2.5,
                                       z= 1),
                            
                        ),
                        
                        legend = dict(orientation="h",
                                      xanchor = "right",
                                      yanchor = "top",
                                      y = 1.05,
                                      x = 1,
                                      
                                      ),
                        
                          )
        
        return fig
    
    # ======================================================================== #
    # ============================= Plotly Colors ============================ #
    # ======================================================================== #
    @staticmethod
    def plotly_Colors():
        
        # get default plotly colors
        # available [Dark24, Light24, Vivid, D3, G10, Bold, Antique]
        # plt_Cols = px.colors.qualitative.Plotly
        plt_Cols = px.colors.qualitative.Vivid
        
        return plt_Cols