import math

#note that this is the gram-schmidt process in three-dimensional real space with the standard inner product (the dot product)

def main():

    #takes user input for the vectors we are working with
    v1 = input("Enter vector 1 in the form (x,y,z): ")
    v2 = input("Enter vector 2 in the form (x,y,z): ")
    v3 = input("Enter vector 3 in the form (x,y,z): ")

    #breaks vectors into their components
    xa, ya, za = piecer(v1)
    xb, yb, zb = piecer(v2)
    xc, yc, zc = piecer(v3)

    #finding the first vector of the orthonormal basis
    e1a, e1b, e1c = normalize(xa, ya, za)

    #finding the second vector
    #h1, h2, h3 are the components of the projection of v2 onto u1
    h1, h2, h3 = projector(xb, yb, zb, xa, ya, za)
    #g1, g2, g3 are the components of u2
    g1, g2, g3 = (xb - h1), (yb - h2), (zb - h3)
    e2a, e2b, e2c = normalize(g1, g2, g3)

    #finding the third vector
    #h1, h2, h3 are the components of the projection of v3 onto u2
    h1, h2, h3 = projector(xc, yc, zc, g1, g2, g3)
    #j1, j2, j3 are the components of the projection of v3 onto u1
    j1, j2, j3 = projector(xc, yc, zc, xa, ya, za)
    #k1, k2, k3 are the components of the sum of projections h and j
    k1, k2, k3 = (h1 + j1), (h2 + j2), (h3 + j3)
    #l1, l2, l3 are the components of u3
    l1, l2, l3 = (xc - k1), (yc - k2), (zc - k3)
    e3a, e3b, e3c = normalize (l1, l2, l3)

    print("Your orthonormal basis consists of ", vector_maker(e1a, e1b, e1c), ",", vector_maker(e2a, e2b, e2c), ", and ", vector_maker(e3a, e3b, e3c))

def piecer(vector):

    #removes excess
    vector = vector.strip().removeprefix("(").removesuffix(")")

    #splits vector into its components
    x, y, z = vector.rsplit(",")

    return float(x), float(y), float(z)

#here v = (a1, b1, c1) and u = (a2, b2, c2)
#this function projects v onto u
def projector(a1, b1, c1, a2, b2, c2):

    float(a1)
    float(b1)
    float(c1)
    float(a2)
    float(b2)
    float(c2)

    #top dot product
    topdot = (a1 * a2) + (b1 * b2) + (c1 * c2)

    #bottom dot product
    botdot = (a2 * a2) + (b2 * b2) + (c2 * c2)

    #returns the three components of the projection (aka the new vector)
    return (topdot / botdot) * a2, (topdot / botdot) * b2, (topdot / botdot) * c2

def normalize(p, r, q):

    #float them all
    p = float(p)
    r = float(r)
    q = float(q)

    #calculates the norm
    norm = math.sqrt((p * p) + (r * r) + (q * q))

    #divides now
    return (p / norm), (r / norm), (q / norm)

def vector_maker(c, d, b):
    c = round(c, 3)
    d = round(d, 3)
    b = round(b, 3)

    return f"({c}, {d}, {b})"

main()