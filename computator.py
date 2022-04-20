import adams
import runge_kutta

def solve_equation(x0, y0, function, h, n):
    points = runge_kutta.runge_kutta_solve(x0, y0, function, h, n)
    result = adams.adams_method_solve(points, function, h, n)
    print("result computator: " + str(result))
    return result