def brute_force(g, W, P):
    
    W, P = zip(*sorted(zip(W, P), reverse=True, key=lambda pair: pair[1]))
    maxPrice = 0
    numPieces = 0
    for i in range(0, 2 ** len(W)):
        price = 0
        weight = 0
        for j in range(0, len(W)):
            if i & (1 << j) > 0:
                price += P[j]
                weight += W[j]
        if weight <= g and price > maxPrice:
            maxPrice = price
            numPieces = i
    return numPieces
