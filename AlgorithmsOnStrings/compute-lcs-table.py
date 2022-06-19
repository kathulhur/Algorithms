
# Detailed Solution (Dynamic Programming)
# Time: O(m + n); Space O(m * n)

def compute_lcs_table(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    l = [[0] * (n) for _ in range(m)]
    # the setting of 0 is unnecessary; included it just for clarity
    for i in range(m):
        l[i][0] = 0

    for j in range(n):
        l[0][j] = 0

    for i in range(1,m):
        for j in range(1,n):
            if X[i-1] == Y[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])
    
    return l


def assemble_lcs(X,Y,l,i,j):
    if l[i][j] == 0:
        return ""

    else:
        if X[i-1] == Y[j-1]:
            return assemble_lcs(X,Y,l,i-1,j-1) + X[i-1]

        else:
            if l[i][j-1] < l[i-1][j]:
                return assemble_lcs(X,Y,l,i,j-1)
            else:
                return assemble_lcs(X,Y,l,i-1,j)

X = "CATCGA"
Y = "GTACCGTCA"
l = compute_lcs_table("CATCGA", "GTACCGTCA")

print(assemble_lcs(X, Y, l, len(X), len(Y)))


# optimized solution:
# Time: O(m*n); space: O(min(m,n))

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = map(len, (text1, text2))
        
    cache = [0] * (n + 1)

    for a in text1:
        prevRow = prevRow = 0
        
        for idx, b in enumerate(text2):
            prevRow, prevRowPrevCol = cache[idx + 1], prevRow
            
            cache[idx+1] = prevRowPrevCol + 1 if a == b else max(prevRow, cache[idx])
            
    return cache[-1]
        
