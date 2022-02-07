"""Not sure yet."""


def is_prime(x: int, ps: list) -> bool:
    """Check whether user int is a prime."""
    ya_prime_boi = False
    for n in ps:
        if x % n == 0:
            ya_prime_boi = False
            break
        else:
            ya_prime_boi = True
    return ya_prime_boi


def primes(x: int) -> list:
    """Find all primes smaller than an inputed num."""
    plist = []
    if x < 2:
        return plist
    elif x == 2:
        plist = [2]
        return plist
    else:
        plist = [2]
        for k in range(3, x + 1):
            for n in plist:
                if k % n == 0:
                    break
                elif k % n != 0 and plist.index(n) == len(plist) - 1:
                    plist = plist + [k]
                elif k % n != 0 and k == x:
                    if k not in plist:
                        plist = plist + [k]
                else:
                    continue
        return plist