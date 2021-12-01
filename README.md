# dragOverSphere-PyFoam
A numerical investigation of drag over a sphere using OpenFOAM and the parameter variation capabilities of PyFoam.
## Background
The drag coefficient of drag over a sphere has been tabulated in Schlicthing, 1955, and is shown below:

<img src="https://user-images.githubusercontent.com/51386700/144309550-d3d8c13f-bd08-46fd-92de-f2cb91292540.png" width="500"/>

This investigation aims to utilize CFD to reproduce these results as accurately as possible within my resources.
## Requirements
- PyFoam library
- OpenFOAM 9

## How to use

Simply run `parameterVariation.py` and OpenFOAM cases with Reynolds numbers varying from 1e-2 to 1e7 will be created and ran using `simpleFoam`.

## Preliminary results
Adapting the `simpleFoam/motorBike` case produced these preliminary results:
<img src="https://user-images.githubusercontent.com/51386700/144313062-62d417a5-f169-43b9-9879-49739e0108fb.png" width="500"/>


## In progress
- Automatic plotting
