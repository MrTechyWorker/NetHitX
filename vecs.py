# vecs.py

import math
from sympy import Matrix, symbols, Eq, solve # type: ignore

class Vector:
    def __init__(self, i: float, j: float, k: float):
        self.i = i
        self.j = j
        self.k = k
        self.magnitude = math.sqrt(i**2 + j**2 + k**2)
        self.vector = [i, j, k]

    def __repr__(self) -> str:
        return f"[{self.i}, {self.j}, {self.k}]"

    def unit_vector(self) -> list[float]:
        return [self.i / self.magnitude, self.j / self.magnitude, self.k / self.magnitude]

    def dot_product(self, b: 'Vector') -> float:
        return self.i * b.i + self.j * b.j + self.k * b.k

    def cross_product(self, b: 'Vector') -> 'Vector':
        x = self.j * b.k - self.k * b.j
        y = self.k * b.i - self.i * b.k
        z = self.i * b.j - self.j * b.i
        return Vector(x, y, z)

    def __add__(self, b: 'Vector') -> 'Vector':
        return Vector(self.i + b.i, self.j + b.j, self.k + b.k)

    def __sub__(self, b: 'Vector') -> 'Vector':
        return Vector(self.i - b.i, self.j - b.j, self.k - b.k)


class Line:
    def __init__(self, pt: Vector, d: Vector, c: str = "s"):
        self.point = pt
        self.dir_vector = d
        self.constant = c

    def __repr__(self) -> str:
        return f"{self.point} + {self.constant} {self.dir_vector}"

    def min_distance(self, b: 'Line') -> float:
        u = self.dir_vector.cross_product(b.dir_vector)
        return abs((b.point - self.point).dot_product(u) / u.magnitude)


def point_in_line(pt: list[float], line: Line) -> bool:
    x, y, z = pt
    var1 = (x - line.point.i) / line.dir_vector.i
    var2 = (y - line.point.j) / line.dir_vector.j
    var3 = (z - line.point.k) / line.dir_vector.k
    return var1 == var2 == var3


def line_with_points(pt1: list[float], pt2: list[float]) -> Line:
    x, y, z = pt1
    a, b, c = pt2
    return Line(Vector(x, y, z), Vector(a - x, b - y, c - z))


def angle_between_vectors(v1: Vector, v2: Vector) -> tuple[float, float]:
    dot = v1.dot_product(v2)
    magp = v1.magnitude * v2.magnitude
    rad = math.acos(dot / magp)
    return rad * 180 / math.pi, rad


def point_of_intersection(line1: Line, line2: Line) -> list[float]:
    a1 = Matrix([line1.point.i, line1.point.j, line1.point.k])
    b1 = Matrix([line1.dir_vector.i, line1.dir_vector.j, line1.dir_vector.k])

    a2 = Matrix([line2.point.i, line2.point.j, line2.point.k])
    b2 = Matrix([line2.dir_vector.i, line2.dir_vector.j, line2.dir_vector.k])

    t, s = symbols('t s')

    r1 = a1 + t * b1
    r2 = a2 + s * b2

    equations = [Eq(r1[i], r2[i]) for i in range(3)]

    solution = solve(equations, (t, s))

    if solution:
        intersection_point = r1.subs(t, solution[t])
        return list(intersection_point)
    else:
        return []
    

class Plane_with_points:
    def __init__(self,p1: Vector ,p2: Vector,p3: Vector) -> None:
        self.p = p1
        self.dir1 = p2 - p1
        self.dir2 = p3 - p2
        self.eq = self.dir1.cross_product(self.dir2)
        self.sol = self.eq.dot_product(self.p)

    def __repr__(self) -> str:
        return f"{self.p} + s{self.dir1} + t{self.dir2}"
    
class Plane_alg:
    def __init__(self,x,y,z,sol) -> None:
        self.eq = Vector(x,y,z)
        self.sol = sol


def line_intersect_plane(plane, line : Line):
    try: 
        d1 = (line.dir_vector.i * plane.eq.i) + (line.dir_vector.k * plane.eq.k) + (line.dir_vector.j * plane.eq.j)
        s = plane.sol - (plane.eq.i*line.point.i) - (plane.eq.k*line.point.k) - (plane.eq.j*line.point.j)

        return f"{s/d1*line.dir_vector.i + line.point.i , s/d1*line.dir_vector.j + line.point.j , s/d1*line.dir_vector.k + line.point.k}"
    except ZeroDivisionError:
        return "Line doesn't intersect [Parallel or Skew]"
    