import math

#todo
def function_to_string(id):
    if id == 1:
        return "[1] y'=tgx*ctgy"
    if id == 2:
        return "[2] 2*x+4"

    return "function with this id does not exist"

def getFunction(id):
    def useFunction(x, y):
        if id == 1:
            return math.tan(x)*(1/math.tan(y))
        if id == 2:
            return 2 * x*y
        return 0
    return useFunction

def getDiffFunction(id):
    def useFunction(x, C):
        if id == 1:
            return math.acos(C*math.cos(x))
        if id == 2:
            return C*math.exp(x**2)
        return 0
    return useFunction

def calculateC(id, x, y):
    if id == 1:
        c = math.log(math.cos(y)/math.cos(x))
        return c
    if id == 2:
        return y/math.exp(x**2)