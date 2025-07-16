import mysql.connector

a=mysql.connector.connect(host='localhost',user='your_username',password='your_password')
b=a.cursor()

b.execute("create database if not exists  a9;")
b.execute("use a9;")
b.execute("create table products(sno int,prodname varchar(20),cost int);")

b.execute("insert into products values(1,'Rice',320);")
b.execute("insert into products values(2,'Candle',10);")
b.execute("insert into products values(3,'Napkin',20);")
b.execute("insert into products values(4,'Bulb',70);")


b.execute("create table out_of_stock(sno int,products varchar(20));")
b.execute("insert into out_of_stock values(1,'Pouch');")
b.execute("insert into out_of_stock values(2,'Pencil');")


b.execute("create table employee(sno int,employee_name varchar(20),salary int);")
b.execute("select * from employee;")
d=b.fetchall()

if d==[]:
    b.execute("insert into employee values(1,'Ramesh',15000);")
    b.execute("insert into employee values(2,'Suresh',14000);")
    b.execute("insert into employee values(3,'Mukesh',10320);")
    b.execute("insert into employee values(4,'Kamlesh',8000);")
    a.commit()


print("     COMPUTER SCIENCE PROJECT     ")
print("                                  ")
print("        WELCOME TO EASYNIGHT        ")
print("                                 \n\n ")

ch=input("START?\t Y/N:\t")

while ch!='N':
    print("\nPLEASE ENTER CHOICE")
    print("1 for ADMIN")
    print("2 for CUSTOMER")
    print("3 for NEITHER\n")
    
    choice=int(input("enter choice:\t"))
    
    
    if choice==3:
        print("PROGRAM ENDED")

    elif choice==1:
        
        e=input("\nenter username:\t")
        f=input("enter password:\t")
        
        if f=='1':
            
            print("\nIT'S BEEN A WHILE GOOD SIR")
            print("\npress 1 to add item")
            print("press 2 to view available items")
            print("press 3 to update any cost")
            print("press 4 to view out of stock products")
            print("press 5 to add items to out of stock")
            print("press 6 to view employee details")
            print("press 7 to update employee salary\n")

            g=int(input("enter your choice:\t"))
            
            if g==1:
                
                def additem():
                    sno=int(input("\nenter serial number:\t"))
                    prod=input("enter product name:\t")
                    cost=int(input("enter the cost:\t"))
                    h=((sno,prod,cost),)
                    b.executemany("insert into products values(%s,%s,%s)",h)
                    a.commit()
                    print("\nSUCCESSFULLY ADDED!!")
                    
                    
                additem()

            elif g==2:
                
                def viewitem():
                    b.execute("select * from products;")
                    c=b.fetchall()
                    t=(['s_no','prodname','cost'])
                    for s_no,prodname,cost in c:
                        print(s_no,":","\t",prodname,":","\t\t","cost",cost)
                viewitem()

            elif g==3:
                
                def updatecost():
                    b.execute("select * from products;")
                    c=b.fetchall()
                    for s_no,prodname,cost in c:
                        print(s_no,":","\t",prodname,":","\t\t","cost",cost)

                    s_no=input("\nenter serial number of item: ")
                    new_cost=input("enter new cost: ")
                    data=((new_cost,s_no),)
                    b.executemany("update products set cost=%s where sno=%s",data)
                    a.commit()
                    print("\nSUCCESSFULLY UPDATED!!\n")

                    b.execute("select * from products;")
                    c=b.fetchall()
                    t=(['s_no','prodname','cost'])
                    for s_no,prodname,cost in c:
                        print(s_no,":","\t",prodname,":","\t\t","cost",cost)
                updatecost()

            elif g==4:
                
                def out_of_stock():
                    b.execute("select * from out_of_stock;")
                    c=b.fetchall()
                    for s_no,product in c:
                        print(s_no,"\t\t:","\t\t",product)
                out_of_stock()

            elif g==5:
                
                def addprod():
                    b.execute("select * from out_of_stock;")
                    c=b.fetchall()
                    for s_no,product in c:
                        print(s_no,"\t\t:","\t\t",product)
                        
                    sno=input("\nenter sno: ")
                    name=input("enter name: ")
                    i=((sno,name),)
                    b.executemany("insert into out_of_stock values(%s,%s)",i)
                    a.commit()
                    print("\nADDED\n")
                    b.execute("select * from out_of_stock;")
                    c=b.fetchall()
                    for s_no,product in c:
                        print(s_no,"\t\t:","\t\t",product)
                addprod()

            elif g==6:
                def viewemployee():
                    
                    b.execute("select * from employee;")
                    c=b.fetchall()
                    for s_no,name,salary in c:
                        print(s_no,":\t",name,":\t\t","salary",salary)
                        
                viewemployee()

            elif g==7:
                def updatesalary():

                    b.execute("select * from employee;")
                    c=b.fetchall()
                    for s_no,name,salary in c:
                        print(s_no,":\t",name,":\t\t","salary",salary)
                        
                    sno=input("\nenter serial number of employee:\t")
                    new_salary=input("enter new salary:\t")
                    L3=((new_salary,sno),)
                    b.executemany("update employee set salary=%s where sno=%s;",L3)
                    a.commit()

                    b.execute("select * from employee;")
                    c=b.fetchall()
                    for s_no,name,salary in c:
                        print(s_no,":\t",name,":\t\t","salary",salary)
                    print("\nSUCCESSFULLY UPDATED")
                    
                updatesalary()

            else:
                print("WRONG INPUT DETECTED")
    
        else:
            print("WRONG PASSWORD, ACCESS DENIED")

    elif choice==2:
        name=input("\nENTER NAME: ")
        phone=int(input("ENTER PHONE NUMBER: "))
        date=input("ENTER DATE: ")
        time=input("ENTER TIME: ")

        def items():
            print("\nPRODUCTS AVAILABLE: ")
            b.execute("select * from products;")
            c=b.fetchall()
            for sno,prod,cost in c:
                print(sno,":\t",prod,":","\t\t",'cost',cost)
                    
        items()

       

        
        sum1=0
        def order(sum1):
            print("\nWhat do you wish to order?\n")
            b.execute("select * from products;")
            c=b.fetchall()

            d=int(input("ENTER DESIRED SERIAL NUMBER: "))
            quantity=int(input("ENTER QUANTITY: "))
            
            totalcost=1
            for sno,prod,cost in c:
                if sno==d:
                    sum1=sum1+(cost*quantity)
                    print(" ------------------------------------------------------")
                    print("                      BILL")
                    print(" ------------------------------------------------------")
                    print("             Name: ",name)
                    print("             Phone No: ",phone)
                    print("             Date of booking:",date)
                    print("             Time of booking:",time)
                    print("             GST included in MRP"         )
                    print("\n           Total Amount: ",sum1,"\n")
                    print("Thank You")
                    print("PLEASE VISIT AGAIN :)")
        order(sum1)   
    break
 
    
else:
    print("PROGRAM ENDED")