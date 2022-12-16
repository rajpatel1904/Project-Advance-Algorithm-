def greedy_method(g, W, P):
    W, P = zip(*sorted(zip(W, P), reverse=True, key=lambda pair: pair[1]))
    price = 0
    weightLeft = g
    numPieces = 0
    while weightLeft > min(W):
        
        for i in range(len(W)):
            if W[i] <= weightLeft:
                break
        weightLeft -= W[i]
        price += P[i]
        numPieces += 1
    return numPieces
