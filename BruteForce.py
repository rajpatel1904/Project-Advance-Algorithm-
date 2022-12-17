def brute_force(g, W, P):
    max_price = 0
    num_pieces = 0

    # Iterate through all possible combinations of items
    for i in range(1 << len(W)):
        weightLeft = g
        price = 0
        pieces = 0
        for j in range(len(W)):
            if 1 << j & i:
                if weightLeft - W[j] < 0:
                    break
                weightLeft -= W[j]
                price += P[j]
                pieces += 1
        if price > max_price and weightLeft == 0:
            max_price = price
            num_pieces = pieces
    return num_pieces

    