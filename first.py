#http://www.runoob.com/python/python-lists.html

print("你好，中文Python")

print('\n==========basic type==========')
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

print(word)
print(sentence)
print(paragraph)
#keyinput = input("\n\nPress the enter key to exit.")

testlist = ['a','ba',sentence,99]
print(testlist)
print(testlist[2])
print(testlist[1:3])
print(testlist[3:])

testdic = {'a1':'va1','a2':'va2'}
testdic['a3'] = 'va3';
testdic[3] = 'da3';
print(testdic)
print(testdic.keys())
print(testdic.values())

a = 96
print('\n========flow control============')
if a in testlist:
	print(a,'is in list "', ', '.join(map(str,testlist)),'"')
elif a == 99:
	print('this is a test')
else:
	print(a,'is NOT in list', str(testlist))
	
print('\n=========loop control===========')
flag = 0
while (flag < 10): 
	flag += 1
	if flag == 5: continue	
	print('flag is ', flag)
else:
	print('current flag is ',flag)

print('\n=======loop=============')
start = 1
end = 10
nlist = []
for num in range(start,end):	# 迭代 10 到 20 之间的数字
	j=0						# 质数标记因子
	for i in range(2,num): # 从2开始迭代
		if num%i == 0:      # 确定第一个因子
			j=num/i          # 计算第二个因子
			#print('%d 等于 %d * %d' % (num,i,j))
	if j==0:
		nlist.append(num)
print('从',start,'到',end,'的质数列表是：',nlist)

print('\n========Random============')
import random
#random.seed(6)
randNum1 = random.choice(range(1,10))
randNum2 = random.randrange(1, 10, 1)
randNum3 = random.random()
randNum4 = random.uniform(1, 10)
print('choice:',randNum1)
print('randrange:',randNum2)
print('random:',randNum3)
print('uniform:',randNum4)
print("Random number with seed 10 : ", random.choice(range(1,10)))
list = [20, 16, 10, 5];
random.shuffle(list)
print("随机排序列表 : ",  list)

print('\n========string============')
str1 = 'Hello Python\n'
str2 = 'Test'
list = ['hello','test','Python']
output1 = '{0[0]} {0[2]} {0[1]}'.format(list)
print(str1,'\nstr1[5:8]:',str1[4:8])
print(str1+' '+str2*2)
print(output1)
import string
intab = "aeiou"
outtab = "12345"
str = "this is string example....wow!!!";
trantab = str.maketrans(intab, outtab)
print(str.translate(trantab));

print('\n==========list==========')
list1 = [2, 3, 1997, 2000]
list2 = [999,888]
list3 = list1+list2*2
list4 = ['$','#','\\']
list3.append(0)
#list3.extend(list4)
print(list3)
del list3[2]
list3[2] = 2001
list3.sort()
list3.reverse()
print("After deleting value at index 2 and change the value at index 3 to 2001: ")
for x in list3: print(x)