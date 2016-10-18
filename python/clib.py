import ctypes

def call_c_func():
    libtest = ctypes.CDLL('./libtest.so', use_errno=True)
    a=libtest.add(ctypes.c_int(4),ctypes.c_int(3))
    print a

def test3expr(a):
    b=(a if a is not None else 'None')
    print b

if __name__=='__main__':
    call_c_func()
    test3expr(None)
    test3expr('1')
    test3expr('2')
