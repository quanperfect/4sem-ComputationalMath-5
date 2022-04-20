import math

#todo
def function_to_string(id):
    if id == 1:
        return "[1] y' = sinx+y"
    if id == 2:
        return "[2] y' = 2xy"

    return "function with this id does not exist"

def getFunction(id):
    def useFunction(x, y):
        if id == 1:
            return math.sin(x)+y
        if id == 2:
            return 2 * x*y

        return 0
    return useFunction

def getDiffFunction(id):
    def useFunction(x, C):
        if id == 1:
            return ((-math.sin(x)/2) - (math.cos(x)/2) + C*math.exp(x))
        if id == 2:
            return C*math.exp(x**2)

        return 0
    return useFunction

def calculateC(id, x, y):
    if id == 1:
        c = (y+(math.sin(x)/2)+(math.cos(x)/2))/math.exp(x)
        return c
    if id == 2:
        return y/math.exp(x**2)
