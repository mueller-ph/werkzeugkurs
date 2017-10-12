import math

A = [0.3, 1.8, -2.2]
B = [-2.5, 3.8, 0.4]

def skalar(A,B):
	return(A[0]*B[0]+A[1]*B[1]+A[2]*B[2])

print skalar(A,B)

def vektor(A,B):
	C=[0,0,0]
	C[0]=A[1]*B[2]-A[2]*B[1]
	C[1]=A[0]*B[2]-A[2]*B[0]
	C[2]=A[0]*B[1]-A[1]*B[0]
	return C

print vektor(A,B)
