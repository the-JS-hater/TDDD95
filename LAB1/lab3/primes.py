# Morgan Nordberg

# Problem find all prime numbers in range 0 -> n

# Algorithm: start by assuming all numbers in the range are prime. then go to
# the first/next prime and mark all numbers in the range that are divisible by
# this prime as not prime. done by simply continuing to multiply the prime by
# itself until we leave the range. we then get an array of bools (bitarray, in
# this case). Some  optimizations are only considering odd numbers since all
# even numbers besides 2 are not prime

# Memory complexity: memory usage is implemented first by only storing odd
# numbers, halving the required memory usage. and then by packing bits in a
# byte array, such that each bool only requires a single bit. So the memory
# usage is a bit for every odd number we need to store

# Time complexity: O(n log log n), since iterate over the array once and for each
# time when we find a prime number we iterate over the rest of the array from
# that starting point in steps of size of the prime number. And the prime
# numbers get larger for each ioteration so the number of iterations whenever
# we find a prime number gets smaller. This would be O(n log n), but because of
# the distribution of prime numbers it is in practice O(n log log n)


def prime_sieve(n):
    prime = bytearray([0xFF]) * ((((n + 1) // 2) + 7) // 8)
    unset(0, prime)
    i = 1
    while (2*i + 1)**2 <= n:
        if get(i, prime):
            p = (2*i + 1)
            for j in range(p**2 // 2, n // 2 + 1, p):
                unset(j, prime)
        i += 1
    return prime

    
def unset(i, prime):
    prime[i >> 3] &= ~(1 << (i & 7))


def get(i, prime):
    return (prime[i >> 3] >> (i & 7)) & 1


if __name__ == "__main__":
    input = open(0).readlines()
    n, q = map(int, input[0].split())
    xs = map(int, input[1:])
    prime = prime_sieve(n)
    print(sum(get(i, prime) for i in range(n // 2 + 1))+1)
    for x in xs:
        if x == 2: print(1)
        elif x < 2 or not x % 2: print(0)
        else: print(get(x // 2, prime))
