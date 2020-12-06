import math
from collections import defaultdict


def sum_for_list(lst):
    prime_dict = defaultdict(list)
    res = []

    for num in lst:
        prime_dict = get_prime(num, prime_dict)
    for k, v in sorted(prime_dict.items()):
        res.append([k, sum(v)])

    return res


def get_prime(num, prime_dict):
    n = abs(num)

    for i in range(2, int(math.sqrt(abs(num)))+1):
        if n % i == 0:
            prime_dict[i].append(num)
        while n % i == 0:
            n = n//i
    if n != 1:
        prime_dict[n].append(num)

    return prime_dict
