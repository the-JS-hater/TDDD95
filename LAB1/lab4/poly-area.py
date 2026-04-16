# Morgan Nordberg

# Problem: calculate area of a simple polygon

# Algorithm: iterate over all edges and add area of a trapezoid bound by the
# edge and x-axis taken with sign to reduce extra area. We can tell if vertices
# were given in clockwise or counter clockwise order by seeing if the total
# area is negative or positive at the end

# Time complexity: O(n) since we only iterate over all edges once 


def area(vs):
    a = 0
    es = [(vs[i], vs[(i+1)%len(vs)]) for i in range(len(vs))]
    for e in es:
        a += (e[0][0] - e[1][0]) * ((e[0][1] + e[1][1])) 
    return a / 2



if __name__ == "__main__":
    parse = lambda line_str: list(map(int, line_str.split()))
    *input, = map(parse, open(0).readlines())
    i = 0
    vs = []
    while i < len(input) - 1:
        n = input[i][0]
        i+=1
        for j in range(i, i+n):
            x,y = input[j]
            vs += [(x,y)]
        a = area(vs)
        s = "CCW" if a > 0 else "CW"
        print(s, abs(a))
        i+=n
        vs = []
