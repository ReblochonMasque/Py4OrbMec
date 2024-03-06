"""
vector.py
Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
"""

import math
import code.stdlib.stdio as stdio
import code.stdlib.stdarray as stdarray

# -----------------------------------------------------------------------


class Vector:

    def __init__(self, a):
        """Construct a new Vector object with numeric Cartesian coordinates
        given in array a.
        """
        self._coords = a[:]   # defensive copy to ensure immutability
        self._n = len(a)      # Dimension.

    def __getitem__(self, i):
        """Return the ith Cartesian coordinate of self.
        """
        return self._coords[i]

    def __add__(self, other):
        """Return the sum of self and Vector object other.
        """
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return Vector(result)

    def __sub__(self, other):
        """Return the difference of self and Vector object other.
        """
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] - other._coords[i]
        return Vector(result)

    def scale(self, alpha):
        """Return the product of self and numeric object alpha.
        """
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector(result)

    def dot(self, other):
        """Return the inner product of self and Vector object other.
        """
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    def __abs__(self):
        """Return the magnitude, that is, the Euclidean norm, of self.
        """
        return math.sqrt(self.dot(self))

    def direction(self):
        """Return the unit vector of self.
        """
        return self.scale(1.0 / abs(self))

    def __str__(self):
        """Return a string representation of self.
        """
        return str(self._coords)

    def __len__(self):
        """Return the dimension of self.
        """
        return self._n
        
# -----------------------------------------------------------------------


def main():
    """testing: create and use some Vector objects.
    """

    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector(xCoords)
    y = Vector(yCoords)

    stdio.writeln('x        = ' + str(x))
    stdio.writeln('y        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('10x      = ' + str(x.scale(10.0)))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# python vector.py
# x        = [1.0, 2.0, 3.0, 4.0]
# y        = [5.0, 2.0, 4.0, 1.0]
# x + y    = [6.0, 4.0, 7.0, 5.0]
# 10x      = [10.0, 20.0, 30.0, 40.0]
# |x|      = 5.477225575051661
# <x, y>   = 25.0
# |x - y|  = 5.0990195135927845



