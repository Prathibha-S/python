n=int(input("Enter the limit:"))
a=[]
for i in range(0,n):
	a.insert(i,int(input("Enter the elements:")))
	print(a)
sq=[]
print("The square of the numbers are:")
for i in range(0,n):
	a[i]=a[i]*a[i]
	sq.append(a[i])
	i=i+1
	print(sq)