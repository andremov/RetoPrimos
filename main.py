


import opc19, sieve, time, primerange_sympy

n = 4
verbose = True

opc19.func(n,verbose)

primerange_sympy.func(n,verbose)

startT = time.time()
print(sieve.func(d)-sieve.func(d-1))
print(time.time()-startT)
