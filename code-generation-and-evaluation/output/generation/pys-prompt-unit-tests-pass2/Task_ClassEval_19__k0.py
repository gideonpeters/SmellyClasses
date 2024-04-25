class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = []

    def generate_primes(self):
        if self.n < 2:
            return []
        sieve = [True] * (self.n + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= self.n:
            if sieve[p]:
                for i in range(p * p, self.n + 1, p):
                    sieve[i] = False
            p += 1
        self.primes = [i for i in range(2, self.n + 1) if sieve[i]]
        return self.primes

    def get_primes(self):
        return self.primes
