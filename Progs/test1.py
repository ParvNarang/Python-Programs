op = input(" ENTER THE CITY CODE YOU WANT TO SEE - ")

if op == "DL":
    file1 = open("f.txt","r")
elif op == "MH":
    file1 = open("f1","r")
elif op == "TN":
    file1 = open("f1","r")
elif op == "HP":                                  ### files have to be changed ......
    file1 = open("f1","r")
elif op == "HR":
    file1 = open("f1","r")
elif op == "PB":
    file1 = open("f1","r")

else:
    print(" NO FILES IN HERE ")

text = file1.read()

#print(text[1])
#print(text)

i = input(" ENTER THE NUMBER PLATE YOU WANT TO SEE - ")           ##input to be taken through camera or image

if i in text:
    print(" YOU HAVE ENTERED - ",i)
    o = input(" DO YOU WANT TO SEE THE DETAILS ?")
    if o == "yes" or o == "YES" or o == "Yes" or o == "Y" or o == "y":
        text1 = file1.readline()
    else:
        print(" OK BYE ")

elif i == "show all":
    print(text)

else:
    print(" NOTHING LIKE THAT ")

file1.close()
