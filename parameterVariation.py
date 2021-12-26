from os import path
import math
from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory
from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile
from PyFoam.Execution.BasicRunner import BasicRunner
from PyFoam.Applications.Decomposer import Decomposer
from PyFoam.Execution.ParallelExecution import LAMMachine

templateCase = SolutionDirectory(
    "flowAroundSphere", archive=None, paraviewLink=False)
# use viscosity to vary Reynolds number
nus = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]

for nu in nus:
    Re = round((1/nu), 2)
    # create each Re case
    case = templateCase.cloneCase(f"flowAroundSphere_Re_{Re}")
    vis = ParsedParameterFile(
        path.join(case.name, "constant", "transportProperties"))
    # change viscosity
    vis["nu"][1] = nu
    vis.writeFile()
    # run blockMesh
    runMesh = BasicRunner(
        argv=["blockMesh", "-case", case.name], silent=True, logname="blockMesh",
    )
    runMesh.start()
    # decompose case for parallel run
    Decomposer(args=["--progress", "--method=simple",
               "--n=3,2,1", "--delta=1e-4", case.name, 6]
               )
    machine = LAMMachine(nr=6)
    # run simpleFoam
    runSolution = BasicRunner(
        argv=["simpleFoam", "-case", case.name], silent=True, logname="simpleFoam", lam=machine
    )
    runSolution.start()
