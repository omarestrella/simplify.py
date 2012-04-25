import json
import time
import numpy as np
import matplotlib.pyplot as plot

from simplify import simplify

def run_test():
    f = open('test_data.json', 'r')
    data = json.loads(f.read())

    origx = []
    origy = []

    for point in data:
        origx.append(point['x'])
        origy.append(point['y'])

    points = simplify(data, 0.1, True)

    simpx = []
    simpy = []

    for point in points:
        simpx.append(point['x'])
        simpy.append(point['y'])

    plot.plot(data)
    plot.show()


if __name__ == '__main__':
    run_test()

