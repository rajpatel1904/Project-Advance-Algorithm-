def brute_force(w, Weight, Price):
    max_price = 0
    num_pieces = 0

    # Iterate through all possible combinations of items
    for i in range(1 << len(Weight)):
        weightLeft = w
        price = 0
        pieces = 0
        for j in range(len(Weight)):
            if 1 << j & i:
                if weightLeft - Weight[j] < 0:
                    break
                weightLeft -= Weight[j]
                price += Price[j]
                pieces += 1
            if price > max_price and weightLeft == 0:
                max_price = price
                num_pieces = pieces
            return num_pieces,max_price
Weight= [1,5,10,15,20,100,1500]
Price= [100,600,1000,1400,5000,10000]
print(brute_force(1000,Weight,Price))

    