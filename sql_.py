import pymysql

def showall():
    try:
        db = pymysql.connect(host="localhost",
                             user='root',
                             passwd="#zomat45",
                             db="bank1")

        cur = db.cursor()
        cur.execute("select*from emp;")
        r=cur.fetchall()    
        print("Id Name Age Salary TransID")
        
        for i in r:
            print(i[0], i[1], i[2], i[3], i[4])

        cur.close()
        db.close()
    except:
        print("Error")
        
def ins():
    try:
        db = pymysql.connect(host="localhost",
                     user='root',
                     passwd="#zomat45",
                     db="bank1")
        Id = int(input("Id = "))
        name = input("Name = ")
        Age = int(input("age = "))
        Salary = int(input("Salary = "))
        TransId = int(input("TransID = "))
        d = (Id,name,Age,Salary,TransId)
        cur = db.cursor()
        sq = "insert into emp values(%s,%s,%s,%s,%s);"
        cur.execute(sq,d)
        db.commit()
        cur.close()
        db.close()
        print("Inserted")
    except:
        print("Error")

def de():
    try:
        db = pymysql.connect(host="localhost",
                             user='root',
                             passwd="#zomat45",
                             db="bank1")    
        cur = db.cursor()

        w = int(input("Enter the id you want to delete = "))
        cur.execute("delete from emp where Id=%s;",(w))
        db.commit()
        cur.close()
        db.close()
        print("Deleted")
    except:
        print("Error")
while True:
    print("**********************************")
    ch = int(input("Enter choice = "))
    if ch==1:
        showall()
    elif ch==2:
        ins()
    elif ch==3:
        de()
    elif ch==0:
        break
    else:
        print("Please enter again.")
