def func(digs,verbose):
  if (verbose):
    print("\nMODDED SYMPY")
    print(".")
  
  import time, primepi_simple
  startT = time.time()

  c = primepi_simple.func(digs) - primepi_simple.func(digs-1)
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime