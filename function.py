#计算整数的次方， x是值，n是幂

def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

	
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
	
def findMinAndMax(L=[]):
	if len(L):
		return(min(L),max(L))
	else:
		return (None,None)

#列表生成式
def listComprehension01():
	L=[]
	for x in range(1,11):
		L.append(x*x)
	return L

def listComprehension02():
	return [x*x for x in range(1,11)]