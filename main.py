from math import sqrt
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import json

with open('config.json', 'r') as f:
    config = json.load(f)

G = 6.67430e-11
c = 299792458
mass = config['celestial_bodies']['sagittarius_a']['mass']
t_coord = config['simulation_settings']['coordinate_time']

closer = [
    [0, 1.5e10, 0, 0], #>12.7M km
    [t_coord, 1.5e10, 0, 0]
] 

farther = [
    [0, 2.523460639e20, 0, 0], #26673 light-years
    [t_coord, 2.523460639e20, 0, 0]
]

def metric(point, mass): #how distances and times are measured at a given point in spacetime
    t, x, y, z = point
    r = sqrt(x**2 + y**2 + z**2)
    if r == 0:
        r = 0.0001
    g00 = (1 - (2 * G * mass) / (r * c**2)) * c**2 #time in meters
    result = [[g00, 0, 0, 0],
              [0, -1, 0, 0],
              [0, 0, -1, 0],
              [0, 0, 0, -1]]
    return result

def sub(a, b): 
    point3 = [0, 0, 0, 0]
    for i in range(4):
        point3[i] = a[i] - b[i]
    return point3

def dot(p1, p2):
    total = 0
    for i in range(4):
        total += p1[i] * p2[i]
    return total

def distance(p1, p2, mass): #spacetime interval between two points
    deltaX = sub(p1, p2)
    midpoint = [(a+b)/2 for a,b in zip(p1,p2)]
    metricT = metric(midpoint, mass)
    deltaX_ = matrix(deltaX, metricT)
    s2 = dot(deltaX, deltaX_)
    return s2

def matrix(point, metricT):
    result = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            result[i] += metricT[i][j] * point[j]
    return result

def time(path, mass):
    total_tau = 0
    for i in range(len(path)-1):
        s2 = distance(path[i], path[i+1], mass)
        total_tau += np.sqrt(abs(s2)) / c #convert from meters to seconds
    return total_tau

t1 = time(closer, mass)
t2 = time(farther, mass)

print(f"t1: {t1:.5f}")
print(f"t2: {t2:.5f}")

distances = []
time_dilations = []
for r in np.linspace(1.28e10, 1e11, 500):
    path = [
        [0, r, 0, 0],
        [t_coord, r, 0, 0]
    ]
    t_proper = time(path, mass)
    distances.append(r)
    time_dilations.append(t_proper)
plt.plot(distances, time_dilations)
plt.xscale('log')
plt.xlabel('Distance from Black Hole (m)')
plt.ylabel(f'Proper Time for {t_coord}s Coordinate Time (s)')
plt.title('Time Dilation Near a Supermassive Black Hole')
plt.grid(True)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f'))
plt.show()