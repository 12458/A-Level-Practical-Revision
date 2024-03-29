"""
File preview
---

Allsun Cappleman,1963-06-29,4175009817473152,8936.03,Customer
Jermayne Braisby,1961-06-20,3531754321948279,41792.88,Priority
Mattheus Dinkin,1982-10-30,3556580019174237,7041.14,Customer
Carmelle Rosenblath,1983-10-14,3533972425269883,264049.44,Priority
Juan Elner,1967-03-14,3544495006743149,62696.98,Priority
Daren Wakeley,1983-04-09,3533901900098889,4135.27,Customer
Corliss Grangier,1962-02-12,5602253667050112,6188.84,Customer
Pamella Bristowe,1996-10-20,5020623004063248,125741.51,Priority
Gavrielle Handford,1975-04-02,56022434361306829,7985.11,Customer
Stacy Roja,1968-05-15,6334035014482772,100821.84,Priority
Petra Temlett,1993-06-09,3578003816253611,62169.49,Priority
Matilda Bader,1993-03-24,5602231117615015,4981.12,Customer
Alidia Grigoriscu,1984-04-29,3577913698719516,8227.70,Customer
Trev Bestwick,1983-11-06,4913539840971282,347195.08,Priority
Jaquenette Miner,1973-01-08,4405664645911377,238585.21,Priority
Carry Tardiff,1978-04-01,3579145692476664,57026.87,Priority
Ronnica Mapstone,1985-06-03,3530315371787677,100686.24,Priority
Abe Rickerd,1996-12-09,560224897399781832,8879.34,Customer
Whitaker Brandel,1970-01-06,5120582070101085,9575.85,Customer
Osgood Orritt,1965-11-29,3560767720993500,81719.29,Priority
"""


with open('CUSTOMER.TXT') as f:
    import csv
    c = csv.reader(f)
    customers = list(c)

import sqlite3

with sqlite3.connect('bank.db') as conn:
    cur = conn.cursor()
    sql = \
    """
    INSERT INTO Customer(FullName, DateOfBirth, CreditCardNumber, IsPriority, SavingsAmount)
    VALUES (?,?,?,?,?)
    """
    for customer in customers:
        priority = 0
        if customer[4] == 'Priority':
            priority = 1
        cur.execute(sql, (customer[0],customer[1],customer[2],priority,float(customer[3])))
    conn.commit()

    ## [9]
    