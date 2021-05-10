###PATTERNS###
'''n = 1
for i in range(4):
    print()
    for j in range(i):
        print(n,end=" ")
        n+=1
        
for j in range(4):
    print()
    for i in range(j):
        print(j,end=" ")

print("\n")

for x in range(4,0,-1):
    print()
    for y in range(x):
        print("*",end=" ")

print("\n")

n=13
for i in range(3,0,-1):
    print()
    for j in range(i):
        print(n,end=" ")   ##change to i for row.
        n-=1

print("\n")

word = "Python"
x = ""
for i in word:
    x += i
    print(x)
    
print("\n")

rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
###PATTERNS###


print('\n')

####FACTORIAL####
n=5
fact=1
while n>0:
    fact *=n
    n -=1

print(fact)
####FACTORIAL####

print('\n')

###FIBONACCI SERIES###
x = 0
y = 1
print(x,y,end=" ")
for i in range(2,19):
    t = x+y
    print(t,end=" ")
    x,y = y,t
###FIBONACCI SERIES###

print('\n')

x = 'yes'
y = 'noo'
for i in range(len(x)):
    print(x[i]+y[i],end="")

name="hello"
for ch in name:
    print(ch,'-',end=' ')

########string and int sum......
num = int(input("enter an integer = "))
word = input("enter an string =  ")
digit = ""
for i in word :
    if i.isdigit() :
        digit += i
a = int(digit)
print(num, ",", word, "->", num, "+", digit, "=", num + a)


##############################################
s = input("Enter a sentence : ")
number_of_words = 1
number_of_characters = len(s)
al_num = 0
for i in s:
    if i.isalnum():
        al_num += 1
    if i == ' ': # there is a space means there is another word 
        number_of_words += 1
print("number of words are", number_of_words)
print("number_of_characters are", number_of_characters)
print("percentage of characters that are alphanumric is", al_num*100/len(s), '%')

###############################################
a = True
while a:
    s = input("")
    if s=='q':
        a = False
    else:
        ans=""
        for i in s:
            if i.isupper():
                ans += i.lower()
            else:
                ans += i.upper()

        print(ans)


###PHONE VERIFY........###############################################

p = input("Enter Phone Number : ")
val = False
# length must be 12
if len(p) == 12 and p[3] == '-' and p[7] == '-':
    if (p[:3]+p[4:7]+p[8:]).isdigit(): # all the characters except dashes should be digits
        val = True

if val:
    print(p, 'is valid')
else:
    print(p, 'is invalid')



#######################################################

l = input().split() # input().split() returns the list
x = l[len(l)-1:] + l[:-1] # last element being added at the start with the list slice that doesn’t contain the last element
print(x)


#######################################################
liste=[]
for i in range(5):
    num=int(input("Enter a number: "))
    liste.append(num)
for i in liste:
    if i>10:
        liste[liste.index(i)]=10
print(liste)

l1 = eval(input(""))
l2 = eval(input(""))
print(l1)
print(l2)
l1[-1:] = l2
print(l1)
'''


str1 = input()
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print(str1)
