
# Time: O(mn)
# Space: O(mn)
def compute_transform_tables(X, Y, Cc, Cr, Cd, Ci):
    m = len(X) + 1
    n = len(Y) + 1

    costs = [[0] * n for _ in range(m)]
    ops = [[0] * n for _ in range(m)]

    costs[0][0] = 0
    
    for i in range(1, m): # fill the first column with delete cost and delete operation;
        costs[i][0] = i * Cd
        ops[i][0] = "del" + X[i-1]

    for j in range(1, n): #fill the first column with insert cost and insert operation;
        costs[0][j] = j * Ci
        ops[0][j] = "ins" + Y[j-1]

    
    for i in range(1, m):
        for j in range(1, n):
            if X[i-1] == Y[j-1]: # if the characters matched; add the copy cost to the previous state
                costs[i][j] = costs[i-1][j-1] + Cc 
                ops[i][j] = "copy" + X[i-1]
            else: # if the characters doesn't match; add replace cost to the previous state
                costs[i][j] = costs[i-1][j-1] + Cr
                ops[i][j] = "rep" + X[i-1] + Y[j-1]

            # if the previous column cell added a delete cost if less than the current cost; replace its value
            if costs[i-1][j] + Cd < costs[i][j]:
                costs[i][j] = costs[i-1][j] + Cd
                ops[i][j] = "del" + X[i-1]

            if costs[i][j-1] + Ci < costs[i][j]: # if the previous column cell added a insert cost if less than the current cost; replace its value
                costs[i][j] = costs[i][j-1] + Ci
                ops[i][j] = "ins" + Y[j-1]

    return costs, ops

# Time: O(m + n)
# Space O(1)
def assemble_transformation(ops, i, j):
    if i == 0 and j == 0:
        return ""

    elif "copy" in ops[i][j] or "rep" in ops[i][j]:
        return assemble_transformation(ops, i-1, j-1) + " " + ops[i][j]


    elif "del" in ops[i][j]:
        return assemble_transformation(ops, i-1, j) + " " + ops[i][j]

    else:
        return assemble_transformation(ops, i, j-1) + " " + ops[i][j]


X = "ACAAGC"
Y = "CCGT"
[costs, ops] = compute_transform_tables(X, Y, -1, 1, 2, 2)

print(assemble_transformation(ops, len(X), len(Y)))




