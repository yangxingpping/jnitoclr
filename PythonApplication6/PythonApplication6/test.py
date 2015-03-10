class Abc(object):
    def __init__(self):
        self.objMap = {'AddOne':Abc.AddOne}
    def AddOne(self, k,v):
        self.objMap[k] = v
    def Call(self):
        print(self.objMap['AddOne'])
        self.objMap['AddOne'](self, 'yang', 'alqaz')
        #self.AddOne('alqaz','yang')

dd = Abc()
dd.Call()
pass;