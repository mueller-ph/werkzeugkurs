import math

s = raw_input()
d = raw_input()

f=open(s)
zeilen=f.readlines()
length=len(zeilen)
f.close

f=open(d, "w")

b=0
while(b<length):
	f.write(zeilen[b])
	b=b+1
f.close

