'''L=[]

def c():
	for i in range(0,5):
		u = input("Enter sentence -")
		L.append(u)

	count = 0
	for j in range(0,5):
		if L[j][0:3]=="the":
			count += 1

	return count
print("Count = ",c())


def sumSquares(n):
    #assert n >= 0
    if (n == 0):
        return 0
    else:
        return sumSquares(n-1)+ n*n

print(sumSquares(10))


def j(o):
	s = ""
	i = ""
	for ch in o:
		if ch.isupper():
			i = ch.lower()
			s+=i
		elif ch.islower():
			i = ch.upper()
			s+=i

		elif ch.isdigit():
			i = "$"
			s+=i
		elif ch==" ":
			i = "#"
			s+=i
		else:
			i = "*"
			s+=i
	return s

f = "Hello 12"
print(j(f))
'''

L=[]
for i in range(0,4):
	u = input("enter")
	L.append(u)

f = {}
for item in L:
   if item in f:
      f[item] += 1
   else:
      f[item] = 1

print("Element Frequency")
for key, value in f.items():
   print(key,'    ',value)
