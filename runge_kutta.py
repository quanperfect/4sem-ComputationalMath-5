def runge_kutta_solve(x0, y0, function, h, n):
    points = [[x0, y0]]
    x_current = x0
    y_current = y0

    for i in range(1, n):
        k1 = function(x_current, y_current)
        k2 = function(x_current + h/2, y_current + h*k1/2)
        k3 = function(x_current + h/2, y_current + h*k2/2)
        k4 = function(x_current + h, y_current + h*k3)

        dyi = (k1 + 2*k2 + 2*k3 + k4)*h/6
        x_current += h
        y_current += dyi
        points.append([x_current, y_current])

    return points