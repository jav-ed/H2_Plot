# Initial Words

This code is part of the paper that is submitted, please find additional information on that [here](https://jav-ed.github.io/H2O_Plot/).
Basically, research has been conducted regarding a new type of airplane that very much depends on hydrogen. An illustrative example of this aircraft can be found below.

![Illustrative example of a Wing- Structure- Integrated high-pressure Hydrogen Tank (SWITH)1](Data/0_Imgs/0_Wing_Tube.png)

Given that these aircraft are intended to be propelled by hydrogen, understanding the impact of hydrogen within this configuration is of great importance.
In the context of SWITHs, several aspects highlight its innovative nature:
1) There are no existing regulations or norms,
2) No SWITHs are currently available in the open market,
3) Tanks are integrated into the structure, thereby bearing structural loads,
4) It's likely that these tanks will be made of composite material,
5) Among other factors.
   
To understand why these points above were listed, what other points were skipped and what their consequences are, please be invited to read the [paper](https://jav-ed.github.io/H2O_Plot/).

## What Does The Code Do
The output of the code is an interactive html file that will show the  density-pressure-temperature relationship of hydrogen. 
The output will be generated inside the folder *Output*.
You can find an online example [here](https://jav-ed.github.io/H2O_Plot/).
The plot's legend can be used to selectively display or hide desired hydrogen (H2) data sets as needed.
When the word *interactive* is used for the html display, it means, among other things, that a pop-up appears in which the values for current density, pressure and temperature are displayed.


## Installation and Execution
1) Make sure to have installed Python, we tested it with python v. **3.10.6**
2) Download it directly though the GUI provided by Github (Click on Code and then on Download Zip) or via git
3) Install the required dependencides
4) Run the main.py file with Python
5) Find the output in the folder called *Output*

```bash
git clone https://github.com/jav-ed/H2O_Plot.git
cd H2O_Plot
pip install -r Others/require.txt
python main.py
xdg-open Output/h2_Desnity_Plt.html
xdg-open Output/z_Compres_Fact.html
```


## Change Resolution
1) open *main.py*
2) adjust '*step_P*' and *step_T*, the smaller the values, the finer the resolution for which evaluations are returned

## Change Range
1) open *main.py*
2) change p_Min, p_Max for the min and max values for the pressure
3) change T_Min, T_Max for the min and max values for the temperature


## Infos About Hydrogen Density Accuracy
1) [220; 1000] K = [-53; 727]°C and p [0;70] MPa with 0.01%
2) [255; 1000] K = [-18; 727]°C and p [0;120] MPa with 0.01%
3) [200; 1000] K = [-73; 727]°C and p [0;200] MPa with 0.1%

For more detailed information about this topic, please refer to the original paper

*Lemmon, E.W.; Huber, M.L.; Friend, D.G.; Paulina, C.; et al. Standardized equation for hydrogen gas densities for fuel consumption applications. In Proceedings of the SAE World Congress, 2006, pp. 3–6.*



### Others
pep8 guide style? - no, thank you