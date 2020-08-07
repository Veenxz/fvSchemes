# version 1.0
# created by Carlo Pasquinucci - carlo.a.pasquinucci@gmail.com
# relaesed under license GPL GNU 3

steady=True
secondorder=True

maxOrtho=80
maxSkew=20






nonOrthogonalCorrectors=1
if(maxOrtho)>80:
	print('Warning: mesh is not so nice. Use 3 nonOrthogonalCorrectors in fvSolution file')
	nonOrthogonalCorrectors=3
if(maxSkew)>8:
	print('Warning: mesh is not so nice')

if(maxOrtho)>80:

	gradSchemes=str('{ default cellLimited Gauss linear 0.5 ; grad(U)faceLimited Gauss linear 1.0; }')
	divSchemes=str('{ div(phi,U) Gauss linearUpwind grad(U); div(phi,omega) Gauss upwind; div(phi,k) Gauss upwind ; div((nuEff*dev(T(grad(U))))) Gauss linear ; }')
	laplacianSchemes=str('{default Gauss linear limited 0.333 ; }')
	snGradSchemes=str('{default Gauss linear limited 0.333 ; }')
	
	blending= 0.2
	nonOrthogonalCorrectors=3

if(maxOrtho)>70:

	gradSchemes=str('{ default cellLimited Gauss linear 0.5 ; grad(U)cellLimited Gauss linear 1.0; }')
	divSchemes=str('{ div(phi,U) Gauss linearUpwindgrad(U) ; div(phi,omega) Gauss linearUpwind default ; div(phi,k) Gauss linearUpwind default;div((nuEff*dev(T(grad(U))))) Gauss linear ; }')
	laplacianSchemes=str('{ default Gauss linear limited 0.5 ; }')
	snGradSchemes=str(' { default  Gauss linear limited 0.5 ; } ')
	
	blending= 0.5
	nonOrthogonalCorrectors=3

if(maxOrtho)>60:

	gradSchemes=str('{ defaultcellMDLimited Gauss linear 0.5 ; grad(U)cellMDLimited Gauss linear 0.5 }')
	divSchemes=str('{ div(phi,U) Gauss linearUpwind grad(U) ; div(phi,omega) Gauss linearUpwinddefault ; div(phi,k) Gauss linearUpwinddefault ; div((nuEff*dev(T(grad(U))))) Gauss linear ; }')
	laplacianSchemes=str('{ default Gauss linear limited 0.777 ; } ')
	snGradSchemes=str('{ default Gauss linear limited 0.777 ; } ')
	
	blending= 0.7
	nonOrthogonalCorrectors=2
	
	
if(maxOrtho)>0:

	gradSchemes=str('{ defaultcellMDLimited Gauss linear 0 ; grad(U)cellMDLimited Gauss linear 0.333 }')
	divSchemes=str('{ div(phi,U) Gauss linearUpwind grad(U) ; div(phi,omega) Gauss linearUpwinddefault;div(phi,k) Gauss linearUpwinddefault;div((nuEff*dev(T(grad(U))))) Gauss linear; }')
	laplacianSchemes=str(' { default Gauss linear limited 0.95 ; }')
	snGradSchemes=str(' { default Gauss linear limited 0.95 ; }')
	blending= 0.8
	nonOrthogonalCorrectors=1
	
	
	
	
if (steady):

	ddtSchemes=str('{default steadyState;}')
else:
	ddtSchemes=str('{default CrankNicolson '+blending+' ;}')
	
	
#open fvSchemes and write inside

f = open("fvSchemes", "w")

f.write("gradSchemes"+"\n")
f.write(gradSchemes+"\n")
f.write("\n")
f.write("divSchemes"+"\n")
f.write(divSchemes+"\n")
f.write("\n")
f.write("laplacianSchemes"+"\n")
f.write(laplacianSchemes+"\n")
f.write("\n")
f.write("snGradSchemes"+"\n")
f.write(snGradSchemes+"\n")
f.write("\n")
f.write("ddtSchemes"+"\n")
f.write(ddtSchemes+"\n")
f.write("\n")
f.write( "wallDist"+"\n")
f.write( "{method meshWave;}"+"\n")


f.close() 

print('File fvSchemes created')
