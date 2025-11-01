def even_fibonacci_numbers(limit):
    a, b = 1, 2
    even_sum = 0

    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b

    return even_sum

limit = 4000000
result = even_fibonacci_numbers(limit)
print(f"The sum of even Fibonacci numbers up to {limit} is: {result}")