def greedy_method(w, Weight, Price):
    Weight, Price = zip(*sorted(zip(Weight, Price), reverse=True, key=lambda pair: pair[1]))
    p = 0
    wl = w
    num_pieces = 0
    while wl > min(Weight):
        
        for i in range(len(Weight)):
            if Weight[i] <= wl:
                break
        wl -= Weight[i]
        p += Price[i]
        num_pieces += 1
    return num_pieces,p
w= 1
Weight= [5,10,15]
Price= [100,600,1000]

print(greedy_method(w,Weight,Price))
