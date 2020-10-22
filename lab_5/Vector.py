import numpy as np

def det(a11, a12, a21, a22):
    """
    Calculates a determinant of matrix {aij}; i = j = 2.

    Parameters
    ----------
    a11 : TYPE float
        DESCRIPTION. Matrix element: line 1, column 1.
    a12 : TYPE float
        DESCRIPTION. Matrix element: line 1, column 2.
    a21 : TYPE float
        DESCRIPTION. Matrix element: line 2, column 1.
    a22 : TYPE float
        DESCRIPTION. Matrix element: line 2, column 2.

    Returns determinant of matrix {aij}; i = j = 2.
    -------
    None.

    """
    return a11 * a22 - a12 * a21

class Vector():
    def __init__(self, x, y, z):
        self.xcoord = x
        self.ycoord = y
        self.zcoord = z
    
    def __str__(self):
        return ('(' + str(self.xcoord) + ', ' + str(self.ycoord) + ', ' + 
                str(self.zcoord) + ')')
    
    def __add__(self, inst):
        return Vector(self.xcoord + inst.xcoord, self.ycoord + inst.ycoord,
                      self.zcoord + inst.zcoord)
    
    def __sub__(self, inst):
        return Vector(self.xcoord - inst.xcoord, self.ycoord - inst.ycoord,
                      self.zcoord - inst.zcoord)
    
    def __mul__(self, inst):
        if type(inst) == int:
            return Vector(self.xcoord * inst, self.ycoord * inst, self.zcoord 
                          * inst)
        else:
            return (self.xcoord * inst.xcoord + self.ycoord * inst.ycoord +
                   self.zcoord * inst.zcoord)
    
    def __rmul__(self, inst):
        if type(inst) == int:
            return Vector(self.xcoord * inst, self.ycoord * inst, self.zcoord 
                          * inst)
        else:
            return (self.xcoord * inst.xcoord + self.ycoord * inst.ycoord + 
                   self.zcoord * inst.zcoord)
    
    def __matmul__(self, inst):
        return Vector(det(self.ycoord, self.zcoord, inst.ycoord, inst.zcoord),
                    - det(self.xcoord, self.zcoord, inst.xcoord, inst.zcoord),
                      det(self.xcoord, self.ycoord, inst.xcoord, inst.ycoord))
    
    def norm(self):
        return (np.sqrt(self.xcoord**2 + self.ycoord**2 + self.zcoord**2))
    
a = Vector(1, 2, 3)
b = Vector(3, 2, 1)
c = a + b
x = 10
print("a =", a)
print("b =", b)
print("a + b =", c)
print("x =", x)
print("a * x =", a * x)
print("x * b =", x * b)
print("a - b =", a - b)
print("b - a =", b - a)
print("[a x b] =", a @ b)
print("[b x a] =", b @ a)
print("|a| =", a.norm())
print("|b| =", b.norm())
print("(a, b) =", a * b)
print("(b, a) =", b * a)