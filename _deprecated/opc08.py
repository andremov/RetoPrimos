def func(digs,verbose):
  if (verbose):
    print("\nOPC08")
    print("Secondary loop back to 'for' loop")
  
  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  n = start
  c = 0

  while n < end:
    if (n%10 != 5):
      isPrime = True
      for x in range(3, int(math.sqrt(n))+1):
        isPrime = isPrime and (n%x != 0)

      if (isPrime):
        c = c + 1

    n = n + 2
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime