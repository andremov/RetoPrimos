def func(digs,verbose):
  if (verbose):
    print("\nOPC19")
    print("resumiendo")
  
  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  next3 = 2
  c = 0

  for n in range(start,end,2):
    m10 = n%10
    if (m10 > next3):
      next3 = (next3+3)%10

    if (m10 == next3):
      next3 = (next3+3)%10
    else:
      if (m10 != 5):
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