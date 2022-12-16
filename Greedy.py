def greedy_method(g, W, P):
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
W=[5,14,18,20,22,28,40,45,50,60]
P=[120,300,400,450,480,600,650,750,800]
print(greedy_method(60,W,P))