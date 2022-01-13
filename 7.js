/** Find the 10001st prime number */

isPrime = (n) => {
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

nextPrime = (n) => {
  next = n;
  while (true) {
    if (isPrime(next)) {
      return next;
    }
    next++;
  }
};

primes = [1];
while (primes.length <= 10001) {
  primes.push(nextPrime(primes[primes.length - 1] + 1));
}

console.log(primes[primes.length - 1]);
