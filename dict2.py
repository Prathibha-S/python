n=int(input("Enter number of students:"))
studlist=[]
for i in range(0,n):
	stud={}
	stud['name']=input("Enter name: ")
	stud["branch"]=input("Enter branch: ")
	stud["roll no"]=int(input("Enter roll no: "))
	studlist.append(stud)
print("Name Branch Roll no")
print()
print()
for i in range(0,n):
	print(studlist[i])