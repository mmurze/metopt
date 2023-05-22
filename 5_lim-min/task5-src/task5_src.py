import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import math as m

import task as t
import zoutendijk as z

def taskPlot():
    x = np.arange(-1.5, 1.5, 0.01)
    y = np.arange(-1.5, 1.5, 0.01)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = 2*(xgrid**2) + ygrid**2 + np.cos(xgrid + ygrid) + 3 * xgrid + 4 * ygrid

    fig = plt.figure(figsize=(7, 4))
    ax_3d = Axes3D(fig)

    #  Создаем массив RGB цветов каждой области:
    ax_3d.plot_surface(xgrid, ygrid, zgrid, rstride=5, cstride=5, cmap=cm.jet)
    plt.show()
    return

def printResult(steps : list, f_min : float):
    iters = len(steps) - 1
    print("-= MAIN RESULT =-")
    print("iters: " + str(iters))
    print("x_min: " + str(steps[len(steps) - 1]))
    print("f(x_min) = " + str(f_min))
    
    print("-= EACH STEP RESULT =-")
    for i in range(len(steps)):
        if (i == 0):
            print("first approximation: " + str(steps[i]))
        else:
            print("iter #" + str(i) + ". x_" + str(i) + ": " + str(steps[i]))
    return

def plotSteps(steps : list):
    zet = 2
    xCoord = np.arange(-zet, zet, 0.01)
    yCoord = np.arange(-zet, zet, 0.01)
    x, y = np.meshgrid(xCoord, yCoord)
    z = x + y + 4 * np.sqrt(1 + 2 * pow(x, 2) + 3 * pow(y, 2))

    fig, ax = plt.subplots()

    fig.set_figwidth(8)     #  ширина и
    fig.set_figheight(8)    #  высота "Figure"

    xSteps = [step[0] for step in steps]
    ySteps = [step[1] for step in steps]
   
    xRest    =  np.arange(-zet, zet, 0.002)
    yRest1_1 =  np.sqrt(3 - xRest ** 2)
    yRest1_2 = -np.sqrt(3 - xRest ** 2)
    yRest2_1 =  np.sqrt(4 - xRest ** 2)
    yRest2_2 = -np.sqrt(4 - xRest ** 2)
    yRest3_1 = xRest*xRest
    # yRest    =  np.arange(-zet, zet, 0.002)
    # xRest3_1 = np.sqrt(3) + yRest - yRest
    # xRest3_2 = -np.sqrt(3) + yRest - yRest

    plt.xlim([-zet, zet])
    plt.ylim([-zet, zet])
    plt.plot(xSteps, ySteps, "bo--")
    plt.plot(xSteps[len(xSteps)-1], ySteps[len(xSteps)-1], "r*")
    # rest 1
    plt.plot(xRest, yRest1_1, "r-")
    plt.plot(xRest, yRest1_2, "r-")
    # rest 2
    plt.plot(xRest, yRest2_1, "y-")
    plt.plot(xRest, yRest2_2, "y-")
    # rest 3
    plt.plot(xRest, yRest3_1, "k-")
    # plt.plot(xRest3_1, yRest, "k-")
    # plt.plot(xRest3_2, yRest, "k-")
    cs = plt.contour(x, y, z)
    plt.clabel(cs)
    plt.show()
    return

def plotS(steps : list):
    xCoord = np.arange(-1.5, 1.5, 0.01)
    yCoord = np.arange(-1.5, 1.5, 0.01)
    x, y = np.meshgrid(xCoord, yCoord)
    z = x + y + 4 * np.sqrt(1 + 2 * pow(x, 2) + 3 * pow(y, 2))

    fig, ax = plt.subplots()

    fig.set_figwidth(8)     #  ширина и
    fig.set_figheight(8)    #  высота "Figure"

    xSteps = [step[0] for step in steps]
    ySteps = [step[1] for step in steps]
    xRest    =  np.arange(-1.5, 1.5 + 0.004, 0.002)
    yRest1_1 =  np.sqrt(3 -  xRest ** 2)
    yRest1_2 = -np.sqrt(3 -  xRest ** 2)
    yRest2_1 =  np.sqrt(4 - xRest ** 2)
    yRest2_2 = -np.sqrt(4 - xRest ** 2)
    yRest3_1 = xRest*xRest

    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.plot(xSteps[len(xSteps) - 1], ySteps[len(xSteps) - 1], "k*--")
    # rest 1
    plt.plot(xRest, yRest1_1, "r-")
    plt.plot(xRest, yRest1_2, "r-")
    # rest 2
    plt.plot(xRest, yRest2_1, "y-")
    plt.plot(xRest, yRest2_2, "y-")
    # rest 3
    plt.plot(xRest, yRest3_1, "k-")
    cs = plt.contour(x, y, z)
    plt.clabel(cs)
    plt.show()
    return

def main():
    #taskPlot()
    currentTask = t.Task()
    zoitendijkSolver = z.Zoitendijk(currentTask)
    steps = zoitendijkSolver.solver(1, 0.5, [0.0, 1.0, 0.0])
    printResult(steps, currentTask.f(steps[len(steps) - 1]))
    plotSteps(steps)
    plotS(steps)
    return
main()