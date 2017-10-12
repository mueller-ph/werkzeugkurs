from cPickle import dump, load

i=0

class Student(object):
	first = ""
	last = ""
	number = 0
	grade = 0.0

#while (i<6):
#	f=open('save'+str(i)+'.pickle','rb')
#	
#	data = load(f)
#
#	f.close()
#
#	print data.first
#	print data.last
#	print data.number
#	print data.grade
#	
#	i=i+1

f=open('save.pickle','r')

data = load(f)

f.close()

print data.last


