"""Gonna generate and then test some prime numbas."""


def is_prime(x: int, ps: list) -> bool:
    """Test x for divisibility in the ps list)."""
    prime_or_not = True
    for i in ps:
        if x % i == 0:
            prime_or_not = False
    return prime_or_not


def primes(n: int) -> list:
    """Return list of primes smaller than n, plus n itself."""
    pr_list = []
    if n < 2:
        return pr_list
    pr_list = [2]  # automatically whack first prime number in the list
    for i in range(2, n + 1):  # for each int up to n, send off for prime test
        prime_or_not = is_prime(i, pr_list)
        if prime_or_not is True:
            pr_list = pr_list + [i]
    return pr_list


if __name__ == "__main__":
    assert primes(1) == []
    assert primes(3) == [2, 3]
    assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]