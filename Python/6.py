def fibonacci_series(n):
   
    fib_sequence = [0, 1]

   
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence


terms = int(input("Enter the number of terms for the Fibonacci series: "))


if terms <= 0:
    print("Please enter a positive integer greater than 0.")
else:
   
    fib_sequence = fibonacci_series(terms)
    print(f"The Fibonacci series up to {terms} terms is: {fib_sequence}")
