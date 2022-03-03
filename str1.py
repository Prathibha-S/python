w=input('enter the string:')
a=[]
str= w.split()
for i in str:
    if i not in a:
        a.append(i)
print(a)
count=0
for i in range(len(w)):
    if(w[i]=='a'):
        count=count+1
print("The occurance of a:",count) 
