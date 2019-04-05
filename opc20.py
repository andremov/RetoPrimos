def func(digs,verbose):
  if (verbose):
    print("\nOPC20")
    print("conteo")
  
  import math, time
  startT = time.time()

  # todos los posibles numeros
  c = (10**digs)-((10**(digs-1)))

  # todos los impares
  c = c * 0.5

  # los numeros no terminados en 5
  c = c * (1-0.1)

  # los numeros no divisibles por 3
  c = c * (1-0.13333333333333333)
  c2 = c

  # los numeros no divisibles por 7
  c = c * (1-0.03809523333333333)
  
  # los numeros no divisibles por 11
  c = c * (1-0.015984011111111113)

  # los numeros no divisibles por 13
  c = c * (1-0.015984011111111113)

  execTime = time.time() - startT
  
  if (verbose):
    print("exectime:",execTime)
    print("solid #: ",c2)
    print("primos: ",c)

  return execTime