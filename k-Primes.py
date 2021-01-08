def count_Kprimes(k, start, nd):
    k_primes = []
    
    for num in range(start, nd+1):
        tmp_num = num
        prime_counter = 0
        prime_factor = 2
        while prime_factor * prime_factor <= tmp_num:
            while (tmp_num % prime_factor) == 0:
                tmp_num /= prime_factor
                prime_counter += 1
            if prime_counter > k:
                break
            prime_factor += 1
        
        if tmp_num == 1 and prime_counter == k or tmp_num > 1 and prime_counter + 1 == k:
            k_primes.append(num)
            
    return k_primes
                    
def puzzle(s):
    one_prime = count_Kprimes(1, 0, s)
    three_prime = count_Kprimes(3, 0, s)
    seven_prime = count_Kprimes(7, 0, s)
    
    return len([s for a in one_prime for b in three_prime for c in seven_prime if (a + b + c == s)])
