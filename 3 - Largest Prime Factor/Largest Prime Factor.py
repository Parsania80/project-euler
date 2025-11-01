def largest_prime_factor(n):
    largest_prime = 0
    for i in range(2, int(n**0.5) + 1):
        if(n % i == 0):
            largest_prime = i
            while n % i == 0:
                n //= i
    return n if n > 1 else largest_prime

# Example usage:
number = 600851475143
print(largest_prime_factor(number)) # Output: 6857  