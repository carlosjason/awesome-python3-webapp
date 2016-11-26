class animal(object):
    def __init__(self,name):
        self.name = name
     
    def __str__(self):
        return 'object name is %s'%self.name

    __repr__ = __str__    
print(animal('dog'))    

a = 'hello world'
a.replace('world', 'python')
print(2)    