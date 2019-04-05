def func(digs,verbose):
  if (verbose):
    print("\nSYMPY")
    print("-")
  
  import time, primepi_mod
  startT = time.time()

  start = (10**(digs-1))
  end = 10**digs

  c = primepi_mod.func(end) - primepi_mod.func(start)
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime