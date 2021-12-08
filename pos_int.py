n=int(input("Enter the limit:"))
a=[]
for i in range(0,n):
	a.insert(i,int(input("Enter the elements:")))
	print(a)
print("The positive intergers are:")
for i in range(0,n):
	if(a[i]>0):
		print(a[i])
