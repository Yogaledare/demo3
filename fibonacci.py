


def print_fibonacci(integer):

    if integer < 0:
        return None
    fibonacci_numbers = [0]
    if integer == 1:
        return fibonacci_numbers
    fibonacci_numbers.append(1)
    if integer == 2:
        return fibonacci_numbers

    while True:
        new_fibonacci_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]

        if len(fibonacci_numbers) < integer:
            fibonacci_numbers.append(new_fibonacci_number)
        else:
            break
    return fibonacci_numbers




a = print_fibonacci(10)
print(a)