
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

    # fill the table with the prefix subsequence counts
    for i in range(1,m):
        for j in range(1,n):
            if X[i-1] == Y[j-1]:# if the characters of the two strings are the same
                l[i][j] = l[i-1][j-1] + 1 # increment the value of the previous subsequence count
            
            else:# if the characters doesn't match
                l[i][j] = max(l[i][j-1], l[i-1][j]) # Get the higher between the top and left cells of the table
    
    return l


# recursive solution for reconstructing the subsequence
def assemble_lcs(X,Y,l,i,j):
    if l[i][j] == 0: # base case: stop when the value of the cell in the table becomes 0
        return ""

    else:
        if X[i-1] == Y[j-1]: # if the characters matches
            return assemble_lcs(X,Y,l,i-1,j-1) + X[i-1] # make a recursive call and concatenate the character at the end

        else:
            if l[i][j-1] > l[i-1][j]: # if the left side of the grid is higher than the top side of the table
                return assemble_lcs(X,Y,l,i,j-1) # make a recursive call going to the left side of the table
            else:
                return assemble_lcs(X,Y,l,i-1,j) # make a recursive call at the right side of the table

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
        
