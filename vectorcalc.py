import math


def vector_dim(v):
    """Returns dimension of vector v"""
    return len(v)


def scalar_mult(v, a):
    """Multiplies vector v by a scalar a"""
    n = []
    dim = len(v)
    for i in range(dim):
        n.append(v[i] * a)
    return n


def add_vec(v, w):
    """Adds two vectors of the same dimension"""
    x = []
    dim = len(v)
    for i in range(dim):
        temp = v[i] + w[i]
        x.append(temp)
    return x


def subtract_vec(v, w):
    """Subtracts vector w from vector v of same dimensions"""
    return add_vec(v, scalar_mult(w, -1))


def mag(v, p=2):
    """Returns the p-norm of v, p defaults to 2"""
    dim = len(v)
    squareLength = 0
    for i in range(dim):
        squareLength = squareLength + abs(v[i]**p)
    return squareLength**(1/p)


def normalize(v, p=2):
    """Returns a unit vector in the same direction as vector v, p defaults to 2"""
    return scalar_mult(v, 1/mag(v, p))


def dot_product(v, w):
    """Finds the dot product of two different vectors of the same dimension"""
    dim = len(v)
    c = []
    for i in range(dim):
        c.append(v[i] * w[i])
    prod = 0
    for j in range(dim):
        prod += c[j]
    return prod


def vector_angle(v, w, choice="radians"):
    """Returns the angle between two vectors in the desired units, default is radians"""
    dim = len(v)
    dot = dot_product(v, w)
    lengths = mag(v, dim) * mag(w, dim)
    cosangle = (dot / lengths)
    angle = math.acos(cosangle / 100)
    if choice == "degrees":
        angle = angle / (math.pi / 180)
        return angle
    else:
        return angle


def cross_product(v, w):
    """Returns the cross product of 2 3-dimensional vectors"""
    dim = len(v)
    dim2 = len(w)
    sol = []
    if dim == 3 and dim2 == 3:
        sol.append((v[1] * w[2]) - (w[1] * v[2]))
        sol.append(-1 * ((v[0] * w[2]) - (w[0] * v[2])))
        sol.append((v[0] * w[1]) - (w[0] * v[1]))
        return sol
    else:
        print("No. You're dumb. Leave.")


def slimed(placed, points, size="small"):
    num = len(points)
    results = []
    if size == "small":
        for i in range(num):
            if mag(subtract_vec(placed, points[i])) <= 1:
                results.append("hit")
            else:
                results.append("missed")
    elif size == "medium":
        for i in range(num):
            if mag(subtract_vec(placed, points[i])) <= 3:
                results.append("hit")
            else:
                results.append("missed")
    elif size == "large":
        for i in range(num):
            if mag(subtract_vec(placed, points[i])) <= 5:
                results.append("hit")
            else:
                results.append("missed")
    return results


if __name__ == "__main__":
    # Note: By adding this if statement, we'll only execute the
    # following code if running this module directly (F5 in Idle or
    # the play button in pycharm). But if we import this module from
    # somewhere else it won't execute this code. Neat trick, huh?

    v = [1, 2, 3]
    w = [4, 5, 6]
    z = add_vec(v, w)
    print(z)            # [5, 7, 9]
    q = subtract_vec(v, w)
    print(q)            # [-3, -3, -3]
    a = scalar_mult(v, -2)
    print(a)            # [-2, -4, -6]
    b = add_vec(a, add_vec(v, w))
    print(b)            # [3, 3, 3]
    d = add_vec(add_vec(v, add_vec(v, v)), w)
    print(d)            # [7, 11, 15]
    c = subtract_vec(add_vec(scalar_mult(v, 2), w), normalize([9, 8, 7]))
    print(c)        # [5.353837657244036, 8.42563347310581, 11.497429288967583]
    print(mag(v, 2))    # 3.7416573867739413
    print(mag(v, 1))    # 6.0
    print(mag(v, 100))  # 3.0
    print(dot_product(v, w))     # 32
    print(vector_angle(v, w)) # 0.2257261285527342
    print(vector_angle(v, w, "degrees"))  # 12.933154491899135
    print(vector_angle([1, 2], [2, -1]))  # 1.5707963267948966
