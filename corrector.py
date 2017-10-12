f=open("list.txt")
inhalt=f.readlines()
str.replace(inhalt, " ", "\n")
print(inhalt)
f.close
