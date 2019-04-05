def func(digs,verbose):
  if (verbose):
    print("\nOPC06")
    print("Skipped multiples of 5")

  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  n = start
  c = 0

  while n < end:
    if (n%10 != 5):
      isPrime = True
      x = 2
      while x < int(math.sqrt(n))+1 and isPrime:
        isPrime = isPrime and (n%x != 0)
        x = x + 1

      if (isPrime):
        c = c + 1

    n = n + 2
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime