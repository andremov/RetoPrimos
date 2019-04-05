import math, time

def func(fn,digs,verbose):
  if (fn == 1):
    if (verbose):
      print("\nOPC01")
      print("Base")
    
    
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

  if (fn == 2):
    if (verbose):
      print("\nOPC02")
      print("Changed main loop from 'for' to 'while'")

    
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

  if (fn == 3):
    if (verbose):
      print("\nOPC03")
      print("Skipped evens")

    
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

      n = n + 2
    
    execTime = time.time() - startT
    
    if (verbose):
      print("exectime:",execTime)
      print("primos: ",c)

    return execTime
    
  if (fn == 4):
    if (verbose):
      print("\nOPC04")
      print("Added break case for secondary loop")

    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    n = start
    c = 0

    while n < end:
      isPrime = True
      x = 2
      while x < n and isPrime:
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

  if (fn == 5):
    if (verbose):
      print("\nOPC05")
      print("Reduced secondary loop to root of n")

    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    n = start
    c = 0

    while n < end:
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

  if (fn == 6):
    if (verbose):
      print("\nOPC06")
      print("Skipped multiples of 5")

    
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

  if (fn == 7):
    if (verbose):
      print("\nOPC07")
      print("Skipped even check")

    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    n = start
    c = 0

    while n < end:
      if (n%10 != 5):
        isPrime = True
        x = 3
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
    
  if (fn == 8):
    if (verbose):
      print("\nOPC08")
      print("Secondary loop back to 'for' loop")
    
    
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

  if (fn == 9):
    if (verbose):
      print("\nOPC09")
      print("Added break to secondary loop")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    n = start
    c = 0

    while n < end:
      if (n%10 != 5):
        isPrime = True
        for x in range(3, int(math.sqrt(n))+1):
          if (n%x == 0):
            isPrime = False
            break

        if (isPrime):
          c = c + 1

      n = n + 2
    
    execTime = time.time() - startT
    
    if (verbose):
      print("exectime:",execTime)
      print("primos: ",c)

    return execTime

  if (fn == 10):
    if (verbose):
      print("\nOPC10")
      print("Replaced multiples of 5 mod check with string ref")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    n = start
    c = 0

    while n < end:
      if (str(n)[digs-1] != '5'):
        isPrime = True
        for x in range(3, int(math.sqrt(n))+1):
          if (n%x == 0):
            isPrime = False
            break

        if (isPrime):
          c = c + 1

      n = n + 2
    
    execTime = time.time() - startT
    
    if (verbose):
      print("exectime:",execTime)
      print("primos: ",c)

    return execTime

  if (fn == 11):
    if (verbose):
      print("\nOPC11")
      print("Changed main loop to 'for' loop again")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    c = 0

    for n in range(start,end,2):
      if (n%10 != 5):
        isPrime = True
        for x in range(3, int(math.sqrt(n))+1):
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
    
  if (fn == 12):
    if (verbose):
      print("\nOPC12")
      print("Skipping evens in secondary loop")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    c = 0

    for n in range(start,end,2):
      if (n%10 != 5):
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

  if (fn == 13):
    if (verbose):
      print("\nOPC13")
      print("Replacing sqrt function with power of half")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    c = 0

    for n in range(start,end,2):
      if (n%10 != 5):
        isPrime = True
        for x in range(3, int(n**(1/2))+1, 2):
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

  if (fn == 14):
    if (verbose):
      print("\nOPC14")
      print("Assuming numbers are prime")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    c = 0

    for n in range(start,end,2):
      if (n%10 != 5):
        c = c + 1
        for x in range(3, int(n**(1/2))+1, 2):
          if (n%x == 0):
            c = c - 1
            break
    
    execTime = time.time() - startT
    
    if (verbose):
      print("exectime:",execTime)
      print("primos: ",c)

    return execTime

  if (fn == 15):
    if (verbose):
      print("\nOPC15")
      print("Skipping secondary loop when multiple of 5")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    c = 0

    for n in range(start,end,2):
      if (n%10 != 5):
        c = c + 1
        for x in range(3, int(n**(1/2))+1, 2):
          if (x%10 != 5):
            if (n%x == 0):
              c = c - 1
              break
    
    execTime = time.time() - startT
    
    if (verbose):
      print("exectime:",execTime)
      print("primos: ",c)

    return execTime
    
  if (fn == 16):
    if (verbose):
      print("\nOPC16")
      print("Copy of OPC12")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    c = 0

    for n in range(start,end,2):
      if (n%10 != 5):
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

  if (fn == 17):
    if (verbose):
      print("\nOPC17")
      print("Volandose 3.")
    
    
    startT = time.time()

    start = (10**(digs-1))+1
    end = 10**digs
    next3 = 2
    c = 0

    for n in range(start,end,2):
      if (n%10 > next3):
        next3 = (next3+3)%10
      
      if (n%10 == next3):
        next3 = (next3+3)%10
      else:
        if (n%10 != 5):
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
    
  if (fn == 18):
    if (verbose):
      print("\nOPC18")
      print("Volandose 3 -> MEM.")
    
    
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
    
  if (fn == 19):
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
    
  if (fn == 20):
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

  return 0