def func(digs,verbose):
  if (verbose):
    print("\nOPC01")
    print("Base")
  
  import math, time
  startT = time.time()

  start = (10**(digs-1))
  end = 10**digs

  c = 0

  for n in range(start, end):
    isPrime = True
    for x in range(2,n-1):
      if (n%x == 0):
        isPrime = False
    
    if (isPrime):
      c = c + 1
  
  execTime = time.time() - startT

  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime