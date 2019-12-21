import numpy as pk
A=pk.array(input("enter the array:"))
B=pk.array(input("enter the array2:"))
g=pk.linalg.matrix_rank(A)
print "\nRank of matrix A:\n",g
L=(A.transpose())
print "\nTranspose of L:\n",L
W=pk.linalg.eig(B)
print "\n eigen values of L:\n",W
print "\nTrace of A:\n",pk.trace(A)
print "\nDeterminant of matrix A:\n",pk.linalg.det(A)
print "\nInverse of A:\n",pk.linalg.inv(A)
print "\nmin of matrix A:\n",pk.min(A)
print "\nmax of matrix A:\n",pk.max(A)
print "\nsquare of matrix A:\n",pk.square(B)
C=A+B
D=A-B
E=A*B
F=A/B
print "\nAddition of matrixes A and B\n",C	
print "\nSubtraction of matrixes A and B\n",D
print "\nMultiplcation of matrixes A and B\n",E
print "\nDivision of matrixes A and B\n",F


