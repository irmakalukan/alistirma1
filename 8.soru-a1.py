n=0
a=0
b=0
d=0
for i in range (100,1000,2):
    if str(i)[0]==str(i)[1]:
	    n=n+1
    elif str(i)[0]==str(i)[2]:
	    a=a+1
    elif str(i)[1]==str(i)[2]:
	    b=b+1
    elif str(i)[0]==str(i)[2]==str(i)[1]:
	    d=d+1


print(a+b+n-2*d)
