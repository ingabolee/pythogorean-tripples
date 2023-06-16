from math import gcd

def find_tripple(number):
    for n in range(1, 10):
        for m in range(1, 10):
            # m should be greater than n and the two should be co-prime
            if m > n and gcd(m,n) == 1:
                a, b, c = m**2-n**2, 2*m*n , m**2+n**2; sum = a + b + c; print(a, b, c)
            
                if number % sum == 0:
                    return a * b * c * (number/sum)**3

if __name__ == "__main__":
    print(find_tripple(1000))