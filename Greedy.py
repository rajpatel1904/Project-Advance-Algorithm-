def prob4Greedy(g, W, P):
    # sort W and P together in descending order by P
    W, P = zip(*sorted(zip(W, P), reverse=True, key=lambda pair: pair[1]))
    price = 0
    weightLeft = g
    numPieces = 0
    while weightLeft > min(W):
        #Let i be the minimum index such that W[I] ≤ weightLeft
        for i in range(len(W)):
            if W[i] <= weightLeft:
                break
        weightLeft -= W[i]
        price += P[i]
        numPieces += 1
    return numPieces
W=[5,14,18,20,22,28,40,45,50]
P=[100,200,300,400,500,600,700,800,900]
print(prob4Greedy(2000,W,P))