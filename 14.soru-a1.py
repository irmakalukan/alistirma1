t=[]
for i in range (1,121213):
    for k in range (1,121213):
	    if i*k==121212:
		    n=i-k
		    if n>0:
			    t.append(n)

	    if i*k==121212 and i-k==min(t):
                print(i,k)
                

