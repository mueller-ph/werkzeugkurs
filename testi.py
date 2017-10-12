import numpy as np
import pylab as pl
import math

length = 10000000

drake=np.random.random([length,2])

index = 0
counter = 0.0

while (index<length):
    
    radius = math.sqrt(drake[index,0]**2 + drake[index,1]**2)
    #print radius
    if(radius<=1):
        counter = counter+1.0
    #print counter
    index = index+1

result = (counter/length)

print result*4




