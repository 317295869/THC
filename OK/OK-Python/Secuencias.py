Python 3.6.8 (default, Aug 20 2019, 17:12:48) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1 = ("M", "E", 27)
>>> print(t1)
('M', 'E', 27)
>>> print(t1[0])
M
>>> print(t1[1])
E
>>> print(t1[2])
27
>>> print(t1[-1])
27
>>> for t in t1:
	print(t)
	type(t)

	
M
<class 'str'>
E
<class 'str'>
27
<class 'int'>
>>> t1 [0:1]
('M',)
>>> t1 [1:2]
('E',)
>>> L1 = ["M", "E",27]
>>> type(t1)
<class 'tuple'>
>>> type(L1)
<class 'list'>
>>> L1.append("L")
>>> L1
['M', 'E', 27, 'L']
>>> L1.remove("E")
>>> L1
['M', 27, 'L']
>>> L1.append("E")
>>> L1.append("I")
>>> L1.append("O")
>>> L1.append("U")
>>> L1
['M', 27, 'L', 'E', 'I', 'O', 'U']
>>> for L in L1:
	print(L1.count(L))

	
1
1
1
1
1
1
1
>>> 
