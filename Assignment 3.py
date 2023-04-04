import numpy as np

def div(a, b):
    try:
        if b == 0:
            return np.nan
        else:
            return a / b
    except unhandled:
        return None

def gen_array():
    a = np.arange(1, 101)
    a = a.reshape(10, 10)
    b = np.where(a % 3, a, 0)
    return b

def dot(arr1, arr2):
    if isinstance(arr1, (np.ndarray)) and isinstance(arr2, (np.ndarray)):
        if arr1.shape == (1, 9) and arr2.shape == (1, 9):
            a = arr1
            b = arr2
            a = np.array([arr1]).reshape(3, 3)
            b = arr2.reshape(3, 3)
            return np.matmul(a, b)
        else:
            raise ValueError
    else:
        raise ValueError

def mult3d(a, b):
    return np.multiply(a.T, b)

class ABM:
    def __init__(self):
        self.timestep = 0

    def step(self):
        self.timestep += 1

    def status(self):
        return 'step'


def step_model(model, steps):
    statuses = []
    for _ in range(steps):
        statuses.append(model.status())
        model.step()
    return statuses

class ABMWithStep(ABM):
    def __init__(self):
        self.timestep = 0
        
    def step(self):
        self.timestep += 1
    
    def status(self):
        return f'step {self.timestep}' 

class Tracker:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def get_position(self):
        return (self.lon, self.lat)

class FlightTracker(Tracker):
    def __init__(self, lon, lat, height):
        self.height = height
        self.lon = lon
        self.lat = lat
    
    def get_position(self):
        return (self.lon, self.lat)
    
    def get_height(self):
        return self.height

class Polygon:
    def __init__(self, *sides):
        self.sides = sides

    def compute_perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, length, width, *sides):
        self.length = length**2
        self.width = width**2
        self.sides = (2 * length, 2 * width)
        
    def perimeter(self):
        return self.sides == 18


class Square(Rectangle):
    def __init__(self, sides):
        self.sides = (sides * 2, sides * 2)

file = open("transition.py", "w")  # opening the module
text = """
import numpy as np
class TransitionMatrix:
    def __init__(self, array):
        if isinstance(array, np.ndarray):
            self.array = array
            self.probabilities = array
            if np.any(array < 0) or np.any(array > 1):
                raise ValueError
        else:
            raise TypeError
    
    def step(self):
        array = TransitionMatrix(self.array)
        array.probabilities = np.multiply(self.probabilities, self.array)
        return array
if __name__ == '_main_':
    most_frequent(filepath)
"""
with open('transition.py', 'w') as f:  # creating the module
    f.write(text)
    f.close()

def zero_crossings(readings):
    return len(np.where(np.diff(np.sign(readings)))[0])

def outer_sum(x, y):
    a = np.array(x).reshape(3, 1)
    b = np.array(y).reshape(1, 4)
    c = list(a + b)
    return c

get_ipython().system('jupyter nbconvert "Assignment 3.ipynb" --stdout --to python --PythonExporter.exclude_markdown=True | pycodestyle - --show-source --ignore=W391,W503,E402,E501')

