def func(digs,verbose):
  if (verbose):
    print("\nOPC15")
    print("Skipping secondary loop when multiple of 5")
  
  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  c = 0

  for n in range(start,end,2):
    if (n%10 != 5):
      c = c + 1
      for x in range(3, int(n**(1/2))+1, 2):
        if (x%10 != 5):
          if (n%x == 0):
            c = c - 1
            break
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime