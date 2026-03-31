# Morgan Nordberg

# The problem is to multiply 2 large polynomials in an efficient manner

# Time complexity is O(n log n) since we are more or less just applying the
# fast fourier tyransform which is itself O(n log n) since it's essentially
# just a single loop, applied in a recurvsive divide-and-conquer manner

# algorithm is padding the polynomials with 0's as coefficients to ensure they
# are equal in length and make sure it's an even legnth (important so we can
# always divide them in 2 equal parts). we then do precisley that, apply fft to
# both parts (recursivley, until we reach the base case of a polynomial of
# length 1), multiply the results and do the inverse fft on the resulting array
# then taking the real part of each resulting complex number to arrive at the
# final result


from math import * 

def fft(poly, inv_flag):
    if len(poly) < 2:
        return
    
    even = poly[::2]
    odd = poly[1::2]
    fft(even, inv_flag)
    fft(odd, inv_flag)
    
    ang = 2 * pi / len(poly) * (1,-1)[inv_flag]
    w = complex(1)
    wn = complex(cos(ang), sin(ang))
    for i in range(len(poly) // 2):
        poly[i] = even[i] + w * odd[i]
        poly[i + len(poly) // 2] = even[i] - w * odd[i]
        if inv_flag:
            poly[i] /= 2
            poly[i + len(poly)//2] /= 2
        w *= wn

def fft_polymul(poly1, poly2):
    n = 1
    while (n < len(poly1) + len(poly2)): n *= 2
    poly1_padded = list(map(complex, poly1)) + [0j] * (n - len(poly1))
    poly2_padded = list(map(complex, poly2)) + [0j] * (n - len(poly2))
    fft(poly1_padded, False)
    fft(poly2_padded, False)
    poly_res = [x * y for x,y in zip(poly1_padded, poly2_padded)]
    fft(poly_res, True)
    return [round(c.real) for c in poly_res[:len(poly1) + len(poly2) - 1]]


if __name__ == "__main__":
    input = open(0).readlines()[1:]
    print(int(input[0]) + int(input[2]))
    *poly1, = map(int, input[1].split())
    *poly2, = map(int, input[3].split())
    print(*fft_polymul(poly1, poly2))
