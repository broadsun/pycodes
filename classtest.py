#coding:utf-8
from types import MethodType
class person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

class bigpersin(person):
    def __init__(self, name, sex): 
        super(bigpersin, self).__init__(name, sex)
        self.__kk = {}
    def __getitem__(self, key):
        return self.__kk.get(key)
    def __setitem__(self, key, value):
        #self.__kk[key] = value
        self.__kk.setdefault(key, value)
    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return "name is not found"
    def __setattr__(self, name, value):
        try:
            object.__setattr__(self, name, value)
        except:
            return "error"
    def __str__(self):
        return "my name is %s, score is %d" % (self.name, self.score)
    def __call__(self, callvalue):
        return "my name isisisisi %s, score is %d, %s" % (self.name, self.score, callvalue)

    
if __name__ == '__main__':
    a = bigpersin('sgb','male')
    print a.name
    a['husband']='syc1111'
    print a['husband']
    a.score = 10
    print a("haha")