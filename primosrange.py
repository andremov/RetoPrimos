import time, primos

def func(digs):
  
  
  startT = time.time()
  c = (primos.func(digs)-primos.func(digs-1))
  
  print(time.time()-startT)

  return c