# dragOverSphere-PyFoam

This is a quick project to determine the drag over a sphere using OpenFOAM and the parameter variation capabililties of the PyFoam Python library.

## Prerequisites

- [OpenFOAM 9](https://openfoam.org/version/9/)
- [PyFoam](https://pypi.org/project/PyFoam/)

## Background

The drag coefficient of a sphere varies with Reynolds number, and this data is tabulated and correlated below (Schlichting, 1955; Morrison, 2013):

<img src="https://user-images.githubusercontent.com/51386700/144309550-d3d8c13f-bd08-46fd-92de-f2cb91292540.png" width="500"/>

## Methodology

- Mesher: blockMesh
- Solver: simpleFoam
- Turbulnce model: laminar

The `0/` and `system/` directories from the `simpleFoam/motorBike` tutorial were adapted for the simulations, as the tutorial was similar to a wind tunnel.

## (Preliminary) Results

<img src="https://user-images.githubusercontent.com/51386700/147396880-fa4856fd-861b-4763-888d-73ca98bcee5a.png" width="500"/>

The simulated drag coefficient aligns well with the data correlation throughout the Stokes region ($Re<1$) until $Re=100$, and a slight deviation is observed for higher Reynolds numbers. The drop in drag coefficient at $Re\approx200,000$, known as the "drag crisis" or "Eiffel paradox" phenomenon is not displayed in the simulated results.


The drag crisis is caused by a transition from a laminar boundary layer flow to a turbulent boundary layer flow, which results in a change from periodic vortex shedding to randomized vortex shedding. Since no turbulence model is used for these results, it is natural that this is not observed.

## To-do

- [x] Plot automation

- [] Mesh convergence study

