def fibonacci_last_digit(n):
  if n <= 1:
    return n

  fibonacci_last_digits = [0, 1]
  for i in range(2, n + 1):
    fibonacci_last_digits.append((fibonacci_last_digits[i - 1] + fibonacci_last_digits[i - 2]) % 10)

  return fibonacci_last_digits[n]


n = int(input())
print(fibonacci_last_digit(n))


