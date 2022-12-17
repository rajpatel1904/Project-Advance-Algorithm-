def dynamic_method(g, W, P):
    table = [[0 for w in range(g + 1)] for j in range(len(W))]

    for j in range(len(W)):
        for w in range(g + 1):
            if w == 0:
                table[j][w] = 0

            elif W[j] > w:
                table[j][w] = table[j - 1][w]

            else:
                table[j][w] = max(table[j - 1][w], P[j] + table[j - 1][w - W[j]])

    res = table[len(W) - 1][g] 
    
    w = g
    numPieces = 0
    
    for i in range(len(W) - 1):
        if res <= 0:
            break
        if res == table[i][w]:
            continue
        else:
            numPieces += 1
            res = res + P[i]
            i = w + W[i]
    return numPieces
W=[1,5,10,15]
P=[100,600,1000,1500]
print(dynamic_method(500,W,P))

