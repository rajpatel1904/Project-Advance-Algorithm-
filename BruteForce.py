def brute_force(wl, numPieces, p, W, P, n):
  if min(W) > wl:
    return [(p, numPieces)]

  S= []
  for i in range(n):
    if W[i] <= wl:
      remainingWeight = wl - W[i]
      totalPieces = numPieces + 1
      totalPrice = p + P[i]
      S1 = brute_force(remainingWeight, totalPieces, totalPrice, W, P, n)
      S.extend(S1)
  return S
