def palindro(n):
    for n in range (100,10000):
		if 99<n<1000 and str(n)[0]==str(n)[2]:
                    print(n)
                    return True
		elif 999<n<10000 and str(n)[0]==str(n)[3]:
			print(n)
			return True
