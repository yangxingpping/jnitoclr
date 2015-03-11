class demo(object):
    def Hello(self,str):
        print('hello, %s' %str)
    def __init__(self):
        self.Mapx = {'Hello':demo.Hello}
        
    
    def call(self):
        self.Mapx['Hello'](self, 'alqaz')
       

cdd = demo()
cdd.call()