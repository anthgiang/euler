/** Find the 10001st prime number */

console.time(); /** Timer: start */

isPrime = (num) => {
  if (num <= 3) {
    return num > 1;
  }

  if (num % 2 === 0 || num % 3 === 0) {
    return false;
  }

  let count = 5;
  while (count ** 2 <= num) {
    if (num % count === 0 || num % (count + 2) === 0) {
      return false;
    }
    count += 6;
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

console.timeEnd(); /** Timer: finish */
