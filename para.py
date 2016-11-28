import inspect 

def a(a, b=0, *c, d, e=1, **f):
    pass
    
aa = inspect.signature(a)
print('aa%s'%aa)
bb = aa.parameters
print('parameters:%s'%bb)
for cc,dd in bb.items():
    print("name cc:%s, param dd:%s"%(cc,dd))
    ee = dd.kind
    print("kind ee:%s"%ee)
    gg = dd.default
    print('default gg%s'%gg)
    print('\n')
        