# Derek Balmer
# ETGG1803-02
# 2-28-19

from vectorcalc import *


class Vector(object):
    """This is a general vector class."""

    def __init__(self, *args):        # args allows the function to take as many arguments of any type, * means optional
        """
        Creates a Vector of any length
        :param args: allows any number of inputs
        """
        self.data = []
        for i in args:
            self.data.append(float(i))
        self.dim = len(args)
        if self.dim == 2:
            self.__class__ = Vector2
        elif self.dim == 3:
            self.__class__ = Vector3

    def __getitem__(self, index):
        """
        :param index: index number of value wanted
        :return: value in specified dimension of Vector
        """
        return self.data[index]

    def __setitem__(self, index, newval):
        """
        :param index: An integer_
        :param newval: A value that can be converted to float
        :return None
        """
        self.data[index] = float(newval)

    def __len__(self):
        """
        :return: dimension of Vector
        """
        return self.dim

    def __str__(self):
        """
        v = Vector(1, 2, 3)     #<Vector3: 1, 2, 3>
        :return: string representation of this vector
        """
        s = "<Vector" + str(self.dim) + ": "
        for i in range(self.dim):
            s += str(self.data[i])
            if i < (self.dim - 1):
                s += ", "
        s += ">"
        return s

    def __eq__(self, other):
        """
        :param other: any value
        :return: A boolean. True if other is a Vector with same dimension and exactly the same values as self.
        """
        if isinstance(other, Vector) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        return False

    def __mul__(self, scalar):
        """
        Multiply a Vector by a scalar. The scalar is on the right of *
        :param scalar: The value to multiply by. (int or float)
        :return: A copy of this vector with all values multiplied by scalar.
        """
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            n = "Vector" + str(self.dim)
            raise TypeError("You can only multiply this " + n + " and a scalar. You attempted to multiply by "
                            + str(scalar) + ".")
        r = self.copy()
        for i in range(self.dim):
            r[i] *= scalar
        return r

    def __rmul__(self, scalar):
        """
        Multiply a Vector by a scalar. The scalar is on the left of *
        :param scalar: The value to multiply by. (int or float)
        :return: A copy of this vector with all values multiplied by scalar.
        """
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            n = "Vector" + str(self.dim)
            raise TypeError("You can only multiply this " + n + " and a scalar. You attempted to multiply by "
                            + str(scalar) + ".")
        r = self.copy()
        for i in range(self.dim):
            r[i] *= scalar
        return r

    def __add__(self, other_vec):
        """
        Adds two Vectors together.
        :param other_vec: The Vector to add to current vector. (Vector)
        :return: A copy of this vector with all values added with other_vec values
        """
        if not isinstance(other_vec, Vector) and self.dim != other_vec.dim:
            raise TypeError("You can only add a Vector object to this Vector object. You tried to add a "
                            + str(other_vec) + ".")
        r = self.copy()
        for i in range(self.dim):
            r[i] += other_vec[i]
        return r

    def __sub__(self, other_vec):
        """
        Subtracts one Vector from another.
        :param other_vec: The Vector to subtract from current vector. (Vector)
        :return: A copy of this vector with all values subtracted by other_vec values
        """
        if not isinstance(other_vec, Vector) and self.dim != other_vec.dim:
            raise TypeError("You can only subtract a Vector object from this Vector object. You tried to subtract a "
                            + str(other_vec) + ".")
        r = self.copy()
        for i in range(self.dim):
            r[i] -= other_vec[i]
        return r

    def __neg__(self):
        """
        Returns a negative version of the Vector
        :return: A copy of the Vector with all values multiplied by -1.
        """
        r = self.copy()
        for i in range(self.dim):
            r[i] *= -1
        return r

    def __truediv__(self, scalar):
        """
        Divides all values of current vector by a scalar
        :param scalar: The value to divide by. (int, float)
        :return: A copy of the current vector with all values divided by scalar.
        """
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            n = "Vector" + str(self.dim)
            raise TypeError("You can only divide this " + n + " and a scalar. You attempted to multiply by "
                            + str(scalar) + ".")
        r = self.copy()
        for i in range(self.dim):
            r[i] *= (1 / scalar)
        return r

    def copy(self):
        """
        creates a deep copy of this Vector
        :return: a new Vector copy of this Vector
        """
        v = Vector(*self.data)
        v.__class__ = self.__class__
        return v

    @property
    def mag(self):
        """
        Returns the 2-norm of the Vector
        :return: 2-norm of the Vector
        """
        squareLength = 0
        for i in range(self.dim):
            squareLength = squareLength + abs(self.data[i] ** 2)
        return squareLength ** (1 / 2)

    @property
    def mag_squared(self):
        """
        Returns the square of the 2-norm without using any square roots.
        :return: 2-norm of Vector squared
        """
        squareLength = 0
        for i in range(self.dim):
            squareLength = squareLength + abs(self.data[i] ** 2)
        return squareLength

    @property
    def normalize(self):
        """
        Returns a unit Vector in the same direction as this Vector.
        :return: unit Vector in same direction as Vector
        """
        n = []
        for i in range(self.dim):
            n.append(self.data[i] * (1 / self.mag))
        return n

    @property
    def is_zero(self):
        """
        :return: True if self is the zero vector, False otherwise
        """
        for value in self:
            if value != 0.0:
                return False
        return True

    @property
    def i(self):
        """
        Returns a tuple of the coordinates of this Vector converted to integers.
        :return: tuple of integer coordinates
        """
        n = []
        for i in range(self.dim):
            n.append(int(self.data[i]))
        return tuple(n)


class Vector2(Vector):
    """Creates a 2-dimensional Vector"""

    def __init__(self, x, y):
        """
        Creates a Vector2 object with 2 dimensions
        :param x: x value of Vector2
        :param y: y value of Vector2
        """
        super().__init__(x, y)

    @property
    def x(self):
        """
        :return: first value in self
        """
        return self[0]

    @x.setter
    def x(self, newval):
        """
        Sets x value to a new value
        :param newval: value to set as x
        """
        self[0] = float(newval)

    @property
    def y(self):
        """
        :return: second value in self
        """
        return self[1]

    @y.setter
    def y(self, newval):
        """
        Sets y value to a new value
        :param newval: value to set as y
        """
        self[1] = float(newval)

    @property
    def degrees(self):
        """
        Returns the degree measure of this cartesian vector in polar space.
        :return: degree measure of this cartesian vector in polar space
        """
        deg = math.degrees(math.atan2(self.y, self.x))
        return deg

    @property
    def degrees_inv(self):
        """
        Negate the y-value to account for pygame’s y-axis.
        :return: negative degree value
        """
        deg = math.degrees(math.atan2(self.y, self.x))
        return -deg

    @property
    def radians(self):
        """
        Returns the radian measure of this cartesian vector in polar space.
        :return: radian measure of this cartesian vector in polar space
        """
        rad = math.atan2(self.y, self.x)
        return rad

    @property
    def radians_inv(self):
        """
        Negate the y-value to account for pygame’s y-axis.
        :return: negative radian value
        """
        rad = math.atan2(self.y, self.x)
        return -rad

    @property
    def perpendicular(self):
        """
        Returns a Vector2 perpendicular to this Vector.
        :return: Vector2 perpendicular to this Vector
        """
        y = self.x
        x = -self.y
        vec = Vector2(x, y)
        return vec


class Vector3(Vector):
    def __init__(self, x, y, z):
        """
        Creates a Vector2 object with 2 dimensions
        :param x: x value of Vector3
        :param y: y value of Vector3
        :param z: z value of Vector3
        """
        super().__init__(x, y, z)

    @property
    def x(self):
        """
        :return: first value in self
        """
        return self[0]

    @x.setter
    def x(self, newval):
        """
        Sets x value to a new value
        :param newval: value to set as x
        """
        self[0] = float(newval)

    @property
    def y(self):
        """
        :return: second value in self
        """
        return self[1]

    @y.setter
    def y(self, newval):
        """
        Sets y value to a new value
        :param newval: value to set as y
        """
        self[1] = float(newval)

    @property
    def z(self):
        """
        :return: third value in self
        """
        return self[2]

    @z.setter
    def z(self, newval):
        """
        Sets z value to a new value
        :param newval: value to set as z
        """
        self[2] = float(newval)


def dot(v, w):
    """
    Returns the dot product of two vectors of the same dimension.
    :param v: Vector 1
    :param w: Vector 2
    :return: dot product of 2 Vectors of same dimensions
    """
    if isinstance(v, Vector) and isinstance(w, Vector) and v.dim == w.dim:
        c = []
        for i in range(v.dim):
            c.append(v[i] * w[i])
        prod = 0
        for j in range(v.dim):
            prod += c[j]
        return prod
    else:
        n = "Vector" + str(v.dim)
        m = "Vector" + str(w.dim)
        raise TypeError("You can not get a dot product of a " + n + " and a " + m + ". You attempted to multiply by " +
                        "two Vectors of different dimensions.")


def cross(v, w):
    """
    Returns a Vector3 giving the cross product of 3D vectors v and w.
    :param v: Vector 1
    :param w: Vector 2
    :return: cross product of two Vector3 objects
    """
    if isinstance(v, Vector3) and isinstance(w, Vector3):
        sol = []
        sol.append((v[1] * w[2]) - (w[1] * v[2]))
        sol.append(-1 * ((v[0] * w[2]) - (w[0] * v[2])))
        sol.append((v[0] * w[1]) - (w[0] * v[1]))
        return sol
    else:
        n = "Vector" + str(v.dim)
        m = "Vector" + str(w.dim)
        raise TypeError("You can not multiply this " + n + " and a " + m + ". You attempted to multiply by two " +
                        "Vectors of different dimensions. Both Vectors must have a dimension of 3")


def polar_to_Vector2(r, angle, inv=True):
    """
    Input polar coordinates of a 2D point and return a Vector2.
    :param r: radius of polar coordinate
    :param angle: angle of polar coordinate
    :param inv: inverse (set to True by default)
    :return: Vector2 equal to polar coordinates
    """
    y = r * math.sin(angle)
    x = r * math.cos(angle)
    if inv:
        y = -y
    vec = Vector2(x, y)
    return vec


def pnorm(vector, p):
    """
    Input a Vector and a positive integer p and return the p-norm.
    :param vector: Vector 1
    :param p: power of norm
    :return: p-norm of the Vector
    """
    if isinstance(vector, Vector) and isinstance(p, int):
        squareLength = 0
        for i in range(vector.dim):
            squareLength = squareLength + abs(vector.data[i] ** p)
        return squareLength ** (1 / p)
    else:
        n = "Vector" + str(vector.dim)
        m = str(p.dim)
        raise TypeError("Input must be a Vector object and an integer. Input received was a " + n + " and a " + m + ".")
