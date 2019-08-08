import time
import pickle

class TimedSet():
    
    def __init__(self):
        self.d = {}
        self.timeout = {}
    
    def set_key(self, key, value, timeout=None):
        if timeout is None:
            self.d[key] = value
            self.timeout[key]=0
        else:
            self.d[key] = value
            # Storing timeout wrt keys
            self.timeout[key] = time.time() + timeout 

    def get_key(self,key):

        if key in self.d.keys() and  self.timeout[key] > time.time():
            print(self.d[key])
        else:
            print('nil') 
 
    def flush(self):
        print('Flushing Done')
        self.d={}


    def save(self):
        f=open('data.dat','w')
        pickle.dump(f,self.d)
        print('Saved to data.dat')
        f.close()
        

    def load(self):
        f=open('data.dat','r')
        self.d=f.read()
        print('Loading Done')
        f.close()




