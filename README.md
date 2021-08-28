# Throttle-operation-thermodynamics

Throttle is an important component of refrigeration cycle wherein it allows a means of reducing the temperature of working fluid. In present problem a n-butane stream is considered at pressure P<sub>1</sub> and temperature T<sub>1</sub> that is throttled to a final pressure P<sub>2</sub>. The temperature T<sub>2</sub> or the quality (vapor mole fraction: x<sub>2</sub><sup>v</sup> ≡ x<sub>2</sub>) of the exit stream are unknown. The throttle process has been modelled as a steady-state, steady-flow adiabatic operation with no moving parts. Kinetic energy and potential energy changes for the flow streams are ignored.With these assumptions, the general energy balance simplifies to: ΔH<sup>12</sup> = 0.

### Description of the files
`Code_file.py` - It containes the final code which computes everything. <br />
`Butane_isobars.xlsx` - Thermophysical properties of n-butane - tabulated data for isobars at 0.1, 1.4, 1.6 MPa. They have been hardcoded into the code file itself but given for reference. 

### What does this code do?
1. Determines the phase of the exit stream among subcooled liquid, liquid-vapor coexistence, superheated vapor.
2. Determines the temperature T<sub>2</sub> of the exit stream. If the exit stream is in liquid-vapor coexistence, also determines the quality x<sub>2</sub>.
3. Some refrigeration cycle operations involve replacement of a throttle valve by an expander device with work output (e.g., turbine). It determines the maximum work that can be obtained on adiabatic expansion of the same inlet stream (P<sub>1</sub>1, T<sub>1</sub>) to the same outlet pressure (P<sub>2</sub>).

### For what parameter values does it work?
_Input parameters_ <br />
P<sub>1</sub> (in MPa): {1.4, 1.6} <br />
T<sub>1</sub> (in K): (200, 400) <br /> <br/>
_Output parameters_ <br />
P<sub>2</sub> (in MPa): 0.1

### How does the code file work? 
The code asks for the initial value of pressure which can be 1.4 MPa or 1.6 MPa and temperature which can be between 200 K to 400 K. If the inlet temperature (T<sub>1</sub>) is equal to the saturation temperature at the inlet pressure (P<sub>1</sub>) then it asks for the quality x<sub>1</sub> of the inlet vapor which needs to be specified. 
Then it gives the result for the thermodynamic operation for the two cases when ΔH<sup>12</sup> = 0 and ΔS<sup>12</sup> = 0. <br/>
The code has been written for P<sub>1</sub> = 1.4 or 1.6 MPa and T<sub>1</sub> between 200 K to 400 K. It can evaluate the final temperature for different inlet values as well if we change the hardcoded values of C<sub>p</sub> and temperature. These values can be taken from [NIST](https://www.nist.gov/) website for different inlet values.
