import math

def fak(n):	
	if (n==0 or n==1): return 1	
	if (n>1):	
		n = n*fak(n-1)
	return n

print fak(500)
