class ServiceRecord:
    def __init__(self, sender, access_date, status, app_type):
        self.Sender = sender # str
        self.AccessDate = access_date # str
        self.Status = status # int
        self.AppType = app_type # str
    
    def isSuccess(self):
        return self.Status == 200
    
    def getAppType(self):
        return self.AppType
"""
LOG.txt
---
54.36.149.41 22/Jan/2021 200 WA
188.226.164.216 22/Jan/2021 0 FB
92783423 22/Jan/2021 200
188.226.164.216 23/Jan/2021 0 FB
88188293 23/Jan/2021 0
"""
logs_raw = []
logs = []

with open('LOG.txt') as f:
    for line in f:
        logs_raw.append(line.strip().split(' '))

for log in logs_raw:
    if len(log) == 3:
        # phone
        logs.append(ServiceRecord(log[0],log[1],int(log[2]),None))
    elif len(log) == 4:
        # ip
        logs.append(ServiceRecord(log[0],log[1],int(log[2]),log[3]))

import sqlite3
with sqlite3.connect('ServiceLog.db') as conn:
    cur = conn.cursor()
    for record in logs:
        cur.execute('INSERT INTO Log(Sender,AccessDate,Status,AppType) VALUES (?,?,?,?)', (record.Sender, record.AccessDate, record.Status, record.AppType))
    conn.commit()

