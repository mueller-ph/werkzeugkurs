import json
f=open('wlcg.json')
a=json.load(f)
capacity = 0

for row in a:
	if(row["Country"]=="Germany" and row["PledgeType"]=="Disk" and row["ATLAS"]!=""):
		capacity = capacity + int(row["ATLAS"])
		print "Capacity:\t", row["ATLAS"]

print "Total capacity:\t", capacity
