def generate_squares():
    squares = [x**2 for x in range(1, 31)]
    first_5 = squares[:5]
    last_5 = squares[-5:]

    print("First 5 elements:", first_5)
    print("Last 5 elements:", last_5)
generate_squares()
