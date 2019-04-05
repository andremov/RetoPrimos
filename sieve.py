def func(digs):
 n = 10**digs
 arr = [0] * n

 for i in range(n):
   arr[i] = i

 lim = int(n ** 0.5)
 c = 0

 for i in range(2, n):
  if (arr[i] != 0):
    c += 1
    if (i <= lim):
      m = arr[i]

      while(arr[i]*m < n):
        np = arr[i]*m
        arr[np] = 0
        m += 1

      #print('')
      #print(arr)

 return c