pn = [0]

def func(digs,verbose):
  if (verbose):
    print("\nMEM SYMPY")
    print(".")
  
  import time, primepi_simple
  startT = time.time()
  
  while (digs >= len(pn)):
    pn.append(primepi_simple.func(10**len(pn)))
  
  
  c = pn[digs] - pn[digs-1]
  
  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("primos: ",c)

  return execTime

def clear():
  pn = [0]