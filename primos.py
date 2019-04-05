def func(digs):
  n = 10**digs
  lim = int(n**(0.5))
  arr1 = [0] * (lim + 1)
  arr2 = [0] * (lim + 1)
  for i in range(1, lim + 1):
    arr1[i] = i - 1
    arr2[i] = n // i - 1
  for i in range(2, lim + 1):
    if arr1[i] != arr1[i - 1]:
      p = arr1[i - 1]
      for j in range(1, min(n // (i * i), lim) + 1):
        st = i * j
        if st <= lim:
          arr2[j] -= arr2[st] - p
        else:
          arr2[j] -= arr1[n // st] - p
      lim2 = min(lim, i * i - 1)
      for j in range(lim, lim2, -1):
        arr1[j] -= arr1[j // i] - p

  return arr2[1]