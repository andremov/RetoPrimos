def func(digs,verbose):
  if (verbose):
    print("\nOPC12")
    print("Skipping evens in secondary loop")
  
  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  c = 0

  for n in range(start,end,2):
    if (n%10 != 5):
      isPrime = True
      for x in range(3, int(math.sqrt(n))+1, 2):
        if (n%x == 0):
          isPrime = False
          break

      if (isPrime):
        c = c + 1
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime