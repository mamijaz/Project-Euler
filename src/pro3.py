def largest_prime_factor(num):
 
    largest_factor = 1
 
    while num % 2 == 0:
        largest_factor = 2
        num = num/2
 
    p = 3
    while num != 1:
        while not (num % p):
            largest_factor = p
            num = num/p
        p += 2
 
    return largest_factor
 
a = largest_prime_factor(600851475143)
 
print(a)
