import math

from cPickle import dump, load

class Student(object):
	first = ""
	last = ""
	number = 0
	grade = 0.0

f=open('students.txt','r')

data = file.readlines(f)

f.close()

length = len(data)

i = 0

#while (i<length):
#	
#	newdata = data[i].split(" ")
#	Student.first = newdata[0]
#	Student.last = newdata[1]
#	Student.number = newdata[2]
#	Student.grade = newdata[3]
#
#	fy=open('save'+str(i)+'.pickle','w')
#	dump(Student(),fy)
#	fy.close()
#	i=i+1


newdata = data[0].split(" ")
Student.first = newdata[0]
Student.last = newdata[1]
Student.number = newdata[2]
Student.grade = newdata[3]

fy=open('savex.pickle','w')
dump(Student(),fy)
fy.close()
i=i+1



