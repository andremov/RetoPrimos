
import sieve, primerange_sympymod, time, primos

d = 4
print("\n\ndigitos:",d)
primerange_sympymod.func(d,True)

print('')
startT = time.time()
print(sieve.func(d)-sieve.func(d-1))
print(time.time()-startT)

print('')
startT = time.time()
print(primos.func(d)-primos.func(d-1))
print(time.time()-startT)
