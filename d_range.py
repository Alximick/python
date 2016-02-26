from decimal import Decimal as D 
def d_range(start=0, end=10, step=0.1):
	start = D(start)
	end = D(end)
	step = D(step)
	number = start
	lst = []
	lst.append(float(start.quantize(D('1.0000'))))
	while True:
		number += step
		lst.append(float(number.quantize(D('1.0000'))))
		if number > (end - step):
			break
	return lst

print(d_range(start=0.01, end=0.03, step=0.0001))
