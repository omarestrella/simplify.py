import json
import time

from simplify import simplify

def run_test():
    f = open('test_data.json', 'r')
    data = json.loads(f.read())

    #print len(data)
    points = simplify(data, 0.1, True)
    #print len(points)

    print points


if __name__ == '__main__':
    run_test()

