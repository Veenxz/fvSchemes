# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# version 3.0
# Based on https://github.com/Carlopasquinucci/fvSchemes
# Generation by Veenxz
# Include more options
# relaesed under license GPL GNU 3.0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# !Should make code clean
# Updated 2021/01/20
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

steady = True               # simpleFoam
precision = 2               # First order 1 or Second order 2
unbounded = False           # ddt backward
pseudo_transient = False    # For pimpleFoam and other solves support LTS
LUST = True                 # Recommend when using LES

# Mesh check results
maxOrtho = 29
maxSkew = 0.35

# Header and Footer
h = [
    "/*--------------------------------*- C++ -*----------------------------------*|",
    "| =========                 |                                                 |",
    "| \\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |",
    "|  \\\    /   O peration     | Website:  https://openfoam.org                  |",
    "|   \\\  /    A nd           | Version:  8                                     |",
    "|    \\\/     M anipulation  |                                                 |",
    "\*---------------------------------------------------------------------------*/",
    "FoamFile", "{", "    version     2.0;", "    format      ascii;",
    "    class       dictionary;", '    location    "system";', "    object      fvSchemes;",
    "}",
    "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //",
    ""
]
footer = '\n// ************************************************************************* //'

nonOrthogonalCorrectors = 1
if (maxOrtho) > 80:
    print(
        'Warning: mesh is not so nice. Use 3 nonOrthogonalCorrectors in fvSolution file'
    )
    nonOrthogonalCorrectors = 3
if (maxSkew) > 8:
    print('Warning: mesh is not so nice')

if (maxOrtho) > 80:

    gradSchemes = (
        '{\n    default          cellLimited Gauss linear 0.5;\n'
           '    grad(U)          faceLimited Gauss linear 1.0;\n}'
    )
    divSchemes = (
        '{\n    div(phi,U)       Gauss linearUpwind grad(U);\n'
           '    div(phi,omega)   Gauss upwind;\n'
           '    div(phi,k)       Gauss upwind;\n'
           '    div(phi,epsilon) Gauss upwind;\n'
           '    div(phi,nuTilda) Gauss limitedLinear 1;\n'
           '    div((nuEff*dev(T(grad(U))))) Gauss linear;\n}'
    )
    laplacianSchemes = (
        '{\n    default          Gauss linear limited 0.333;\n}'
    )
    snGradSchemes = (
        '{\n    default          limited 0.333;\n}'
    )

    blending = 0.2
    nonOrthogonalCorrectors = 3

if (maxOrtho) > 70:

    gradSchemes = (
        '{\n    default          cellLimited Gauss linear 0.5;\n'
           '    grad(U)          cellLimited Gauss linear 1.0;\n}'
    )
    divSchemes = (
        '{\n    div(phi,U)       Gauss linearUpwind grad(U);\n'
           '    div(phi,omega)   Gauss linearUpwind grad(omega);\n'
           '    div(phi,k)       Gauss linearUpwind grad(k);\n'
           '    div(phi,epsilon) Gauss linearUpwind grad(epsilon);\n'
           '    div(phi,nuTilda) Gauss limitedLinear 1;\n'
           '    div((nuEff*dev(T(grad(U))))) Gauss linear;\n}'
    )
    laplacianSchemes = (
        '{\n    default          Gauss linear limited 0.5;\n}'
    )
    snGradSchemes = (
        '{\n    default          limited 0.5;\n}'
    )

    blending = 0.5
    nonOrthogonalCorrectors = 3

if (maxOrtho) > 60:

    gradSchemes = (
        '{\n    default          cellMDLimited Gauss linear 0.5;\n'
           '    grad(U)          cellMDLimited Gauss linear 0.5;\n}'
    )
    divSchemes = (
        '{\n    div(phi,U)       Gauss linearUpwind grad(U);\n'
           '    div(phi,omega)   Gauss linearUpwind grad(omega);\n'
           '    div(phi,k)       Gauss linearUpwind grad(k);\n'
           '    div(phi,epsilon) Gauss linearUpwind grad(epsilon);\n'
           '    div(phi,nuTilda) Gauss limitedLinear 1;\n'
           '    div((nuEff*dev(T(grad(U))))) Gauss linear;\n}'
    )
    laplacianSchemes = (
        '{\n    default          Gauss linear limited 0.777;\n} '
    )
    snGradSchemes = (
        '{\n    default          limited 0.777;\n} '
    )

    blending = 0.7
    nonOrthogonalCorrectors = 2

if (maxOrtho) > 0:

    gradSchemes = (
        '{\n    default          cellMDLimited Gauss linear 0;\n'
           '    grad(U)          cellMDLimited Gauss linear 0.333;\n}'
    )
    divSchemes = (
        '{\n    div(phi,U)       Gauss linearUpwind grad(U);\n'
           '    div(phi,omega)   Gauss linearUpwind grad(omega);\n'
           '    div(phi,k)       Gauss linearUpwind grad(k);\n'
           '    div(phi,epsilon) Gauss linearUpwind grad(epsilon);\n'
           '    div(phi,nuTilda) Gauss limitedLinear 1;\n'
           '    div((nuEff*dev(T(grad(U))))) Gauss linear;\n}'
    )
    laplacianSchemes = (
        '{\n    default          Gauss linear limited 0.95;\n}'
    )
    snGradSchemes = (
        '{\n    default          limited 0.95;\n}'
    )

    blending = 0.8
    nonOrthogonalCorrectors = 1

if (LUST):
    gradSchemes = (
        '{\n    default          Gauss linear;\n'
           '    grad(U)          cellMDLimited Gauss linear 0.333;\n}'
    )
    divSchemes = (
        '{\n    div(phi,U)       Gauss LUST grad(U);\n'
           '    div(phi,omega)   Gauss LUST grad(omega);\n'
           '    div(phi,k)       Gauss LUST grad(k);\n'
           '    div(phi,epsilon) Gauss LUST grad(epsilon);\n'
           '    div(phi,nuTilda) Gauss limitedLinear 1;\n'
           '    div((nuEff*dev(T(grad(U))))) Gauss linear;\n}'
    )
    laplacianSchemes = (
        '{\n    default          Gauss linear corrected;\n}'
    )
    snGradSchemes = (
        '{\n    default          corrected;\n}'
    )
    
    blending = 0.7
    nonOrthogonalCorrectors = 1

if (steady):
    ddtSchemes = (
        '{\n    default          steadyState;\n}'
    )
    divSchemes = (
        '{\n    default          none;\n'
           '    div(phi,U)       bounded Gauss linearUpwind limited;\n'
           '    div(phi,omega)   bounded Gauss limitedLinear 1;\n'
           '    div(phi,k)       bounded Gauss limitedLinear 1;\n'
           '    div(phi,epsilon) bounded Gauss limitedLinear 1;\n'
           '    div(phi,nuTilda) bounded Gauss limitedLinear 1;\n'
           '    div((nuEff*dev2(T(grad(U))))) Gauss linear;\n}'
    )
else:
    ddtSchemes = (
        '{\n    default          CrankNicolson ' + str(blending) + ';\n}'
    )
    if precision == 1:
        ddtSchemes = (
            '{\n    default           Euler;\n}'
        )
    if (unbounded):
        ddtSchemes = (
            '{\n    default           backward;\n}'
        )

if (pseudo_transient):
            ddtSchemes = (
                '{\n    default          localEuler;\n}'
            )
      
interpolationSchemes = (
    "{\n    default          linear;\n}"
)


fluxRequired = (
    "{\n}\n"
)


wallDist = (
    "{\n    method           meshWave;\n}"
)

#open fvSchemes and write inside

f = open("system/fvSchemes", "w")

for i in h:
	f.write(i + "\n")

f.write("ddtSchemes" + "\n")
f.write(ddtSchemes + "\n")
f.write("\n")
f.write("gradSchemes" + "\n")
f.write(gradSchemes + "\n")
f.write("\n")
f.write("divSchemes" + "\n")
f.write(divSchemes + "\n")
f.write("\n")
f.write("laplacianSchemes" + "\n")
f.write(laplacianSchemes + "\n")
f.write("\n")
f.write("interpolationSchemes" + "\n")
f.write(interpolationSchemes + "\n")
f.write("\n")
f.write("snGradSchemes" + "\n")
f.write(snGradSchemes + "\n")
f.write("\n")
f.write("fluxRequired" + "\n")
f.write(fluxRequired + "\n")
f.write("\n")
f.write("wallDist" + "\n")
f.write(wallDist + "\n")
f.write(footer)

f.close()

print('nonOrthogonalCorrectors in fvSolution is', nonOrthogonalCorrectors)
print('File fvSchemes created')
