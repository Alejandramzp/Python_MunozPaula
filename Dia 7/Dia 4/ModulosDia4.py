
def pares(l_n, n, k):
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            if (l_n[i]+l_n[j]) % k == 0:
                pairs.add((min(l_n[i],l_n[j]), max(l_n[i],l_n[j])))
    return len(pairs)