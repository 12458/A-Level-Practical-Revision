from flask import Flask, render_template
import sqlite3

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
    
    
class AppServiceRecord(ServiceRecord):
    def getAppType(self):
        if self.AppType == 'WA':
            return 'WHATSAPP'
        elif self.AppType == 'FB':
            return 'FACEBOOK MESSENGER'
    
    def getSuccess(self):
        return 'SUCCESS' if self.isSuccess() else 'FAILED'
    
    
class SmsServiceRecord(ServiceRecord):
    def getAppType(self):
        return 'SHORT MESSAGE SERVICE'
    
    def getSuccess(self):
        return 'SUCCESS' if self.isSuccess() else 'FAILED' 

app = Flask(__name__)

@app.route('/')
def root():
    apps = []
    with sqlite3.connect('ServiceLog.db') as conn:
        cur = conn.cursor()
        logs = cur.execute('SELECT * FROM Log').fetchall()
        
    for log in logs:
        if log[4] == None:
            apps.append(SmsServiceRecord(log[1],log[2],log[3],log[4]))
        else:
            apps.append(AppServiceRecord(log[1],log[2],log[3],log[4]))
            
    return render_template('index.html', apps=apps)

app.run()