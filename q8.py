import math

f=open("numbers.dat")
inhalt = f.readlines()
a=len(inhalt)
b=0
max=0.0
min=0.0
while(b<a):
	inhalt[b] = float(inhalt[b])
	if (inhalt[b]>max):
		max = inhalt[b]	
	if (inhalt[b]<min):
		min = inhalt[b]	
	b=b+1
print max
print min

userin = input()

d=100
b=0
while(b<a):
	difference = abs(userin-inhalt[b])
	if (difference<d):
		d = difference
		current = b
	b=b+1

print "Stelle:\t", current
print "Wert:\t", inhalt[current]
	

