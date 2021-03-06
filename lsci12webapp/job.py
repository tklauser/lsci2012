from google.appengine.ext import db

class Job(db.Model):
    
    jobId = db.IntegerProperty()
    vmIp = db.StringProperty()
    paraSigma = db.FloatProperty()
    paraEA = db.FloatProperty()
    result = db.FloatProperty()
    running = db.BooleanProperty()
    finished = db.BooleanProperty()
    counter = db.IntegerProperty(required=True, default=0)
    

    def getJSON(self):
        s = {'jobId': self.jobId, 'vmIp': self.vmIp, 'paraSigma': self.paraSigma, 'paraEA': self.paraEA, 'running': self.running, 'finished': self.finished, 'result': self.result, 'counter': self.counter}
        return s
    
    def __repr__(self):
        return "jobId: "+str(self.jobId)+" vmIp: "+str(self.vmIp)+" paraSigma: "+str(self.paraSigma)+" paraEA:"+str(self.paraEA)+" running: "+str(self.running)+" finished: "+str(self.finished)+" result: "+str(self.result)+" counter: "+str(self.counter)
    
    def set(self, job):
        self.jobId = job['jobId']
        self.vmIp = job['vmIp']
        self.paraSigma = job['paraSigma']
        self.paraEA = job['paraEA']
        self.running = job['running']
        self.finished = job['finished']
        self.result = job['result']
        self.counter = job['counter']