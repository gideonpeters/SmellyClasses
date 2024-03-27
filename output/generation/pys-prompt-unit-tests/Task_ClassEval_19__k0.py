class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = []

    def generate_primes(self):
        sieve = [True] * (self.n + 1)
        p = 2
        while p**2 <= self.n:
            if sieve[p]:
                for i in range(p**2, self.n + 1, p):
                    sieve[i] = False
            p += 1
        self.primes = [p for p in range(2, self.n + 1) if sieve[p]]
        return self.primes

    def get_primes(self):
        return self.primes
`