def fibonacci(n):
  a, b = 0, 1
  yield 0
  
  while b <= n:
    yield b
    a, b = b, a + b

fib_list = [num for num in fibonacci(2000000000)] # till 2 Million

sum = 0
for num in fib_list:
    sum = sum + num

print(fib_list)
print(sum)