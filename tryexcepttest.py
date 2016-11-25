#coding:utf-8
if __name__ == "__main__":
    try:
        print 'try...'
        r = 10 / 0
    except Exception, e:
        print 'except:', e
    else:
        print 'result:', r
    finally:
        print 'finally...'
    print 'END'