
# next_state = [
#     {'A': 1, 'C': 0, 'G': 0, 'T': 0},
#     {'A': 2, 'C': 0, 'G': 0, 'T': 0},
#     {'A': 2, 'C': 3, 'G': 0, 'T': 0},
#     {'A': 1, 'C': 0, 'G': 0, 'T': 0}
# ]


# Time: O(n)
def fa_string_matcher(T, next_state, m, n):

    state = 0
    for i in range(1, n):
        state = next_state[state][T[i-1]]
        if state == m:
            print("The pattern occurs with shift", i-m)


#Time: q(m+1)
def build_next_state_table(alphabet, P):
    m = len(P)
    next_state = [{a: 0 for a in alphabet}  for _ in range(m+1)]
    k = 0

    for k in range(m+1):
    
        for a in alphabet:
            Pk_a = P[:k] + a
            i = min(len(Pk_a), m)

            while not Pk_a.endswith(P[:i]):
                i = i - 1

            next_state[k][a] = i
            k = i
    return next_state

def match_string(T, P):
    next_state = build_next_state_table(T,P)

    fa_string_matcher(T, next_state, len(P), len(T))

alphabet = 'CATG'
print(build_next_state_table("GTAACAGTAAACG", "AAC"))
print(match_string("GTAACAGTAAACG", "AAC"))

