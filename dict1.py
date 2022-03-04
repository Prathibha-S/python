stud={}
n=int(input("Enter the number of students:"))
for i in range(0,n):
	a=input("Enter the name of student:")
	stud[a]=int(input("Enter the mark of the student:"))
print(stud)
b=list(stud.keys())
print(b)
b.sort()
for i in range(n):
	print(b[i],"   ",stud[b[i]])
