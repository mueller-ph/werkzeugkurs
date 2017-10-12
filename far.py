# print Fahrenheit->Celsius Tabelle
lower = 0
upper = 300
step = 20

fahr = lower
while ( fahr < upper ): 
    celsius = 5./9 * (fahr - 32) # conversion
#    print 'Fahrenheit %6.1f = Celsius %6.3f' % (fahr , celsius) # formatierte Ausgabe
    print "Fahrenheit ", fahr," = Celsius ", celsius
    fahr += step  # increment

# end of loop

