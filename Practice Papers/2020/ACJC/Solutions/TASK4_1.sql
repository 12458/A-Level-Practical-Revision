CREATE TABLE Employee (Employee_ID INTEGER PRIMARY KEY, Employee_name TEXT, Job_type TEXT, Date_of_employment TEXT, Service_status TEXT);

CREATE TABLE Sales (Employee_ID INTEGER PRIMARY KEY, Total_sales INTEGER, FOREIGN KEY (Employee_ID) REFERENCES  Employee(Employee_ID));

CREATE TABLE Tech_support (Employee_ID INTEGER PRIMARY KEY, Bugs_resolved INTEGER, FOREIGN KEY (Employee_ID) REFERENCES  Employee(Employee_ID));