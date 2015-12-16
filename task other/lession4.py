import re
match = re.search('ooo', 'red poooo')
match1 = re.search('ooo', 'red poooo')
print 

Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> 
>>> imort re
SyntaxError: invalid syntax
>>> import re
>>> 
>>> 
>>> 
>>> def find(pat,text):
	match = re.search(pat, text)
	if match:
		print (match.group())
	else:
		print ('Not Found')

		
>>> find('ooo','red mooon')
ooo
>>> find('ooo','red mooo222n')
ooo
>>> 
>>> find('ooo','red mo1oo222n')
Not Found
>>> find('m..n','red mo1oo222n')
Not Found
>>> find('m..n','red moon')
moon
>>> find('m..n','red mooN')
Not Found
>>> find('mean.','red mooN.')
Not Found
>>> find('mean.','red mooN mean.')
mean.
>>> find('\.','red mooN mean.')
.
>>> find(r,'\.','red mooN mean.')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    find(r,'\.','red mooN mean.')
NameError: name 'r' is not defined
>>> find(r'\.','red mooN mean.')
.
>>> find(r':\w\w\w','redd mooN mean cat dfsd sdf sdg.')
Not Found
>>> find(r':\w\w\w','redd mooN me:an cat dfsd sdf sdg.')
Not Found
>>> find(r':\w\w\w','redd mooN me:an :cat dfsd sdf sdg.')
:cat
>>> find(r'\d','redd mooN me:an :cat dfsd sdf sdg0.')
0
>>> find(r':\w+\d','redd mooN me:an :cat0 dfsdsdfsdg0.')
:cat0
>>> find(r':\w+\d+','redd mooN me:an :cat0432 dfsdsdfsdg0.')
:cat0432
>>> find(r':\w+\d+',':ывавыа .')
Not Found
>>> find(r':\w+\d+',':ывавыа424 .')
:ывавыа424
>>> find(r':\w+\d+',':ывавыа424 .')
:ывавыа424
>>> def find_mail(pat,text):
	match = re.search(pat, text)
	if match:
		print (match.group())
	else:
		print ('Not Found')

		
>>> find(r'\S+@\S+\.\S+','mail@mail.ru')
mail@mail.ru
>>> def find_mail(pat,text):
	match = re.findall(pat, text)
	if match:
		print (match.group())
	else:
		print ('Not Found')

		
>>> find(r'\S+@\S+\.\S+','mail@mail.ru safdas@fd.dsf dsfsd @.fsd')
mail@mail.ru
>>> find_mail(r'\S+@\S+\.\S+','mail@mail.ru safdas@fd.dsf dsfsd @.fsd')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    find_mail(r'\S+@\S+\.\S+','mail@mail.ru safdas@fd.dsf dsfsd @.fsd')
  File "<pyshell#41>", line 4, in find_mail
    print (match.group())
AttributeError: 'list' object has no attribute 'group'
>>> m = re.findall(u'(\S+)@(\S+\.\S+)',u'mail@mail.ru sfdsf@mail.ru')
>>> m
[('mail', 'mail.ru'), ('sfdsf', 'mail.ru')]
>>> m.group(2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    m.group(2)
AttributeError: 'list' object has no attribute 'group'
>>> m.group(1)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    m.group(1)
AttributeError: 'list' object has no attribute 'group'
>>> m = re.searcj(u'(\S+)@(\S+\.\S+)',u'mail@mail.ru sfdsf@mail.ru')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    m = re.searcj(u'(\S+)@(\S+\.\S+)',u'mail@mail.ru sfdsf@mail.ru')
AttributeError: module 're' has no attribute 'searcj'
>>> m = re.search(u'(\S+)@(\S+\.\S+)',u'mail@mail.ru sfdsf@mail.ru')
>>> m
<_sre.SRE_Match object; span=(0, 12), match='mail@mail.ru'>
>>> m.group(1)
'mail'
>>> m.group(2)
'mail.ru'
>>> tempdictman = re.search(u '<td>\w+</td>' , u '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
SyntaxError: invalid syntax
>>> re.search(u '<td>\w+</td>' , u '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
SyntaxError: invalid syntax
>>> re.search(r '<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
SyntaxError: invalid syntax
>>> find(r '<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
SyntaxError: invalid syntax
>>> find
<function find at 0x105657620>
>>> find (r 'a','aa')
SyntaxError: invalid syntax
>>> find ('a','aa')
a
>>> find('<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
<td>1</td>
>>> find(r'<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
<td>1</td>
>>> findall(r'<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    findall(r'<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
NameError: name 'findall' is not defined
>>> re.findall(r'<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
['<td>1</td>', '<td>Michael</td>', '<td>Jessica</td>']
>>> m = re.findall(r'<td>\w+</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
>>> m
['<td>1</td>', '<td>Michael</td>', '<td>Jessica</td>']
>>> m[1]
'<td>Michael</td>'
>>> tempdictman = {}
>>> tempdictman[m[1]] = m[0]
>>> tempdictman
{'<td>Michael</td>': '<td>1</td>'}
>>> tempdictman.value
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    tempdictman.value
AttributeError: 'dict' object has no attribute 'value'
>>> tempdictman.value()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    tempdictman.value()
AttributeError: 'dict' object has no attribute 'value'
>>> tempdictman.items()
dict_items([('<td>Michael</td>', '<td>1</td>')])
>>> for k,v in tempdictman.items():
	print k,c
	
SyntaxError: Missing parentheses in call to 'print'
>>> for k,v in tempdictman.items():
	print k,v
	
SyntaxError: Missing parentheses in call to 'print'
>>> for k,v in tempdictman.items():
	print (k,v)

	
<td>Michael</td> <td>1</td>
>>> m = re.findall(r'<td>(\w+)</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
>>> m
['1', 'Michael', 'Jessica']
>>> tempdictman[m[1]] = m[0]
>>> for k,v in tempdictman.items():
	print (k,v)

	
Michael 1
<td>Michael</td> <td>1</td>
>>> m = re.findall(r'<td>(\w+)</td>','<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>')
>>> m[0]
'1'
>>> m
['1', 'Michael', 'Jessica']
>>> 