This repository contains the emission line fluxes predicted with the Cloudy photoionization code version 17.01 (Ferland et al. 2017) for the star-forming models described in Section 3.1 of Calabro et al. (2023):
https://arxiv.org/abs/2306.08605

We use for the calculations the package pyCloudy v.0.9.11: 
https://github.com/Morisset/pyCloudy/tree/0.9.11. 
# Description of the models
In all cases, the incident radiation field shape is obtained with BPASS stellar population models (Eldridge et al. 2017), assuming a Salpeter IMF with an upper mass limit of 300 M<sub>sun</sub> , stellar metallicity equal to the gas phase metallicity of the surrounding gas cloud, and continuous star-formation history with age of $10^8$ yr. 
The brightness of the incident radiation field is defined through the ionization parameter log(U) varying between $−4$ and $−1$. 
Regarding the properties of the gas cloud surrounding the ionizing source (we adopt the spherical shell geometry), we assume a hydrogen number density ranging from $10^2$ to $10^4$ $cm^{−3}$, and a gas-phase metallicity Z<sub>gas</sub> from $10\%$ solar to two times solar, where the solar abundance of each element is set as in Savage \& Sembach (1996). The Cloudy calculation is stopped when reaching a temperature of $500$ K. 
# Line predictions available
Each table contains the predictions of the line intensity (in units of *erg/s*, obtained with the command 'get_emis_vol' in pycloudy) of a specific emission line (relative to $H\beta$) specified in the filename, as a function of the following model parameters : <br />
**dens** = gas density of the cloud (in units of $1/cm^3$ and logarithmic scale) <br />
**met** = gas-phase metallicity  <br />
**OH** = corresponding oxygen abundance of the cloud (12+log(O/H)) <br />
**logU** = ionization parameter <br />

# 
Currently, the flux predictions are available for the following emission lines, in order of increasing wavelength : \
$H\beta$ \
[OIII] $5006.84$ &angst; <br />
$H\alpha$ \
[NII] $6583.45$ &angst; <br />
[SIII] $9530.62$ &angst; <br />
[CI]  $9850.26$ &angst; <br />
$Pa\gamma$ \
[PII] $11882.8$ &angst; <br />
[FeII] $12566.8$ &angst; <br />
$Pa\beta$ \
[FeII] $16435.5$ &angst; <br />
$Pa\alpha$
