import matplotlib.pyplot as plt
import numpy as np
import lagrange
import functions

def scan_x_for_minmax(points):
    max = points[0][0]
    min = points[0][1]

    for i in points:
        if i[0] > max:
            max = i[0]
        if i[0] < min:
            min = i[0]

    return [min, max]

def plot(equationId, points, isAnalyticalGraphNeeded):
    plt.title("Adams method differential equation solver")
    minmax = scan_x_for_minmax(points)
    min = minmax[0]
    max = minmax[1]

    lagrange_polynom = lagrange.create_Lagrange_polynomial(points)

    x = np.linspace(min, max, 100)
    y = []

    for i in x:
        y.append(lagrange_polynom(i))

    plt.plot(x, y, color='red', zorder=2, label='polynom', linewidth=2)

    if (equationId >= 1 and equationId <= 2 and isAnalyticalGraphNeeded):
        idfunction_x_points = x
        idfunction_y_points = []
        C = functions.calculateC(equationId, points[0][0], points[0][1])
        diffFunction = functions.getDiffFunction(equationId)

        for i in idfunction_x_points:
            idfunction_y_points.append(diffFunction(i, C))

        label = "function (id = " + str(equationId) + ")"
        plt.plot(idfunction_x_points, idfunction_y_points, '--', color='green', zorder=4, label=label)

    x_points = []
    y_points = []
    plt.scatter(points[0][0],points[0][1],color='purple',zorder=5,label='init point')
    for i in range(1, len(points)):
        x_points.append(points[i][0])
        y_points.append(points[i][1])
    plt.scatter(x_points, y_points, color='blue',zorder=3,label='points')
    plt.legend(loc='lower right')
    plt.show()