import mysql.connector as sqltor
from datetime import datetime
import sys
from tabulate import tabulate
mycon = sqltor.connect(host='localhost', user='root', passwd='hellojv')

if mycon.is_connected():
    print("Connected Successfully")
else:
    print("Error")

cur = mycon.cursor()

# Creating database
cur.execute("CREATE DATABASE IF NOT EXISTS PS")
cur.execute("USE PS")

# Creating a table
cur.execute("CREATE TABLE IF NOT EXISTS Criminal_Record (Criminal_Id INT  PRIMARY KEY, Criminal_Name VARCHAR(50) NOT NULL, DOB DATE NOT NULL, Address VARCHAR(50), Locality VARCHAR(20), Crime VARCHAR(20) NOT NULL, Imprisonment VARCHAR(5))")
s1="insert into Criminal_Record(Criminal_Id,Criminal_Name,DOB,Address,Locality,Crime,Imprisonment) values(%s,%s,%s,%s,%s,%s,%s)"
val=[(1,"Rajesh Yadav","1999-05-09","Delhi","Firozabad","Ragging","Yes"),
     (2,"Jagdish punia","2000-05-12","Varanasi","Koirajpur","Ragging","No"),
     (3,"Vinod Kumar","1992-11-09","Bhadohi","Suriyawa","Murder","Yes"),
     (4,"Arsal Jamshed","1988-09-10","Varanasi","Shivpur","Thievery","No"),
     (5,"Seema Raj","1986-02-23","Varanasi","Babatpur","Thievery","Yes"),
     (6,"Ujjwal Sehgal","1994-01-29","Delhi","Gurgaon","Cyber Crime","Yes"),
     (7,"Usha Singh","1989-06-02","Jaunpur","Madhiyau","Burglary","No"),
     (8,"Faiz Ullah","1997-11-21","Varanasi","Harhua","Rape","Yes"),
     (9,"Jagdeep Kumar","1981-11-04","Varanasi","Godowlia","Domestic Abuse","No"),
     (10,"Surya Yadav","1995-11-23","Delhi","Seemapuri","Molestation","Yes")]
#cur.executemany(s1,val)
#mycon.commit()
ps=input("Enter the password")
if ps=="11223344":
    print("Welcome")
    while True:

     def see():
        cur.execute("SELECT * FROM Criminal_Record")
        data = cur.fetchall()
        print(data)

     def add():
        crno=int(input("Enter the Criminal's Id"))
        crna = input("Enter the Criminal name")
        dob = input("Enter Date of Birth")
        add = input("Enter address")
        loc=input("Enter the Locality")
        cri = input("Enter the Crime")
        imp=input("Is the criminal currently imprisoned(Yes/No)")
        query = "INSERT INTO Criminal_Record(Criminal_Id,Criminal_Name,DOB,Address,Locality,Crime,Imprisonment)VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(crno,crna,dob,add,loc,cri,imp)
        cur.execute(query,values)
        mycon.commit()
        print("Record added successfully")

     def delete(cr):
        delq = "DELETE FROM Criminal_Record WHERE Criminal_Id = %s;"
        cur.execute(delq, (cr,))
        mycon.commit()
        print("Record deleted successfully.")

     def update(cri, new):
        updq = "UPDATE Criminal_Record SET Imprisonment = %s WHERE Criminal_Id = %s;"
        cur.execute(updq, (new, cri))
        mycon.commit()
        print("Record updated successfully.")
     def search():
        print("Press 1 to search by name")
        print("Press 2 to search by Criminal Id")
        print("Press 3 to search by Crime")
        choice=input("Enter your choice")
        if choice=="1":
            nam=input("Enter the criminal's name")
            q="SELECT * FROM Criminal_Record WHERE Criminal_Name='%s'"%nam
            cur.execute(q)
            row=cur.fetchall()
            print(tabulate(row,headers=('Criminal_Id','Criminal_Name','DOB','Address','Locality','Crime','Imprisonment')))
        elif choice=="2":
            crd=int(input("Enter the criminal's id"))
            q="SELECT * FROM Criminal_Record WHERE Criminal_Id=%s"%crd
            cur.execute(q)
            row=cur.fetchall()
            print(tabulate(row,headers=('Criminal_Id','Criminal_Name','DOB','Address','Locality','Crime','Imprisonment')))
        elif choice=="3":
            crime=input("Enter the criminal's crime")
            q="SELECT * FROM Criminal_Record WHERE Crime='%s'"%crime
            cur.execute(q)
            row=cur.fetchall()
            print(tabulate(row,headers=('Criminal_Id','Criminal_Name','DOB','Address','Locality','Crime','Imprisonment')))
        else:
            print("Invalid Choice")
        

     print("Press 1 to see criminal record")
     print("Press 2 to add criminal record")
     print("Press 3 to delete criminal record")
     print("Press 4 to update criminal's imprisonment record")
     print("Press 5 to search any record")
     print("Press 6 to exit")
     
     ch = input("Enter your choice")

     if ch == "1":
        see()
     elif ch == "2":
        add()
     elif ch == "3":
        cr = input("Enter the Criminal Id to delete the record")
        delete(cr)
     elif ch == "4":
        cri = input("Enter the Criminal Id to update the record")
        new = input("Is the criminal currently imprisoned? (Yes/No)")
        update(cri, new)
     elif ch=="5":
        search()
     elif ch == "6":
        print("Thank You")
        break
     else:
        print("Invalid Choice")
else:
    print("Invalid password")
