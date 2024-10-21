# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# List to store prime numbers
prime_numbers = []

# Loop through numbers from 1 to 100
for num in range(1, 101):
    if is_prime(num):
        prime_numbers.append(num)

# Print the prime numbers
print("Prime numbers between 1 and 100 are:", prime_numbers)
