def create_basic_polynomial(points, i):
    def basic_polynomial(x):
        upperPart = 1
        dividerPart = 1
        for j in range (len(points)):
            if j != i:
                upperPart *= (x-points[j][0])
                dividerPart *= (points[i][0] - points[j][0])
        return upperPart/dividerPart
    return basic_polynomial

def create_Lagrange_polynomial(points):
    basic_polynomials = []
    for i in range (len(points)):
        basic_polynomials.append(create_basic_polynomial(points, i))

    def lagrange_polynomial(x):
        result = 0
        for i in range(len(points)):
            result += points[i][1]*basic_polynomials[i](x)
        return result
    return lagrange_polynomial