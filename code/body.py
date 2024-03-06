"""
The body types that populate the universe
"""

from stdlib.vector import Vector
from constants import G


class Body:
    """A body has the attributes of position, velocity, and mass
    """
    def __init__(self, pos, vel: Vector, mass: float) -> None:
        self._pos = pos
        self._vel: Vector = vel
        self._mass = mass

    @property
    def pos(self):
        return self._pos

    @property
    def mass(self):
        return self._mass

    def move(self, force: Vector, d_time: float) -> None:
        """move the body in universe
        """
        acc = force.scale(1 / self._mass)
        self._vel += acc.scale(d_time)
        self._pos += self._vel.scale(d_time)

    def force_from(self, other: 'Body') -> Vector:
        """gravitational attraction from another body
        """
        delta: Vector = other.pos - self._pos
        dist: float = abs(delta)
        magnitude: float = (G * self._mass * other.mass) / (dist * dist)
        print(magnitude, delta.direction().scale(magnitude))
        return delta.direction().scale(magnitude)

        # return Vector((2, 2))

    def draw(self) -> None:
        """A body draws itself to screen
        """


if __name__ == '__main__':

    sun = Body(Vector((0, 0)), Vector((0, 0)), 1000)
    earth = Body(Vector((100, 0)), Vector((-10, -10)), 10)
    print(f'0 - earth._vel={earth._vel}, earth._pos={earth._pos}')
    for step in range(10):
        earth.move(earth.force_from(sun), 0.1)
        print(f'{step + 1} - earth._vel={earth._vel}, earth._pos={earth._pos}')


