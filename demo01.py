#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''01 input
name=input('Please input your name:')
print('Hello ',name)
'''

'''02 storage
a = 'abc'
b = a
a = 'c'
print(b)
'''

'''03 unicode
print(ord('黄'),ord('友'),ord('文'))
print(chr(40644),chr(21451),chr(25991))
'''

'''04 bytes transfer to str
print(b'ABC'.decode())
'''

'''05 format
print ('Name:%s \nage:%d' %('william',24))
'''
'''
y1=72
y2=85
rate=((85/72)-1)*100
print ('Hello,{0} {1:.2f}%'.format('william',rate) )
print ('Hello,{0} {1:.3f}%'.format('william',rate) )
'''

'''06 list
classmate=['William','Cathy','Evan','Shirely']
print(classmate)
print('list length:', len(classmate))
#add new element to list
classmate.append('Hun')
print ('Add new classmate:', classmate[len(classmate)-1])
print(classmate)
#remove last element in the list
print ("remove last element:" , classmate.pop())
print (classmate)
#remove specified element in the list (remove secondary element)
print ("remove second element:", classmate.pop(1))
print (classmate)
#replace some element
classmate[2]='Smile'
print(classmate)
#tuple type
classmate.append(['Hun','Elcho'])
print(classmate)
#exercise for list
listP=[
	['Apple','Google','Microsoft'],
	['Java','Python','Ruby','PHP'],
	['Adam','Bart','Lisa'],
]
#print 'Apple'
print(listP[0][0])
#print Python
print(listP[1][1])
#print Lisa
print (listP[2][2])
'''

'''07 if
height=1.75
weight=80.5
bmi=int(weight/(height**2))
print(bmi)
if bmi<18.5:
	print("过轻")
elif 18.5<bmi<25:
	print("正常")
elif 25<bmi<28:
	print("过重")
elif 28<bmi<32:
	print("肥胖")
else :
	print("严重费胖")
'''

'''08 while
names=['william','evan','cathy']
print(names)
for name in names:
	print(name)
#计算0~100的整数之后
sum=0
for x in range(101):
	sum+=x
print("0~100 之和:",sum)
#打印奇数
n=0
while n<10:
	n=n+1
	if n%2 ==0:
		continue
	print(n)
'''

'''09 set & dict
#dict
d={'william':24,'cathy':23,'Evan':23}
if d.get('william'):  #判断这个key在字典里是否存在
	print("The person's age is :",d['william'])
#set
s1=set([1,1,2,3])
s2=set([2,3,5,6])
print("s1:",s1)
print("s2:",s2)
s2.remove(3)
print("After remove 3:",s2)
#交集
print("交集:",s1&s2)
#并集
print("并集:",s1|s2)
'''

'''10 basic function & define function use 'def'
#将整数转成十六进制hex(), a是hex()的一个别名
a=hex
print(a(255))
print(a(1000))
'''

'''11 import api
import function
print(function.power(2,10))
#递归函数
print(function.fact(15))
'''

import function
print("complex function:",function.listComprehension01())
print("easy function:",function.listComprehension02())







































