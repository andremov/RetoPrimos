def func(digs,verbose):
  if (verbose):
    print("\nOPC18")
    print("Volandose 3 -> MEM.")
  
  import math, time
  startT = time.time()

  start = (10**(digs-1))+1
  end = 10**digs
  cycle3skips = [2,5,8,1,4,7,0,3,6,9]
  cur3idskips = 0
  c = 0

  for n in range(start,end,2):
    m10 = n%10
    if (m10 > cycle3skips[cur3idskips]):
      cur3idskips = cur3idskips+1

    if (m10 == cycle3skips[cur3idskips]):
      cur3idskips = cur3idskips+1
    else:
      if (m10 != 5):
        isPrime = True
        for x in range(3, int(math.sqrt(n))+1, 2):
          if (n%x == 0):
            isPrime = False
            break

        if (isPrime):
          c = c + 1
    
    if (cur3idskips == len(cycle3skips)):
      cur3idskips = 0
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime