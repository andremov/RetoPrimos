def func(digs,verbose):
  if (verbose):
    print("\nOPC02")
    print("Changed main loop from 'for' to 'while'")

  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  n = start
  c = 0

  while n < end:
    isPrime = True
    for x in range(2,n-1):
      if (n%x == 0):
        isPrime = False
    
    if (isPrime):
      c = c + 1

    n = n + 1
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime