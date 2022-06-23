
# next_state = [
#     {'A': 1, 'C': 0, 'G': 0, 'T': 0},
#     {'A': 2, 'C': 0, 'G': 0, 'T': 0},
#     {'A': 2, 'C': 3, 'G': 0, 'T': 0},
#     {'A': 1, 'C': 0, 'G': 0, 'T': 0}
# ]


# Time: O(n)
def fa_string_matcher(T, next_state, m, n): # traverse the string while using the finite automaton using the next_state table
    state = 0
    for i in range(1, n):
        state = next_state[state][T[i-1]]
        if state == m:# if accept state is reached
            print("The pattern occurs with shift", i-m)


#Time: q(m+1)
def build_next_state_table(alphabet, P):# builds the transition table
    m = len(P)
    next_state = [{a: 0 for a in alphabet}  for _ in range(m+1)]
    k = 0

    for k in range(m+1): # navigate through the states
        for a in alphabet: # navigate through the alphabets
            Pk_a = P[:k] + a # previously seen symbol plus the current symbol
            i = min(len(Pk_a), m) # get the shorter length between the Pk_a (could be m+1) and m

            while not Pk_a.endswith(P[:i]): # iterate while the prefix of the pattern (P) is not a suffix of currently seen symbols
                i = i - 1

            next_state[k][a] = i # set the transition value to i
            k = i # set the k to the next state
    return next_state

def match_string(T, P):
    next_state = build_next_state_table(T,P)
    fa_string_matcher(T, next_state, len(P), len(T))

alphabet = 'CATG'
print(build_next_state_table("GTAACAGTAAACG", "AAC"))
print(match_string("GTAACAGTAAACG", "AAC"))

