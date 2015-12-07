d = {'word':'garfild','count':42}
>>> 'i want %(count)d copes of %(word)s' %d
'i want 42 copes of garfild'
>>> 'i want {count} copes of {word}' .format (count = 10, word ='w')
'i want 10 copes of w'
>>> 'i want {count} copes of {word}' .format (**d)
'i want 42 copes of garfild'
>>> 




>>> for k,v in d.items():
	print (k,v)

	
o omega
g gamma
a alpha
>>> for k,v in sorted(d.items()):
	print (k,v)

	
a alpha
g gamma
o omega
>>> for k,v in sorted(d.values()):
	print (k,v)





>>> import os
>>> os.getcwd()
'/Users/Alexey/Documents'
>>> 