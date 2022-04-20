def adams_method_solve(points, function, h, n):
    if (len(points) < 4):
        return points

    points_result = []
    x = []
    y = []
    for i in points:
        x.append(i[0])
        y.append(i[1])

    for i in range(4, n):
        yi = y[i-1] + h/24*(55*function(x[i-1],y[i-1]) - 59*function(x[i-2],y[i-2]) + 37*function(x[i-3],y[i-3]) - 9*function(x[i-4],y[i-4]))
        xi = x[i-1] + h
        x.append(xi)
        y.append(yi)

    for i in range(len(x)):
        points_result.append([x[i],y[i]])

    return points_result