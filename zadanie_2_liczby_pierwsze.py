# import pdb;pdb.set_trace()
def sum_of_primes(x):
    lista =[]
    if x > 1:
        for z in range(2,x):
            for i in range(2,z):
                if z%i == 0:
                    break
            else:
                lista.append(z)
    return sum(lista)
assert sum_of_primes(60) == 440
assert sum_of_primes(10) == 17
