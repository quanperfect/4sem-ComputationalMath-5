import adams
import runge_kutta

def solve_equation(x0, y0, function, h, n):
    n_for_runge_kutta = 4
    points = runge_kutta.runge_kutta_solve(x0, y0, function, h, n_for_runge_kutta)

    result = adams.adams_method_solve(points, function, h, n)

    return result