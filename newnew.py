from cPicke import dump, load
from maintype  import MyType
obj = MyType()
obj2 = MyType()
obj2.message='Guten Tag'
obj2.hello()

f=open('myobj.pickle','wb')
dump(obj,f)
dump(obj2,f)
f.close()

