"""
Operators
"""
def arithmeticOperators():
    print(2 + 3)
    print(2-6)
    print(2-5.6)
    print(3*8)
    print(5/5)
    print(10%2)
    print(2**3)
    print(910//27)

def assignmentOperators():
    x = 5
    x <<= 3
    x |= 3
    x &= 3
    print(x)

def logicalOperators():
    print(3<4 and 3<10)
    print(4>6 or 4>2)
    print(not(1<4 and 4<11))
    x = ["apple","banana"]
    z = ["pear", "apple"]
    y = ["apple","banana"]
    print(x is z)
    print(x[0] is z[1])
    print((x is y),(x == y)) # is => checks object, == => checks value
    print(x[0] in z)

logicalOperators()



