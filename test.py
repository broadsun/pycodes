import functools



def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log("haha")
def now(*args, **kw):
    print '2013-12-25'

if __name__ == '__main__':
    ka = 530.7
    xianjin = 600-240
    #huaxiao
    huijia = 100
    huabei = 1439.71
    jiebei = 1041.37
    zhaoshang = 259.3
    guangfa = 106
    pufa = 989.5+1161.24
    zhongxin = 77.87
    zhongguo = 831
    
    all = ka+xianjin+8000
    sheng = all-huijia-jiebei-zhaoshang-guangfa-pufa-zhongxin-zhongguo
    print sheng
    print sheng-1500
