# Generation Exception when division by zero using raise keyword.
from Dev1 import PinError
def divop(a,b):
    if b==0:
        raise PinError # raise keyword is used for hitting the exception.
    else:
        return a/b
    