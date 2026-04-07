# Morgan Nordberg

# The problem is using gaussian elimination to solve linear systems of equations

# guassian elimination goes along the diagonal indices of a matrix and in the
# current column, takes the largest abs value as a pivot element, then swaps
# whichever row that is found at with the current row, the divides the current
# row by the pvit value, and the subtracts the current row from all other rows
# before repeating this for the next diagonal coordinate. if a column is all
# 0's we simply skip onto the next position. That column is a free variable.
# the where list keeps track of where the pivot elements are, used for finding
# the solution or checking of a solution exists

# Time complexity is O(n^3) since we loop over all rows to do the limination,
# but for each row we must loop over all rows to find the pivot element, and
# then we must loop over all rows to subtract the current row from it. 

def gauss(matrix, vec):
    n = len(matrix)
    m = n  
    eps = 1e-9
    where = [-1] * m
    row = 0
    
    for col in range(m):
        pivot = max(range(row, n), key=lambda i: abs(matrix[i][col]))
        if abs(matrix[pivot][col]) < eps:
            continue  
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        vec[row], vec[pivot] = vec[pivot], vec[row]
        pivot_val = matrix[row][col]
        matrix[row] = [x / pivot_val for x in matrix[row]]
        vec[row] /= pivot_val
        for i in range(n):
            if i == row:
                continue
            factor = matrix[i][col]
            matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[row])]
            vec[i] -= factor * vec[row]
        where[col] = row
        row += 1

    solution = [0] * m
    for j in range(m):
        if where[j] != -1:
            solution[j] = vec[where[j]]

    for i in range(n):
        total = sum(solution[j] * matrix[i][j] for j in range(m))
        if abs(total - vec[i]) > eps:
            return "inconsistent", []

    if any(where[j] == -1 for j in range(m)):
        return "multiple", []

    return "solution", solution


if __name__ == "__main__":
    lines = [list(map(float, line.split())) for line in open(0)]
    i = 0
    while i < len(lines):
        n = int(lines[i][0])
        if n == 0:
            break
        matrix = [lines[j][:n] for j in range(i+1, i+1+n)]
        vec = lines[i+1+n][:n]
        state, solution = gauss(matrix, vec)
        if state == "solution": print(*solution)
        else: print(state)
        i += 1 + n + 1
