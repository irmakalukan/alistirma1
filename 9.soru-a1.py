for i in range (1,999):
	if i<9:
		print(i)
	elif 9<i<100 and int(str(i)[0])+int(str(i)[1])<9:
		print(i)
	elif 99<i<999 and int(str(i)[0])+int(str(i)[1])+int(str(i)[2])<9:
		print(i)
