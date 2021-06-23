#l = [123,43,234,56,23,56,23,54645,324,567]
'''
### BUBBLE SORT ####
def bubble(a):
	for i in range(len(a)):
		for j in range(0,len(a)-i-1):
			if a[j]>a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]

	return a



print("Sorted list using bubble sort is = ",bubble(l))


def suml(n):
	if len(n)==0:
		return 0
	else:
		return n[0] + suml(n[1:])

l = [1,2,3]
print(suml(l)) 


def od(n):
	s = 0
	i = 1 
	while i<=n:
		s += i
		i += 2

	return s

n = int(input())
print(od(n))


def fac(x):
	if x<0:
		return -1
	elif x<2:
		return 1
	else:
		return x * fac(x-1)
n=5
print(fac(n))


def fib(n):
	f = 0
	s = 1
	print(f)
	print(s)
	for a in range(2,n):
		t = f+s
		print(t,a)
		f,s=s,t

fib(19)


def fib(n):
	if n<=1:
		return n
	else:
		return fib(n-1)+fib(n-2)

n_ = int(input())
for i in range(n_):
	print(fib(i))


def rev(n):
	if len(n)==0:
		return n

	else:
		return rev(n[1:]) + n[0]
x="rat"
print(rev(x))


def power(a,b):
	if b==0:
		return 1
	else:
		return a * power(a,b-1)
print(power(10,2))


n = int(input("enter"))
r = 0
for i in range(1,n):
	if n%i==0:
		r+=i
if r==n:
	print("yes")


### INSERTION SORT
def insertion(a):
	for i in range(1,len(a)):
		k = a[i]
		j = i-1
		print(j)
		while(j>=0 and k<a[j]):
			a[j+1] = a[j]
			j = j-1
			print(j)
		a[j+1] = k
	print(a)
l=["AAA","BBB","AAB","AAD","33D"]
insertion(l) 
'''
def LinearRecS(arr, index, value):
	if index>=len(arr):
		return "not found"     # or -1

	if arr[index]==value:
		return index	#index+1 acc. to you.

	else:
		return LinearRecS(arr,index+1,value)

arr = [1,2,2,3,2]

print("present at index = ",LinearRecS(arr,0,3))

'''
def BinarySearch(arr,key,low,high):
	if low>high:
		return False
	else:
		mid = (low+high)//2
		if key==arr[mid]:
			return True
		elif key < arr[mid]:
			return BinarySearch(arr,key,low,mid-1)
		else:
			return BinarySearch(arr,key,mid+1,high)

arr = [4,5,6,7,8]
print(BinarySearch(arr,18,0,4))


def selection(x):
	for i in range(len(x)):
		m=i
		for j in range(i+1,len(x)):
			if x[m]>x[j]:
				m=j
		x[i],x[m] = x[m],x[i]

	print(x)

arr = [32,5,23,567]
selection(arr)



def recLinearSearch(arr, l, r, x): 
    if r < l: 
        return -1
    if arr[l] == x: 
        return l 
    if arr[r] == x: 
        return r 
    return recLinearSearch(arr, l+1, r-1, x) 
    
lst = [1,2,2,3]
x = 3
res = recLinearSearch(lst, 0, len(lst)-1, x) 
 
if res != -1:
	print('{} was found at index {}.'.format(x, res))
else:
	print('{} was not found.'.format(x))

'''
