import sqlite3
import csv
def isPriority(s): #1m
    return 1 if s == "Priority" else 0

f=open("CUSTOMER.TXT","r")
csv_reader = csv.reader(f) #1m, strip, split
db = sqlite3.connect("bank.db") #1m
for customer in csv_reader: #1m
    sql_str= "INSERT INTO Customer (FullName, DOB, CreditCardNumber,IsPriority,SavingAmount) VALUES (?, ?, ?, ?, ?)" #1m
    db.execute(sql_str, \
              (customer[0],customer[1],customer[2],isPriority(customer[4]),customer[3]) 
              )    #2m
f.close()
db.commit() #1m
db.close() #1m
