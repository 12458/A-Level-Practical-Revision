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