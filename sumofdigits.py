def sum(n):
	s=0
	while(n>0):
		digit=n%10
		s=s+digit
		n=n/10
	print("Sum of digits:",s)
a=int(input("Enter a number: "))
sum(a)