import math

#x = 0

#print "x\tsq\tcu"

#while (x<=150):
#	print x, "\t", x*x, "\t", x*x*x
#	x=x+1


def first(n):
	a=0
	i=1
	while (i<=n):
		a=a+(i*i*i)
		i=i+1
	return(a)

def second(n):
	a=0
	i=1
	while (i<=n):
		a=a+i
		i=i+1
	return(a*a)

s=1
while (s<=200):
	if(first(s)!=second(s)): 
		print "Bad"
		break
	else: 
		print "I checked ", s		
		s=s+1
else:
	print "All OK"

