import math

print("Hola, mundo!")
print("\nNúmeros primos impares menores a 1000:")

def is_prime(n):
    """Checks if a number is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Start from 3 and check only odd numbers up to 1000, as 2 is the only even prime.
for num in range(3, 1000, 2):
    if is_prime(num):
        print(num)
