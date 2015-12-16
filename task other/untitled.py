def check():
	i = 200000000
	while(i):
		k = 0
		for j in range(1,21):
			if i % j == 0:
				k = k + 1
			break
		if k == 20:
			print (i)
			break
		i = i + 1
		if i > 2000000000:
			print (i)
			break


def check1():
	j = 0
	for i in range(1001):
		if i % 3 == 0 and i % 5 == 0:
			j = j + i
	print(j)
check()